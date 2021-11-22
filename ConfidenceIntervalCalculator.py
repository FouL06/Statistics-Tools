import scipy.stats as sp
import math

#Confidence Interval Formula Values
Sample_Mean = 4
Sample_Deviation = 2

#Finds the alpha value for the confidence calculation
def FindAlphaValue(confidencePercentage):
    a = 1 - confidencePercentage
    return a

#Finds the T value from distribution gallery by making use of the sample size and alpha value.
def FindTValue(a, n):
    t = sp.t.ppf(q=a, df=n-1)
    return t

#Finds the mue of the confidence interval
def CalculateMue(mean, t, s, n):
    mue = mean + t * (s / math.sqrt(n))
    return mue

#Compute the confidence interval
a = FindAlphaValue(0.99)
t = abs(FindTValue(a, 25))
mue = CalculateMue(Sample_Mean, t, Sample_Deviation, 25)
print("We are confident that the value is: " + str(mue))