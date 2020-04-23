from behave.fixture import use_fixture
import logging
from package.browser.Chromium import Chromium


logger = logging.getLogger('Browser')


def use_fixture_by_tag(tag, context, fixture_registry):
    fixture_data = fixture_registry.get(tag, None)
    if fixture_data is None:
        raise LookupError('Unknown fixture-tag: %s' % tag)

    fixture_func, fixture_args, fixture_kwargs = fixture_data
    return use_fixture(fixture_func, context, *fixture_args, **fixture_kwargs)


def browser(context, timeout=60, **kwargs):
    context.browser = Chromium()
    context.add_cleanup(context.browser.shutdown)
    return browser
