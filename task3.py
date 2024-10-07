name = ["juan","pedro","lucas","jose","luna"]
 
userdata = input("do you want to remove any element in this list?")
 
if userdata == "yes":
    userdata = input("what name you want to remove?")
    name.remove(userdata)

print(name)