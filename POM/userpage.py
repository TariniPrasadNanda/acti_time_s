class UserPage:
    def __init__(self,driver):
        self.driver=driver
    def user_button(self):
        self.driver.find_element("xpath","//span[.='User']").click()
    def first_name(self,data):
        self.driver.find_element("name","firstName").send_keys(data)
    def last_name(self,data):
        self.driver.find_element("name","lastName").send_keys(data)
    def email(self, data):
        self.driver.find_element("class name", "emailField").send_keys(data)
    def user_name(self, data):
        self.driver.find_element("id", "userDataLightBox_usernameField").send_keys(data)
    def password(self, data):
        self.driver.find_element("name", "password").send_keys(data)
    def retype_password(self,data):
        self.driver.find_element("class name","passwordCopyField").send_keys(data)
    def create_user_button(self):
        self.driver.find_element("xpath", "//div[.='Create User']").click()