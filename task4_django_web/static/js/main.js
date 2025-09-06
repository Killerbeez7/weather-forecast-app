$(document).ready(function () {
    'use strict';

    let isLoading = false;

    initializeApp();

    function initializeApp() {
        console.log('🌤️ Weather Forecast App - Task 4 (Django) Initialized');

        bindEventHandlers();

        checkApiStatus();

        $('main').addClass('fade-in-up');
    }

    function bindEventHandlers() {
        // Random weather button
        $('#randomWeatherBtn').on('click', function () {
            if (!isLoading) {
                getRandomWeather();
            }
        });

        // City search form
        $('#citySearchForm').on('submit', function (e) {
            e.preventDefault();
            if (!isLoading) {
                searchCityWeather();
            }
        });

        // Enter key in city input
        $('#cityInput').on('keypress', function (e) {
            if (e.which === 13) { // Enter key
                e.preventDefault();
                if (!isLoading) {
                    searchCityWeather();
                }
            }
        });

        setTimeout(function () {
            $('.alert').fadeOut();
        }, 5000);
    }


    function checkApiStatus() {
        $.ajax({
            url: '/api/status/',
            method: 'GET',
            dataType: 'json',
            success: function (response) {
                console.log('API Status:', response);
                if (response.api_key_configured) {
                    $('#randomWeatherBtn, #searchCityBtn').prop('disabled', false);
                }
            },
            error: function (xhr, status, error) {
                console.error('API Status Check Failed:', error);
            }
        });
    }

    function getRandomWeather() {
        if (isLoading) return;

        isLoading = true;
        showLoading();
        hideAlerts();

        $.ajax({
            url: '/api/random-weather/',
            method: 'POST',
            dataType: 'json',
            headers: {
                'X-CSRFToken': $('[name=csrfmiddlewaretoken]').val()
            },
            success: function (response) {
                console.log('Random Weather Response:', response);
                if (response.success) {
                    displayWeatherCards(response.weather_data);
                    displayStatistics(response.statistics);
                    showSuccess('Successfully fetched weather for 5 random cities!');
                } else {
                    showError(response.error || 'Failed to fetch weather data');
                }
            },
            error: function (xhr, status, error) {
                console.error('Random Weather Error:', error);
                let errorMessage = 'Failed to fetch weather data';

                if (xhr.responseJSON && xhr.responseJSON.error) {
                    errorMessage = xhr.responseJSON.error;
                } else if (xhr.status === 400) {
                    errorMessage = 'API key not configured';
                } else if (xhr.status === 500) {
                    errorMessage = 'Server error occurred';
                }

                showError(errorMessage);
            },
            complete: function () {
                isLoading = false;
                hideLoading();
            }
        });
    }

    function searchCityWeather() {
        if (isLoading) return;

        const city = $('#cityInput').val().trim();
        if (!city) {
            showError('Please enter a city name');
            return;
        }

        isLoading = true;
        showLoading();
        hideAlerts();

        $.ajax({
            url: '/api/city-weather/',
            method: 'POST',
            dataType: 'json',
            headers: {
                'X-CSRFToken': $('[name=csrfmiddlewaretoken]').val(),
                'Content-Type': 'application/json'
            },
            data: JSON.stringify({
                city: city
            }),
            success: function (response) {
                console.log('City Weather Response:', response);
                if (response.success) {
                    displaySingleCityWeather(response.weather_data);
                    showSuccess(`Successfully fetched weather for ${city}!`);
                    $('#cityInput').val(''); // Clear input
                } else {
                    showError(response.error || `Failed to fetch weather for ${city}`);
                }
            },
            error: function (xhr, status, error) {
                console.error('City Weather Error:', error);
                let errorMessage = `Failed to fetch weather for ${city}`;

                if (xhr.responseJSON && xhr.responseJSON.error) {
                    errorMessage = xhr.responseJSON.error;
                } else if (xhr.status === 400) {
                    errorMessage = 'API key not configured or invalid city name';
                } else if (xhr.status === 404) {
                    errorMessage = `City "${city}" not found`;
                } else if (xhr.status === 500) {
                    errorMessage = 'Server error occurred';
                }

                showError(errorMessage);
            },
            complete: function () {
                isLoading = false;
                hideLoading();
            }
        });
    }

    function displayWeatherCards(weatherData) {
        const container = $('#weatherCards');
        container.empty();

        weatherData.forEach(function (data, index) {
            const card = createWeatherCard(data);
            card.addClass('fade-in-up');
            card.css('animation-delay', (index * 0.1) + 's');
            container.append(card);
        });

        $('#resultsSection').show();
        $('html, body').animate({
            scrollTop: $('#resultsSection').offset().top - 100
        }, 800);
    }

    function displaySingleCityWeather(weatherData) {
        const container = $('#weatherCards');
        container.empty();

        const card = createSingleCityCard(weatherData);
        card.addClass('fade-in-up');
        container.append(card);

        $('#resultsSection').show();
        $('html, body').animate({
            scrollTop: $('#resultsSection').offset().top - 100
        }, 800);
    }

    function createWeatherCard(data) {
        const template = $('#weatherCardTemplate').html();
        const card = $(template);

        // Populate card data
        card.find('.city').text(data.name);
        card.find('.country').text(data.sys.country);
        card.find('.temp-value').text(Math.round(data.main.temp));
        card.find('.feels-value').text(Math.round(data.main.feels_like));
        card.find('.condition-text').text(data.weather[0].description);
        card.find('.humidity').text(data.main.humidity);
        card.find('.pressure').text(data.main.pressure);
        card.find('.wind-speed').text(data.wind.speed);

        // Set weather icon based on condition
        const weatherIcon = getWeatherIcon(data.weather[0].main);
        card.find('.weather-icon i').removeClass().addClass('bi ' + weatherIcon + ' display-4 text-warning');

        return card;
    }


    function createSingleCityCard(data) {
        const template = $('#singleCityTemplate').html();
        const card = $(template);

        // Populate card data
        card.find('.city-name').text(data.name + ', ' + data.sys.country);
        card.find('.temp-value').text(Math.round(data.main.temp));
        card.find('.feels-value').text(Math.round(data.main.feels_like));
        card.find('.condition-text').text(data.weather[0].description);
        card.find('.humidity').text(data.main.humidity);
        card.find('.pressure').text(data.main.pressure);
        card.find('.wind-speed').text(data.wind.speed);

        // Set weather icon based on condition
        const weatherIcon = getWeatherIcon(data.weather[0].main);
        card.find('.weather-icon i').removeClass().addClass('bi ' + weatherIcon + ' display-1 text-warning');

        return card;
    }


    function getWeatherIcon(condition) {
        const iconMap = {
            'Clear': 'bi-sun',
            'Clouds': 'bi-cloud',
            'Rain': 'bi-cloud-rain',
            'Drizzle': 'bi-cloud-drizzle',
            'Thunderstorm': 'bi-cloud-lightning',
            'Snow': 'bi-snow',
            'Mist': 'bi-cloud-fog',
            'Fog': 'bi-cloud-fog',
            'Haze': 'bi-cloud-haze',
            'Dust': 'bi-cloud-haze',
            'Sand': 'bi-cloud-haze',
            'Ash': 'bi-cloud-haze',
            'Squall': 'bi-wind',
            'Tornado': 'bi-tornado'
        };

        return iconMap[condition] || 'bi-cloud-sun';
    }


    function displayStatistics(stats) {
        if (stats.error) {
            $('#statisticsSection').hide();
            return;
        }

        const content = `
            <div class="row">
                <div class="col-md-4 text-center">
                    <div class="mb-3">
                        <i class="bi bi-snow display-4 text-primary"></i>
                        <h5 class="mt-2">Coldest City</h5>
                        <h4 class="text-primary">${stats.coldest_city}</h4>
                        <p class="text-muted">${Math.round(stats.coldest_temperature)}°C</p>
                    </div>
                </div>
                <div class="col-md-4 text-center">
                    <div class="mb-3">
                        <i class="bi bi-thermometer display-4 text-info"></i>
                        <h5 class="mt-2">Average Temperature</h5>
                        <h4 class="text-info">${Math.round(stats.average_temperature * 10) / 10}°C</h4>
                        <p class="text-muted">Across all cities</p>
                    </div>
                </div>
                <div class="col-md-4 text-center">
                    <div class="mb-3">
                        <i class="bi bi-globe display-4 text-success"></i>
                        <h5 class="mt-2">Total Cities</h5>
                        <h4 class="text-success">${stats.total_cities}</h4>
                        <p class="text-muted">Cities analyzed</p>
                    </div>
                </div>
            </div>
        `;

        $('#statisticsContent').html(content);
        $('#statisticsSection').show();
    }

    function showLoading() {
        $('#progressContainer').show();
        $('#randomWeatherBtn, #searchCityBtn').prop('disabled', true).addClass('loading');
    }


    function hideLoading() {
        $('#progressContainer').hide();
        $('#randomWeatherBtn, #searchCityBtn').prop('disabled', false).removeClass('loading');
    }


    function showSuccess(message) {
        $('#successMessage').text(message);
        $('#successAlert').show().addClass('fade-in-up');


        setTimeout(function () {
            $('#successAlert').fadeOut();
        }, 5000);
    }


    function showError(message) {
        $('#errorMessage').text(message);
        $('#errorAlert').show().addClass('fade-in-up');


        setTimeout(function () {
            $('#errorAlert').fadeOut();
        }, 8000);
    }


    function hideAlerts() {
        $('#successAlert, #errorAlert').hide();
    }


    function formatTemperature(temp) {
        return Math.round(temp * 10) / 10;
    }


    function formatWindSpeed(speed) {
        return Math.round(speed * 10) / 10;
    }


    $('a[href^="#"]').on('click', function (e) {
        e.preventDefault();
        const target = $(this.getAttribute('href'));
        if (target.length) {
            $('html, body').animate({
                scrollTop: target.offset().top - 100
            }, 800);
        }
    });


    $('[data-bs-toggle="tooltip"]').tooltip();


    $('[data-bs-toggle="popover"]').popover();


    $(window).on('resize', function () {
        // Adjust layout if needed
        if ($(window).width() < 768) {
            $('.weather-card').removeClass('h-100');
        } else {
            $('.weather-card').addClass('h-100');
        }
    });


    $(document).on('keydown', function (e) {
        // Ctrl/Cmd + R for random weather
        if ((e.ctrlKey || e.metaKey) && e.key === 'r') {
            e.preventDefault();
            if (!isLoading) {
                getRandomWeather();
            }
        }

        // Escape to clear results
        if (e.key === 'Escape') {
            $('#resultsSection').fadeOut();
            hideAlerts();
        }
    });

    console.log('✅ Weather Forecast App - Task 4 (Django) Ready!');
});
