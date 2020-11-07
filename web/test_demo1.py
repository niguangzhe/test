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

    # 跳过手动扫码，浏览器的复用
    def test_weixin(self):
        self.driver.find_element(By.XPATH, "//*[@id='menu_contacts']/span").click()
        sleep(3)

    def test_cookie(self):
        # get_cookies()可以获取当前打开页面的cookies信息
        # add_cookie()可以把cookie 添加到当前页面中去
        # cookies = self.driver.get_cookies()
        cookies = [
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'Hm_lpvt_9364e629af24cb52acc78b43e8c9f77d',
             'path': '/', 'secure': False, 'value': '1604742054'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False,
             'value': '1688853249148608'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1604770263, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/',
             'secure': True, 'value': '8ft8kat'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False,
             'value': '1688853249148608'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False,
             'value': 's6kLtherO4cOndp4Ji2KdojzAMseZaXErdKBc4RGiPrETkuTCvmIS1sUHzDiKbEY'},
            {'domain': '.qq.com', 'expiry': 1604828473, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False,
             'value': 'GA1.2.579566054.1604738729'},
            {'domain': 'work.weixin.qq.com', 'expiry': 1604770263, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/',
             'secure': False, 'value': '8ft8kat'},
            {'domain': '.qq.com', 'expiry': 1876050929, 'httpOnly': False, 'name': 'mobileUV', 'path': '/',
             'secure': True, 'value': '1_16b606db093_1a808'},
            {'domain': '.qq.com', 'expiry': 1667814073, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False,
             'value': 'GA1.2.1535228834.1597643906'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1607334076, 'httpOnly': False, 'name': 'wwrtx.i18n_lan',
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
            {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvid', 'path': '/',
             'secure': True, 'value': '4231241347'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': True,
             'value': 'direct'},
            {'domain': '.qq.com', 'expiry': 1876050163, 'httpOnly': False, 'name': 'tvfe_boss_uuid', 'path': '/',
             'secure': True, 'value': '053ebda23bc83256'},
            {'domain': '.qq.com', 'expiry': 1626243181, 'httpOnly': False, 'name': 'eas_sid', 'path': '/',
             'secure': True, 'value': 'D1F5z964F700q7i1O8S1p7m5H5'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': True,
             'value': '20336694772727588'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False,
             'value': 'Fz-JbMg-xxxhdzhAl_h12VGRZRfoAO4538X2q8n2M7O0IjlO2snPPX15X8v7Ul-7St9gaYjIbJFUXmHJ07RGWwApq0TesbzV_VV9Vw6Zli2fy_pLUAIGSyjYyx5XnHkKR1-9ELq5JeoK5R2abu4tQfEa8XccQz12GsxokZqB3qYBP8DYTRV5AoMcd_vN8dWyxt5TwHnetUL6mQoRpa9R9HjTiMU9tfNqohMmPLVYUSwiADmEBUPz6xmvmwouHiIddQ2H8PAQzk5aflMGzLyXHg'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1636278053, 'httpOnly': False,
             'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False,
             'value': '1604738728,1604741940,1604742054'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False,
             'value': '1'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False,
             'value': 'a454824'},
            {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'o_cookie', 'path': '/',
             'secure': True, 'value': '781571872'},
            {'domain': '.qq.com', 'expiry': 2147483647, 'httpOnly': False, 'name': 'RK', 'path': '/', 'secure': True,
             'value': 'LfDJpL0cMJ'}]
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
