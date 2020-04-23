import logging
from .ServiceClient import ServiceClient


logger = logging.getLogger('Soap')


class ContractDetailsClient(ServiceClient):

    def __init__(self):
        super().__init__('Contract_Details')

    def filter(self, field, criteria):
        return self.factory().Contract_Details_Filter(Field=field,
                                                      Criteria=criteria)

    def Create(self, payload: dict):
        contract_details = self.factory().Contract_Details(**payload)
        return self.service().Create(Contract_Details=contract_details)

    def Delete(self, key: str):
        try:
            return self.service().Delete(Key=key)
        except IndexError as e:
            logger.info('IndexError %s', e)
            return None

    def Read(self, no: str):
        try:
            return self.service().Read(No=no)
        except IndexError as e:
            logger.info('IndexError %s', e)
            return None

    def ReadMultiple(self, filter, setSize):
        return self.service().ReadMultiple(filter=filter, setSize=setSize)
