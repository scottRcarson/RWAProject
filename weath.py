# Have a pro subscription? Then use:
# owm = pyowm.OWM(API_key='your-API-key')
import pyowm
from urllib2 import urlopen
import win_inet_pton
from geoip import geolite2
my_ip = urlopen('http://ip.42.pl/raw').read()
match = geolite2.lookup(my_ip)
print(my_ip)
print(match)
print(match.location[0])
print(isinstance(match.location[0],str))
owm = pyowm.OWM('14963a49f9571f300dd0d464fa4e5c2e')  # You MUST provide a valid API key

# Have a pro subscription? Then use:
# owm = pyowm.OWM(API_key='your-API-key', subscription_type='pro')

# Will it be sunny tomorrow at this time in Milan (Italy) ?
forecast = owm.daily_forecast("Milan,it")
tomorrow = pyowm.timeutils.tomorrow()
forecast.will_be_sunny_at(tomorrow)  # Always True in Italy, right? ;-)

# Search for current weather in London (UK)
# observation = owm.weather_around_coords(match.location[0], match.location[1])
observation = owm.weather_at_coords(match.location[0], match.location[1])
print(observation)
# reg = owm.city_id_registry()
# print(reg.ids_for('Wanaque'))
w = observation.get_weather()
print(w)
print(w.get_sunset_time('iso'))
print(observation.get_location())
    # <Weather - reference time=2013-12-18 09:20,
                              # status=Clouds>

# Weather details
print "cat"
print(w.get_wind())                 # {'speed': 4.6, 'deg': 330}
print(w.get_humidity())             # 87
print(w.get_temperature('fahrenheit'))  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}

# Search current weather observations in the surroundings of
# lat=22.57W, lon=43.12S (Rio de Janeiro, BR)
observation_list = owm.weather_around_coords(-22.57, -43.12)
# Will it be sunny tomorrow at this time in Milan (Italy) ?
forecast = owm.daily_forecast(observation.get_location().get_name())
# print(forecast.get_weather_at("2017-09-06 12:00:00+00"))
tomorrow = pyowm.timeutils.tomorrow()
forecast.will_be_sunny_at(tomorrow)  # Always True in Italy, right? ;-)

# Search for current weather in London (UK)
observation = owm.weather_at_place('London,uk')
w = observation.get_weather()