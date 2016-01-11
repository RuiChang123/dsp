[Think Stats Chapter 8 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2009.html#toc77) (scoring)

>> The sampling distribution follows a normal distribution. The 90% confidence interval is (0.41,0.58)

The code and the plots are shown below:

```
#sampling L
np.random.seed(100) #set seed
l=[]
for i in range(1000):
    s=np.random.exponential(0.5,10)
    l=l+[s.mean()]
#plot the pmf
plt.hist(l,bins=20)
plt.title('sampling distribution of L')
plt.savefig('/Users/ruichang/ds/metis/prework/dsp/statistics/8-2-1.png')

#plot the cdf
y=np.linspace(0,1,50)
x=[np.percentile(l,e*100) for e in y]
plt.scatter(x,y,color='blue',label='distribution of L: cdf') #calculate the percentile value at each given percentage
#normal distribution with mu=0.5, sigma=0.5/(10**0.5)
from scipy import stats
x_norm=np.arange(-2.5,3.5,0.01)
y_norm=stats.norm.cdf(x_norm,0.5,0.5/(10**0.5))
plt.plot(x_norm,y_norm,color='red',label='Normal: cdf')
#plt.plot(x,y)
plt.legend(bbox_to_anchor=[1,0.2])
plt.savefig('/Users/ruichang/ds/metis/prework/dsp/statistics/8-2-2.png')

#compute the standard error and confidence interval
sd=np.array(l).std()
standardError=sd/(10**0.5)
mean=np.array(l).mean()
con_interval=stats.norm.interval(0.9, loc=mean, scale=standardError)
con_interval

#simulate standard error with different sample size
np.random.seed(100) #set seed
l=[]
sd=[]
n=np.linspace(100,5000,50)
for e in n:
    for i in range(1000):
        s=np.random.exponential(0.5,e)
        l=l+[s.mean()]
    sd=sd+[np.array(l).std()]
plt.plot(n,sd)
plt.xlabel('sample size')
plt.ylabel('standard error')
plt.savefig('/Users/ruichang/ds/metis/prework/dsp/statistics/8-2-2.png')
```
![alt text](https://github.com/RuiChang123/dsp/blob/master/statistics/8-2-1.png "8-2")
![alt text](https://github.com/RuiChang123/dsp/blob/master/statistics/8-2-2.png "8-2")
![alt text](https://github.com/RuiChang123/dsp/blob/master/statistics/8-2-3.png "8-2")
