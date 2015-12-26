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
#change full names to last names
for i in range(len(f['name'])):
    x=f['name'][i].split(' ')
    f['name'][i]=x[-1]