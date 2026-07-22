number= int(input("enter an integer:"))
if number%2==0:
    print(f"{number}is even")
else:
    print(f"{number}is odd")

age=int(input("\nenter our age:"))
if age<13:
    print("you r a child")
elif 13<= age <20:
    print("u r a teen")
elif 20<= age <60:
    print("u r an adult")
else:
    print("u r a senior citizen")
