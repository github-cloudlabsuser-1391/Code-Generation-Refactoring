const fetch = require('node-fetch');

const apiKey = 'YOUR_API_KEY';
const lat = 'YOUR_LATITUDE';
const lon = 'YOUR_LONGITUDE';

const getWeatherData = async () => {
    const url = `https://api.openweathermap.org/data/2.5/weather?lat=${lat}&lon=${lon}&appid=${apiKey}`;
    try {
        const response = await fetch(url);
        if (!response.ok) {
            throw new Error('Network response was not ok ' + response.statusText);
        }
        const data = await response.json();
        console.log(data);
    } catch (error) {
        console.error('There has been a problem with your fetch operation:', error);
    }
};

getWeatherData();