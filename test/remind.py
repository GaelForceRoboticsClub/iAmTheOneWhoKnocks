import requests
import json
import base64
import random
import config
from quotes import quotes

def pretty(data):
	return json.dumps(data, indent=4, sort_keys=True)

url = 'https://api.remind.com/v2'

# TODO: replace with environmental variables
email = config.email
password = config.password
classCode = config.classCode

tokenReqData = {
	'user': {
		'email': email,
		'password': password
	}
}

tokenReq = requests.post(url+'/access_tokens', data=json.dumps(tokenReqData))
accessToken = tokenReq.json()['token']

headers = {
	'Content-Type': 'application/json',
	'Accept': 'application/json',
	'Authorization': 'Bearer ' + accessToken,
}

classesMembersReq = requests.get(url+'/classes/'+classCode, headers=headers)
classId = classesMembersReq.json()['id']

message = {
	'message': {
		'body': random.choice(quotes)+'\nThe robotics room is open!',
		'group_ids': [classId]
	}
}

messageReq = requests.post(url+'/messages', headers=headers, data=json.dumps(message))