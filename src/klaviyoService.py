import requests
import json


class KlaviyoAPI:
    def __init__(self,url,apiKey,revisionDate):
        self.url = url
        self.apiKey = apiKey
        self.revisionDate = revisionDate

    def getProfileById(self,id):
        url = self.url + '/profiles/' + id
        headers = {
                    'revision': self.revisionDate,
                    'Accept': 'application/vnd.api+json',
                    'Authorization': 'Klaviyo-API-Key ' + self.apiKey
                    }
        payload = {}

        try:
            response = requests.request("GET",url=url,headers=headers,data=payload)
            return response.json()
        except:
            return response.json()
    
    def createProfile(self,payload):
        url = self.url + '/profiles'
        headers = {
                    'revision': self.revisionDate,
                    'Accept': 'application/json',
                    'Authorization': 'Klaviyo-API-Key ' + self.apiKey,
                    'Content-Type': 'application/json'
                }
        try:
            response = requests.request("POST",url=url,headers=headers,data=payload)
            return response.json()
        except:
            return {'error':'An error occured'}
        
    def updateProfile(self,payload,id):
        url = self.url + '/profiles:' + str(id)
        payload['data']['id'] = id
        headers = {
                    'revision': self.revisionDate,
                    'Accept': 'application/json',
                    'Authorization': 'Klaviyo-API-Key ' + self.apiKey,
                    'Content-Type': 'application/json'
                }
        try:
            response = requests.request("PATCH",url=url,headers=headers,data=payload)
            return response.json()
        except:
            return {'error':'An error occured'}