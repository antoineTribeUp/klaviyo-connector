import json
import jsonschema


class MappingService:
    def __init__(self):
        self.mapping = True

    def mappingProfile(self,jsonY2):
        jsonKlaviyo = {
                "data": {
                    "type": "profile",
                    "attributes": {
                        "email": "",
                        "phone_number": "",
                        "external_id": "",
                        "first_name": "",
                        "last_name": "",
                        "organization": "",
                        "locale": "",
                        "title": "",
                        "image": "",
                        "location": {
                            "address1": "",
                            "address2": "",
                            "city": "",
                            "country": "",
                            "latitude": "",
                            "longitude": "",
                            "region": "",
                            "zip": "",
                            "timezone": "",
                            "ip": ""
                        },
                        "properties": {}
                    }
                }
            }
        #mapping
        #Email mapping
        try:
            if jsonY2["company"]["communication"]["email"]["value"] != "" or jsonY2["company"]["communication"]["email"]["value"] is not None:
                jsonKlaviyo["data"]["attributes"]["email"] = jsonY2["company"]["communication"]["email"]["value"]
            else:
                jsonKlaviyo["data"]["attributes"]["email"] = jsonY2["individual"]["communication"]["emails"][0]["value"]
        except:
            jsonKlaviyo["data"]["attributes"]["email"] = jsonY2["individual"]["communication"]["emails"][0]["value"]

        #Phone Number mapping
        try:
            if jsonY2["company"]["communication"]["phones"][0]["value"] != "" or jsonY2["company"]["communication"]["phones"][0]["value"] is not None:
                jsonKlaviyo["data"]["attributes"]["phone_number"] = jsonY2["company"]["communication"]["phones"][0]["value"]
            else:
                del jsonKlaviyo["data"]["attributes"]["phone_number"]
        except IndexError:
            del jsonKlaviyo["data"]["attributes"]["phone_number"]
        except:
            del jsonKlaviyo["data"]["attributes"]["phone_number"]
        else:
            jsonKlaviyo["data"]["attributes"]["phone_number"] = jsonY2["individual"]["communication"]["phones"][0]["value"]

    
        #external_id mapping
        jsonKlaviyo["data"]["attributes"]["external_id"] = jsonY2["identifier"]["id"]

        #first_name mapping
        try:
            if jsonY2["company"]["additionalName"] != "" or jsonY2["company"]["additionalName"] is not None:
                jsonKlaviyo["data"]["attributes"]["first_name"] = jsonY2["company"]["additionalName"]
            else:
                jsonKlaviyo["data"]["attributes"]["first_name"]  = jsonY2["individual"]["firstName"]
        except:
            jsonKlaviyo["data"]["attributes"]["first_name"]  = jsonY2["individual"]["firstName"]

        #last_name mapping
        try:
            if jsonY2["company"]["name"] != "" or jsonY2["company"]["name"] is not None:
                jsonKlaviyo["data"]["attributes"]["last_name"] = jsonY2["company"]["name"]
            else:
                jsonKlaviyo["data"]["attributes"]["last_name"]  = jsonY2["individual"]["lastName"]
        except:
            jsonKlaviyo["data"]["attributes"]["last_name"]  = jsonY2["individual"]["lastName"]

        #organization mapping
        del jsonKlaviyo["data"]["attributes"]["organization"]

        #locale mapping
        if jsonY2['languageId'] is None or jsonY2['languageId'] == "":
            jsonKlaviyo["data"]["attributes"]["locale"] = "fr-FR"
        else:
            jsonKlaviyo["data"]["attributes"]["locale"] = jsonY2['languageId'][0:2].lower() + "-" + jsonY2['languageId'][0:2].upper()
        
        #title mapping
        try:
            if jsonY2["company"]["legalForm"] is not None or jsonY2["company"]["legalForm"] != "":
                jsonKlaviyo["data"]["attributes"]["title"] = jsonY2["company"]["legalForm"]
            else:
                del jsonKlaviyo["data"]["attributes"]["title"]
        except:
            if jsonY2["individual"]["titleId"] != "":
                jsonKlaviyo["data"]["attributes"]["title"] = jsonY2["individual"]["titleId"]
            else:
                del jsonKlaviyo["data"]["attributes"]["title"]

        #image mapping
        del jsonKlaviyo["data"]["attributes"]["image"]

        #location mapping
        try:
            if jsonY2["address"]["lines"][0]["value"] is not None or jsonY2["address"]["lines"][0]["value"] != "":
                jsonKlaviyo["data"]["attributes"]["location"]["address1"] = jsonY2["address"]["lines"][0]["value"]
            else:
                del jsonKlaviyo["data"]["attributes"]["location"]["address1"]
        except:
            del jsonKlaviyo["data"]["attributes"]["location"]["address1"]
        try:
            if jsonY2["address"]["lines"][1]["value"] is not None or jsonY2["address"]["lines"][1]["value"] != "":
                jsonKlaviyo["data"]["attributes"]["location"]["address2"] = jsonY2["address"]["lines"][1]["value"]
            else:
                del jsonKlaviyo["data"]["attributes"]["location"]["address2"]
        except:
            del jsonKlaviyo["data"]["attributes"]["location"]["address2"]

        if jsonY2["address"]["city"] != "":
            jsonKlaviyo["data"]["attributes"]["location"]["city"] = jsonY2["address"]["city"]
        else:
            del jsonKlaviyo["data"]["attributes"]["location"]["city"]

        if jsonY2["address"]["countryId"] != "":
            jsonKlaviyo["data"]["attributes"]["location"]["country"] = jsonY2["address"]["countryId"]
        else: 
            del jsonKlaviyo["data"]["attributes"]["location"]["country"]

        if jsonY2["address"]["regionId"] != "":
            jsonKlaviyo["data"]["attributes"]["location"]["region"] = jsonY2["address"]["regionId"]
        else:
            del jsonKlaviyo["data"]["attributes"]["location"]["region"]
        if jsonY2["address"]["zipCode"] != "":
            jsonKlaviyo["data"]["attributes"]["location"]["zip"] = jsonY2["address"]["zipCode"]
        else:
            del jsonKlaviyo["data"]["attributes"]["location"]["zip"]

        #timezone mapping
        del jsonKlaviyo["data"]["attributes"]["location"]["timezone"]

        #ip mapping
        del jsonKlaviyo["data"]["attributes"]["location"]["ip"]

        #latitude mapping
        del jsonKlaviyo["data"]["attributes"]["location"]["latitude"]
        #longitude mapping
        del jsonKlaviyo["data"]["attributes"]["location"]["longitude"]

        return json.dumps(jsonKlaviyo)