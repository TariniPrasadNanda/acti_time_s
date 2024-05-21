from Generic.verifytitle import *
from POM.loginpage import *
from POM.homepage import *
from POM.userpage import *
from Generic.verifytext import *

def test_TC2(launch):
    driver=launch
    verify_title(driver,"actiTIME - Login")
    l=LoginPage(driver)
    l.username("admin")
    l.password("manager")
    l.login_button()
    verify_title(driver,"actiTIME - Enter Time-Track")
    
