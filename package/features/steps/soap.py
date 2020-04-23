from behave import given, when, register_type
import logging
import parse

from package.soap.ContractDetailsClient import ContractDetailsClient


@parse.with_pattern(r"\d+")
def parse_number(text):
    return int(text)


register_type(Number=parse_number)

logger = logging.getLogger('Soap')


@given(u'a contract details SOAP endpoint')
def step_impl(context):
    context.client = ContractDetailsClient()


@when(u'I fetch the first {size:Number} records from the SOAP endpoint filtered by')
def step_impl(context, size):
    field = context.table[0]['filter']
    value = context.table[0]['value']
    filter = context.client.filter(field, value)
    context.result = context.client.ReadMultiple(filter=filter, setSize=size)


@when(u'I create a new record on the SOAP endpoint with')
def step_impl(context):
    payload = table_to_dict(context.table)
    logger.info(payload)
    context.result = context.client.Create(payload)
    context.storage = {'No': context.result['No'],
                       'Key': context.result['Key']}
    logger.info(context.result)


@when(u'I fetch "{no}" from the SOAP endpoint')
def step_impl(context, no):
    context.result = context.client.Read(no)
    logger.info(context.result)


@when(u'I fetch the created record from the SOAP endpoint')
def step_impl(context):
    context.result = context.client.Read(context.storage['No'])
    logger.info(context.result)


@when(u'I delete the created record from the SOAP endpoint')
def step_impl(context):
    context.result = context.client.Delete(context.storage['Key'])
    logger.info(context.result)


def table_to_dict(table):
    keys = [row["key"] for row in table.rows]
    values = [row["value"] for row in table.rows]
    return dict(zip(keys, values))
