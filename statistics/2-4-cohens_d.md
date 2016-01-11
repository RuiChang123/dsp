[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)

>>
Cohen's d between the weight of first babies and the weight of the babies not born first is -0.089 standard error. This means the difference is small. The Cohen's d of the preg length between the two groups is 0.029, which is even smaller.

I rewrote the code for the by myself, the code is shown below:
```
import os
import pandas as pd
import numpy as np

path='/Users/ruichang/ds/metis/prework/ThinkStats2/code'
os.chdir(path)

def read_stats(file_dat_gz,file_dct):
#this function read .dat.gz and .dct file and convert it into a dataframe
    dct=open(file_dct)
    dct=dct.readlines()[1:-1]
#get names and start,end index from .dct file and put them into a dataframe
    start=[]
    names=[]
    for line in dct:
        l=line.split()
        start=start+[int(l[0][l[0].index('(')+1:l[0].index(')')])]
        names=names+[l[2]]
    data={'start':start,'name':names}
    df=pd.DataFrame(data)
    end=start[1:]+[0]
    df['end']=end
#get the range of each column of .dat file
    colspecs=df[['start','end']]-1
    colspecs=colspecs.astype(np.int).values.tolist()
#read .dat.gz file
    df_preg=pd.read_fwf(file_dat_gz,colspecs=colspecs,names=names,compression='gzip')
    return df_preg
    
#clean data
def clean_FemPreg(df):
#change mother's age into years
    df.agepreg /=100.0
#replace the values of birthwgt_lb which are greater than 20 to NaN
    df.loc[df.birthwgt_lb>20,'birthwgt_lb']=np.nan
#replace 'not ascertained','refused','don't know' with NaN
    na_vals=[97,98,99]
    df.birthwgt_lb.replace(na_vals,np.nan,inplace=True)
    df.birthwgt_oz.replace(na_vals,np.nan,inplace=True)
    df.hpagelb.replace(na_vals,np.nan,inplace=True)
    df.babysex.replace([7,9],np.nan,inplace=True)
    df.nbrnaliv.replace([9],np.nan,inplace=True)
#create a new column that shows the total weight in lb
    df['totalwgt_lb']=df.birthwgt_lb+df.birthwgt_oz/16.0
    df.cminttvw=np.nan
    
#chapter 2 Q4
#clean the data set and get the live birth data (outcome=1)
preg=read_stats('2002FemPreg.dat.gz','2002FemPreg.dct')
clean_FemPreg(preg)
live=preg[preg.outcome==1]

def cohend(group1,group2):
#this function takes two sets of data and calculates the Cohen'd
#group1 and group2 should be series
    diff=group1.mean()-group2.mean()
    n1=len(group1)
    n2=len(group2)
#considering the degree of freedom, we should use n-1 instead of n when calculating var and pooled var. Although there 
#is not much difference for big size samples.
    var1=np.var(group1,ddof=1)
    var2=np.var(group2,ddof=1)
    pooled_var=((n1-1)*var1+(n2-1)*var2)/(n1+n2-2)
    return diff/pooled_var**0.5
    
#seperate the data of the first birth from others
firsts=live[live.birthord==1]
others=live[live.birthord!=1]
first_pl=firsts.prglngth
other_pl=others.prglngth
first_tw=firsts.totalwgt_lb
other_tw=others.totalwgt_lb

print cohend(first_pl,other_pl)
print cohend(first_tw,other_tw)

OUTPUT:
0.0288790518999
-0.0886729334723

def get_hist(data):
#this function takes a list of data and returns a dict which shows the frequency of each data in the list
    d={}
    l=[]
    for e in data:
        if e in l:
            d[e]=d[e]+1
        else:
            d[e]=1
            l=l+[e]
    return d
    

