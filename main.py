from src.businessNotificationService import BusinessNotificationService
from dotenv import load_dotenv
import os


if __name__ == '__main__':
    load_dotenv()

    service = BusinessNotificationService(port=5000)
    service.run()