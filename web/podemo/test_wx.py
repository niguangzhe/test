from web.podemo.index_page import IndexPage


class TestWx:
    def setup(self):
        self.index = IndexPage()

    def test_register(self):
        assert True == self.index.goto_login().goto_register().register()
        # self.index.goto_register().register()
