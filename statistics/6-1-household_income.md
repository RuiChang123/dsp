[Think Stats Chapter 6 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2007.html#toc60) (household income)

```
If we set the upper bound on the highest range to be 10^6. 
The summary of the data is:

mean 74278.7075312
std 93946.9299635
median 51226.4544789
skewness 4.94992024443
pearson skewness 0.736125801914

If we set the upper bound on the highest range to be 10^7.
The summary of the data is:

mean 124267.397222
std 559608.501374
median 51226.4544789
skewness 11.6036902675
pearson skewness 0.391564509277

As we can see, when the upper bound on the highest range increases, the skewness increases but the pearson skewness decreases. 
When changing the upper bound higher, the data becomes more skewed. In this case the skewness moves to the right direction but
pearson's skewness moves to the opposit direction. This is due to the change of standard devision of the sample when we change the
upper bound. The std changes much greater than the difference between mean and median, which leads the pearson's skewness become
smaller.

The precentile at the mean is 66.0% for 10^6 upper bound and 85.7% for 10^7 upper bound.
```

The code and plot is shown below:
```
df=pd.read_csv('hinc06.csv')
#create a dataframe which has the upper_band income, number of respondents
df2=df.iloc[8:].iloc[:,0:2]
df2.columns=['income','freq']

#Add log upper bound and log lower bound to the dataframe
res=[]
for i in range(len(df2.income)-1):
    income=int(df2.iloc[i].income.split()[-1].strip('$').replace(',',''))
    freq=int(df2.iloc[i].freq.replace(',',''))
    res.append((income,freq))
res=res+[(1000000,int(df2.iloc[-1].freq.replace(',','')))] #set the last value of the dataframe to 1000000
df3=pd.DataFrame(res)
df3.columns=['income','freq']
df3['income'][0]=4999  #reset the first value of the dataframe
df3['log_upper']=np.log10(df3.income) #compute the log of upper band
df3['log_lower']=df3.log_upper.shift(1) #compute the log of lower band
df3['log_lower'][0]=3

def get_logSample(df):
#This function generates the pseudo-sample from the dataframe and returns an array
    arrays=[]
    for _, row in df3.iterrows():
        vals=np.linspace(row.log_lower,row.log_upper,row.freq)
        arrays.append(vals)
    log_sample=np.concatenate(arrays)
    return log_sample

#The shape of the data can be simply plotted by a histogram.   
log_sample=get_logSample(df3)
sample=np.power(10,log_sample)
plt.hist(sample,bins=100)
plt.savefig('/Users/ruichang/ds/metis/prework/dsp/statistics/6-1.png')

#get the summary of the data
import density
mean, median = density.Summarize(sample)

def mean_percentile(sample,mean):
#this function calaulates the percentile at the mean
    counter=0
    for e in sample:
        if e<=mean:
            counter +=1 
    return counter/float(len(sample))
    
#change the highest income to 10^7
df3['log_upper'][41]=7.0

log_sample2=get_logSample(df3)
sample2=np.power(10,log_sample2)
mean2, median2 = density.Summarize(sample2)

mean_percentile(sample2,mean2)
```
![alt text](https://github.com/RuiChang123/dsp/blob/master/statistics/6-1.png "6-1")
