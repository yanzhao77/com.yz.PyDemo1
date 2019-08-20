import argparse

#创建一个解析器
parser = argparse.ArgumentParser()
#添加解析参数
parser.add_argument("eho")
args = parser.parse_args()
print(args.eho)