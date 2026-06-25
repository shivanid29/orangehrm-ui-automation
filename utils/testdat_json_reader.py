import json

import testdata

def return_url():
    with open('testdata/urls.json', 'r') as f:
        data = json.load(f)
    return data


