import scipy as sp
import math

#Hypothesis Testing Variables
Null_Mean = 3
Sample_Mean = 3.38
Sample_Variance = 1.769
Sample_Standard_Deviation = 5.237
Sample_Size = 50

#Finds the T value for a specific significance level for the data
def FindTValue(x, u, s, n):
    t = (x-u)/(s / math.sqrt(n))
    return abs(t)

#T-Test using sample variance
print(FindTValue(Sample_Mean, Null_Mean, Sample_Variance, Sample_Size))

#T-Test using sample deviation
print(FindTValue(Sample_Mean, Null_Mean, Sample_Standard_Deviation, Sample_Size))

