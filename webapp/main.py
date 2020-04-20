from datetime import datetime
from flask import Flask, render_template
import csv
import locale
import pytz

locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')

def get_season(n): 
    if n >= 321 and n < 621:  
        season = 'OTOÑO'
    elif n >= 621 and n < 921: 
        season = 'invierno'
    elif n >= 921 and n < 1221: 
        season = 'primavera' 
    else: 
        season = 'verano' 
    return season

def seasoncsv_ver(INPUT):
    with open(INPUT, "r",encoding='utf8') as f_in:
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
    with open(INPUT, "r",encoding='utf8') as f_in:
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
#    now = datetime.datetime.now()
#    today = date.today()
    tz = pytz.timezone("America/Argentina/Buenos_Aires")
    today = datetime.now(tz)
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
        
    result = 'Hoy es '+today.strftime('%d')+' de '+today.strftime('%B')+', estamos en '+estacion+'.<br/>'
    if verduras != []:
        result = result+'<br/>Las <b>verduras</b> para comer en '+today.strftime('%B')+' son: '+', '.join(verduras)+'.<br/>'
    if inpver != []:
        result = result+'Acaban de entrar: '+', '.join(inpver)+'.<br/>'
    if outver != []:
        result = result+'Es la última oportunidad para: '+', '.join(outver)+'.<br/>'
    if frutas != []:
        result = result+'<br/>Las <b>frutas</b> para comer son: '+', '.join(frutas)+'.<br/>'
    if inpfru != []:
        result = result+'Acaban de entrar: '+', '.join(inpfru)+'.<br/>'
    if outfru != []:
        result = result+'Es la última oportunidad para: '+', '.join(outfru)+'.<br/>'
    return result

app = Flask(__name__)

@app.route('/')
def index():
    webresult = season()
    return render_template('index.html', time=webresult)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
    #app.run(debug=True, host='192.168.0.252')
