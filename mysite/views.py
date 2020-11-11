from django.shortcuts import render
from datetime import datetime, timedelta
import requests

def home(request):
    response = requests.get('https://api.kawalcorona.com/indonesia/provinsi')
    data_prov = response.json()
    case_prov = []
    for prov in data_prov :
        result_prov = {}
        result_prov['kode_prov' ] = prov['attributes']['Kode_Provi']
        result_prov['provinsi' ] = prov['attributes']['Provinsi']
        result_prov['kasus_positif'] = prov['attributes']['Kasus_Posi']
        result_prov['kasus_sembuh'] = prov ['attributes']['Kasus_Semb']
        result_prov['kasus_meninggal'] = prov['attributes']['Kasus_Meni']
        case_prov.append(result_prov)


    response_indo = requests.get('https://api.kawalcorona.com/indonesia')
    data_indo = response_indo.json()
    case_indo = []
    for d in data_indo :
        result = {}
        result['name'] = d['name']
        result['positif'] = d['positif']
        result['sembuh'] = d['sembuh']
        result['meninggal'] = d['meninggal']
        case_indo.append(result)
    
    update = datetime.now()-timedelta(days=1)
        
    context = {
        'Title' : 'API-Corona',
        'Judul' : 'Corona Virus Cases in Indonesia',
        'data' : case_prov,
        'case_indo' : case_indo,
        'update' : update,
    }
    return render (request,'index.html', context)

    


