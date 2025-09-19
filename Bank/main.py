
import json 
import random
import string
from pathlib import Path 


class Bank:
    database ='data.json'
    data=[]

    try: 
        if Path(database).exists():
             with open(database) as fs:
                 data=json.loads(fs.read())
        else :
            print("No such file exits") 
            
        
    except Exception as err:
        print(f"an exception occured as {err}")
        
        
    
    @staticmethod
    def __update():
        with open(Bank.database,"w") as fs :
            fs.write(json.dumps(Bank.data))
            
    @classmethod
    def __accountgenerate(cls):
        alpha = random.choices(string.ascii_letters,k=3)
        num=random.choices(string.digits,k=3)
        spchar= random.choices("!@#$%^&*",k=1)
        id= alpha+num+spchar
        random.shuffle(id)
        return "".join(id)
    
        
    
    def createAccount(self):
        info={
            "name":input("Tell your name :- "),
            "age":int(input("Tell Your age ")),
            "email":input("Enter your email"),
            "pin":int(input("Enter your pin :- ")),
            "accountNumber": Bank.__accountgenerate(),
            "balance":0
        }
        
        if info['age']<18 or len(str(info['pin']))!=4 :
            print("Sorry your cannot create your account")
        else : 
            print("Account has been created successfully ")
            for i in info:
                print(f"{i} : {info[i]}")
            print("please note down your account numeber")
                
            Bank.data.append(info)
            
            Bank.__update()
            
    def withdrawmoney(self):
        accountNumber= int(input("Enter your account numebr :- "))
        pin=int(input("Enter your pin :- "))
        # print(Bank.data)
        userdata= [i for i in Bank.data if i['accountNumber']==accountNumber and i['pin']==pin]
        
        # print(userdata)
        if userdata==False:
            print("Sorry no Account Found !!")
        else :
            amount=int(input("How mush you wants to withdrwal"))
            if amount<userdata[0]['balance']:
                input("Sorry ! your balance is insufficient || balance is low !! ")
            else:
                userdata[0]['balance']-=amount
                Bank.__update()
        
            
    def depositMoney(self):
        accountNumber=input("Enter your account number :- ")
        pin=int(input("Enter your pin :- "))
        # print(Bank.data)
        userdata= [i for i in Bank.data if i['accountNumber']==accountNumber and i['pin']==pin]
        
        # print(userdata)
        if userdata==False:
            print("**********************Sorry no Account Found !! ***********************")
        else :
            amount=int(input("How mush you wants to deposit"))
            if amount<0 or amount>=10000:
                input("*************Sorry the amount is too many you can depost below 10000 or above 0 ***************")
            else:
                userdata[0]['balance']+=amount
                Bank.__update()
    
    
    def updateDetails(self):
        accountNumber=input("Enter your account Number")
        pin=int(input("Enter your pin"))
        
        userdata=[i for i in Bank.data if i['accountNumber']==accountNumber and i['pin']==pin]
        
        if userdata==False:
            print("Sorry no any Account found !!")
        else : 
            print("******************Enter the details where you wants to update else skip this **********")
            print("******************you don't update the AccountNumber , age and balance **********")
            
            newdata = {
                "name": input("please tell new name or press enter : "),
                "email":input("please tell your new Email or press enter to skip :"),
                "pin": input("enter new Pin or press enter to skip: ")
            }
            
            if newdata["name"] == "":
                newdata["name"] = userdata[0]['name']
            if newdata["email"] == "":
                newdata["email"] = userdata[0]['email']
            if newdata["pin"] == "":
                newdata["pin"] = userdata[0]['pin']
            
            newdata['age'] = userdata[0]['age']

            newdata['accountNumber'] = userdata[0]['accountNumber']
            newdata['balance'] = userdata[0]['balance']
            
            if type(newdata['pin']) == str:
                newdata['pin'] = int(newdata['pin'])
            

            for i in newdata:
                 if newdata[i] == userdata[0][i]:
                     continue
                 else:
                     userdata[0][i] = newdata[i]

            Bank.__update()
            print("details updated successfully")
            
        
    def viewDetails(self):
        accountNumber=input("*****Enter your account number :- ")
        pin=int(input("*********Enter your pin :- "))
        
        userdata= [i for i in Bank.data if i['accountNumber']==accountNumber and i['pin']==pin]
        
        if userdata==False:
            print("******************Sorry no Account found !!********************")
        else :
            info= userdata[0]
            for i in info:
                print(f"{i} :  {info[i]}")
                
        
            
        









user=Bank()

print("Press 1 for creating an account")
print("press 2 for Deposit money in the bank")
print("Press 3 for withdrawing the money")
print("Press 4 for details")
print("Press 5 for updating the details")
print("Press 6 for deleting your acccount")

check=int(input("Tell your response :- "))

if  check==1:
    user.createAccount()
if check==2:
    user.depositMoney()
if check==3:
    user.depositMoney()
if check==4:
    user.viewDetails()
if check==5:
    user.updateDetails()
    