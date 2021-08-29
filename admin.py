import csv

#__________________________________ admin settings  _________________________________________________

def hospitals_available():
    print("1.Hospital_1")
    print("2.Hospital_2")
    print("3.Hospital_3")
    print("4.Hospital_4")
    print("5.Hospital_5")



def Donation_camps():
    print("1.Address_1")
    print("2.Address_2")
    print("3.Address_3")
    print("4.Address_4")
    print("5.Address_5")


def emergency_notifications():
    print("__________IMPORTANT NOTICS__________")
    print("Blood group A is in limited supply For those who are in need in Blood group A.")
    print(" please search for alternative solutions too please don't depend 100% on us ")
    print("We are sorry for the inconvinience happened!!!!!!!!")


def register():
    with open("users.csv", mode="a", newline="") as f:
        writer = csv.writer(f, delimiter=",")
        name = input("please enter name : ")
        password = input("please enter password : ")
        password2 = input("please re-enter password : ")
        if password == password2:
            writer.writerow([name, password])
            print("registration is successful !!")
            return 1
        else:
            print("please try again")
            return 0
            

def login():
    name = input("please enter name : ")
    password = input("please enter password : ")
    with open("users.csv", mode="r") as f:
        reader = csv.reader(f, delimiter=",")
        for row in reader:
            if row == [name, password]:
                print("you are logged in !!")
                return 1
            else:
                continue


def request():
    print("Group A = 1")
    print("Group B = 2")
    print("Group AB = 3")
    print("Group O = 4")
    responce = input("which blood group you are willing to request, please select corrosponding code ")
    
    if responce == "1":
        with open("group_A.csv", mode="a", newline="") as f:
            writer = csv.writer(f, delimiter=",")
            name = input("enter your name again : ")
            password = input("enter your passward again : ")
            email=input("enter your email address : ")
            sex=input("please enter your gender : male , female? : ")
            age=input("enter your age : ")
            writer.writerow([name, password, email, sex,age])
            print("your name is now added group A request list .... after approving your request soon you will get the mail which will contain further instructions!!!!")
    elif responce == "2":
        with open("group_B.csv", mode="a", newline="") as f:
            writer = csv.writer(f, delimiter=",")
            name = input("enter your name again : ")
            password = input("enter your passward again : ")
            email=input("enter your email address : ")
            sex=input("please enter your gender : male , female? : ")
            age=input("enter your age : ")
            writer.writerow([name, password, email, sex,age])
            print(
                "your name is now added group B request list .... after approving your request soon you will get the mail which will contain further instructions!!!!")
    elif responce == "3":
        with open("group_AB.csv", mode="a", newline="") as f:
            writer = csv.writer(f, delimiter=",")
            name = input("enter your name again : ")
            password = input("enter your passward again : ")
            email=input("enter your email address : ")
            sex=input("please enter your gender : male , female? : ")
            age=input("enter your age : ")
            writer.writerow([name, password, email, sex,age])
            print(
                "your name is now added group AB request list .... after approving your request soon you will get the mail which will contain further instructions!!!!")
    elif responce == "4":
        with open("group_O.csv", mode="a", newline="") as f:
            writer = csv.writer(f, delimiter=",")
            name = input("enter your name again : ")
            password = input("enter your passward again : ")
            email=input("enter your email address : ")
            sex=input("please enter your gender : male , female? : ")
            age=input("enter your age : ")
            writer.writerow([name, password, email, sex,age])
            print(
                "your name is now added group O request list .... after approving your request soon you will get the mail which will contain further instructions!!!!")


def Donation():
    print("Group A = 1")
    print("Group B = 2")
    print("Group AB = 3")
    print("Group O = 4")
    responce = input("which blood group you are willing to donate? please select corrosponding code ")
    if responce == "1":
        with open("Group_A_Blood_doner.csv", mode="a", newline="") as f:
            writer = csv.writer(f, delimiter=",")
            name = input("enter your name again : ")
            password = input("enter your passward again : ")
            email=input("enter your email address : ")
            sex=input("please enter your gender : male , female? : ")
            age=input("enter your age : ")
            writer.writerow([name, password, email, sex,age])
            print("Thank you for your responce your  name is added in the doner list of group A .")
            print("you can donate blood in nearby hospitals as mentioned on main menu")    
    elif responce == "2":
        with open("Group_B_Blood_doner.csv", mode="a", newline="") as f:
            writer = csv.writer(f, delimiter=",")
            name = input("enter your name again : ")
            password = input("enter your passward again : ")
            email=input("enter your email address : ")
            sex=input("please enter your gender : male , female? : ")
            age=input("enter your age : ")
            writer.writerow([name, password, email, sex,age])
            print("Thank you for your responce your  name is added in the doner list of group B .")
            print("you can donate blood in nearby hospitals as mentioned on main menu")    
    elif responce == "3":
        with open("Group_AB_Blood_doner.csv", mode="a", newline="") as f:
            writer = csv.writer(f, delimiter=",")
            name = input("enter your name again : ")
            password = input("enter your passward again : ")
            email=input("enter your email address : ")
            sex=input("please enter your gender : male , female? : ")
            age=input("enter your age : ")
            writer.writerow([name, password, email, sex,age])
            print("Thank you for your responce your  name is added in the doner list of group AB .")
            print("you can donate blood in nearby hospitals as mentioned on main menu")    
    elif responce == "4":
        with open("Group_O_Blood_doner.csv", mode="a", newline="") as f:
            writer = csv.writer(f, delimiter=",")
            name = input("enter your name again : ")
            password = input("enter your passward again : ")
            email=input("enter your email address : ")
            sex=input("please enter your gender : male , female? : ")
            age=input("enter your age : ")
            writer.writerow([name, password, email, sex,age])
            print("Thank you for your responce your  name is added in the doner list of group O .")
            print("you can donate blood in nearby hospitals as mentioned on main menu")    

def success():
    print("If you have successfull doner please select -- 1")
    print("IF your are successfull blood reciver = 2")
    responce = input("which blood group you are willing to donate? please select corrosponding code ")
    if responce == "1":
        with open("success_doners.csv", mode="a", newline="") as f:
            writer = csv.writer(f, delimiter=",")
            name = input("enter your name again : ")
            password = input("enter your passward again : ")
            email=input("enter your email address : ")
            sex=input("please enter your gender : male , female? : ")
            age=input("enter your age : ")
            blood_group=input("enter your blood group you have donated : ")
            hospital = input("name of center where you have donated the blood")
            writer.writerow([name, password, email, sex,age,blood_group , hospital])
            print("Thank you for your responce your  name is added in successfull doner list .")
            
    elif responce == "2":
        with open("success_recivers.csv", mode="a", newline="") as f:
            writer = csv.writer(f, delimiter=",")
            name = input("enter your name again : ")
            password = input("enter your passward again : ")
            email=input("enter your email address : ")
            sex=input("please enter your gender : male , female? : ")
            age=input("enter your age : ")
            blood_group=input("enter your blood group you have recived : ")
            hospital = input("name of center where you have recived the blood")
            writer.writerow([name, password, email, sex,age,blood_group , hospital])
            print("Thank you for your responce your  name is added in the successfull reciver .")
            print("you can donate blood in nearby hospitals as mentioned on main menu")    
    