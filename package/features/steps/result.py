from behave import then, register_type
from hamcrest import assert_that, equal_to, none
import logging
import parse


@parse.with_pattern(r"\d+")
def parse_number(text):
    return int(text)


register_type(Number=parse_number)

logger = logging.getLogger('root')


@then(u'the delete succeeded')
def step_impl(context):
    assert_that(context.result, equal_to(True))


@then(u'I receive a record with')
def step_impl(context):
    expected_payload = table_to_dict(context.table)
    for key in expected_payload:
        logger.info('Comparing “%s”: %s == %s',
                    key, context.result[key], expected_payload[key])
        assert_that(context.result[key], equal_to(expected_payload[key]))


@then(u'I do not receive a record')
def step_impl(context):
    assert_that(context.result, none())


@then(u'I received {length:Number} records')
def step_impl(context, length):
    assert_that(len(context.result), equal_to(length))


def table_to_dict(table):
    keys = [row["key"] for row in table.rows]
    values = [row["value"] for row in table.rows]
    return dict(zip(keys, values))
