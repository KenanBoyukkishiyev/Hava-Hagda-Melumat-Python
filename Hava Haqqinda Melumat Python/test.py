import pyowm
city=input('Sizi hansi sher maraglandirir? : ')
owm=pyowm.OWM('e4b796328673811095c29edf76bf2e36')
observation = owm.weather_at_place(city)
w = observation.get_weather()
temperature=w.get_temperature('celsius')['temp']
wind=w.get_wind() ['speed']
humidity=w.get_humidity() 
detalied=w.get_detailed_status()
print("bu sherde " + city + " tempuraturu ise " + str(temperature) + " Selsiya " + " Kuleyin sureti ise " + str(wind) + " Rutubeti ise " + str(humidity))
print("secdiyiniz seherde " + str(detalied))