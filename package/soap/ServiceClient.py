import os
import logging
import requests
from requests.auth import HTTPBasicAuth

from zeep import Client
from zeep.transports import Transport

from package.utilities.OutputLogger import OutputLogger
from .SoapMessageDumpPlugin import SoapMessageDumpPlugin


logger = logging.getLogger('Soap')

requests.packages.urllib3.disable_warnings()


class ServiceClient():

    def __init__(self, name):
        self.dump_plugin = SoapMessageDumpPlugin('./reports/soap')
        self.name = name
        self.dump()

    def dump(self):
        with OutputLogger() as output:
            self.client().wsdl.dump()
        logger.info("\n".join(output))

    def client(self) -> Client:
        return Client(self.__wsdl(),
                      transport=self.__transport(),
                      plugins=[self.dump_plugin])

    def service(self):
        return self.client().service

    def factory(self):
        return self.client().type_factory('ns0')

    def __transport(self) -> Transport:
        return Transport(session=self.__session())

    def __session(self) -> requests.Session:
        session = requests.Session()
        session.auth = HTTPBasicAuth(os.getenv('NAV_USER'),
                                     os.getenv('NAV_PASSWORD'))
        session.verify = False
        return session

    def __wsdl(self) -> str:
        return self.__url() + self.name

    def __url(self) -> str:
        host = os.getenv('SOAP_HOST') or ''
        env = os.getenv('ENVIRONMENT') or ''
        company = os.getenv('COMPANY') or ''
        return 'https://' + host + '/' + env + '/WS/' + company + '/Page/'
