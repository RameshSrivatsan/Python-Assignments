
# coding: utf-8

# In[ ]:

#1 Compilers vs Interpreters 
Generally Compilers and Interpreters are used for converting the code written by humans into a code which can be understood
by the machines. But there is a small difference in the way they work. Interpreters execute the every line and converts it
into a machine code whereas compilers scan the whole program and convert them into machine codes at a strech. Compilers are fast
whereas Interpreters are slow.
Python is an object oriented language.


# In[7]:

#2 printing a limerick
limerick="""There was a guy named Lizz
Who loves Appy Fizz
He awoke in a fright
In the middle of the night
And found it was a dizz """
print(limerick)
            


# In[10]:

#2
limerick="There was a guy named Lizz \nWho loves Appy Fizz \nHe awoke in a fright \nIn the middle of the night \nAnd found it was a dizz "
print(limerick)


# In[ ]:

#3 printing 5 continous backslashes
print("\\\\\")


# In[ ]:

#4 escape sequence for tab and carriage return
The escape sequence characters for tab and carriage returns are as follows:
    Horizontal tab : \t
    Vertical tab: \v
    Carriage return: \r


# In[ ]:

#5 About Pip
Pip is a package management system that can be used for installing various directories or software packages.


# In[ ]:

#6 How to find out the arguments that can be passed with print
The arguments that can be passed with print are:
    file,sep,end,flush
Type print? in the jupyter notebook to know the arguments that can be passed with print


# In[ ]:

#7 PEP8 vs PEP257
PEP8 convention is widely followed.


# In[27]:

#8 positive x-intercept
A=1
B=3
C=-4
x1=((((-1)*B)+(((B**2)-4*A*C)**0.5))/(2*A))
x2=((((-1)*B)-(((B**2)-4*A*C)**0.5))/(2*A))
if(x1>0):
    print(x1)
else:
    print(x2)
    


# In[ ]:

#9 modulo 2
for x in range(1,10):
    a=(3*x)%2
    print(a)


# In[ ]:

#9 modulo 3
for x in range(1,10):
    b=(3*x)%3
    print(b)


# In[ ]:

#10 printing our favorite word one million times
print("Winter\n"*10000000)


# In[ ]:

#11 Decoding UTF-8 to string
b'\xf0\x9f\x8d\xa9 + \xf0\x9f\x8d\xb5'.decode('utf-8')


# In[ ]:




# In[ ]:



