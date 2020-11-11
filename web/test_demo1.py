import shelve
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class TestTestdemo():
    def setup_method(self):
        options = Options()
        options.debugger_address = "127.0.0.1:9222"
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)

    def teardown_method(self):
        self.driver.quit()

    def test_testdemo(self):
        self.driver.get("http://www.baidu.com")

    # 跳过手动扫码，浏览器的复用,webdriver.Chrome()中要加入options=options
    def test_weixin(self):
        self.driver.find_element(By.XPATH, "//*[@id='menu_contacts']/span").click()
        sleep(3)

    # cookie登陆
    def test_cookie(self):
        # get_cookies()可以获取当前打开页面的cookies信息
        # add_cookie()可以把cookie 添加到当前页面中去
        # cookies = self.driver.get_cookies()
        # print(cookies)
        cookies = [
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False,
             'value': '1688853249148608'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False,
             'value': '1688853249148608'},
            {'domain': '.qq.com', 'expiry': 1605107640, 'httpOnly': False, 'name': '_gat', 'path': '/', 'secure': False,
             'value': '1'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'Hm_lpvt_9364e629af24cb52acc78b43e8c9f77d',
             'path': '/', 'secure': False, 'value': '1605107579'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False,
             'value': '1589912890777787'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False,
             'value': 's6kLtherO4cOndp4Ji2KdvUWpxZXD46vDnGPIMhm5_5vC4-cJqMWTjKtXYdDLP0P'},
            {'domain': '.qq.com', 'expiry': 1605193995, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False,
             'value': 'GA1.2.2048015754.1605076124'},
            {'domain': 'work.weixin.qq.com', 'expiry': 1605107657, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/',
             'secure': False, 'value': 'sjgqpn'},
            {'domain': '.qq.com', 'expiry': 1876050929, 'httpOnly': False, 'name': 'mobileUV', 'path': '/',
             'secure': True, 'value': '1_16b606db093_1a808'},
            {'domain': '.qq.com', 'expiry': 1668179595, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False,
             'value': 'GA1.2.1535228834.1597643906'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1607699597, 'httpOnly': False, 'name': 'wwrtx.i18n_lan',
             'path': '/', 'secure': False, 'value': 'zh'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1628145171, 'httpOnly': False, 'name': 'wwrtx.c_gdpr',
             'path': '/', 'secure': True, 'value': '0'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False,
             'value': '1970324970153911'},
            {'domain': '.qq.com', 'expiry': 1908868540, 'httpOnly': False, 'name': 'pac_uid', 'path': '/',
             'secure': True, 'value': '1_781571872'},
            {'domain': '.qq.com', 'expiry': 2147483647, 'httpOnly': False, 'name': 'ptcz', 'path': '/', 'secure': True,
             'value': '1796b037f14afcb9dc77daa6420843112158c57341a96b32605055f79cdcc720'},
            {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvi', 'path': '/',
             'secure': True, 'value': '1981400064'},
            {'domain': '.qq.com', 'expiry': 1876050163, 'httpOnly': False, 'name': 'tvfe_boss_uuid', 'path': '/',
             'secure': True, 'value': '053ebda23bc83256'},
            {'domain': '.qq.com', 'expiry': 1626243181, 'httpOnly': False, 'name': 'eas_sid', 'path': '/',
             'secure': True, 'value': 'D1F5z964F700q7i1O8S1p7m5H5'},
            {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvid', 'path': '/',
             'secure': True, 'value': '4231241347'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False,
             'value': '1'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False,
             'value': 'ezLTTqitSlO9MALcZD64xCFWalDATA75LY8rK5ImOF-Yb8AXYuEIgSmeB7zOpJ3WPX4dZrwI0vDFAVvR-5tT9PSEOhTdU_ZBljf_i8BjBozJdJc048aG7bdKi_tYR6AlJjmZ__PrM8odpnIn6zgOIDjYzgmvH4UQeYBe7D1eorPJs8i-P6Nb75j8NPjgEOqDlW3uPk1VJ3co5MehDnv6JO8leKx5XZEo0xu2yRyu67HTJr19BNSczDsgjn0QHYODxExDW7r01K9l-93gaK2pww'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1636643579, 'httpOnly': False,
             'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False,
             'value': '1605076123,1605107079,1605107302,1605107579'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False,
             'value': 'direct'},
            {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'o_cookie', 'path': '/',
             'secure': True, 'value': '781571872'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False,
             'value': 'a5213905'},
            {'domain': '.qq.com', 'expiry': 2147483647, 'httpOnly': False, 'name': 'RK', 'path': '/', 'secure': True,
             'value': 'LfDJpL0cMJ'}]

        # shelve: python的内置模块，专门用来对数据进行持久化存储的库，相当于小型数据库
        # 可以通过key,value 来把数据保存到shelve中
        # db = shelve.open("cookies")
        # db['cookie'] = cookies
        # db.close()

        # 打开页面
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        # 注入cookie
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        # 刷新页面
        self.driver.refresh()
        # 再次访问页面
        # self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        sleep(3)

    # 用shelve将cookie存储起来，再通过调用shelve库拿到cookie登陆
    def test_shelve(self):
        # shelve: python的内置模块，专门用来对数据进行持久化存储的库，相当于小型数据库
        # 可以通过key,value 来把数据保存到shelve中
        # 读取cookie
        db = shelve.open("cookies")
        cookies = db['cookie']
        db.close()
        # 利用读取的cokie 完成登陆操作
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        for cookie in cookies:
            self.driver.add_cookie(cookie)

        self.driver.refresh()
        # 找到"导入联系人"按钮
        self.driver.find_element(By.XPATH, "//*[@id='_hmt_click']/div[1]/div[4]/div[2]/a[2]/div").click()
        # 上传文件
        self.driver.find_element(By.XPATH, "//*[@id='main']/div/div[2]/div[2]/div[1]/a/input").send_keys(
            "/Users/qianwei/Downloads/xixi.xlsx")
        filename = self.driver.find_element(By.XPATH, "//*[@id='main']/div/div[2]/div[2]/div[1]/div[2]").text
        # 验证上传文件
        assert 'xixi.xlsx' == filename
        sleep(3)
