a='this is 200 century 12.841 cr people live here work 2-4 hr'
b='rahulnarwade2050@gmail.com   vija@dkf$@gmail.com anike45@yahoo.com'

import re

c=re.findall('[0-9.-]+',a)
print(c)

d=re.findall('[a-z]+[0-9]+["@"][gmail]+[.][com]+',b)

print(d)



 

