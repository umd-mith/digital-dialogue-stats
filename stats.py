#!/usr/bin/env python

import csv
import requests
from os import environ as env

token = env.get('ACCESS_TOKEN')

def get(path, params):
    url = 'https://api.vimeo.com/' + path
    resp = requests.get(
        url,
        params=params,
        headers={'Authorization': 'bearer ' + token})
    return resp.json()

page = 0
out = csv.writer(open('stats.csv', 'w'))
out.writerow(['title', 'created', 'plays', 'url'])

while True:
    page += 1
    results = get('me/videos', {"page": page})

    if 'data' not in results:
        break

    for video in results['data']:
        out.writerow([
            video['name'],
            video['created_time'],
            video['stats']['plays'],
            'https://vimeo.com' + video['uri']
        ])












