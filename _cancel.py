import json, requests
from webhook import url

data = {'text':"Request for help has been canceled on the touchscreen."}

response = requests.post(
    url, data=json.dumps(data),
    headers={'Content-Type': 'application/json'}
)
if response.status_code != 200:
    raise ValueError(
        'Request returned an error %s, the response is:\n%s'
        % (response.status_code, response.text)
    )
