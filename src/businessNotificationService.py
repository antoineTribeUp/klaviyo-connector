from flask import Flask, request, jsonify
from .Y2Service import Y2CustomerService
from .mappingService import MappingService
from .klaviyoService import KlaviyoAPI
from dotenv import load_dotenv
import os
import logging
from datetime import datetime



class BusinessNotificationService:
    def __init__(self,port):
        self.port = port
        self.app = Flask(__name__)
        logging.basicConfig(
            level=logging.DEBUG, 
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler("businessNotification_" + datetime.now().strftime("%Y-%m-%d") + ".log")
            ]
        )
        self.y2CustomerService = Y2CustomerService(url=os.getenv('URLY2'),user=os.getenv('USERY2'),password=os.getenv('PASSWORDY2'),domain=os.getenv('DOMAINY2'))
        self.mapping = MappingService()
        self.klaviyo = KlaviyoAPI(url=os.getenv('URLKLAVIYO'),apiKey=os.getenv('APIKEYKLAVIYO'),revisionDate=os.getenv('REVISIONDATE'))
        self.setup_routes()

    def setup_routes(self):
        @self.app.route('/customers', methods=['POST'])
        def manage_businessNotification_customer():
            try:
                body = request.get_json()
                headers = request.headers
                logging.info("Business notification received")
                customerId = body['Body']['Key']['customerId']
                logging.info("Y2 Webservice start call")
                customerDetails = self.y2CustomerService.getCustomerById(customerId)
                logging.info("Y2 Webservice end call")
                logging.info("Start Mapping")
                profileDetails = self.mapping.mappingProfile(jsonY2=customerDetails)
                logging.info("End mapping")
                logging.info("Start Klaviyo webservice call")
                self.klaviyo.createProfile(payload=profileDetails)
                logging.info("End Klaviyo webservice call")
                return jsonify(body), 200
            except Exception as e:
                logging.error("An error occured: " + str(e))
                return jsonify({"message": "Erreur interne du serveur", "error": str(e)}), 500

    def run(self, host='localhost', port=5000):
        self.app.run(host=host, port=port)
