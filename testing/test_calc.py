import pytest
import yaml

from pythoncode.calculator import Calculator


def get_datas():
    with open("./datas/calc.yml") as f:
        datas = yaml.safe_load(f)
    add_datas = datas['add']['datas']
    add_ids = datas['add']['ids']
    print(add_datas)
    print(add_ids)

    return [add_datas, add_ids]


class TestCalc:
    def setup_class(self):
        print("计算开始")
        self.calc = Calculator()

    def teardown_class(self):
        print("计算结束")


    # 加法
    @pytest.mark.parametrize('a,b,expect', get_datas()[0], ids=get_datas()[1])
    def test_add(self, a, b, expect):
        # calc = Calculator()
        result = self.calc.add(a, b)
        assert result == expect

    # 除法
    @pytest.mark.parametrize('a,b,expect', [[1, 1, 1], [100, 2, 50], [0.1, 0.1, 1]],
                             ids=['x_case', 'y_case', 'z_case'])
    def test_div(self, a, b, expect):
        result = self.calc.div(a, b)
        assert result == expect

    # 浮点数可以用round函数保留小数点后面两位
    @pytest.mark.parametrize('a,b,expect', [[0.1, 0.2, 0.3], [0.1, 0.1, 0.2]])
    def test_add_float(self, a, b, expect):
        result = self.calc.add(a, b)
        assert round(result, 2) == expect

    # 除数为0的情况
    @pytest.mark.parametrize('a,b', [[0.1, 0], [1, 0]])
    def test_div1(self, a, b):
        # 捕获异常
        with pytest.raises(ZeroDivisionError):
            result = self.calc.div(a, b)

        # try:
        #     result = self.calc.div(1,0)
        # except ZeroDivisionError:
        #     print("除数为零")
