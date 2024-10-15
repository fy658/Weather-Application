import axios from 'axios';

const API_URL = process.env.REACT_APP_API_URL || 'http://localhost:5000/api';

export const getWeather = async (city: string) => {
  try {
    const response = await axios.get(`${API_URL}/weather`, {
      params: { city }
    });
    return response.data;
  } catch (error) {
    console.error('Error fetching weather data:', error);
    throw error;
  }
};