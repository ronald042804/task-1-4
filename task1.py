num_elements = [2,4,6,8]

useranswer = input("do you want to add more? ")

if useranswer == "yes":
    userdata = input("number u want to add: ")
    num_elements.append(userdata)
    print(num_elements)
elif useranswer == "no":
    print(num_elements)