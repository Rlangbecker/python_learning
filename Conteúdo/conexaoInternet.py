import urllib.request
import json

def conectaInternet():
    objUrl = urllib.request.urlopen("http://www.google.com")

    if objUrl.getcode() == 200:
        dados = objUrl.read()
        print(dados)


#conectaInternet()

def manipularJson():
    endereco = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/1.0_hour.geojson"
    webUrl = urllib.request.urlopen(endereco)

    if webUrl.getcode() == 200:
        dados = webUrl.read()
        oJSON = json.loads(dados)

        contagem = oJSON["metadata"]["count"]

        print("Count:",str(contagem))

        for local in oJSON["features"]:
            print(local["properties"]["place"])

manipularJson()