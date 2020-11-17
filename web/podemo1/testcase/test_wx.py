from web.podemo1.page.main_page import MainPage


# class TestWx:
#     def setup(self):
#         self.main = MainPage()
#
#     def test_addmember(self):
#         username = "aaaaa"
#         account = "aaaaa-ayaya"
#         phonenum = "13699999999"
#
#         # addmember = self.main.goto_addmember()
#         # addmember.add_member(username, account, phonenum)
#         # assert username in addmember.get_member()
#
#         addmember = self.main.goto_addmember()
#         addmember.add_member(username, account, phonenum)
#         assert username in addmember.get_member(username)
class TestWX:
    def setup(self):
        self.main = MainPage()

    def test_addmember(self):
        username = "aaaaaac"
        account = "aaaaaac_hogwarts"
        phonenum = "13400000002"
        # 验证是否添加成功
        addmember = self.main.goto_addmember()
        addmember.add_member(username, account, phonenum)
        assert username in addmember.get_member()
