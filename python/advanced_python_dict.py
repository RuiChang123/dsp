#read file
path='/Users/ruichang/ds/metis/prework/dsp/python/faculty.csv'
f=pd.read_csv(path)
f.columns=['name','degree','title','email'] #set column names
#change all the phd formates in the dataframe to "Ph.D."
for i in range(len(f['degree'])):
    x=f['degree'][i].strip(' ').split(' ')
    for e in range(len(x)):
        if 'Ph' in x[e]:
            x[e]='Ph.D.'
    f['degree'][i]=' '.join(x)

#get titles
for i in range(len(f['title'])):
    x=f['title'][i].split(' ')[:-2]
    f['title'][i]=' '.join(x)
#change full names to last names
for i in range(len(f['name'])):
    x=f['name'][i].split(' ')
    f['name'][i]=x[-1]
#create the dict for Q6
l={}
n=[]
for i in range(len(f['name'])):
    if f['name'][i] in n:
        l[f['name'][i]]=l[f['name'][i]]+[[f['degree'][i],f['title'][i],f['email'][i]]]
    else:
        n=n+[f['name'][i]]
        l[f['name'][i]]=[f['degree'][i],f['title'][i],f['email'][i]]
#Print the first 3 key and value pairs of the dictionary
#because the dict is sorted by keys we need to find the first three keys
k=[]
for e in l.keys():
    k=k+[e]
k=sorted(k)
for x in k[:3]:
    print (x,l[x])

#Q7
f1=pd.read_csv(path)
f1.columns=['name','degree','title','email']
f1['degree']=f['degree']
f1['title']=f['title']
#change full name to first and last name pair
for i in range(len(f1['name'])):
    x=f1['name'][i].split(' ')
    t=(x[0],x[-1])
    f1['name'][i]=t
#create the dict
l1={}
n1=[]
for j in range(len(f1['name'])):
    if f1['name'][j] in n1:
        l1[f1['name'][j]]=l1[f1['name'][j]]+[[f1['degree'][j],f1['title'][j],f1['email'][j]]]
    else:
        n1=n1+[f1['name'][j]]
        l1[f1['name'][j]]=[f1['degree'][j],f1['title'][j],f1['email'][j]]
#print the first 3 key and value pairs of the dictionary
k1=[]
for e in l1.keys():
    k1=k1+[e]
k1=sorted(k1)
for x in k1[:3]:
    print (x,l1[x])
#sort the keys by last name and print
k1=sorted(k1,key=lambda x: x[1])
for x in k1[:3]:
    print (x,l1[x])

 
    
