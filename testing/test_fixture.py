def test_case1(login):
    print(login)
    print("用例1")


def test_case2():
    print("用例2")


# 如果需要返回login的返回值，case的参数里必须加上login
def test_case3(conn_db):
    print(conn_db)
    print("用例3")
