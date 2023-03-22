import sys
import os 
import json

class Link:
    
    Link=""
    def __init__(self):
         self.filepath=sys.argv[1]
    def getlink(self):
        if os.stat("utils.json").st_size==0:
            username=input("Enter the username of your Github :")
            Repo=input("Enter your Repo :")
            personalInfo={
                "username":username.strip(),
                "repo":Repo.strip()
            }
            y=json.dumps(personalInfo)
            f=open("utils.json",'w')
            f.write(y)
            f.close()
            Link="https://github.com/{}/{}/blob/main/{}".format(username,Repo,self.filepath)

        else :
            with open("utils.json") as readFile:
                info=json.load(readFile)
                username=info['username']
                Repo=info['repo']  
                Link="https://github.com/{}/{}/blob/main/{}".format(username,Repo,self.filepath)
        return Link
x=Link()
print(x.getlink())