from datetime import datetime
import logging
import logging.config
import sys

from .PublicationListClient import PublicationListClient
from .ContractsClient import ContractsClient
from .ContractDetailsClient import ContractDetailsClient


logging.config.fileConfig(fname='package/config/logger.ini',
                          disable_existing_loggers=False)
logger = logging.getLogger('Soap')


if (sys.argv[-1] == 'contracts'):

    soap_client = ContractsClient()
    # soap_client.dump()

    filter = soap_client.filter('Contract_Type_Code', 'PC-FIX')
    contracts = soap_client.ReadMultiple(filter=filter, setSize=10)

    for contract in contracts:
        logger.info(contract)
    logger.info('%s items retrieved' % len(contracts))


elif (sys.argv[-1] == 'contract_details'):

    soap_client = ContractDetailsClient()
    # soap_client.dump()

    filter = soap_client.filter('Contract_Type_Code', 'PC-FIX')
    contracts = soap_client.ReadMultiple(filter=filter, setSize=1)

    for contract in contracts:
        logger.info(contract)
    logger.info('%s items retrieved' % len(contracts))

    payload = {
        'Contract_Type_Code': 'PC-FIX',
        'Sell_to_Customer_No': 'C00389',
        'Sell_to_Contact_No': 'CT00255',
        'Sell_to_Cont_Alt_Addr_Code': '_MAIN',
        'Sell_to_Name': 'Institute of Medicine',
        'Sell_to_Address': '611 Huse Road',
        'Sell_to_Post_Code': '03103',
        'Sell_to_City': 'Manchester',
        'Sell_to_Country_Region_Code': 'US',
        'Sell_to_Contact': 'Melanie Nicholson',
        'Order_Date': datetime.now(),
        'Template_Code': 'TIPS ADVIES',
        'Salesperson_Code': 'PMU',
        'Order_Type_Code': 'BACKORDER',
        'Bill_to_Customer_No': 'C00389',
        'Bill_to_Contact_No': 'CT00255',
        'Bill_to_Cont_Alt_Addr_Code': '_MAIN',
        'Bill_to_Name': 'Institute of Medicine',
        'Bill_to_Address': '611 Huse Road',
        'Bill_to_Post_Code': '03103',
        'Bill_to_City': 'Manchester',
        'Bill_to_Country_Region_Code': 'US',
        'Bill_to_Contact': 'Melanie Nicholson',
        'Area': None}

    created_contract = soap_client.Create(payload)
    logger.info(created_contract['Key'])
    logger.info(created_contract['No'])

    contract = soap_client.Read(created_contract['No'])
    logger.info(contract)


elif (sys.argv[-1] == 'publication_list'):

    soap_client = PublicationListClient()
    soap_client.dump()

    filter = soap_client.filter('Type_of_Publication', 2)
    publications = soap_client.ReadMultiple(Header='?',
                                            filter=filter, setSize=1)

    for publication in publications:
        logger.info(publication)
    logger.info('%s items retrieved' % len(publications))
