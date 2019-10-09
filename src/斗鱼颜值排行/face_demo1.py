import requests
import jsonpath
from urllib.request import urlretrieve

url = 'https://www.douyu.com/gapi/rknc/directory/yzRec/1'

response = requests.get(url).json()
#这是一个爬虫测试，爬取斗鱼直播颜值区主播的照片
images = jsonpath.jsonpath(response, "$..rs16")
names = jsonpath.jsonpath(response, "$..nn")

for image, name in zip(images, names):
    filePath2 = r'F:\IDEADownloads\com.yz.PyDemo1\src\斗鱼颜值排行\douyumm\douyuFace' + "\\" + name + ".png"
    print(filePath2)
    urlretrieve(image, filePath2)
