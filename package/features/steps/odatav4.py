from behave import given, when, register_type
import logging
import parse

from package.odatav4.ODataClient import ODataClient


@parse.with_pattern(r"\d+")
def parse_number(text):
    return int(text)


register_type(Number=parse_number)

logger = logging.getLogger('OData')


@given(u'an OData endpoint for "{key}"')
def step_impl(context, key):
    context.client = ODataClient(key).query()


@when(u'I fetch the first {size:Number} records from the OData endpoint')
def step_impl(context, size):
    # context.client = query.order_by(Supplier.Post_Code.asc())
    context.client = context.client.limit(2)
    print(context.client.as_string())
    context.result = context.client.all()


@when(u'I fetch the first {size:Number} records from the OData endpoint filtered by')
def step_impl(context, size):
    return
