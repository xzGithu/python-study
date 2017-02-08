#-*- coding:utf-8-*-




def functionList():
    print '''1:check 2:add 3:modify 4:delete 5:return 6:quit'''

def phoneInput(phonenumber):
    if phonenumber.isdigit() == True:
    #if len(phonenumber)==11 and phonenumber.isdigit()==True:
        return True
    else:
        return False

def nameList():
    namelist = []
    for i in range(len(infolist)):
        if infolist[i]["name"] not in namelist:
            namelist.append(infolist[i]["name"])
    return namelist

def findNameLocation(name):
    for j in range(len(infolist)):

        if infolist[j]["name"]==name:
            return j

def listInfo():
    if len(infolist)==0:
        print 'Empty contact list!'
    else:

        for i in range(len(infolist)):
            nameinfo = infolist[i]
            print "Name:%s,Phone:%s,Extra:%s" %(infolist[i]["name"],infolist[i]["phone"],infolist[i]["extra"])
            print "  "
            print ""

def addPerson():
    while True:
        nameInput = raw_input("Please input one name:")
        namelist = nameList()
        if nameInput in namelist:
            print "Contact is already exist"
            print ""
        else:
            newInfo={}
            newInfo["name"]=nameInput
            while True:
                phone = raw_input("Please input its phone num:")
                if phoneInput(phone) == True:
                    newInfo["phone"] = phone
                    break
                else:
                    print "Input again:"
            #while True:
            extra = raw_input("Please input more information of this contact:")
            newInfo["extra"] = extra
            infolist.append(newInfo)
            print "已成功添加联系人"
            print "Name:%s,Phone:%s,Extra:%s"%(newInfo["name"],newInfo["phone"],newInfo["extra"])
            break
        break

def delPerson():
    while True:
        nameInput = raw_input("Please input which contact you want to delete:")
        namelist = nameList()
        if nameInput in namelist:
            j = findNameLocation(nameInput)
            del infolist[j]
            print "Delete succeed"
            break
        else:
            print "Contact doesn't exist!"

def modPerson():
    while True:
        nameInput = raw_input("Which person do you want to modify:")
        namelist = nameList()
        if nameInput in namelist:
            print "Please input what do you want to modify:"
            print "1 Name"
            print "2 Phone number"
            print "3 Extra information"
            while True:
                num = raw_input("Please select:")
                if num == "1":
                    newnameInput = raw_input("Please input your name:")
                    j = findNameLocation(nameInput)
                    infolist[j]["name"]=newnameInput
                    print "Succeed"
                    break
                elif num == "2":
                    while True:

                        newphone = raw_input("Please input new NUM:")
                    #j = findNameLocation(nameInput)
                        if phoneInput(newphone)==True:
                            j = findNameLocation(nameInput)
                            infolist[j]["phone"] = newphone
                            print "succeed"
                            break
                        else:
                            print "Please retry the NUM:"
                    break

                elif num == "3":

                    newextra = raw_input("Please input new extra information:")
                    j = findNameLocation(nameInput)
                    infolist[j]["extra"] = newextra
                    print "succeed"
                    break
                else:
                    print "Some error! Input again."
            break

        else:
            print "The name you input doesn't exist"

def serchPerson():
    nameInput = raw_input("Please input the name you want to search:")
    namelist = nameList()
    if nameInput in namelist:
        print "Succeed"
        j = findNameLocation(nameInput)
        print "Name:%s,Phone:%s,Extra:%s"%(infolist[j]["name"],infolist[j]["phone"],infolist[j]["extra"])
    else:
        print "Not exist."

infolist=[]
print "Welcome to my contact manager prom"
print ""
print ""
functionList()

while True:
    Input = raw_input("What do you want to do:")

    if Input == "1":
        listInfo()
        continue
    elif Input == "2":
        addPerson()
        continue
    elif Input == "3":
        modPerson()
        continue
    elif Input == "4":
        delPerson()
        continue
    elif Input == "5":
        functionList()
        continue
    elif Input == "6":
        break
    else:
        print "Error! Retry."
