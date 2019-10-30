import re
mystr ="""
Hello bro, my name is deepak tiwari and my email id is deepak@gmail.com,
And I am learning programming on code with harry youtube channel and I have one more
email:"deepak@dt.com"
and some more
email id:<dt@codewithharry.com>

email:"deepak@dt.com.in" and I have one more harrybhai@codewithharry.com.

"""
# email = re.compile(r'\S+@\S+')
# \S matches any non-whitespace character 
# @ for as in the Email 
# + for Repeats a character one or more times 
# matches = email.finditer(mystr)
# for i in matches:
#     print(i)


#----short to find all ------
# short = re.findall(r'\w+@\S+\w',mystr)
# print(short)



#---------Nice Way----
email = re.findall(r"[0-9a-zA-Z._+%]+@[0-9a-zA-Z._+%]+[.][a-zA-Z.0-9]",mystr)
#number 0-9 upper and lower case a-zA-Z symbols ._+% 
# + means more than one occurance 
# @ only one and .
print(email)
