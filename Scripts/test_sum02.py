import pytest,yaml,os
from Base.getData import GetData

def get_yaml():
    data_l=[]
    # with open("../Data"+os.sep+"sum.yml","r")as f:
    #     data =yaml.safe_load(f)
    data = GetData().get_yaml_data("sum.yml")

    for i in data.values():
        data_l.append((i.get("a"),i.get("b"),i.get("c")))
    return data_l


class TestSum:
    @pytest.mark.parametrize("a,b,c",get_yaml())
    def test_s(self,a,b,c):
        print("\n{}+{}={}".format(a,b,c))
        assert a+b==c