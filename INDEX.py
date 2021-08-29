from admin import*
def mainmenu():
    while (1):
            print("1.__To view available hospitals near you select -- 1")
            print("2.__To make a request for a perticular blood group select -- 2")
            print("3.__To see any emergency notifications from Blood bank select -- 3")
            print("4.__To view blood donation camps near you select -- 4")
            print("5.__For your sincere blood donation please select -- 5")
            print("6.__To register your name as a successfull doner or successfull reciver please select -- 6")
            print("7.__To exit please select -- 7")
            response = input("Please select corrosponding choice : ")
            if response == "1":
                hospitals_available()

            elif response == "2":
                request()

            elif response == "3":
                emergency_notifications()

            elif response == "4":
                Donation_camps()

            elif response == "5":
                Donation()

            elif response == "6":
                success()   

            elif response == "7":
                exit(1)

def work():
    print("*__for login please select--1")
    print("*__if you are new then please register , for registration please select --2")
    choice = input("*__Please select corrosponding choice : ")
    if choice == "1":
        if login():
            mainmenu()

            
        
    elif choice == "2":
        if register():
            mainmenu()
        mainmenu()









    


work()
