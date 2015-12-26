import pandas as pd

#read file
path='/Users/ruichang/ds/metis/prework/dsp/python/faculty.csv'
f=pd.read_csv(path)
f.columns=['name','degree','title','email'] #set column names

emails=[x for x in f['email']]
#add '/n' at the end of each email address
email_list=[]
for e in emails:
    email_list=email_list+[e]+['\n']
#creat file
path2='/Users/ruichang/ds/metis/prework/dsp/python/emails.csv'
f=open(path2,'w')
#write email list to the file
f.writelines(email_list)
f.close()

