import requests as r


def sort(self, data, begin, finish):
    start = data.find(begin) + len(begin)
    end = data.find(finish)
    substring = data[start:end]
    return substring


def check(self, data, string1, string2):
    if string1 in str(data):
        info = sort(self, data, string1, string2)
        return info
    else:
        return 'None'


class wx:
    def metarMap(self, category):
        if category == 'VFR':
            return (0, 255, 0)
        if category == 'MVFR':
            return (0, 0, 255)
        if category == 'IFR':
            return (255, 0, 0)
        if category == 'LIFR':
            return (255, 20, 147)
        return (0, 255, 255)

    def __init__(self, airport):
        url = 'http://www.aviationweather.gov/adds/dataserver_current/httpparam?dataSource=metars&requestType=retrieve&format=xml&hoursBeforeNow=3&mostRecentForEachStation=true&stationString='
        self.name = airport.upper()
        self.data = r.get(url+self.name).text
        self.index = airport.index(self.name)
        self.url = url + airport.upper()
        self.raw = check(self, self.data, '<raw_text>', '</raw_text>')
        self.category = check(
            self, self.data, '<flight_category>', '</flight_category>')
        self.color = wx.metarMap(self, self.category)
        self.observation_time = check(
            self, self.data, '<observation_time>', '</observation_time>')
        self.temp = check(
            self, self.data, '<temp_c>', '</temp_c>')
        self.dewpoint = check(
            self, self.data, '<dewpoint_c>', '</dewpoint_c>')
        self.wind_direction = check(
            self, self.data, '<wind_dir_degrees>', '</wind_dir_degrees>')
        self.wind_speed = check(
            self, self.data, '<wind_speed_kt>', '</wind_speed_kt>')
        self.visibility = check(
            self, self.data, '<visibility_statute_mi>', '</visibility_statute_mi>')
        self.sea_level_pressure = check(
            self, self.data, '<sea_level_pressure_mb>', '</sea_level_pressure_mb>')
        self.altimeter = check(
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
        self.city = check(self, self.data, '<site>', '</site>')
        self.state = check(self, self.data, '<state>', '</state>')
        self.country = check(self, self.data, '<country>', '</country>')
        self.name = check(
            self, self.data, '<station_id>', '</station_id>')
        self.lat = check(self, self.data, '<latitude>', '</latitude>')
        self.long = check(
            self, self.data, '<longitude>', '</longitude>')
        self.elevation = 3.28084 * float(check(
            self, self.data, '<elevation_m>', '</elevation_m>'))

    def __repr__(self):
        return str('Ident: ' + self.ident + '\n' +
                   'City: ' + self.city + '\n' +
                   'State: ' + self.state + '\n' +
                   'Country: ' + self.country + '\n' +
                   'Name: ' + self.name + '\n' +
                   'Latitude: ' + self.lat + '\n' +
                   'Longitude: ' + self.long + '\n' +
                   'Elevation: ' + self.elevation + '\n'
                   )
