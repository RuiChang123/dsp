[Think Stats Chapter 5 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2006.html#toc50) (blue men)

>> 
For this question, I first ploted the cdf of the data together with a normal distrubtion. The plot indicates that the data is normal distributed.
Then we can compute the percentage: 34%

The code and plot is shown below:
```
import brfss
brfss=brfss.ReadBrfss()

male=brfss[brfss.sex==1]
female=brfss[brfss.sex==2]

#normal distribution
nor=np.random.normal(178,7.7,1000)
nor_hist=collections.Counter(nor)
nor_freq=get_freq(nor_hist)
nor_cdf=freq_cdf(nor_freq)

#get rid of the nan
male=male[pd.notnull(male.htm3)] #remove NaN
maleHight=male.htm3
m_hist=collections.Counter(maleHight)
m_freq=get_freq(m_hist)
m_cdf=freq_cdf(m_freq)

#plot the cdf of the data and a normal distrubtion 
plt.scatter(nor_cdf.keys(),nor_cdf.values(),color='red',label='normal',alpha=0.1)
plt.scatter(m_cdf.keys(),m_cdf.values(),color='blue',label='data',alpha=0.3)
plt.legend(bbox_to_anchor=[1,0.2])
plt.savefig('/Users/ruichang/ds/metis/prework/dsp/statistics/5-1.png')

#computer blue man group percentage
from scipy.stats import norm
#calculate the z statistics of the lower side and higher side
mu=178
sigema=7.7
hight_min=177.8
hight_max=185.4
z_min=(hight_min-mu)/sigema
z_max=(hight_max-mu)/sigema
p=norm.cdf(z_max)-norm.cdf(z_min)
```
![alt text](https://github.com/RuiChang123/dsp/blob/master/statistics/5-1.png "5-1")
