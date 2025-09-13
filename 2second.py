
#  string is data type that store a squenece of characters.

# concatenation "hello"+"world"= "helloworld"

# length  str="hellow" len(str)

# str= input("Enter the string.")

# print("You intered the string", str)

# print("Length of string is",len(str))

# print(str[2:6])   slice , give the substring in the string , starting index : ending index (but ending index is not geted)


# string functions


# str.endsWith("er.")   returns true if string end with string

#  str.capitalize()    capitalize 1st char

#   str.replace(old,new)    replace all occurrence of old with new

#   str.find(word)      return 1st index of 1st occurrence

#   str.count("am")         counts the occurrence of substr in string


# if-elif-else

a=int(input("Enter the first number"))
b=int(input("Enter the second number"))
c=int(input("Enter the third number"))


if(a>=b and a>=c):
    print("largest number is ",a)
elif(b>=c):
    print("largest number is ",b)
else:
    print("largest number is ",c)