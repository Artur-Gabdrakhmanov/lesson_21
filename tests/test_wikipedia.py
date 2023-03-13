import allure
from appium.webdriver.common.appiumby import AppiumBy
from selene import have
from selene.support.shared import browser

text_title = (AppiumBy.ID, 'org.wikipedia.alpha:id/primaryTextView')
btn_continue = (AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_forward_button')
btn_skip = (AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_skip_button')


@allure.label('owner', 'Artur Gabdrakhmanov')
@allure.title('Navigation in the Wikipedia app')
def test_skip_screens():
    with allure.step('Checking the start screen'):
        browser.element(text_title).should(have.text('The Free Encyclopedia'))
        browser.element(btn_continue).click()
    with allure.step('"Continue" page one'):
        browser.element(text_title).should(have.text('New ways to explore'))
        browser.element(btn_continue).click()
    with allure.step('"Continue" page two'):
        browser.element(text_title).should(have.exact_text('Reading lists with sync'))
        browser.element(btn_continue).click()
    with allure.step('"Continue" page three'):
        browser.element(text_title).should(have.text('Send anonymous data'))