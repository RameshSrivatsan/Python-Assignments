
# coding: utf-8

# In[8]:

#1
class Store():
    
    def elec_bill(self,area):
        a = 0.15
        b = 0.19
        self.bill= area*a*b
        return(self.bill)

        
    


# In[9]:

d = Store()
d.elec_bill(120)


# In[54]:

#2
class Counter_():
    d = {}
    l = []
    
    def inital(self,sentence):
        self.sentence_1 = sentence.split(" ")
        for j in self.sentence_1: 
            self.l.append(j)
            
        
        
        
    def count_(self,sentence):
        for j in self.l:
            self.d.setdefault(j,0)
            self.d[j]+=1
            
        return(self.d)
  
    


        
    


# In[55]:

e = Counter_()
e.inital("Hello World Hello")
e.count_("Hello World Hello")


# In[77]:

#3
class MyCounter():
    l = []
    def __init__(self,sentence):
        self.sentence = sentence
        
    def __str__(self):
        self.sentence_2 = sentence.split(" ")
        print(self.sentence_2)
        print("MyCounter" + "(" + str(len(self.sentence_2)) + ")")
         
         
        
        
obj = MyCounter('Fe Fi Fo Fum where is my drum')
str(obj)


# In[ ]:




# In[103]:

#4
class MyCounter():
    
    def __init__(self,sentence):
        self.sentence = sentence
        
    def __str__(self,sentence):
        self.sentence_2 = self.sentence.split(" ")
        print("MyCounter" + "(" + str(len(self.sentence_2)) + ")")
         
    def __repr__(self,sentence):
        self.sentence_3 = self.sentence.split(" ")
        print("<" + "MyCounter " +"'" +str(self.sentence[:13]) + '....' + "'"+'>')
         
        
        
obj = MyCounter('Fe Fi Fo Fum, where is my drum')
obj.__str__('Fe Fi Fo Fum, where is my drum')
obj.__repr__('Fe Fi Fo Fum, where is my drum')


# In[110]:

#5
class Question():
    l = ['I am fine','Course is pretty good']
    m = ['How are you?','How are your courses?']
    
    def __str__(self):
        for a, b in zip(self.m, self.l):
            print(a, b)
            
obj = Question()
obj.__str__()


# In[115]:

#6
I dont know how to solve this


# In[6]:

#7
class ValueExceptionError(Exception):
        
    MSG = 'It has raised a ValueExceptionError'

    def __init__(self, *args, **kwargs):
        super().__init__(self.MSG, *args, **kwargs)

class PartyError():
    MSG = ''
    
    def __init__(self,n):
        self.n=n
    
   
        
    def Error(self):
        if self.n<10:
            raise ValueExceptionError()
    


# In[7]:

p=PartyError(8)
p.Error()


# In[20]:

#8
class Bankaccount():
    def __init__(self,account_no,balance):
        self.account_no = account_no
        self.balance = balance

    def deposit(self,deposit_amount):
        self.balance = self.balance + deposit_amount
        return(self.balance)
    def withdraw(self,withdrawal_amount):
        self.balance = self.balance - withdrawal_amount
        return(self.balance)
    def print_balance(self):
        print("Account No.:  " + str(self.account_no ) +' '+ "Balance:  " + str(self.balance))

        
a = Bankaccount(12345678, 10)

a.deposit(5)
a.withdraw(3)
a.print_balance()


# In[37]:

#9

class Bankaccount:
    def __init__(self,account_no,balance):
        self.account_no = account_no
        self.balance = balance

    def deposit(self,deposit_amount):
        self.balance = self.balance + deposit_amount
        return(self.balance)
    def withdraw(self,withdrawal_amount,minimum_balance):
        self.balance = self.balance - withdrawal_amount
        if self.balance < minimum_balance:
            raise ValueError("No Money")

        return(self.balance)
    def print_balance(self):
        print("Account No.:  " + str(self.account_no ) +' '+ "Balance:  " + str(self.balance))
class MinBalanceAccount(Bankaccount):

    def __init__(self,account_id,balance,minimum_balance):
        self.account_id = account_id
        self.minimum_balance = minimum_balance
        self.balance = balance
    
    

a = MinBalanceAccount(1,100,10)

a.withdraw(95,10)


# In[ ]:



