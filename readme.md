# Weather Application

This project is a full-stack weather application that allows users to search for weather information of Chinese cities. 
It consists of a React frontend and a Flask backend API.

## Table of Contents

1. [Features](#features)
2. [Prerequisites](#prerequisites)
3. [Backend Setup](#backend-setup)
4. [Frontend Setup](#frontend-setup)
5. [Running the Application](#running-the-application)
6. [API Documentation](#api-documentation)
7. [Run unit test ](#test)

## Features

- Search weather information by city name
- Display of temperature, humidity, wind speed, and weather description
- User-friendly web interface
- RESTful API with Swagger documentation
- HTTPS support for secure communication

## Prerequisites

- Python 3.9.0
- Node.js 19.9.0
- npm 9.6.3
- OpenWeatherMap API key

## Backend Setup

1. Clone the repository:
   ```
   git clone https://github.com/fy658/Weather-Application.git
   cd Weather-Application
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   .\venv\Scripts\activate
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Generate SSL certificate for HTTPS:
   ```
   openssl req -x509 -newkey rsa:4096 -nodes -out cert.pem -keyout key.pem -days 365
   ```

## Frontend Setup

1. Navigate to the frontend directory:
   ```
   cd frontend
   ```

2. Install the required packages:
   ```
   npm install
   ```



## Running the Application

1. return root directory and start the backend server:
   ```
   cd ..
   python app.py
   ```

2. In a new terminal, start the frontend development server:
   ```
   cd frontend
   npm start
   ```

3. Open your browser and visit `http://localhost:3000` to use the application.
4. Please fill english name for Chinese cities such as shanghai in search box, then click Search button,
the result will display below.
 
## API Documentation

Once the backend is running, you can access the Swagger UI documentation at `https://localhost:5000/` to 
explore and test the API endpoints.


## Test
Please run the unit test in root directory.
   ```
   pytest test_app.py
   ```