import React, { useState } from 'react';

// Define the shape of our weather data
interface WeatherData {
  city: string;
  temperature: number;
  description: string;
  humidity: number;
  wind_speed: number;
}

const App: React.FC = () => {
  const [city, setCity] = useState('');
  const [weatherData, setWeatherData] = useState<WeatherData | null>(null);
  const [error, setError] = useState('');

  const handleSearch = async (e: React.FormEvent) => {
    e.preventDefault();
    setError('');
    setWeatherData(null);

    try {
      const response = await fetch(`http://localhost:5000/api/weather?city=${encodeURIComponent(city)}`);
      if (!response.ok) {
        throw new Error('Failed to fetch weather data');
      }
      const data: WeatherData = await response.json();
      setWeatherData(data);
    } catch (err) {
      setError('Failed to fetch weather data. Please try again.');
    }
  };

  return (
    <div style={{ fontFamily: 'Arial, sans-serif', maxWidth: '600px', margin: '0 auto', padding: '20px' }}>
      <header style={{ backgroundColor: '#3f51b5', color: 'white', padding: '1rem', textAlign: 'center', marginBottom: '20px' }}>
        <h1 style={{ margin: 0, fontSize: '1.5rem' }}>Weather App</h1>
      </header>

      <form onSubmit={handleSearch} style={{ display: 'flex', gap: '10px', marginBottom: '20px' }}>
        <input
          type="text"
          value={city}
          onChange={(e) => setCity(e.target.value)}
          placeholder="Enter city name"
          style={{
            flex: '1',
            padding: '10px',
            fontSize: '16px',
            border: '1px solid #ccc',
            borderRadius: '4px'
          }}
        />
        <button
          type="submit"
          style={{
            padding: '10px 20px',
            fontSize: '16px',
            backgroundColor: '#4CAF50',
            color: 'white',
            border: 'none',
            borderRadius: '4px',
            cursor: 'pointer'
          }}
        >
          Search
        </button>
      </form>

      {error && (
        <p style={{ color: 'red', textAlign: 'center' }}>{error}</p>
      )}

      {weatherData && (
        <div style={{ marginTop: '2rem', border: '1px solid #ccc', padding: '1rem', borderRadius: '4px' }}>
          <h3>{weatherData.city}</h3>
          <p>Temperature: {weatherData.temperature}°C</p>
          <p>Description: {weatherData.description}</p>
          <p>Humidity: {weatherData.humidity}%</p>
          <p>Wind Speed: {weatherData.wind_speed} m/s</p>
        </div>
      )}
    </div>
  );
};

export default App;