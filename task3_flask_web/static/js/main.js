$(document).ready(function () {
    initializeApp();

    $('#randomWeatherBtn').click(getRandomWeather);
    $('#searchCityBtn').click(searchCity);
    $('#cityInput').keypress(function (e) {
        if (e.which === 13) {
            searchCity();
        }
    });
});

function initializeApp() {
    console.log('Weather Forecast App - Task 3 initialized');
    checkApiStatus();
    hideElements();
}

function checkApiStatus() {
    $.get('/api/status')
        .done(function (data) {
            console.log('API Status:', data);
            if (!data.api_key_configured) {
                showError('API key is not configured. Please check your config.py file.');
            }
        })
        .fail(function () {
            console.error('Failed to check API status');
        });
}

function getRandomWeather() {
    console.log('Getting random weather data...');

    showLoading();
    hideElements();

    $.ajax({
        url: '/api/random-weather',
        method: 'POST',
        contentType: 'application/json',
        success: function (response) {
            console.log('Random weather response:', response);
            displayRandomWeather(response);
            showSuccess('Weather data loaded successfully!');
        },
        error: function (xhr) {
            console.error('Error getting random weather:', xhr);
            const errorMsg = xhr.responseJSON?.error || 'Failed to fetch weather data';
            showError(errorMsg);
        },
        complete: function () {
            hideLoading();
        }
    });
}

function searchCity() {
    const city = $('#cityInput').val().trim();

    if (!city) {
        showError('Please enter a city name');
        return;
    }

    console.log('Searching weather for:', city);

    showLoading();
    hideElements();

    $.ajax({
        url: '/api/city-weather',
        method: 'POST',
        contentType: 'application/json',
        data: JSON.stringify({ city: city }),
        success: function (response) {
            console.log('City weather response:', response);
            displaySingleCityWeather(response);
            showSuccess(`Weather data for ${city} loaded successfully!`);
        },
        error: function (xhr) {
            console.error('Error getting city weather:', xhr);
            const errorMsg = xhr.responseJSON?.error || 'Failed to fetch weather data';
            showError(errorMsg);
        },
        complete: function () {
            hideLoading();
        }
    });
}

function displayRandomWeather(response) {
    const weatherData = response.weather_data;
    const statistics = response.statistics;

    $('#weatherCards').empty();

    weatherData.forEach(function (cityData, index) {
        const card = createWeatherCard(cityData);
        $('#weatherCards').append(card);

        setTimeout(function () {
            card.addClass('fade-in');
        }, index * 100);
    });

    displayStatistics(statistics);

    $('#resultsSection').show();
}

function displaySingleCityWeather(response) {
    const weatherData = response.weather_data;

    $('#weatherCards').empty();

    const singleCityCard = createSingleCityCard(weatherData);
    $('#weatherCards').append(singleCityCard);

    setTimeout(function () {
        singleCityCard.addClass('fade-in');
    }, 100);

    $('#statisticsSection').hide();

    $('#resultsSection').show();
}

function createWeatherCard(cityData) {
    const template = $('#weatherCardTemplate').html();
    const card = $(template);

    card.find('.city').text(cityData.name);
    card.find('.country').text(cityData.sys.country);
    card.find('.temp-value').text(Math.round(cityData.main.temp));
    card.find('.feels-value').text(Math.round(cityData.main.feels_like));
    card.find('.condition-text').text(cityData.weather[0].description);
    card.find('.humidity').text(cityData.main.humidity);
    card.find('.pressure').text(cityData.main.pressure);
    card.find('.wind-speed').text(cityData.wind.speed);

    const weatherIcon = getWeatherIcon(cityData.weather[0].main);
    card.find('.weather-icon i').removeClass().addClass(weatherIcon);

    return card;
}

function createSingleCityCard(cityData) {
    const template = $('#singleCityTemplate').html();
    const card = $(template);

    card.find('.city-name').text(`${cityData.name}, ${cityData.sys.country}`);
    card.find('.temp-value').text(Math.round(cityData.main.temp));
    card.find('.feels-value').text(Math.round(cityData.main.feels_like));
    card.find('.condition-text').text(cityData.weather[0].description);
    card.find('.humidity').text(cityData.main.humidity);
    card.find('.pressure').text(cityData.main.pressure);
    card.find('.wind-speed').text(cityData.wind.speed);

    const weatherIcon = getWeatherIcon(cityData.weather[0].main);
    card.find('.weather-icon i').removeClass().addClass(weatherIcon);

    return card;
}

function displayStatistics(statistics) {
    const statsHtml = `
        <div class="row">
            <div class="col-md-4">
                <div class="stat-item text-center">
                    <div class="stat-value">${statistics.coldest_city}</div>
                    <div class="stat-label">Coldest City</div>
                </div>
            </div>
            <div class="col-md-4">
                <div class="stat-item text-center">
                    <div class="stat-value">${Math.round(statistics.coldest_temperature)}°C</div>
                    <div class="stat-label">Coldest Temperature</div>
                </div>
            </div>
            <div class="col-md-4">
                <div class="stat-item text-center">
                    <div class="stat-value">${Math.round(statistics.average_temperature)}°C</div>
                    <div class="stat-label">Average Temperature</div>
                </div>
            </div>
        </div>
    `;

    $('#statisticsContent').html(statsHtml);
    $('#statisticsSection').show();
}

function getWeatherIcon(weatherMain) {
    const iconMap = {
        'Clear': 'bi bi-sun display-4 text-warning',
        'Clouds': 'bi bi-cloud display-4 text-secondary',
        'Rain': 'bi bi-cloud-rain display-4 text-primary',
        'Drizzle': 'bi bi-cloud-drizzle display-4 text-info',
        'Thunderstorm': 'bi bi-cloud-lightning display-4 text-danger',
        'Snow': 'bi bi-snow display-4 text-light',
        'Mist': 'bi bi-cloud-fog display-4 text-muted',
        'Fog': 'bi bi-cloud-fog display-4 text-muted',
        'Haze': 'bi bi-cloud-haze display-4 text-muted'
    };

    return iconMap[weatherMain] || 'bi bi-cloud-sun display-4 text-warning';
}

function showLoading() {
    $('#progressContainer').show();
    $('button').prop('disabled', true);
    $('input').prop('disabled', true);
}

function hideLoading() {
    $('#progressContainer').hide();
    $('button').prop('disabled', false);
    $('input').prop('disabled', false);
}

function showError(message) {
    $('#errorMessage').text(message);
    $('#errorAlert').show();
    $('#successAlert').hide();

    setTimeout(function () {
        $('#errorAlert').fadeOut();
    }, 5000);
}

function showSuccess(message) {
    $('#successMessage').text(message);
    $('#successAlert').show();
    $('#errorAlert').hide();

    setTimeout(function () {
        $('#successAlert').fadeOut();
    }, 3000);
}

function hideElements() {
    $('#resultsSection').hide();
    $('#errorAlert').hide();
    $('#successAlert').hide();
}
