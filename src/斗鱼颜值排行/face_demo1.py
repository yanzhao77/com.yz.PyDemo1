import requests
import jsonpath
from urllib.request import urlretrieve

url = 'https://www.douyu.com/gapi/rknc/directory/yzRec/1'

response = requests.get(url).json()

images = jsonpath.jsonpath(response, "$..rs16")
names = jsonpath.jsonpath(response, "$..nn")

for image, name in zip(images, names):
    filePath2 = r'F:\douyuFace' + "\\" + name + ".png"
    urlretrieve(image, filePath2)
