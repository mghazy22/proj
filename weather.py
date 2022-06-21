import json
import requests
class weather:
    url='http://api.weatherapi.com/v1/'
    def __init__(self,city):
        self.city=city
    @property
    def get_currdata(self):
        resp_api = requests.get(f'{self.url}current.json?key=f5dce8891ed54e2285d124629220306&q={self.city}')
        data = resp_api.text
        pp = json.loads(data)
        return pp

    def get_current_temperature(self):
        newcurr=self.get_currdata
        curr=newcurr['current']['temp_c']
      #  curr=newcurr['current']
        print(f'Current Temp. = {curr}')


    def get_temperature_after(self,days, hour=None):
        resp_api = requests.get(f'{self.url}forecast.json?key=f5dce8891ed54e2285d124629220306&q={self.city}&days={days}')
        data = resp_api.text
        pp = json.loads(data)
        print(pp['forecast']['forecastday'])


    def get_lat_and_long(self):
        newlong=self.get_currdata
        lat=newlong['location']['lat']
        lon=newlong['location']['lon']
        print(f'Latitude = {lat} and Longitude={lon}')


w1=weather('cairo')
#w1.get_current_temperature()
#w1.get_lat_and_long()
w1.get_temperature_after(7)



  #  response_api=requests.get('current.jsoncairo')
