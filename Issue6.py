#Revision #1 Begin Date: 2/4/2022
#Begin Abigail Noyes 2/4/2020

import string
from random import randint


password = " "
for i in range(5):
    #import random letter from alphabet
    i = chr(randint(65,90))
    for j in range (5):
        j = chr(randint(65,90)).lower()
    password = str(password) + i + j
print(password)
        
    
    
#Revision #1 End Date: 2/4/2022
#End Abigail Noyes / Project #1
#Manager:Abigail Noyes / Lead Tech: Abigail Noyes / Project #1
