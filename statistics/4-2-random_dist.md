[Think Stats Chapter 4 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2005.html#toc41) (a random distribution)

The code and plots for this question is shown below:
```
import random
r=[]
for i in range(1000):
    r=r+[random.random()]
r_hist=collections.Counter(r)
r_freq=get_freq(r_hist)

#plot pmf
fig,ax=plt.subplots()
ax.stem(r_freq.keys(),r_freq.values())
plt.axis([-0.2,1.2,0,0.0015])
plt.title('Uniform_pmf')
plt.savefig('/Users/ruichang/ds/metis/prework/dsp/statistics/4-2-pmf.png')

#plot cdf
def freq_cdf(r_freq):
    r_cdf={}
    sort_key=sorted(r_freq.keys())
#set the first value of cdf
    r_cdf[sort_key[0]]=r_freq[sort_key[0]]
#calculate the rest values of cdf
    for i in range(1,len(sort_key)):
        r_cdf[sort_key[i]]=r_cdf[sort_key[i-1]]+r_freq[sort_key[i]]
    return r_cdf
r_cdf=freq_cdf(r_freq)
plt.scatter(r_cdf.keys(),r_cdf.values())
plt.axis([0,1,0,1])
plt.title('Uniform_cdf')
plt.savefig('/Users/ruichang/ds/metis/prework/dsp/statistics/4-2-cdf.png')
```

![alt text](https://github.com/RuiChang123/dsp/blob/master/statistics/4-2-pmf.png "3-1")
![alt text](https://github.com/RuiChang123/dsp/blob/master/statistics/4-2-cdf.png "3-1")
