from app.model import db

class User(object):
    coll = db['testupload']
    def save_info(self,object_info):
        #object_info=object_info
        self.coll.insert(object_info)
        print("save_info() is ok")

    def query_info(self,object_info):
        #object_info=object_info
        info= self.coll.find_one(object_info)
        print("query_info() is ok")
        return info

    def remove_info(self,object_info):
        #object_info=object_info
        self.coll.remove(object_info)
        print("remove_info() is ok")
'''
    def save_user(self,object_user):
        #user = {"name":self.name,"email":self.email}
        user = object_user
        self.coll.insert(user)
        print("aaa")
        print(self.coll.count())
        print("bbb")

    def query_user(self,object_user):
        #users = coll.find(self.object_user).pretty
        user = object_user
        users = self.coll.find_one(user)
        print("ccc")
        print(users)
        print("ddd")
        return users

    def remove_user(self,object_user):
        user = object_user
        print("eee")
        print(user)
        print("fff")
        self.coll.remove(user)
'''