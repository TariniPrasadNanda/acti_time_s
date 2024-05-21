from Generic.verifytitle import *
from POM.homepage import *
from POM.loginpage import *


def test_TC1(launch):
    driver=launch
    verify_title(driver,"actiTIME - Login")
    l=LoginPage(driver)
    l.username("admin")
    l.password("manager")
    l.login_button()
    verify_title(driver,"actiTIME - Enter Time-Track")
    h=HomePage(driver)
    h.logout_link()
    verify_title(driver,"actiTIME - Login")
