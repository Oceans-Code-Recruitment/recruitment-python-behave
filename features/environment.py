"""Environment module for behave"""
from behave.model_core import Status
from behave.fixture import use_fixture_by_tag
from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait # CAN BE USEFUL
from selenium.webdriver.chrome.service import Service
from chromedriver_py import binary_path
from selenium.webdriver.common.by import By

def before_all(context):
    """Before_all
    """
    service_object = Service(binary_path)
    context.driver = webdriver.Chrome(service=service_object)
    context.driver.set_page_load_timeout(60)
    context.driver.implicitly_wait(30)
    context.driver.maximize_window()
    context.driver.get("https://app.clickup.com/login")

def before_scenario(context, scenario):  # pylint: disable=W0613
    """Before scenario hook
    """
    print(f"=============Started {scenario.name}")

def after_scenario(context, scenario):  # pylint: disable=W0613
    """After scenario hook if the scenario is failed take a screenshot
    """
    if scenario.status == Status.failed:
        print(f"============ Ooops Failed scenario {scenario.name}")
    print(f"=============Finished {scenario.name}")

def before_feature(context, feature):  # pylint: disable=W0613
    """Before feature hook
    """

def after_feature(context, feature):  # pylint: disable=W0613
    """after feature hook
    """

FIXTURE_REGISTRY = {}

def before_tag(context, tag):  # pylint: disable=W0613
    """Just a simple before_tag hook
    """

def after_tag(context, tag):  # pylint: disable=W0613, R1710
    """Just a simple after_tag hook
    """
    if tag.startswith("fixture."):
        return use_fixture_by_tag(tag, context, FIXTURE_REGISTRY)

def after_all(context):
    """Before_all
    """
    context.driver.quit()
