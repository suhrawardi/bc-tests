from behave import when, then
import logging
import os
import time


logger = logging.getLogger('Browser')


@when(u'I visit the web client')
def step_impl(context):
    context.browser.get(get_url('/'))


@when(u'I visit {path}')
def step_impl(context, path):
    context.browser.get(get_url(path))


@when(u'I log in')
def step_impl(context):
    context.browser.fill_in('User name:', os.getenv('NAV_USER'))
    context.browser.fill_in('Password:', os.getenv('NAV_PASSWORD'))
    context.browser.click_on_button('Sign In')
    context.browser.wait_until_page_contains('Dynamics 365 Business Central')
    time.sleep(3.5)
    context.browser.switch_to_iframe()
    context.browser.wait_until_page_contains(os.getenv('COMPANY'))
    logger.info('On page %s', context.browser.current_url)


@when(u'I go to the "{text}" page')
def step_impl(context, text):
    context.browser.follow_the_navigation_item(text)
    time.sleep(1)
    context.browser.save_screenshot(context.scenario.name)
    logger.info('On page %s', context.browser.current_url)


@when(u'I click on "{text}"')
def step_impl(context, text):
    context.browser.follow_the_link(text)
    time.sleep(1)
    context.browser.save_screenshot(context.scenario.name)
    logger.info('On page %s', context.browser.current_url)


@then(u'I see "{text}"')
def step_impl(context, text):
    context.browser.save_screenshot(context.scenario.name)
    logger.info('On page %s', context.browser.current_url)
    context.browser.wait_until_page_contains(text)


@then(u'I see the "{text}" form')
def step_impl(context, text):
    context.browser.wait_until_form_exists(text)


@when(u'I fill in "{key}" with "{value}"')
def step_impl(context, key, value):
    context.browser.fill_in(key, value)
    time.sleep(1.5)


@when(u'I select "{value}" from "{key}"')
def step_impl(context, value, key):
    context.browser.select(key, value)


def get_url(path):
    host = os.getenv('HOST')
    env = os.getenv('ENVIRONMENT')
    return 'https://' + host + '/' + env + path
