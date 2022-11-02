#!/usr/bin/env python
# coding: utf-8

# # Problem Set2

# ### Question 1 
# Consider the following Python module:
# <br>
# a = 0
# <br>
# def b():
# <br>
# global a
# <br>
# a = c(a)
# <br>
# def c(a):
# <br>
# return a + 2
# 
# b()
# <br>
# b()
# <br>
# b()
# <br>
# a
# <br>
# ?

# #### What value is displayed when the last expression (a) is evaluated? Explain your answer by indicating what happens in every executed statement.

# In[1]:


a = 0
def b():
 global a    
 a = c(a)   
def c(a):
 return a + 2
b()
b()
b()
a 


# #### Explanation:
# 
# First call
# b(): a's value is 0 it calls the function c(a)
# <br>so as c(a)=a+2 then a=0+2=2, now global a's value gets changed to 2 
# <br>
# Second call
# b(): a's value is 2 again calls c(a)
# <br>now a= 2+2=4, now global a's value gets updated to 4
# <br>
# Third call
# <br>b()
# Similarly (a)=a+2, then a = 4+2=6  global a's value gets changed to 6
# <br>
# Hence Final value after 3 call a value = 6

# ### Question 2
# Function fileLength(), given to you, takes the name of a file as input and returns
# the length of the file:
# <br>
# fileLength('midterm.py')
# <br>
# 284
# <br>
# fileLength('idterm.py')
# <br>
# Traceback (most recent call last):
# <br>
# File "<pyshell#34>", line 1, in <module>
# <br>
# fileLength('idterm.py')
# <br>
# File "/Users/me/midterm.py", line 3, in fileLength
#  <br>
# infile = open(filename)
#  <br>
# FileNotFoundError: [Errno 2] No such file or directory:
#  <br>
# 'idterm.py'
#  <br>
#     
# As shown above, if the file cannot be found by the interpreter or if it cannot be read
# as a text file, an exception will be raised. Modify function fileLength() so that a
# friendly message is printed instead:
#     <br>
#     
# fileLength('midterm.py')
#     <br>
# 358
#     <br>
# fileLength('idterm.py')
#     <br>
# File idterm.py not found.

# In[71]:


def fileLength(fileName):
    try:                                           
        open_file=open(fileName)
        file_data=open_file.read()
        length=len(file_data)
        open_file.close()
        return length
    except IOError:                                  
        print('File ' + fileName + ' not found.') 


# In[72]:


fileLength("Filelength.txt")


# In[73]:


fileLength("idterm.py")


# ### Question 3
# Write a class named Marsupial that can be used as shown below:
# <br>
# m = Marsupial()
# <br>
# m.put_in_pouch('doll')
# <br>
# m.put_in_pouch('firetruck')
# <br>
# 
# m.put_in_pouch('kitten')
# <br>
# 
# m.pouch_contents()
# <br>
# 
# ['doll', 'firetruck', 'kitten']

# In[57]:


class Marsupial:
    def __init__(self):
        self.myList = []
        
    def put_in_pouch(self,item):       
        self.myList.append(item)
        
    def pouch_contents(self):          
        return self.myList

m = Marsupial()
m.put_in_pouch('doll')
m.put_in_pouch('firetruck')
m.put_in_pouch('kitten')
m.pouch_contents()


# Now write a class named Kangaroo as a subclass of Marsupial that inherits all the
# attributes of Marsupial and also:
# <br>
# 
# a. extends the Marsupial __init__ constructor to take, as input, the
# coordinates x and y of the Kangaroo object,
# <br>
# 
# b. supports method jump that takes number values dx and dy as input and
# movesthe kangaroo by dx units along the x-axis and by dy units along the yaxis, and
# <br>
# 
# c. overloads the __str__ operator so it behaves as shown below.
# <br>
# 
# k = Kangaroo(0,0)
# <br>
# 
# print(k)
# <br>
# I am a Kangaroo located at coordinates (0,0)
# <br>
# k.put_in_pouch('doll')
# <br>
#  k.put_in_pouch('firetruck')
# <br>
#  k.put_in_pouch('kitten')
# <br>
# k.pouch_contents()
# ['doll', 'firetruck', 'kitten']
# <br>
#  k.jump(1,0)
# <br>
# k.jump(1,0)
# <br>
# k.jump(1,0)
# <br>
# print(k)
# <br>
# 
# I am a Kangaroo located at coordinates (3,0)

# In[58]:


class Kangaroo(Marsupial):
    def __init__(self,x,y):        
        Marsupial.__init__(self)
        self.x = x
        self.y = y
        
    def jump(self,dx,dy):          
        self.x += dx
        self.y += dy
        
    def __str__(self):            
        return 'I am a Kangaroo located at co-ordinates ({},{})'.format(self.x,self.y)
k = Kangaroo(0,0)

print(k)
k.put_in_pouch('doll')
k.put_in_pouch('firetruck')
k.put_in_pouch('kitten')
print(k.pouch_contents())
k.jump(1,0)
k.jump(1,0)
k.jump(1,0)
print(k)


# ### Question 4
# Write function collatz() that takes a positive integer x as input and prints the
# Collatz sequence starting at x. A Collatz sequence is obtained by repeatedly applying
# this rule to the previous number x in the sequence:
# <br>
# x = {
# 𝑥/2 𝑖𝑓 𝑥 𝑖𝑠 𝑒𝑣𝑒𝑛3𝑥
# +1 𝑖𝑓 𝑥 𝑖𝑠 𝑜𝑑𝑑
# <br>
# 
# Your function should stop when the sequence gets to number 1. Your
# implementation must be recursive, without any loops.
# <br>
# 
# <br>
# collatz(1)
# <br>
# 1
# <br>
#  collatz(10)
# <br>
# 10
# <br>
# 5
# <br>
# 16
# <br>
# 8
# <br>
# 4
# <br>
# 2
# <br>
# 1
# <br>
# 

# In[74]:


def collatz(x):
    if x == 1:               
        return [x]
    elif x%2==0:             
        return [x] + collatz(int(x/2))
    else:                    
        return [x] + collatz(int(x*3+1))

y=collatz(1)
z=collatz(10)
print("collatz(1)")
print(*y)


# In[76]:


print("\ncollatz(10)")
print(*z, sep = "\n")


# ### Question 5
# Write a recursive method binary() that takes a non-negative
# integer n and prints the binary representation of integer n.
# <br>
# <br>
#  binary(0)
# <br>
# 0
# <br>
#  binary(1)
# <br>
# 1
# <br>
#  binary(3)
# <br>
# 11
# <br>
#  binary(9)
# <br>
# 1001
# 

# In[61]:


def binary(i): 
    if i<0: 
        return ("Enter postive integer")
    
    elif i >=1: 
        return ((10*binary(int(i/2))) + (i%2))
        
    else: 
        return 0


# In[62]:


binary(0)


# In[63]:


binary(1)


# In[64]:


binary(3)


# In[65]:


binary(9)


# ### Question 6
# Implement a class named HeadingParser that can be used to parse an HTML
# document, and retrieve and print all the headings in the document. You should
# implement your class as a subclass of HTMLParser, defined in Standard Library
# module html.parser. When fed a string containing HTML code, your class should
# print the headings, one per line and in the order in which they appear in the
# document.Each heading should be indented asfollows: an h1 heading should haveindentation 0, and h2 heading should have indentation 1, etc. Test your
# implementation using w3c.html.
# <br>
# infile = open('w3c.html')
# <br>
#  content = infile.read()
# <br>
#  infile.close()
# <br>
#  hp = HeadingParser()
# <br>
#  hp.feed(content)
# <br>
# W3C Mission
# <br>
# Principles
# 

# In[79]:


from html.parser import HTMLParser

class HeadingParser(HTMLParser):
    headers = ["h1", "h2","h3","h4","h5","h6"]
    current = -1

    def handle_starttag(self, tag, attrs):      
        if tag in HeadingParser.headers:         
            HeadingParser.current = HeadingParser.headers.index(tag)
    
    def handle_endtag(self, tag):                
        if tag == HeadingParser.headers[HeadingParser.current]:          
            HeadingParser.current = -1
            
    def handle_data(self, data):
        if HeadingParser.current >= 0:
            print(" " * HeadingParser.current + data)


# In[80]:


infile = open("w3c.html","r")
content = infile.read()
infile.close()
hp = HeadingParser()
hp.feed(content)


# ### Question 7
# Implement recursive function webdir() that takes as input: a URL (as a string) and
# non-negative integers depth and indent. Your function should visit every web
# page reachable from the starting URL web page in depth clicks or less, and print
# each web page's URL. As shown below, indentation, specified by indent, should
# be used to indicate the depth of a URL.
# <br>
# webdir('http://reed.cs.depaul.edu/lperkovic/csc242/test1.html'
# , 2, 0)
# 
# <br>
# http://reed.cs.depaul.edu/lperkovic/csc242/test1.html
# <br>
# 
# <br>
# http://reed.cs.depaul.edu/lperkovic/csc242/test2.html
# <br>
# http://reed.cs.depaul.edu/lperkovic/csc242/test4.html
# <br>
# http://reed.cs.depaul.edu/lperkovic/csc242/test3.html
# <br>
# http://reed.cs.depaul.edu/lperkovic/csc242/test4.html

# In[69]:


from urllib.request import urlopen
from urllib.parse import urljoin
from html.parser import HTMLParser

class Collector(HTMLParser):

  def __init__(self, url):
      HTMLParser.__init__(self)
      self.url = url
      self.links = []


  def handle_starttag(self, tag, attrs):
      if tag == 'a':
          for attr in attrs:          
              if attr[0] == 'href': 
                  absolute = urljoin(self.url, attr[1])
                  if absolute[:4] == 'http':
                      self.links.append(absolute)

  def getLinks(self):
    return self.links


allLinks = []
    
def webdir(url,depth,indent):
        global allLinks   
        print(indent*" " + url)
        if depth == 0:
            return 
        for i in allLinks: 
            webdir(i, depth-1, indent+1)


# In[81]:


url = ' http://reed.cs.depaul.edu/lperkovic/test1.html'
resource = urlopen(url)
content = resource.read().decode()
collector = Collector(url)
collector.feed(content)
allLinks = collector.getLinks()

webdir(url,2,0)


# ### Question 8
# Write SQL queries on the below database table that return:
# <br>
# a) All the temperature data.
# <br>
# 
# <br>
# b) All the cities, but without repetition.
# <br>
# c) All the records for India.
# <br>
# d) All the Fall records.
# <br>
# e) The city, country, and season for which the average rainfall is between 200
# and 400 millimeters.
# <br>
# f) The city and country for which the average Fall temperature is above 20
# degrees, in increasing temperature order.
# <br>
# g) The total annual rainfall for Cairo.
# 04
# <br>
# h) The total rainfall for each season.

# In[82]:


import sqlite3
con = sqlite3.connect('city.db')
cur = con.cursor()
cur.execute("CREATE TABLE cityweather (City text, Country text, Season text,Temperature float,Rainfall float)")


# In[83]:


cur.execute("INSERT INTO cityweather VALUES ('Mumbai', 'India', 'Winter',24.8,5.9)")
cur.execute("INSERT INTO cityweather VALUES ('Mumbai', 'India', 'Spring',28.4,16.2)")
cur.execute("INSERT INTO cityweather VALUES ('Mumbai', 'India', 'Summer',27.9,1549.4 )")
cur.execute("INSERT INTO cityweather VALUES ('Mumbai', 'India', 'Fall',27.6,346.0)")
cur.execute("INSERT INTO cityweather VALUES ('London', 'United Kingdom', 'Winter',4.2,207.7 )")
cur.execute("INSERT INTO cityweather VALUES ('London', 'United Kingdom', 'Spring',8.3,169.6)")
cur.execute("INSERT INTO cityweather VALUES ('London', 'United Kingdom', 'Summer',15.7,157.0)")
cur.execute("INSERT INTO cityweather VALUES ('London', 'United Kingdom', 'Fall',10.4,218.5)")
cur.execute("INSERT INTO cityweather VALUES ('Cairo', 'Egypt', 'Winter',13.6,16.5)")
cur.execute("INSERT INTO cityweather VALUES ('Cairo', 'Egypt', 'Spring',20.7,6.5)")
cur.execute("INSERT INTO cityweather VALUES ('Cairo', 'Egypt', 'Summer',27.7,0.1)")
cur.execute("INSERT INTO cityweather VALUES ('Cairo', 'Egypt', 'Fall',22.2,4.5)")


# ### a) All the temperature data.

# In[84]:


cur.execute("Select Temperature from cityweather ")
for i in cur:
    print(i)


# ### b) All the cities, but without repetition.

# In[85]:


cur.execute('SELECT DISTINCT City FROM cityweather')
for i in cur:
    print(i)


# ### c) All the records for India

# In[86]:


cur.execute("SELECT * FROM cityweather WHERE Country='India'")
for i in cur:
    print(i)


# ### d) All the Fall records

# In[87]:


cur.execute("SELECT * FROM cityweather WHERE Season='Fall'")
for i in cur:
    print(i)


# ### e) The city, country, and season for which the average rainfall is between 200 and 400 millimeters.
# 

# In[88]:


cur.execute("SELECT City,country,Season FROM cityweather WHERE Rainfall BETWEEN 200 AND 400")
for i in cur:
    print(i)


# ### f) The city and country for which the average Fall temperature is above 20 degrees, in increasing temperature order.

# In[89]:


cur.execute("SELECT City,country,temperature FROM cityweather WHERE Season='Fall' AND temperature > 20 ORDER BY temperature ASC")
for i in cur:
    print(i)


# ### g) The total annual rainfall for Cairo.

# In[90]:


cur.execute("SELECT City,SUM(Rainfall) FROM cityweather WHERE City='Cairo'")
for i in cur:
    print(i)


# ### h) The total rainfall for each season.

# In[91]:


cur.execute("SELECT Season,SUM(Rainfall) FROM cityweather GROUP BY Season")
for i in cur:
    print(i)


# ### Question 9
# Suppose list words is defined as follows:
# <br>words = ['The', 'quick', 'brown', 'fox', 'jumps', 'over',
# 'the', 'lazy', 'dog']
# <br>Write list comprehension expressions that use list words and generate the following
# lists:
# 
# 

# In[45]:


words = ['The', 'quick', 'brown', 'fox', 'jumps', 'over','the', 'lazy', 'dog']


# #### a) ['THE', 'QUICK', 'BROWN', 'FOX', 'JUMPS', 'OVER', 'THE','LAZY', 'DOG']

# In[46]:


a = [i.upper() for i in words]
print(a)


# #### b) ['the', 'quick', 'brown', 'fox', 'jumps', 'over', 'the','lazy', 'dog']

# In[48]:


b = [i.lower() for i in words]
print(b)


# #### c) [3, 5, 5, 3, 5, 4, 3, 4, 3] (the list of lengths of words in list words).

# In[49]:


c = [len(i) for i in words]
print(c)


# #### d) [['THE', 'the', 3], ['QUICK', 'quick', 5], ['BROWN','brown', 5], ['FOX', 'fox', 3], ['JUMPS', 'jumps', 5],['OVER', 'over', 4], ['THE', 'the', 3], ['LAZY', 'lazy',4], ['DOG', 'dog', 3]] 
# (the list containing a list for every word of list words, where each list contains the word in uppercase and lowercase and the length of the word.)

# In[50]:


d = [[i.upper(),i.lower(),len(i)] for i in words]
print(d)


# #### e) ['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog'] 
# (the list of words in list words containing 4 or more
# characters.)

# In[51]:


e = [i for i in words if len(i)>=4]
print(e)

