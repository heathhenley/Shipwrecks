# Shipwrecks
A simple single page app to display shipwrecks location in the New England area

## Data
The wreck data in the map was pulled from various sources on the web, the Beaver Tail Lighthouse Museum has a comprehensive database of wrecks, some with locations, at their [site](https://beavertaillight.org/wrecks/). Please refer to their site for more detailed information about a specific wreck, and be sure to check with them regarding how the data is allowed to be reproduced.

## Architecture
The app is currently a simple [Django](https://www.djangoproject.com/) app, the backend database is simply an sqlite file. The front end uses [Leaflet.js](https://leafletjs.com/) to render the map and plot the wrecks in the provided locations.

## Contributing
If you have a suggestion or bug report, please create an issue: https://github.com/heathhenley/Shipwrecks/issues/new 

To contribute to development:
- clone this project locally
- (probably in a virtual environement) install the requirements: `pip install -r requirements.txt' 
- run `python manage.py runserver' to start the project locally
- make your changes and submit a PR
*Note: please do not submit PRs for changes to the database data*
