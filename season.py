from datetime import date
import csv

today = date.today()
date = int(today.strftime('%m%d'))

def get_season(n): 
	if n >= 321 and n < 621:  
		season = 'otoño' 
	elif n >= 621 and n < 921: 
		season = 'invierno' 
	elif n >= 921 and n < 1221: 
		season = 'primavera' 
	else: 
		season = 'verano' 
	return season

estacion = get_season(date)

verduras = []

def seasoncsv(INPUT):
    with open(INPUT, "r") as f_in:
        reader = csv.reader(f_in) 
        for row in reader:
            if row[1] == estacion:
                verduras.append(row[0])
    return
    
seasoncsv('data/de_estacion.csv')

print ('Hoy es ',today.strftime('%d'),' de ',today.strftime('%B'),', estamos en ',estacion,'. Las verduras para comer en ',estacion,' son:',sep='',end=" ")
print (*verduras, sep = ", ")
