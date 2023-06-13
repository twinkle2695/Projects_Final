l=[]
while True:
    print("Admin")
    print("User")
    print("Exit")
    n=int(input("Enter your choice: "))
    if n==1:
        print("You have logged in as Admin")
        while True:
            print("1.Insert")
            print("2.Update")
            print("3.Delete")
            print("4.Display")
            print("0.Exit")
            c=int(input("Enter your choice: "))
            if c==1:
                print("1.Insert")
                dct1={}
                a=input("Enter your question: ")
                b=input("Enter option 1: ")
                c=input("Enter option 2: ")
                d=input("Enter option 3: ")
                e=input("Enter option 4: ")
                ans=input("Enter your ans: ")
                dct1["q"]=a
                dct1["o"]=[b,c,d,e]
                dct1["rans"]=ans
                l.append(dct1)
                print(l)





            elif c==2:
                print("2.Update")
                oq=input("Enter old question")
                if oq in dct1:
                    print("Found")
                    oq=input("Enter new Question: ")
                    dct1["q"]=oq
                    print("Done")
                    print(dct1)
                else:
                    print("Invalid")



            elif c==3:
                print("Delete")
                l2=[]
                a=input("Enter the question to delete: ")
                for i in l:
                    if a in i["q"]:
                        print("Question Deleted!!!")
                        l2 = l
                        l.remove(i)
                        print(l)
                    else:
                        print("not found")





            elif c==4:
                print("Display")
                for i in l:
                    for k,v in i.items():
                        print(k,":",v)
            elif c==0:
                print("Exit,Bye-Bye!!!!!")
                break
    elif n==2:
        print("Welcome to Quiz")
        ul=[]
        while True:
            print("Register")
            print("Login")
            print("Exit")
            z=int(input("Enter your choice"))
            if z==1:
                f={}
                print("Register")
                name=input("Enter your Username: ")
                password=input("Enter your password: ")
                f["Name"]=name
                f["Password"]=password
                ul.append(f)
                print(ul)
                print("Registered Successfully")

            elif z==2:
                print("Login")
                a=input("Enter your username: ")
                b=input("Enter your password: ")
                for i in ul:
                    if(i["Name"]==a and i["Password"]==b):
                        print("Login Successfully")
                        for i in l:
                            print("Q.1",i['q'])
                            for j in i['o']:
                                    print(j)
                            rans=input("Enter you answer")

            elif z==0:
                print("Exit")
                break
            else:
                print("Invalid Input")


    elif n==0:
        print("You have Logout")
        break
    else:
        print("Invalid Input")