import base64

from aip import AipFace


def face_rg(filePath):
    """ 你的 APPID AK SK """
    APP_ID = '16225674'
    API_KEY = 'XVQt1ZkN0xzZ52iGzR4Kblse'
    SECRET_KEY = 'PoKaeGt6bSzlMX0Ob3acuyP9WF0v0DwG'
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
print(face_rg(r"C:\Users\yan34177\Pictures\Phototastic\微信图片_20190511134211.jpg"))
#print(face_rg(r"C:\Users\yan34177\Pictures\Phototastic\微信图片_20190524134152.jpg"))
#print(face_rg(r"C:\Users\yan34177\Pictures\Phototastic\微信图片_20180703191034.jpg"))
#print(face_rg(r"C:\Users\yan34177\Pictures\Phototastic\微信图片_20190511140833.jpg"))
#print(face_rg(r"C:\Users\yan34177\Pictures\Phototastic\微信图片_20190710182117.jpg"))