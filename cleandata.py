import csv
from datetime import date,time
import numpy as np 


ColNum = {
	"year" : 0,
	"month": 1,
	"day":2,
	"dayweek" : 3,
	"airline" :4,
	"flight_number":5,
	"tail_number":6,
	"origin_airport":7,
	"destination_airport":8,
	"scheduled_departure" : 9,#Heure programmée
	"departure_time":10,#Heure réelle de départ
	"departure_delay":11,#Délai entre les deux
	"taxi_out":12,#Aucune idée
	"wheels_off":13,#temps sans les roues
	"scheduled_time":14,#Surement temps de vol prévu
	"elapsed_time":15,
	"air_time":16,
	"distance":17,
	"wheels_on":18,
	"taxi_in":19,
	"scheduled_arrival":20,
	"arrival_time":21,
	"arrival_delay":22,
	"diverted":23,
	"cancelled":24,
	"cancel_reason":35,
	"air_system_delay":26,
	"security_delay":27,
	"airline_delay":28,
	"late_aircraft_delay":29,
	"weather_delay":30
}

columns =[
	"airline",
	"flight_number",
	"tail_number",
	"origin_airport",
	"destination_airport",
	"distance",
	"diverted",
	"cancelled",
	"scheduled_time"
]

columnsTime = [
	"scheduled_departure",
	"scheduled_arrival"
]


def preprocess():
	import csv 
	data = []
	data.append(["day"]+columns+columnsTime)

	with open('data/flights.csv', newline='') as f:
		reader = csv.reader(f)
		next(reader,None)
		cpt=0
		for row in reader:
			if row[ColNum["tail_number"]] == "":
				continue
				
			newdata=[]
			if int(row[ColNum["month"]]) > 1:
				break
			cpt= +cpt+1
			day = date(int(row[ColNum["year"]]),int(row[ColNum["month"]]),int(row[ColNum["day"]]))
			newdata.append(str(day))
			for col in columns :
				newdata.append(row[ColNum[col]])
			for col in columnsTime:
				value = row[ColNum[col]]
				hour = time(int(value[:1]),int(value[2:]))
				newdata.append(str(hour))

			data.append(newdata)
	print(data[len(data)-1])
	with open('data/adapted_flights.csv', 'w', newline='') as f:
	    writer = csv.writer(f)
	    writer.writerows(data)

if __name__ == '__main__':
	preprocess()
