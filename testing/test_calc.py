import pytest
import yaml


# 解析测试数据文件
def get_datas():
    with open("./datas/calc.yml") as f:
        datas = yaml.safe_load(f)
    add_datas = datas['add']['datas']
    add_ids = datas['add']['ids']
    print(add_datas)
    print(add_ids)

    return [add_datas, add_ids]


# 解析测试步骤文件
def steps(addstepsfile, calc, a, b, expect):
    with open(addstepsfile) as f:
        steps = yaml.safe_load(f)
    for step in steps:
        if 'add' == step:
            print("step:add")
            result = calc.add(a, b)
        elif 'add1' == step:
            print("step:add1")
            result = calc.add1(a, b)
        assert expect == result


class TestCalc:
    # def setup_class(self):
    #     print("计算开始")
    #     self.calc = Calculator()
    #
    # def teardown_class(self):
    #     print("计算结束")

    # 加法
    @pytest.mark.parametrize('a,b,expect', get_datas()[0], ids=get_datas()[1])
    def test_add(self, get_calc, a, b, expect):
        # calc = Calculator()
        # result = self.calc.add(a, b)
        result = get_calc.add(a, b)
        assert result == expect

    # 除法
    @pytest.mark.parametrize('a,b,expect', [[1, 1, 1], [100, 2, 50], [0.1, 0.1, 1]],
                             ids=['x_case', 'y_case', 'z_case'])
    def test_div(self, get_calc, a, b, expect):
        # result = self.calc.div(a, b)
        result = get_calc.div(a, b)
        assert result == expect

    # 浮点数可以用round函数保留小数点后面两位
    @pytest.mark.parametrize('a,b,expect', [[0.1, 0.2, 0.3], [0.1, 0.1, 0.2]])
    def test_add_float(self, get_calc, a, b, expect):
        # result = self.calc.add(a, b)
        result = get_calc.add(a, b)
        assert round(result, 2) == expect

    # 除数为0的情况
    @pytest.mark.parametrize('a,b', [[0.1, 0], [1, 0]])
    def test_div1(self, get_calc, a, b):
        # 捕获异常
        with pytest.raises(ZeroDivisionError):
            # result = self.calc.div(a,b)
            result = get_calc.div(a, b)

        # try:
        #     result = self.calc.div(1,0)
        # except ZeroDivisionError:
        #     print("除数为零")

    # 测试步骤调用
    def test_add_steps(self, get_calc):
        a = 1
        b = 1
        expect = 2

        steps("./steps/add_steps.yml", get_calc, a, b, expect)
        # assert 2 == self.calc.add(1, 1)
        # assert 3 == self.calc.add1(1, 2)
        # assert 0 == self.calc.add1(-1, 1)
