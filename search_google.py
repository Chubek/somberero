from unittest import result
import requests
from dotenv import load_dotenv
import os
from string import Template
from typing import Dict, List

load_dotenv()

G_KEY = os.environ['G_KEY']
G_CX = os.environ['G_CX']

TEMP = Template(f"https://www.googleapis.com/customsearch/v1?key=$key&cx=$cx&q=$query&start=$start")



def search_google(
        query: str, 
        starts=[11, 21, 31, 41, 51, 61, 71, 81, 91]
    ) -> List[Dict]:

    results = []

    for st in starts:
        url = TEMP.substitute(
            key=G_KEY,
            cx=G_CX,
            query=query,
            start=st
        )

        resp = requests.get(url)

        resp_json = resp.json()

        results.append(resp_json)

    links = []

    for res in results:
        try:
            items = res['items']
        except:
            continue

        for it in items:
            try:
                links.append(it['formattedUrl'])
            except:
                continue

    return links

