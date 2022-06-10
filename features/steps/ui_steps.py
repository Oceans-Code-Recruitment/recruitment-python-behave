"""Module for common steps"""
from behave import given, when, then
from selenium.webdriver.common.by import By

@given('the user logs in with')
def step_sign_in(context):
    """Sample login

    :param context: Global context from behave
    :type context: obj
    """
    for row in context.table:
        context.driver.find_element(By.CSS_SELECTOR, '#login-email-input').click()
        context.driver.find_element(By.CSS_SELECTOR, '#login-email-input').send_keys(row['email'])
        context.driver.find_element(By.CSS_SELECTOR, '#login-password-input').click()
        context.driver.find_element(By.CSS_SELECTOR, '#login-password-input').send_keys(row['password'])
        context.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

@when('the user clicks on Profile menu')
def step_clikc_on_profile(context):
    """Sample step to retrieve numbers

    :param context: Global context from behave
    :type context: obj
    """
    context.driver.find_element(By.CSS_SELECTOR, '.cu-avatar-container').click()

@then('verifies that the Profile User Name is "{username}"')
def step_verify_board_details(context, username):
    assert context.driver.find_element(By.CSS_SELECTOR, '[data-test="user-settings-menu"] [class*="column-title-name"]').text == username
