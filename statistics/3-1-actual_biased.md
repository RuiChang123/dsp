[Think Stats Chapter 3 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2004.html#toc31) (actual vs. biased)

The code and the plot for this question is shown below:
```
import collections
#read data
resp=read_stats('2002FemResp.dat.gz','2002FemResp.dct')

def get_freq(hist):
#get the frequency from a hist dict
    n=0
    for key in hist:
        n=n+hist[key]
    d={}
    for key in hist:
        d[key]=hist[key]/float(n)
    return d
    
numkd_hist=collections.Counter(resp.numkdhh) #get a hist dict from a given set of data
numkd_freq=get_freq(numkd_hist)

#actual to baised
numkd_histBaised={}
for key in numkd_hist:
    numkd_histBaised[key]=key*numkd_hist[key]
numkd_freqBaised=get_freq(numkd_histBaised)

#plot actual and baised together
#modify data for step function ploting: shift 0.5 and add two 0 points at each ends
index=[numkd_freq.keys()[0]-0.5]+[x+0.5 for x in numkd_freq.keys()]+[numkd_freq.keys()[0]+5.5]
values_act=[0]+numkd_freq.values()+[0]
values_baised=[0]+numkd_freqBaised.values()+[0]
plt.step(index,values_act,label='actual',color='red',linewidth=2)
plt.step(index,values_baised,label='baised',color='blue',linewidth=2)
plt.axis([-1,6,0,0.6])
plt.xlabel('number of children')
plt.ylabel('frequency')
plt.legend()
plt.savefig('/Users/ruichang/ds/metis/prework/dsp/statistics/3-1.png')
```

![alt text](https://github.com/RuiChang123/dsp/statistics/3-1.png "3-1")

