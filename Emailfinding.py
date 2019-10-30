import re
mystr ="""
Hello bro, my name is deepak tiwari and my email id is deepak@gmail.com,
And I am learning programming on code with harry youtube channel and I have one more
email:"deepak@dt.com"
and some more
email id:<dt@codewithharry.com>

email:"deepak@dt.com.in" and I have one more harrybhai@codewithharry.com.

"""
patt = re.compile(r'\S+@\S+')
# \S matches any non-whitespace character 
# @ for as in the Email 
# + for Repeats a character one or more times 

matches = patt.finditer(mystr)

for match in matches:
    print(match)
