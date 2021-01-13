import requests as r
import utils as u


class wx:
    def __init__(self, airport):
        url = 'http://www.aviationweather.gov/adds/dataserver_current/httpparam?dataSource=metars&requestType=retrieve&format=xml&hoursBeforeNow=3&mostRecentForEachStation=true&stationString='
        self.name = airport.upper()
        self.data = r.get(url+self.name).text
        self.index = airport.index(self.name)
        self.url = url + airport.upper()
        self.raw = u.Utils.check(self, self.data, '<raw_text>', '</raw_text>')
        self.category = u.Utils.check(
            self, self.data, '<flight_category>', '</flight_category>')
        self.color = u.Utils.color(self, self.category)
        self.observation_time = u.Utils.check(
            self, self.data, '<observation_time>', '</observation_time>')
        self.temp = u.Utils.check(
            self, self.data, '<temp_c>', '</temp_c>')
        self.dewpoint = u.Utils.check(
            self, self.data, '<dewpoint_c>', '</dewpoint_c>')
        self.wind_direction = u.Utils.check(
            self, self.data, '<wind_dir_degrees>', '</wind_dir_degrees>')
        self.wind_speed = u.Utils.check(
            self, self.data, '<wind_speed_kt>', '</wind_speed_kt>')
        self.visibility = u.Utils.check(
            self, self.data, '<visibility_statute_mi>', '</visibility_statute_mi>')
        self.sea_level_pressure = u.Utils.check(
            self, self.data, '<sea_level_pressure_mb>', '</sea_level_pressure_mb>')
        self.altimeter = u.Utils.check(
            self, self.data, '<altim_in_hg>', '</altim_in_hg>')

    def __repr__(self):
        return str('Name: ' + self.name + '\n' +
                   'Index: ' + str(self.index) + '\n' +
                   'URL: ' + self.url + '\n' +
                   'Raw: ' + self.raw + '\n' +
                   'Category: ' + self.category + '\n' +
                   'Color: ' + str(self.color) + '\n' +
                   'Time: ' + self.observation_time + '\n' +
                   'Temp: ' + str(self.temp) + '\n' +
                   'Dewpoint: ' + str(self.dewpoint) + '\n' +
                   'Wind Direction: ' + str(self.wind_direction) + '\n' +
                   'Wind Speed: ' + str(self.wind_speed) + '\n' +
                   'Visibility: ' + str(self.visibility) + '\n' +
                   'SLP: ' + str(self.sea_level_pressure) + '\n' +
                   'Baro: ' + str(self.altimeter) + '\n' + '\n'
                   )


class info:
    def __init__(self, airport):
        url = 'https://www.aviationweather.gov/adds/dataserver_current/httpparam?dataSource=stations&requestType=retrieve&format=xml&stationString='
        self.ident = airport.upper()
        self.data = r.get(url+self.ident).text
        self.city = u.Utils.check(self, self.data, '<site>', '</site>')
        self.state = u.Utils.check(self, self.data, '<state>', '</state>')
        self.country = u.Utils.check(
            self, self.data, '<country>', '</country>')
        self.name = u.Utils.check(
            self, self.data, '<station_id>', '</station_id>')
        self.lat = u.Utils.check(self, self.data, '<latitude>', '</latitude>')
        self.long = u.Utils.check(
            self, self.data, '<longitude>', '</longitude>')
        self.elevation = u.Utils.check(
            self, self.data, '<elevation_m>', '</elevation_m>')

    def __repr__(self):
        return str('Ident: ' + str(self.ident) + '\n' +
                   'City: ' + str(self.city) + '\n' +
                   'State: ' + str(self.state) + '\n' +
                   'Country: ' + str(self.country) + '\n' +
                   'Name: ' + str(self.name) + '\n' +
                   'Latitude: ' + str(self.lat) + '\n' +
                   'Longitude: ' + str(self.long) + '\n' +
                   'Elevation: ' + str(self.elevation) + '\n'
                   )

