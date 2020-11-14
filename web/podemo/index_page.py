from selenium import webdriver
from selenium.webdriver.common.by import By

from web.podemo.login_page import LoginPage
from web.podemo.register_page import RegisterPage


class IndexPage:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://work.weixin.qq.com/")

    # 进入登陆页面
    def goto_login(self):
        self.driver.find_element(By.CSS_SELECTOR, '.index_top_operation_loginBtn').click()
        return LoginPage(self.driver)

    # 进入注册页面
    def goto_register(self):
        self.driver.find_element(By.Xpath, '//*[@id="tmp"]/div[1]/a')
        return RegisterPage(self.driver)
