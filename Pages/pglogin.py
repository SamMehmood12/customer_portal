
from Elements.customerportallogin import loginelements


class login(loginelements):

    def __init__(self,driver):
        super().__init__(driver)


    def enter_username(self,uname):

        self.input_element(self.username , uname)



    def enter_password(self, passw):

        self.input_element(self.password, passw)




    def click_login(self):

        self.click_element(self.loginbtn)


    def click_login1(self):

        self.click_element(self.options)


    def click_logout(self):
        self.click_using_js(self.LOGOUT)