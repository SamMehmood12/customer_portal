import time

from behave import *

from Constant.URL import TestData
from Pages.pglogin import login


@when("User is at login Page")
def step_impl(context):

   context.driver.get(TestData.CUSTOMERPORTAL)
   time.sleep(5)
#
# # @then("User Enters abc123 and pJPAiUshc541")
# # def step_impl(context):
#     """
#     :type context: behave.runner.Context
#     """
#     raise NotImplementedError(u'STEP: Then User Enters abc123 and pJPAiUshc541')
@then("User Enters {uname} and {pwd}")
def step_impl(context , uname ,pwd ):
    context.loginpage.enter_username(uname)
    context.loginpage.enter_password(pwd)


@then("User Clicks on Login Button")
def step_impl(context):
    context.loginpage.click_login()
