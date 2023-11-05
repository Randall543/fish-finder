# get the info regarding an animal
import requests as req
import hashlib
from dotenv import load_dotenv
from os import getenv

load_dotenv('.env')
exit()
api = 'https://www.movebank.org/movebank/service/direct-read'
alternate = 'https://www.movebank.org/movebank/service/public/json?'
test = 'https://www.movebank.org/movebank/service/public/json?study_id=2911040&individual_local_identifiers=4262-84830876&sensor_type=gps'

# parameters = {'study_id' : '2391441038','entity_type' : 'individual'}
parameters = {'study_id' : '2391441038','entity_type' : 'event'}
# parameters = {'entity_type' : 'study'}
# response = req.get(alternate,params=parameters,auth=(user,ps))
response = req.get(api,params=parameters,auth=(getenv('username'),getenv('password')))
# response = req.get('https://www.movebank.org/movebank/service/direct-read?entity_type=study&study_id=2911040',auth=(user,ps))

if response.status_code == 200:
    if 'License Terms' in str(response.content):
        hash = hashlib.md5(response.content).hexdigest()
        parameters['license-md5'] = hash
        response = req.get(api,params=parameters,cookies=response.cookies,auth=(user,ps))

print(response.text)