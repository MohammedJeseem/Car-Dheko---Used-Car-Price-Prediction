# 🚗 Car Price Prediction App

This project is a **machine learning-based web application** developed using **Streamlit** to predict the price of used cars. The app allows users to input key features of a car, such as mileage, engine capacity, age, and transmission type, and generates an estimated price using a pre-trained **Random Forest Regressor** model.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Model Training and Tuning](#model-training-and-tuning)
- [Contributing](#contributing)

## Overview

The **Car Price Prediction App** enables users to predict the resale value of a car based on its features. The prediction is generated using a machine learning model trained on historical car sales data. The app is designed with an intuitive interface to make it easy for users to input car features and get immediate price predictions.

## Features

- **Input fields for car features**: 
  - Mileage (kmpl)
  - Engine capacity (cc)
  - Age of the car (years)
  - Transmission type (manual or automatic)
- **Real-time price prediction**: Users can get an instant prediction of the car's price based on the input features.
- **Interactive visualizations**: Display a bar chart showing the impact of each input feature on the prediction.
- **Streamlit UI**: A user-friendly interface for car price prediction.
- **Model Explanation**: The app includes a section that explains how the inputs influence the predicted price.
  
## Installation

### Prerequisites
- Python 3.x
- Streamlit
- scikit-learn
- Matplotlib
- Pandas
- Numpy
- Pillow (for image processing)

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/MohammedJeseem/Car-Dheko-Used-Car-Price-Prediction.git
   cd Car-Dheko-Used-Car-Price-Prediction
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Download the pre-trained model:
   - Ensure that the `random_forest_model.pkl` file (pre-trained Random Forest model) is placed in the project directory.

4. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```
5. Run the Streamlit app: (for all features)
   ```bash
   streamlit run app_final.py
   ```

## Usage

1. After starting the app, open the browser to access the app interface.
2. Input the following car features:
   - **Mileage**: Enter the car’s fuel efficiency in kilometers per liter.
   - **Engine**: Enter the engine capacity in cubic centimeters (cc).
   - **Age of Car**: Use the slider to select how old the car is in years.
   - **Transmission Type**: Choose between manual or automatic transmission.
3. Click the `Predict Car Price` button to view the predicted price.
4. A bar chart will display the impact of your inputs, and the predicted price will appear below the form.

## Model Training and Tuning

The model used in this project is a **Random Forest Regressor**, trained on historical car sales data. 

### Hyperparameter Tuning
Hyperparameters were optimized using **RandomizedSearchCV** for better model accuracy. The following hyperparameters were tuned:
- `n_estimators`: Number of trees in the forest.
- `max_depth`: Maximum depth of the tree.
- `min_samples_split`: Minimum number of samples required to split a node.
- `min_samples_leaf`: Minimum number of samples required to be at a leaf node.

### Feature Engineering
Key features used in the model include:
- Mileage
- Engine Capacity
- Age of Car
- Transmission Type (Manual/Automatic)

## Contributing

We welcome contributions to the project! To contribute:

1. Fork the repository.
2. Create a new branch for your feature (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -am 'Add a feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a pull request.
