from datetime import date
import csv

today = date.today()
date = int(today.strftime('%m%d'))
m = int(today.strftime('%m')) 
d = int(today.strftime('%d'))
mp = 0
mn = 0
if m == 1:
    mp = 12
    mn = m + 1
elif m == 12:
    mp = m - 1
    mn = 1
else:
    mp = m-1
    mn = m+1


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
inpver = []
outver = []
frutas = []
inpfru = []
outfru = []

def seasoncsv_ver(INPUT):
    with open(INPUT, "r") as f_in:
        reader = csv.reader(f_in) 
        for row in reader:
            if int(row[m])>=2:
                if int(row[mp])>=2 and int(row[mn])>=2:
                	verduras.append(row[0])
                if int(row[mp])<2:
                	inpver.append(row[0])
                if int(row[mn])<2:
                	outver.append(row[0])
    return
    
def seasoncsv_fru(INPUT):
    with open(INPUT, "r") as f_in:
        reader = csv.reader(f_in) 
        for row in reader:
            if int(row[m])>=2:
                if int(row[mp])>=2 and int(row[mn])>=2:
                	frutas.append(row[0])
                if int(row[mp])<2:
                	inpfru.append(row[0])
                if int(row[mn])<2:
                	outfru.append(row[0])    	
    return
    
seasoncsv_ver('data/de_estacion - hortalizas.csv')
seasoncsv_fru('data/de_estacion - frutas.csv')

print ('Hoy es ',today.strftime('%d'),' de ',today.strftime('%B'),', estamos en ',estacion,'.',sep='')
if verduras != []:
    print ('Las verduras para comer en ',today.strftime('%B'),' son:',sep='',end=" ")
    print (*verduras, sep = ", ")
if inpver != []:
    print ('Acaban de entrar:',end=" ")
    print (*inpver, sep = ", ")
if outver != []:
    print ('Es la ultima oportinidad para:',end=" ")
    print (*outver, sep = ", ")
if frutas != []:
    print ('Las frutas para comer en ',today.strftime('%B'),' son:',sep='',end=" ")
    print (*frutas, sep = ", ")
if inpfru != []:
    print ('Acaban de entrar:',end=" ")
    print (*inpfru, sep = ", ")
if outfru != []:
    print ('Es la ultima oportinidad para:',end=" ")
    print (*outfru, sep = ", ")
