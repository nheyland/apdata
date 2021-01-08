# APData
An open source package to get live information about airports and weather data

Docs
ap.wx(airport).*
    *.name
    *.data
    *.index
    *.url
    *.raw
    *.category
    *.color
    *.observation_time
    *.temp
    *.dewpoint
    *.wind_direction
    *.wind_speed
    *.visibility
    *.sea_level_pressure
    *.altimeter

ap.info(airport).*
    *.ident
    *.data
    *.city
    *.state
    *.country
    *.name
    *.lat
    *.long
    *.elevation
Ex:
import ap
print(ap.info('KPSM').state)
