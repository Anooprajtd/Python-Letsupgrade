#!/usr/bin/env python
# coding: utf-8

# In[1]:


port1 = {21: "FTP", 22:"SSH", 23: "telnet", 80: "http"}
print(dict((v,k) for k,v in port1.items()))


# In[2]:


sum3=[]
sum1 = [(1,2), (3,4), (5,6)]
for k,v in sum1:
    sum2=k+v
    sum3.append(sum2)
print(sum3)


# In[4]:


list2=[]
list1=[(1,2,3),[1,2],["a","hit","less"]]
for i in list1:
    if type(i)==tuple:
        for each in i:
            list2.append(each)            
    if type(i)==list:
        for each in i:
            list2.append(each)
print(list2)

