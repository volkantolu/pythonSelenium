from selenium import webdriver
import time
import unittest


class MyNewClass(unittest.TestCase):
    def __init__(message=10):
        print("hosgeldiniz: " + str(message))


    def web_login(self, driverArg):

        driverArg.get("https://www.instagram.com/accounts/login/")

        time.sleep(1)

        username_input = driverArg.find_element_by_name("username")
        username_input.clear()
        username_input.send_keys("volkantolu")

        password_input = driverArg.find_element_by_name("password")
        password_input.clear()
        password_input.send_keys("12345678")

        login_button = driverArg.find_element_by_xpath("//*[@type='submit']")
        login_button.click()

        time.sleep(1)

        result = self.validate_title(driver)
        print("function boolean return value is: " + str(result))

        driverArg.close()
        driverArg.quit()


    def validate_title( driverArg):
        print("page title is: " + driverArg.title)
        if ((driverArg.title) == "Giriş Yap • Instagram"):
            return True
        else:
            return False


    def printMessage(message):
        print("Welcome " + message)


obj = MyNewClass()
driver = webdriver.Chrome("chromedriver.exe")
#obj.web_login(driver)

# Define main method that calls other functions
def main():
    obj.printMessage('volkan')
    obj.web_login(driver)

# Execute main() function
if __name__ == '__main__':
    main()
    #unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='reports'))


