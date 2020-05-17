import os
import zipfile


def unzip(zipFile):

    print('开始解压'+zipFile)

    path = 'file/amiibo/'
    zFile = zipfile.ZipFile(path + os.sep + zipFile, "r")
    for file in zFile.namelist():

        if file.rsplit('.', 1)[1].lower() in {'bin','BIN'}:
            zFile.extract(file,path)

            #文件名 空格改为_，并且改为小写
            oldName = path + os.sep + file   # os.sep添加系统分隔符
            newName = path + os.sep + file.replace(' ','_').lower()
            #print(file.lower())
            os.rename(oldName,newName)

    zFile.close()

    os.remove(path+ os.sep + zipFile) # 删除压缩包

    print('解压完毕，'+zipFile+'已删除')

def save(cmd):

    msg ='\n'

    for _ in cmd:
        msg += _


    path = 'file/scriptcopy.txt'
    with open(path,'w') as f:
        f.write(msg)

def sendCMD(cmd):
    return cmd+'\n'
def readAmiibo():

    cmd = list()

 #   print('开始读取全部的amiibo')

    path = 'file/amiibo/'

    fileList=os.listdir(path)

    cmd.append(sendCMD('DOWN'))
    cmd.append(sendCMD('2000'))

    for amiibo in fileList:
        if amiibo.rsplit('.', 1)[1].lower() == 'bin':

            cmd.append(sendCMD('Y'))
            cmd.append(sendCMD('amiibo '+amiibo))
            cmd.append(sendCMD('A'))
            cmd.append(sendCMD('2000'))
            cmd.append(sendCMD('A'))
            cmd.append(sendCMD('2000'))
            cmd.append(sendCMD('A'))
            cmd.append(sendCMD('2000'))

#    print('amiibo全部读取完毕')
    cmd.append(sendCMD('B'))
    cmd.append(sendCMD('2000'))
    cmd.append(sendCMD('B'))
    
    return cmd

def run(zipName):

    #解压上传的压缩包
    unzip(zipName)
                                                                                                                                                                                                 #批量读取amiibo
    a = readAmiibo()

    save(a)

