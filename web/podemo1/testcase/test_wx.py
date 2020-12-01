from web.podemo1.page.main_page import MainPage


class TestWX:
    def setup(self):
        self.main = MainPage()

    def test_addmember(self):
        username = "aaaaaae"
        account = "aaaaaae_hogwarts"
        phonenum = "13400000004"
        # 验证是否添加成功
        addmember = self.main.goto_addmember()
        addmember.add_member(username, account, phonenum)
        assert username in addmember.get_member()
