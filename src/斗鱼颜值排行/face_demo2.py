import base64

from aip import AipFace

#这是一个人脸识别，要联网
#调用百度的智能云，测评打分后返回数据
def face_rg(filePath):
    """ 你的 APPID AK SK """
    APP_ID = '17478660'
    API_KEY = 'KnGt4QsKBZqUL7Tuzi9fBqqZ'
    SECRET_KEY = '9ZUIcTGrqH87qGTlwyM7ZvIOqRAszg9q'
    client = AipFace(APP_ID, API_KEY, SECRET_KEY)
    with open(filePath, 'rb') as fp:
            data = base64.b64encode(fp.read())

    image = data.decode()

    options = {}
    options["face_field"] = "beauty"
    imageType = "BASE64"

    """调用人脸识别"""
    result = client.detect(image, imageType, options)
    return result


#print(face_rg(r"F:\douyuFace\斐小白.png"))
#print(face_rg(r"C:\Users\yan34177\Pictures\Phototastic\QQ图片20190924153708.jpg"))
#print(face_rg(r"C:\Users\yan34177\Pictures\Phototastic\微信图片_20180703191034.jpg"))
print(face_rg(r"C:\Users\yan34177\Pictures\Phototastic\微信图片_20191009180509.jpg"))
#print(face_rg(r"C:\Users\yan34177\Pictures\Phototastic\微信图片_20190511140833.jpg"))
#print(face_rg(r"C:\Users\yan34177\Pictures\Phototastic\微信图片_20190710182117.jpg"))