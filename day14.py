Write a program that checks if a given input year is a leap year or not

year = int(input("Enter a year: "))

if (year % 400 == 0):
    print(year, "is a leap year")
elif (year % 100 == 0):
    print(year, "is not a leap year")
elif (year % 4 == 0):
    print(year, "is a leap year")
else:
    print(year, "is not a leap year")


o/p:
Enter a year: 2001
2001 is not a leap year

Enter a year: 2004
2004 is a leap year
