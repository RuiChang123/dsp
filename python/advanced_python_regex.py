import pandas as pd

#read file
path='/Users/ruichang/ds/metis/prework/dsp/python/faculty.csv'
f=pd.read_csv(path)
f.columns=['name','degree','title','email'] #set column names

#get lists of names, degrees, title and email
names=[x for x in f['name']]
degrees=[x.upper().strip(' ').replace('.','').split(' ') for x in d if len(x)>1]
titles=[x for x in f['title']]
emails=[x for x in f['email']]

#creat a function to make a dictionary out of a list to get the information
def get_info(list1):
	x={}
	for e in list1:
		if e in x:
			x[e]=x[e]+1
		else:
			x[e]=1
	return x

#Q1
#creat a list of all the degrees
d=[]
for e in degrees:
	d=d+e
#get degree information of the file
get_info(d)

#Q2
#For this question, I assume that all the titles are in the same format: 
#professor title(Assistant/associate) of field(Biostatistics in this case).
t=[' '.join(x.split(' ')[:-2]) for x in titles] #make a list of strings, each string shows the title 
#get the information of title 
get_info(t) 

#Q3 
#print email 
emails 

#Q4 
#get a list of domains of each email 
email_dom=[] 
for e in emails: 
    i=e.find('@') 
    email_dom=email_dom+[e[i+1:]] 
#get the dict of domain information 
dom_info=get_info(email_dom) 
#print keys of dom_info to get the list of domains 
for key in dom_info: 
	print key 



