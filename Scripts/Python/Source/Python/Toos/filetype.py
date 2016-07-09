#coding:utf-8

# Python通过文件头来判断文件类型
#

import struct

# 支持文件类型
# 用16进制字符串的目的是可以知道文件头是多少字节
# 各种文件头的长度不一样，少半2字符，长则8字符


def imageTypeList():
    return {
        "FFD8FF": "JPEG",
        "89504E47": "PNG",
        "47494638": "GIF",
    }

# 字节码转16进制字符串


def bytes2hex(bytes):
    num = len(bytes)
    hexstr = u""
    for i in range(num):
        t = u"%x" % bytes[i]
        if len(t) % 2:
            hexstr += u"0"
        hexstr += t
    return hexstr.upper()

# 获取文件类型


def isImageFileType(binfile):
    # binfile = open(filename, 'rb') # 必需二制字读取
    isImage = False
    tl = imageTypeList()
    for hcode in tl.keys():
        numOfBytes = 3 #len(hcode) / 2  # 需要读多少字节
        binfile.seek(0)  # 每次读取都要回到文件头，不然会一直往后读取
        hbytes = struct.unpack_from("B" * numOfBytes, binfile.read(numOfBytes))        
        print(numOfBytes)
        #hbytes = struct.unpack_from("B" * numOfBytes, binfile[0:numOfBytes])
        f_hcode = bytes2hex(hbytes)
        if f_hcode == hcode:
            isImage = True
            break
    return isImage

isImageFileType('./test.jpg')