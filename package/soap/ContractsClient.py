from .ServiceClient import ServiceClient


class ContractsClient(ServiceClient):

    def __init__(self):
        super().__init__('Contracts')

    def filter(self, field, criteria):
        return self.factory().Contracts_Filter(Field=field, Criteria=criteria)

    def ReadMultiple(self, filter, setSize):
        return self.service().ReadMultiple(filter=filter, setSize=setSize)
