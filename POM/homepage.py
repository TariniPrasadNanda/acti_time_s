class HomePage:
    def __init__(self,driver):
        self.driver=driver
    def logout_link(self):
        self.driver.find_element("xpath","//a[.='Logout']").click()


    def user_tab(self):
        self.driver.find_element("xpath", "//div[.='Users']").click()

