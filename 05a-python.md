# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

###Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>> Both list and tuple are a list of values. The difference is you can add/remove/change the values in the list while the values in a tule are fixed. Because the values in tuples are fixed, tuples will work as keys.

---

###Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>> 
```
The lists and sets are very different in Python:
1. Lists can have duplicate elements but sets can not.
2. Sets don't support indicating.
3. Sets support mathematical operations like: union, intersection, difference and symmetric difference.
```
>>
```
Finding an element:
    list: list.index(element)
    set: because elements in sets don't have order, the index you get may be different as what you see in the sets.
         list(set).index(element)
```
---

###Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>> 
```
In Python, lambda creats a function to be called later. It returns the function instead of assigning it to a name.
The lambdas can be used as a function shorthand that allows us to embed a function within the code.
example 1:
a=[1,2,3,4]
b=[11,12,13,14]
c=[5,6,7,8]
map(lambda x,y,z: x+y+z, a,b,c)
output: [17, 20, 23, 26]
example 2:
a=[1,2,3,4,5,6,7,8,9,10]
filter(lambda x: x%2==0, a)
output: [2,4,6,8,10]
example 3:
colors = ["blue", "lavender", "red", "yellow"]
sorted(colors, key=lambda color: len(color), reverse=True)
output: ['lavender', 'yellow', 'blue', 'red']
example 4:
student_tuples = [('john', 'A', 15),('jane', 'B', 12),('dave', 'B', 10)]
sorted(student_tuples, key=lambda s: s[2])
output: [('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]

---

###Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> 
```
List comprehensions provide a concise way to create lists. 
It consists of brackets containing an expression followed by a for clause. The expressions can be anything.
example 1:
a=[1,2,3,4]
b=[x**2 for x in a]
print b
output: [1,4,9,16]
equals to: map(lambda x: x**2, a)
example 2:
a=[1,2,3,4,5,6,7,8,9]
b=[e for e in a if e%3==0]
print b
output: [3, 6, 9]
equals to: filter(lambda x: x%3==0, a)
set comprehensions:
a={'a','b','c'}
b={'q','a','r','b','c','p'}
c={e for e in b if e not in a}
print c
output: {'p', 'q', 'r'}
dictionary comprehensions:
print {i:chr(i+64) for i in range(1,5)}
output: {1: 'A', 2: 'B', 3: 'C', 4: 'D'}

---

###Complete the following problems by editing the files below:

###Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE (answer will be in number of days)

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE (answer will be in number of days)

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE  (answer will be in number of days)

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

###Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

###Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

###Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)





