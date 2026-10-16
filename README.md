# Student Performance Prediction

A web application that predicts expected student exam marks based on daily study hours, attendance percentage, and previous exam marks using a Linear Regression model.

## Features
- **Machine Learning Model**: Built with scikit-learn (Linear Regression).
- **Backend API**: Built with Flask and Flask-CORS.
- **Frontend UI**: Clean, responsive interface for user inputs and instant prediction results.

## Project Structure
- model.py: Trains the regression model and serializes it to model.pkl.
- pp.py: Flask REST API serving prediction endpoints.
- index.html: Client-side interface to send requests to the API.
- equirements.txt: Python dependencies.

## Getting Started

### 1. Install Dependencies
`ash
pip install -r requirements.txt
`

### 2. Train the Model (Optional)
`ash
python model.py
`

### 3. Start the Flask Server
`ash
python app.py
`

### 4. Open the Frontend
Open index.html in your browser and enter student data to get predictions.
