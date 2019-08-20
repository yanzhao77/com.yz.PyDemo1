import requests
import jsonpath
from urllib.request import urlretrieve

url = 'https://http://www.avgq6.com/play/28622-0-0.html?url=\x2f\x6b\x69\x6e\x38\x2d\x31\x37\x37\x38\x2f\x6b\x69\x6e\x38\x2d\x31\x37\x37\x38\x2e\x6d\x33\x75\x38'

response = requests.get(url).json()

images = jsonpath.jsonpath(response, "$..rs16")
names = jsonpath.jsonpath(response, "$..nn")

for image, name in zip(images, names):
    filePath2 = r'F:\douyuFace' + "\\" + name + ".mp4"
    urlretrieve(image, filePath2)
