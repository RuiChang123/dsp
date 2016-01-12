[Think Stats Chapter 8 Exercise 3](http://greenteapress.com/thinkstats2/html/thinkstats2009.html#toc77)


This way of making estimate is not biased because the mean error is very small. The standard error and 90% confidence interval for
different lam is shown below. As the value of lam increases, the standard error increases.
If we set lam=2, the mean error is 0.0026 and the RMSE is 1.4
```
lam= 2
standard error=0.443485
confidence interval= (1.2731523521117789, 2.7320876478882212)
lam= 3
standard error=0.549187
confidence interval= (2.0972570948704425, 3.9039229051295568)
lam= 4
standard error=0.630875
confidence interval= (2.9668025969147842, 5.0421974030852157)
lam= 5
standard error=0.714241
confidence interval= (3.8321083504808655, 6.1817516495191356)
lam= 6
standard error=0.774665
confidence interval= (4.7358188838048099, 7.2842411161951901)
lam= 7
standard error=0.839356
confidence interval= (5.6288529483559175, 8.3900870516440804)
lam= 8
standard error=0.899714
confidence interval= (6.5278423840798236, 9.4876376159201747)
lam= 9
standard error=0.956995
confidence interval= (7.4410336200609972, 10.589266379939003)
```
The code and plot is shown below:
```
def predictGoals(lam):
    import numpy as np
    '''this function predicts the total goals of a game.
    lam: goal-scoring rate
    '''
    time_interval=0
    n=0
    while True:
        time_interval=time_interval+float(np.random.exponential(1.0/lam,1))
        if time_interval<=1.0:
            n=n+1
        else:
            break
    return n
    
def predictLam(lam,n,m):
    '''this function uses the predictGoals function to simulate m samples of size n.
    each estimated lam comes from the mean of each sample
    It returns a list of estimated lam'''
    l=[]
    for i in range(m):
        sample=[predictGoals(lam) for j in range(n)]
        sampleMean=np.mean(sample)
        l=l+[sampleMean]
    return l

#sampling lam    
def sampling(lam=2,n=10,m=10000):
    l=predictLam(lam,n,m)
    return l
np.random.seed(99)
l=sampling(lam,n,m)

#plot sampling distribution
plt.hist(l,bins=35)
plt.savefig('/Users/ruichang/ds/metis/prework/dsp/statistics/8-3.png')

#compute standard error and confidence interval
from scipy import stats
def samplingError(l):
    mean=np.array(l).mean()
    standardError=(np.var(l,ddof=1))**0.5
    con_interval=stats.norm.interval(0.9, loc=mean, scale=standardError)
    print 'standard error=%f' %standardError
    print 'confidence interval=',con_interval
    
#compute the mean error
meanError=np.array([x-lam for x in l]).mean()
meanError
#compute RMSE
SE=[(x-lam)**2 for x in l]
MSE=np.array(SE).mean()
RMSE=MSE**0.5
RMSE

#different lam simulation
for lam in range(2,10):
    print 'lam=',lam
    l=sampling(lam)
    se=samplingError(l)
```

![alt text](https://github.com/RuiChang123/dsp/blob/master/statistics/8-3.png "8-3")
