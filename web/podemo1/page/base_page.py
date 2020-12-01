# 基类：最基本的方法，driver实例化，find()等
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver


# 1、解决driver 传递和复用的问题
# 2、用例第一次实例化MainPage() 的时候 ，会创建一个driver， 当完成页面切换的时候，会传递driver， 实现driver 复用
# 3、base_url 配置想要打开的页面
# 4、find 方法也可以封装在base_page.py 基类里

class BasePage:
    driver: WebDriver
    base_url = ""

    def __init__(self, driver: WebDriver = None):
        if driver == None:
            # 第一次初始化
            options = Options()
            options.debugger_address = "127.0.0.1:9222"
            self.driver = webdriver.Chrome(options=options)
        else:
            # 进行页面跳转操作
            self.driver = driver

        # base_url 打开某个页面
        if self.base_url != "":
            self.driver.get(self.base_url)

    def find(self, by, locator):
        return self.driver.find_element(by, locator)
