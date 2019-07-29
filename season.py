from datetime import date
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

print ('Hoy es ',today.strftime('%d'),' de ',today.strftime('%B'),'\nEstamos en ',estacion)
