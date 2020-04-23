import base64
from behave.fixture import fixture_call_params
from fixtures import use_fixture_by_tag, browser
import glob
import logging.config
import os
import sys


logging.config.fileConfig(fname='package/config/logger.ini',
                          disable_existing_loggers=False)
logger = logging.getLogger('Features')

fixture_registry = {
    'fixture.browser': fixture_call_params(browser)
}


os.environ['DEBUG'] = str('@wip' in sys.argv or '@debug' in sys.argv)


def before_tag(context, tag):
    if tag.startswith('fixture.'):
        return use_fixture_by_tag(tag, context, fixture_registry)


def after_step(context, step):
    if step.status != 'failed' and os.getenv('DEBUG') != 'True':
        return

    logger.error(step.exception)
    logger.info(step.exception,
                exc_info=(None, step.exception, step.exc_traceback))

    if 'fixture.browser' not in context.tags:
        return

    files = glob.glob('reports/screenshots/*.png')

    if (len(files) > 0):
        screenshot = max(files, key=os.path.getctime)
        with open(screenshot, mode='rb') as f:
            b64data = base64.encodestring(f.read()).decode('UTF-8')
            step.embeddings.append({'mime_type': 'image/png',
                                    'data': b64data})
        if step.status == 'failed':
            msg = 'Scenario failed, attaching %s from %s'
            logger.info(msg, screenshot, context.browser.current_url)
            context.browser.dump()
