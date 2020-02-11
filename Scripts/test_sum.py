import pytest,yaml,os

def get_yaml():
    data_l=[]
    with open("../Data"+os.sep+"sum.yml","r")as f:
        data =yaml.safe_load(f)
        # print("data={}".format(data))
        for i in data.values():
            data_l.append((i.get("a"),i.get("b"),i.get("c")))
    return data_l
# print(get_yaml())
# get_yaml()

# data={
# 'test_001': {'b': 2, 'a': 1, 'c': 3},
# 'test_002': {'b': 3, 'a': 2, 'c': 5},
# 'test_003': {'b': 5, 'a': 4, 'c': 6}
# }
# data_l = []  #data.values = [{'b': 2, 'a': 1, 'c': 3},{'b': 3, 'a': 2, 'c': 5},{'b': 5, 'a': 4, 'c': 6}]
# for i in data.values():
# #     data_l.append(tuple(i.values()))
# #
#     data_l.append((i.get("a"),i.get("b"),i.get("c")))
# print(data_l)

class TestSum:
    @pytest.mark.parametrize("a,b,c",get_yaml())
    def test_s(self,a,b,c):
        print("\n{}+{}={}".format(a,b,c))
        assert a+b==c