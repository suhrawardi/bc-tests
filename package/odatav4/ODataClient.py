from odata import ODataService
import os
import logging
import requests
from requests.auth import HTTPBasicAuth


logger = logging.getLogger('OData')

requests.packages.urllib3.disable_warnings()


class ODataClient():

    def __init__(self, name):
        self.name = name

    def query(self):
        return self.__service().query(self.__client(),
                                      options=self.__options())

    def __client(self):
        return self.__entities()[self.name]

    def __entities(self):
        return self.__service().entities

    def __service(self) -> ODataService:
        return ODataService(self.__url(),
                            session=self.__session(),
                            reflect_entities=True)

    def __session(self) -> requests.Session:
        session = requests.Session()
        session.auth = HTTPBasicAuth(os.getenv('NAV_USER'),
                                     os.getenv('NAV_PASSWORD'))
        session.verify = False
        return session

    def __options(self):
        return {'company': os.getenv('COMPANY')}

    def __url(self) -> str:
        host = os.getenv('ODATA_HOST') or ''
        env = os.getenv('ENVIRONMENT') or ''
        return 'https://' + host + '/' + env + '/ODataV4/'
