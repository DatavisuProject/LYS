import os

#Fichier avec les aérports, codes, coordonnées GPS
airports = ""

with open("/data/code_airports.txt", encoding = "utf-8") as file_airports:
    for line in file_airports:
        line = line.split(',')
        if line[3] == '"United States"':
            lat = round(float(line[6]),2)
            lon = round(float(line[7]),2)
            airports += line[1] + ',' + line[2] + ',' + line[4] + ',' + str(lat) + ',' + str(lon) + '\n'

with open("/data/code_airports_modif.csv", "w", encoding = "utf-8") as file:
    file.write('airport_name,city,code,lat,lon \n')
    file.write(airports)

