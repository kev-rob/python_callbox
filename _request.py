import json, requests
from webhook import url

data = {'text':"Hello, assistance is needed. \r \r Please reply if you are available. Press \"Cancel\"' on the touchscreen to automatically update this channel."}

response = requests.post(
    url, data=json.dumps(data),
    headers={'Content-Type': 'application/json'}
)
if response.status_code != 200:
    raise ValueError(
        'Request returned an error %s, the response is:\n%s'
        % (response.status_code, response.text)
    )

