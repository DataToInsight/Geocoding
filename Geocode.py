import requests
import csv


inputfile = open('placelist2.txt', 'r')
outputfile = csv.writer(open('geocoded-placelist.txt', 'w'))

for row in inputfile:
    row in row.rstrip()
    url = 'https://maps.googleapis.com/maps/api/geocode/json'
    payload = {'address':row, 'sensor':'false'}
    r = requests.get(url, params=payload)
    json = r.json()

    lat = json['results'][0]['geometry']['location']['lat']
    lng = json['results'][0]['geometry']['location']['lng']

    newrow = [row,lat,lng]
    outputfile.writerow(newrow)
