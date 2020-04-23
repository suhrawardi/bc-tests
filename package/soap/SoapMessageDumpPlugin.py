import logging
from datetime import datetime
from lxml import etree
from zeep import Plugin


logger = logging.getLogger('Soap')


class SoapMessageDumpPlugin(Plugin):

    def __init__(self, directory):
        self.directory = directory
        super().__init__()

    def ingress(self, envelope, http_headers, operation):
        self.__log(envelope, http_headers, operation)
        self.__write_soap_message(envelope, operation, 'response')
        return envelope, http_headers

    def egress(self, envelope, http_headers, operation, binding_options):
        self.__log(envelope, http_headers, operation)
        self.__write_soap_message(envelope, operation, 'request')
        return envelope, http_headers

    def __write_soap_message(self, envelope, operation, action):
        message = etree.tostring(envelope, pretty_print=True)
        filename = self.__filename(operation, action)
        path = self.directory + '/' + filename
        logger.info('Stored SOAP message “' + filename + '”')
        with open(path, 'wb') as file:
            file.write(message)

    def __log(self, envelope, headers, operation):
        logger.info(operation)
        logger.info(headers)

    def __filename(self, operation, action):
        endpoint = operation.__str__().split(':')[-1].lower()
        op = operation.name.lower()
        prefix = datetime.now().strftime('%Y%m%d-%H%M%S.%f')
        return prefix + '_' + op + '_' + endpoint + '_' + action + '.xml'
