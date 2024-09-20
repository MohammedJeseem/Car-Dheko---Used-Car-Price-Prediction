import pickle
import pandas as pd
import streamlit as st

# Load the saved model
model_filename = "random_forest_model_with_preprocessor.pkl"
with open(model_filename, "rb") as file:
    loaded_model, preprocessor = pickle.load(file)

# Streamlit Page Title
st.title("Car Price Prediction")

data = pd.read_csv("data\\df_filtered.csv")

if data is not None:
    # Extract unique values for dropdowns from the dataset
    cities = data["City"].unique()
    insurances = data["Insurance"].unique()
    manufacturers = data["Manufacturer"].unique()

    # Expander for Car Specifications
    with st.expander("Car Specifications", expanded=True):
        st.header("Car Specifications")

        # Step 1: Select Manufacturer
        Manufacturer = st.selectbox("Manufacturer", manufacturers)

        # Step 2: Filter car models based on the selected manufacturer
        filtered_car_models = data[data["Manufacturer"] == Manufacturer][
            "CarModel"
        ].unique()
        CarModel = st.selectbox("Car Model", filtered_car_models)

        # Step 3: Filter variant names based on the selected car model
        filtered_variants = data[data["CarModel"] == CarModel]["VariantName"].unique()
        VariantName = st.selectbox("Variant Name", filtered_variants)

        filtered_fueltypes = data[data["CarModel"] == CarModel]["FuelType"].unique()
        FuelType = st.selectbox("Fuel Type", filtered_fueltypes)

        filtered_bodytypes = data[data["CarModel"] == CarModel]["BodyType"].unique()
        BodyType = st.selectbox("Body Type", filtered_bodytypes)

        filtered_transmissiontypes = data[data["CarModel"] == CarModel][
            "TransmissionType"
        ].unique()
        TransmissionType = st.selectbox("Transmission Type", filtered_transmissiontypes)

        filtered_No_of_Cylinders = data[data["CarModel"] == CarModel][
            "No of Cylinder"
        ].unique()
        No_of_Cylinder = st.selectbox("Number of Cylinders", filtered_No_of_Cylinders)

        filtered_seats = data[data["CarModel"] == CarModel]["Seats"].unique()
        Seats = st.selectbox("Number of Seats", filtered_seats)

        # Step 5: Calculate mean values for Mileage and Engine based on selected CarModel, VariantName, and FuelType
        filtered_data_mileage_engine = data[
            (data["CarModel"] == CarModel)
            & (data["VariantName"] == VariantName)
            & (data["FuelType"] == FuelType)
        ]

        if not filtered_data_mileage_engine.empty:
            mean_mileage = filtered_data_mileage_engine[
                "Mileage"
            ].mean()  # Mean Mileage
            mean_engine = filtered_data_mileage_engine[
                "Engine"
            ].mean()  # Mean Engine Capacity
            mean_model_year = filtered_data_mileage_engine["ModelYear"].mean()
        else:
            mean_mileage = 15.0  # Default value if no data is found
            mean_engine = 1200.0
            mean_model_year = 2000  # Default value if no data is found

        Mileage = st.number_input(
            "Mileage (km/l)",
            min_value=5.0,
            max_value=40.0,
            step=0.1,
            value=float(mean_mileage),
        )
        Engine = st.number_input(
            "Engine Capacity (cc)",
            min_value=600,
            max_value=5000,
            step=50,
            value=int(mean_engine),
        )
        ModelYear = st.number_input(
            "Model Year",
            min_value=1990,
            max_value=2024,
            step=1,
            value=int(mean_model_year),
        )
        AgeOfCar = 2024 - ModelYear

    # Expander for Other Details
    with st.expander("Other Details", expanded=True):
        st.header("Other Details")

        # Other inputs
        City = st.selectbox("City", cities)
        Insurance = st.selectbox("Insurance", insurances)
        KmsDriven = st.number_input(
            "Kilometers Driven", min_value=0, max_value=1000000, step=5000, value=100000
        )
        NumberOwner = st.selectbox("Number of Owners", [1, 2, 3, 4])

    # When the user clicks 'Predict Price'
    if st.button("Predict Price"):
        # Define new car data for prediction
        new_data = {
            "City": City,
            "FuelType": FuelType,
            "BodyType": BodyType,
            "TransmissionType": TransmissionType,
            "Insurance": Insurance,
            "Manufacturer": Manufacturer,
            "CarModel": CarModel,
            "VariantName": VariantName,
            "KmsDriven": KmsDriven,
            "NumberOwner": NumberOwner,
            "ModelYear": ModelYear,
            "Mileage": Mileage,
            "Engine": Engine,
            "No of Cylinder": No_of_Cylinder,
            "Seats": Seats,
            "AgeOfCar": AgeOfCar,
        }

        # Convert new data to a DataFrame
        new_data_df = pd.DataFrame([new_data])

        # Apply the same preprocessing used during training
        new_data_preprocessed = preprocessor.transform(new_data_df)

        # Predict the price
        predicted_price = loaded_model.predict(new_data_preprocessed)

        # Display the prediction
        st.write(f"### Predicted Price: ₹{predicted_price[0]:,.2f}")
