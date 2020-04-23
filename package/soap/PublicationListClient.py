import logging
from .ServiceClient import ServiceClient


logger = logging.getLogger('Soap')


class PublicationListClient(ServiceClient):

    def __init__(self):
        super().__init__('Publication_List')

    def filter(self, field, criteria):
        return self.factory().Publication_List_Filter(Field=field,
                                                      Criteria=criteria)

    def Read(self, no: str):
        try:
            return self.service().Read(No=no)
        except IndexError as e:
            logger.info('IndexError %s', e)
            return None

    def ReadMultiple(self, filter, setSize):
        return self.service().ReadMultiple(filter=filter, setSize=setSize)
