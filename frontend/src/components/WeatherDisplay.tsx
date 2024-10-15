import React from 'react';

interface WeatherData {
  city: string;
  temperature: number;
  description: string;
  humidity: number;
  wind_speed: number;
}

interface WeatherDisplayProps {
  weatherData: WeatherData | null;
}

const WeatherDisplay: React.FC<WeatherDisplayProps> = ({ weatherData }) => {
  if (!weatherData) return null;

  return (
    <div style={{
      border: '1px solid #ccc',
      borderRadius: '4px',
      padding: '20px',
      backgroundColor: '#f9f9f9'
    }}>
      <h2 style={{
        margin: '0 0 15px 0',
        color: '#333'
      }}>
        {weatherData.city}
      </h2>
      <p style={{ margin: '10px 0' }}>Temperature: {weatherData.temperature}°C</p>
      <p style={{ margin: '10px 0' }}>Description: {weatherData.description}</p>
      <p style={{ margin: '10px 0' }}>Humidity: {weatherData.humidity}%</p>
      <p style={{ margin: '10px 0' }}>Wind Speed: {weatherData.wind_speed} m/s</p>
    </div>
  );
};

export default WeatherDisplay;