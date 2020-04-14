from datetime import date
from flask import Flask
import datetime
import csv
import locale

locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')

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

def season():
    now = datetime.datetime.now()
    today = date.today()
    dateseason = int(today.strftime('%m%d'))

    global m, d, mp, mn, verduras, inpver, outver, frutas, inpfru, outfru
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

    estacion = get_season(dateseason)

    verduras = []
    inpver = []
    outver = []
    frutas = []
    inpfru = []
    outfru = []

    seasoncsv_ver('data/de_estacion - hortalizas.csv')
    seasoncsv_fru('data/de_estacion - frutas.csv')
        
    result = 'Hoy es '+now.strftime('%d')+' de '+today.strftime('%B')+', estamos en '+estacion+now.strftime('%S')+'.\n'
    if verduras != []:
        result = result+'Las verduras para comer en '+today.strftime('%B')+' son: '+', '.join(verduras)+'.\n'
    if inpver != []:
        result = result+'Acaban de entrar: '+', '.join(inpver)+'.\n'
    if outver != []:
        result = result+'Es la ultima oportinidad para: '+', '.join(outver)+'.\n'
    if frutas != []:
        result = result+'Las frutas para comer en '+today.strftime('%B')+' son: '+', '.join(frutas)+'.\n'
    if inpfru != []:
        result = result+'Acaban de entrar: '+', '.join(inpfru)+'.\n'
    if outfru != []:
        result = result+'Es la ultima oportinidad para: '+', '.join(outfru)+'.\n'
    return result

app = Flask(__name__)

@app.route('/')
def index():
    webresult = season()
    return webresult

if __name__ == '__main__':
    app.run(debug=True, host='192.168.0.252')

