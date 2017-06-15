import bson.binary
from io import StringIO
from app.model.dbtest import User
import gridfs

##def save_file(SN,file_content):
def save_file(SN,img_filename):

    with open(img_filename,'rb') as myimage:
        #content = StringIO(myimage.read())
        content = myimage.read()
        #img_file_content = bson.binary.Binary(content)

        new_object = {"userSN":SN,"user_IMG":content}
        User().save_info(new_object)

    #file_content =  img_file_content.read()

    #print(SN)
    #print(file_content)
    ##new_object = {"userSN":SN,"user_IMG":file_content}
    ##User().save_info(new_object)


def query_file(SN):
    query_object = {"userSN":SN}
    SN_OK = User().query_info(query_object)

    if SN_OK is None:
        print ("There is no userSN:" + SN)

    return SN_OK



