import csv
from datetime import *
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
	"elapsed_time",
]

columnsTime = [
	"departure_time",
	"arrival_time"
]


def mytime(value):
	v = value[:2]
	#if v == "00":
	#	v="24"
	return v+":"+value[2:]+":00" 

def preprocess():
	import csv 
	data = []
	data.append(["delay"]+columns+columnsTime+["day"])

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
			cpt= cpt+1
			day = int(row[ColNum["day"]])
			year = int(row[ColNum["year"]])
			month=int(row[ColNum["month"]])
			actualdate = date(year,month,day)
			delay = int(row[ColNum["arrival_delay"]]) - int(row[ColNum["departure_delay"]]) if row[ColNum["arrival_delay"]] !="" else 0
			newdata.append(str(delay))
			for col in columns :
				if col != "elapsed_time":
					newdata.append(row[ColNum[col]])
				else : 
					newdata.append(row[ColNum[col]]) if row[ColNum[col]] != "" else newdata.append(row[ColNum["scheduled_time"]])
			for col in columnsTime:
				value = row[ColNum[col]]
				if col == "departure_time": 
					if value != "" :
						t = datetime(int(row[ColNum["year"]]),int(row[ColNum["month"]]),int(row[ColNum["day"]]),int(row[ColNum["scheduled_departure"]][:2]),int(row[ColNum["scheduled_departure"]][2:]))
						#t2 = datetime(int(row[ColNum["year"]]),int(row[ColNum["month"]]),int(row[ColNum["day"]]),row[ColNum["departure_time"]][:2],row[ColNum["departure_time"]][2:])
						if row[ColNum["departure_delay"]] !="" :
							a = int(row[ColNum["departure_delay"]])
						else:
							a= 0
						tmp = t + timedelta(minutes = a)
						actualdate = date(tmp.year, tmp.month, tmp.day )
						hour = str(tmp.hour)+":"+str(tmp.minute)+":00"
					else:
						hour = mytime(row[ColNum["scheduled_departure"]])							
				elif col == "arrival_time": 
					hour = mytime(value) if value != "" else mytime(row[ColNum["scheduled_arrival"]])
				else :
					hour = mytime(value)
				newdata.append(str(hour))
			newdata.append(str(actualdate))
			data.append(newdata)
	print(data[1])
	with open('data/adapted_flights2.csv', 'w', newline='') as f:
	    writer = csv.writer(f)
	    writer.writerows(data)

if __name__ == '__main__':
	preprocess()
