Car Price Prediction using Machine Learning

A simple Car Price Prediction web application built with Python, Machine Learning, Pandas, and Streamlit. The application takes car details from the user and predicts the estimated selling price using a pre-trained machine learning model.

Project Overview

This project provides an interactive Streamlit interface where users can enter:

Car brand

Manufacturing year

Driven kilometers

Fuel type

Selling type

Transmission

Number of previous owners

The entered values are converted into the numerical format expected by the trained model, and the application displays the predicted car price.

Project Files

.
├── app.py
├── cardata.csv
├── model.pkl
├── Untitled1.ipynb
└── README.md

File Description

File

Description

app.py

Streamlit application that collects inputs and predicts the car price

cardata.csv

Car dataset used by the application

model.pkl

Saved/pre-trained machine learning model

Untitled1.ipynb

Jupyter Notebook containing the project/model development work

README.md

Project documentation

The Streamlit app loads the saved model from model.pkl and the car data from cardata.csv. fileciteturn1file0L10-L19

Features

Interactive Streamlit user interface

Car-brand selection

Manufacturing-year slider

Driven-kilometers slider

Fuel-type selection

Selling-type selection

Transmission selection

Owner selection

Machine-learning-based price prediction

These input fields are implemented directly in the Streamlit application. fileciteturn1file0L26-L34

Technologies Used

Python

Pandas

NumPy

Streamlit

Pickle

Machine Learning

How It Works

The application loads the trained model using Pickle.

The car dataset is loaded using Pandas.

Car names are converted to brand names.

The user selects the required car details.

Categorical values such as fuel type, selling type, transmission, and owner are converted into numerical values.

The processed input is passed to the trained model.

The predicted car price is displayed in the Streamlit application.

The preprocessing and prediction steps are implemented in app.py. fileciteturn1file0L21-L24 fileciteturn1file0L34-L50

Installation

Make sure Python is installed on your system.

Install the required libraries:

pip install pandas numpy streamlit

Run the Project

Keep app.py, cardata.csv, and model.pkl in the same project folder.

Then run:

streamlit run app.py

The Streamlit application will open in your browser.

Usage

Start the Streamlit application.

Select the car brand.

Select the manufacturing year.

Enter/select the driven kilometers.

Select the fuel type.

Select the selling type.

Select the transmission type.

Select the number of previous owners.

Click Predict Price.

View the predicted car price.

The application displays the prediction after calling the trained model. fileciteturn1file0L34-L52

Project Purpose

The purpose of this project is to demonstrate how a trained machine learning model can be integrated into an interactive web application using Streamlit for practical car-price prediction.

Author

Gagan

