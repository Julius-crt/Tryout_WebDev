import requests
#wir bauen einen Client, der die BVG API nutzt und alle BUsse von Kottbusser tor
#bis zur Hardenberg menas anzeigt

#Daten für die API:
# "id": "900023152","name": "Steinplatz (Berlin)",
# "id": "900014151","name": "Waldemarstr./Adalbertstr. (Berlin)", 

#1. initialisiere eine Anfrage 
#   r ist ein Response object und hat alle infos der Anfrage
#   r1 hat querey, die sucht nach stops mit namen 'Kottbusser Tor' id=900013102
#   wir sollten uns die Id der richtigen U Bahnstation merken. 
#r1 = requests.get('https://v6.bvg.transport.rest/locations?poi=false&addresses=false&query=Kottbusser Tor')

#   r.text greift auf die smarte Decodierung von requests zu.
#   (nimmt Infos aus http objekt header)
#print(r1.text)

#2. r2 speichert alle abfahrenden FAhrten an einem Bahnhof mit ihrer Abfahrtszeit und Zielbahnhof
#r2 = requests.get('https://v6.bvg.transport.rest/stops/900013102/departures?results=5')
#print(r2.text)

#3. r3 speichet ein jason mit allen Jorneys von einem Bahnhof(kotti) zum anderen Bahnhof(Mehringdamm) 
#r3 = requests.get('https://v6.bvg.transport.rest/journeys?from=900013102&to=900017101&departure=tomorrow+2pm&results=2')

print('Where do you want to start?')
usrinput1 = input()
station1req = requests.get('https://v6.bvg.transport.rest/locations?poi=false&addresses=false&query='+usrinput1,timeout=2)
station1 = station1req.json() #json object als directory

#print(station1[0]['name'])
#print(station1[0]["products"]["subway"])

print('Where do you want to go?')
usrinput2 = input()
station2req = requests.get('https://v6.bvg.transport.rest/locations?poi=false&addresses=false&query='+usrinput2,timeout=2)
station2 = station2req.json()

journey1req = requests.get('https://v6.bvg.transport.rest/journeys?from={station1id}&to={station2id}&departure=now&results=2'.format(station1id=station1[0]['id'],station2id =station2[0]['id']))
journey1 = journey1req.json()["journeys"][0]['legs']
#print(journey1)



s = '''
    One recommended Route from: 
        "{station1name} ---> {station2name}"

    is as followes:'''.format(station1name=station1[0]['name'],station2name=station2[0]['name'])
print(s)

for leg in journey1:
    s1 = '''        Use the {vehikel} {linienname} at {stationName} departing {stationuhrzeit}'''.format(vehikel = leg['line']['mode'], linienname=leg['line']['name'], stationuhrzeit=leg['departure'], stationName=leg['origin']['name'])
    print(s1)

print('\n        Arriving: {ankunftszeit} at your Destination: {stationname}\n'.format(ankunftszeit=leg['arrival'],stationname=leg['destination']['name']))
#print(station1.contains)print(Steige ein in 
#print(station1.)
#station1name = 

#r3 = requests.get('http://httpbin.org/get') #man sollte immer einen Timeout hinzufügen
#print(r3.headers)# as python dict