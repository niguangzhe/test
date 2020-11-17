from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from web.podemo1.page.add_member_page import AddMemberPage


class MainPage:

    def __init__(self):
        # 复用浏览器
        options = Options()
        options.debugger_address = "127.0.0.1:9222"
        self.driver = webdriver.Chrome(options=options)
        # self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")

    def goto_addmember(self):
        # 跳转到添加成员页面
        self.driver.find_element(By.CSS_SELECTOR, ".index_service_cnt_itemWrap:nth-child(1)").click()
        return AddMemberPage(self.driver)
