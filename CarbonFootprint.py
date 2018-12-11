def CarbonFootprint(file):

	from geopy.geocoders import Nominatim
	from geopy.distance import geodesic
	import pandas

	data = pandas.read_csv(file, names=['Origin','Destination'], delimiter=';',dtype=None)

	#Origin = ["Paris"]
	#Destination = ["New York"]
	Total = 0

	for i in range(len(data['Origin'])):

		geolocator = Nominatim(user_agent="specify_your_app_name_here")

		location1 = geolocator.geocode(data['Origin'][i])
		#print(location1.latitude, location1.longitude)

		location2 = geolocator.geocode(data['Destination'][i])
		#print(location2.latitude, location2.longitude)

		#print(data['Origin'][i] + "-->" + data['Destination'] + " in kilometers")
		dist = geodesic((location1.latitude, location1.longitude),(location2.latitude, location2.longitude)).miles/0.62137
		if dist < 1500:
			Total = Total + (2*dist)*0.15 #short-flights - in Co2 kg /eq_passenger/km 
		else: 
			Total = Total + (2*dist)*0.12 #long-flights  - in Co2 kg /eq_passenger/km
		
	print('Total Carbon footprint in tons CO2:')
	print(Total/1000.)
	print('Total Carbon footprint in tons CO2 including radiative forcing:')
	print(Total/1000.)*1.891 	# (as recommended by the Department for Environment, Food & Rural Affairs)

