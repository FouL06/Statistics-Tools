import scipy.stats as sp
import math

#Confidence Interval Formula Values
Sample_Mean = 4
Sample_Deviation = 2

def FindAlphaValue(confidencePercentage):
    a = 1 - confidencePercentage
    return a

def FindTValue(a, n):
    t = sp.t.ppf(q=a, df=n-1)
    return t

def CalculateMue(mean, t, s, n):
    mue = mean + t * (s / math.sqrt(n))
    return mue

a = FindAlphaValue(0.99)
t = -(FindTValue(a, 25))

mue = CalculateMue(Sample_Mean, t, Sample_Deviation, 25)
print("We are confident that the value is: " + str(mue))