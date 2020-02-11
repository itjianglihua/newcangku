import yaml
# with open("./data1.yaml","r") as f:
with open("./data2.yml","r",encoding="utf-8") as f:
    value = yaml.safe_load(f)
    #打印解析数据
    print("value={}".format(value))
    #打印类型
    print("类型={}".format(type(value)))


