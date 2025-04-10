import requests
from requests.exceptions import HTTPError, ConnectionError, Timeout, RequestException

class Y2CustomerService:
    def __init__(self,url, user,password,domain):
        self.url = url
        self.user = user
        self.password = password
        self.domain = domain
    
    def getCustomerById(self,id):
        url = self.url + "/" + self.domain + "/api/customers/v2/" + id + "?fields=Address&fields=Communication&fields=Identification&fields=Informations&fields=SystemFields"
        payload = {}
        try:
            response = requests.request("GET", url, headers={}, data=payload, auth=(self.domain + "\\" + self.user,self.password))
        except HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
        except ConnectionError as conn_err:
            print(f"Connection error occurred: {conn_err}")
        except Timeout as timeout_err:
            print(f"Timeout error occurred: {timeout_err}")
        except RequestException as req_err:
            print(f"An error occurred: {req_err}")

        return response.json()
    
    def updateCustomerExternalId(self,id,externalId):
        url = self.url + "/" + self.domain + "/api/customers/v2/" + id
        payload = {
            "id": id,
            "properties" : {
                "externalReference": externalId
            }
        }
        try:
            response = requests.request("PATCH", url, headers={}, data=payload, auth=(self.domain + "\\" + self.user,self.password))
        except HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
        except ConnectionError as conn_err:
            print(f"Connection error occurred: {conn_err}")
        except Timeout as timeout_err:
            print(f"Timeout error occurred: {timeout_err}")
        except RequestException as req_err:
            print(f"An error occurred: {req_err}")
