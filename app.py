from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_restx import Api, Resource, fields
import requests
from dotenv import load_dotenv
import os
from urllib.parse import quote

load_dotenv()

app = Flask(__name__)
CORS(app)
api = Api(app, version='1.0', title='Weather API',
          description='A simple Weather API for Chinese cities')

ns = api.namespace('api', description='Weather operations')

weather_model = api.model('Weather', {
    'city': fields.String(required=True, description='City name'),
    'temperature': fields.Float(description='Temperature in Celsius'),
    'description': fields.String(description='Weather description'),
    'humidity': fields.Float(description='Humidity percentage'),
    'wind_speed': fields.Float(description='Wind speed in m/s')
})

OPENWEATHERMAP_API_KEY = "9b88f181ab504ad2eab4fe335df9b87f"
OPENWEATHERMAP_API_URL = "http://api.openweathermap.org/data/2.5/weather"


@ns.route('/weather')
class WeatherResource(Resource):
    @ns.doc(params={'city': 'City name'})
    @ns.response(model=weather_model, code=200, description='Success')
    @ns.response(code=400, description='Validation Error')
    @ns.response(code=500, description='Internal Server Error')
    def get(self):
        # Get the city parameter from query string
        city = request.args.get('city')
        if not city:
            return {'error': "City parameter is required"}, 400

        try:
            # Prepare API request parameters
            params = {
                "q": f"{quote(city)},CN",
                "appid": OPENWEATHERMAP_API_KEY,
                "units": "metric"
            }
            # Send request to OpenWeatherMap API
            response = requests.get(OPENWEATHERMAP_API_URL, params=params)
            response.raise_for_status()
            weather_data = response.json()

            # Return processed weather data
            return {
                "city": weather_data["name"],
                "temperature": weather_data["main"]["temp"],
                "description": weather_data["weather"][0]["description"],
                "humidity": weather_data["main"]["humidity"],
                "wind_speed": weather_data["wind"]["speed"]
            }
        except requests.RequestException as e:
            # Handle API request errors
            return {'error': "Failed to fetch weather data"}, 500


if __name__ == "__main__":
    # Check if certificate files exist
    if not os.path.exists("cert.pem") or not os.path.exists("key.pem"):
        print("Certificate files not found. Please run generate_cert.py first.")
        # Run without HTTPS for testing
        app.run(debug=True)
    else:
        # Run the application with HTTPS
        app.run(debug=True, ssl_context=('cert.pem', 'key.pem'))