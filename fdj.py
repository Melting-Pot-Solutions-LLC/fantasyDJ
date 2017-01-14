import requests
import time
import json
from random import randint
import io

import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText


from cStringIO import StringIO
import sys

old_stdout = sys.stdout
sys.stdout = mystdout = StringIO()



class Payload(object):
     def __init__(self, j):
         self.__dict__ = json.loads(j)


tracks_ids = [
    '6NMNgWgEAzde5M8U3lc6FN',
    '1FvU97lrWOG2NRxErh6OZz',
    '5aAx2yezTd8zXrkmtKl66Z',
    '7BKLCZ1jbUBVqRi2FVlTVw',
    '6fujklziTHa8uoM5OQSfIo',
    '5GFDrUTLGJix84sNhjCG0g',
    '56cswAa9WdFBsjsTyPBAKA',
    '3NdDpSvN911VPGivFlV5d0',
    '7yyRTcZmCiyzzJlNzGC9Ol',
    '206uaQyzb8kOiZ7rHw9wCn',
    '6I6NX6tjGsxFAsIfGzY9lJ',
    '4RepvCWqsP6zBuzvwYibAS',
    '5MFzQMkrl1FOOng9tq6R9r',
    '6b8Be6ljOzmkOmFslEb23P',
    '4pdPtRcBmOSQDlJ3Fk945m',
    '6fwdbPMwP1zVStm8FybmkO',
    '5uDASfU19gDxSjW8cnCaBp',
    '4F7A0DXBrmUAkp32uenhZt',
    '1xznGGDReH1oQq0xzbwXa3',
    '4gmmRb6bZJffOOiww1JGTO',
    '6DG2g1UhROp5pnM8fx7zH2',
    '23L5CiUhw2jV1OIMwthR3S',
    '4pLwZjInHj3SimIyN9SnOz',
    '5uCax9HTNlzGybIStD3vDh',
    '6i0V12jOa3mr6uu4WYhUBr',
    '4ckuS4Nj4FZ7i3Def3Br8W',
    '0D21XvHcVsIvJM6FcGY2BT',
    '0utlOiJy2weVl9WTkcEWHy',
    '2rizacJSyD9S1IQUxUxnsK',
    '42ydLwx4i5V49RXHOozJZq',
    '6bLopGnirdrilrpdVB6Um1',
    '78rIJddV4X0HkNAInEcYde',
    '5EbX5xL3O2xT8FxCpYzgUO',
    '6nxQdXa1uAL0rY72wPZu89',
    '3EmmCZoqpWOTY1g2GBwJoR',
    '3OalxlWH0v14kyBcNBMINt',
    '4mU5iXHeLgbR94siF7p1sY',
    '0WjYgf4qH3B0v0HmW61doL',
    '2ANLarE8yHVsLWW21nj79M',
    '6AGON2BGdPmPMJGiiNuuwl',
    '11KJSRSgaDxqydKYiD2Jew',
    '0v9Wz8o0BT8DU38R4ddjeH',
    '4h90qkbnW1Qq6pBhoPvwko',
    '4CpKEkdGbOJV51cSvx7SoG',
    '6mapJIPnQ23RTAevUoE0DL',
    '1Tt4sE4pXi57mTD1GCzsqm',
    '6DNtNfH8hXkqOX1sjqmI7p',
    '5knuzwU65gJK7IF5yJsuaW',
    '20dP2DaMHIAmwWAbp7peSr',
    '3kxfsdsCpFgN412fpnW85Y'
]




f = io.open('fantasy_dj.csv', 'r', encoding='utf8')

single_line = f.read()
list_of_lines = single_line.split('\n')


f.close()

f = io.open('fantasy_dj.csv', 'w', encoding='utf8')

for i in range(0, len(tracks_ids)):
    response = requests.get('https://api.spotify.com/v1/tracks/' + tracks_ids[i]).content
    time.sleep(float(randint(0,9))/10)
    # string_to_write = "'" + json.loads(response)['name'] + "' by '" + ((json.loads(response))['artists'][0])['name'] + "'\n"
    string_to_write = list_of_lines[i] + "," + str(json.loads(response)['popularity']) + "\n"
    print string_to_write.encode('utf-8').strip()
    f.write(string_to_write)


f.close()

#change stdout back to original stdout
sys.stdout = old_stdout

#send an email
fromaddr = "dml1002313@gmail.com"
toaddr = "konstantinrubin@engineer.com"
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "FantasyDJ bot executed"
body = mystdout.getvalue()
msg.attach(MIMEText(body, 'plain'))
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, "SteveNash701")
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()
