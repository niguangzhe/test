import pytest

from pythoncode.calculator import Calculator


@pytest.fixture(autouse=True, scope="function", params=['tom', 'jerry'])
def login(request):
    # setup操作
    print("登陆操作")
    username = request.param
    # yield相当与return操作
    yield username
    # teardown操作
    print("登出操作")


@pytest.fixture(autouse=True, scope="session")
def conn_db():
    print("完成 数据库连接")
    yield "database"
    print("断开 数据库连接")


@pytest.fixture(scope="class")
def get_calc():
    print("计算开始")
    calc = Calculator()
    yield calc
    print("计算结束")
