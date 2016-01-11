[Think Stats Chapter 7 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2008.html#toc70) (weight vs. age)

>> The computed Pearson's and Spearman's correlations are 0.069 and 0.094. This means there is a weak correlation between the two variables. The difference between the Pearson's correlation and Spearman's correlation suggests some influence of outliers or non-linear relationship.
By plotting the percentiles of weight vs mother's age suggests that there is a non-linear relationship between the two.

The code and plots are shown below:

```
df7=live.dropna(subset=['totalwgt_lb','agepreg']) #remove NaN

#plot mother's age vs birth weight
plt.scatter(df7.agepreg,df7.totalwgt_lb,alpha=0.1)
plt.xlabel("mother's age")
plt.ylabel('birth weight/lb')
plt.savefig('/Users/ruichang/ds/metis/prework/dsp/statistics/7-1-1.png')

#plot mother's age vs percentiles of birth weight
bins=np.arange(15,45,3) #seperate mother's age into 11 groups
indices=np.digitize(df7.agepreg,bins)
groups=df7.groupby(indices)
motherAge=[group.agepreg.mean() for i, group in groups]

precent=[10,30,50,70,90] #set values of percentiles
for e in precent:
    weight=[np.percentile(group.totalwgt_lb,e) for i, group in groups]
    label='%dth' %e
    plt.plot(motherAge,weight,label=label)
plt.axis([10,45,0,15])
plt.xlabel("mother's age")
plt.ylabel('birth weight/lb')
plt.legend()
plt.savefig('/Users/ruichang/ds/metis/prework/dsp/statistics/7-1-2.png')
```

![alt text](https://github.com/RuiChang123/dsp/blob/master/statistics/7-1-1.png "7-1")
![alt text](https://github.com/RuiChang123/dsp/blob/master/statistics/7-1-2.png "7-1")
