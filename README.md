
# Multiple Disease Prediction System

This project is a **Multiple Disease Prediction System** that uses machine learning models to predict whether a person has **Diabetes**, **Heart Disease**, or **Parkinson's Disease**. Built with **Streamlit** for an interactive web interface, it provides users with predictions based on input parameters for each disease.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Future Enhancements](#future-enhancements)
- [Acknowledgments](#acknowledgments)

## Overview

This project provides a user-friendly platform to predict diseases using three trained machine learning models:
- **Diabetes Prediction**
- **Heart Disease Prediction**
- **Parkinson's Disease Prediction**

Each model is loaded from a saved file and used to predict the likelihood of each disease based on the input features entered by the user.

## Features

- **Diabetes Prediction**: Predicts the likelihood of diabetes based on features like glucose level, blood pressure, BMI, and age.
- **Heart Disease Prediction**: Predicts the likelihood of heart disease using inputs like age, cholesterol, blood pressure, and heart rate.
- **Parkinson's Disease Prediction**: Predicts the presence of Parkinson's disease using voice-related parameters such as jitter, shimmer, and NHR (Noise-to-Harmonic Ratio).

## Technologies Used

- **Python**: For model development and backend functionality
- **Streamlit**: For creating the interactive web app
- **Scikit-Learn**: For loading and using machine learning models
- **Pickle**: For saving and loading trained models

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/multiple-disease-prediction-system.git
   ```
   
2. Change into the project directory:
   ```bash
   cd multiple-disease-prediction-system
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Ensure you have the saved models (`diabetes_model.sav`, `heart_disease_model.sav`, and `parkinsons_model.sav`) in the project directory.

5. Run the Streamlit application:
   ```bash
   streamlit run app.py
   ```

## Usage

1. Once the app is running, use the sidebar menu to navigate between different prediction pages:
   - **Diabetes Prediction**
   - **Heart Disease Prediction**
   - **Parkinson's Disease Prediction**

2. For each page, enter the required medical data.
3. Click on the prediction button to view the result, which will indicate whether the person is likely to have the disease.

## Project Structure

- `app.py` - The main application file, containing the code for the Streamlit interface and loading models.
- `diabetes_model.sav`, `heart_disease_model.sav`, `parkinsons_model.sav` - Saved machine learning models for each disease.
- `requirements.txt` - A list of required packages for setting up the environment.

## Future Enhancements

- Expand the model to include additional diseases.
- Improve the accuracy of predictions by training with larger datasets.
- Add user authentication for more secure and personalized predictions.
