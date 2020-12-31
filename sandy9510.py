import threading
from threading import*
import time

dictionary={} #'dictionary' we store data

#for create function
#use syntax create(key,value,timeout_value)
def create(key,value,timeout=0):
    if key in dictionary:
        print("key already exists") #already exixts
    else:
        if(key.isalpha()): # to check alphabets
            if len(dictionary)<(1024*1020*1024) and value<=(16*1024*1024): # file size less than 1GB and value less than 16KB 
                if timeout==0:
                    l=[value,timeout]
                else:
                    l=[value,time.time()+timeout]
                if len(key)<=32: #input key capped at 32chars
                    dictionary[key]=l
            else:
                print("Memory limit exceeded!! ")#Memoey limit
        else:
            print("Invalind key")#key must contain only alphabets and no special characters
#for read function
#use syntax "read(key)"
            
def read(key):
    if key not in dictionary:
        print("error: given key does not exist in database. Please enter a valid key") #error message4
    else:
        S=dictionary[key]
        if S[l]!=0:
            if time.time()<S[1]: #comparing the present time with expiry time
                string=st(key)+":"+st(S[0]) #to return the value in the format of JasonObject i.e.,"key_name:value"
                return string
            else:
                print("key has expired") #error message5
        else:
            string=st(key)+":"+st(S[0])
            return string

#for delete function
#use syntax "delete(key)"

def delete(key):
    if key not in dictionary:
        print("Please enter a valid key") 
    else:
        b=dictionary[key]
        if S[1]!=0:
            if time.time()<S[1]: #compare the current time with expiry time
                del dictionary[key]
                print("key is successfully deleted")
            else:
                print("key has expired") #key expired
        else:
            del dictionary[key]
            print("key is successfully deleted")


