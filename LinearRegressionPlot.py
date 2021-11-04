"""
Designed to calculate the linear regression of any data passed in.
Must take in at least two sets of data (x, y) axis in order for a
linear regression line to be calculated.

Author: Ashton Foulger
Version: 0.01, 11/3/21
Python-Version: 3.10.0
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

"""
Takes in two sets of data to compute the sum of X times Y
variables from both sets of data. Returning an int value of
the sum of the two data arrays.
"""
def Compute_SumXY(data1, data2):
    data_XY = []

    for n1, n2 in zip(data1, data2):
        data_XY.append(n1 * n2)

    return sum(data_XY)  

"""
Takes in a data set, an alpha and beta values to compute points
on the linear regression line. To then be used to plot the line of 
regression.
"""
def Compute_Regression_Slope_Points(data, a, b):
    y = 0
    squarePoints = []

    for i in range(len(data)):
        y = a + b * data[i]
        squarePoints.append(y)

    return squarePoints 

"""
Computes the Sum of Squares Error used in calculating the
coefficient of determination. Taking in a data array, points
(found on line of regression), and an n value to act as a count
for how may points we need to sum. Returning an int value of the sum
of squares error.
"""
def Compute_SSE(data, squares, n):
    temp = []

    for i in range(n):
        data[i] - squares[i]
        temp.append((data[i] - squares[i])**2)

    return sum(temp)   

"""
Computes the Sum of Squares Total used in calculating the coefficent
of determination. Taking in a data array, Mean of Y axis points, and an
n value to act as a count for how many points we need to sum. Returning
an int value of the sum of squares total.
"""
def Compute_SST(Y_data, Y_mean, n):
    temp = []
    for i in range(n):
        temp.append((Y_data[i] - Y_mean)**2)

    return sum(temp)

"""
Computes the Coefficent of Determination for linear regression line from the data.
Taking in a Sum of Squares Error int value, and Sum of Squares Total in value.
Returning an int value of R squared.
"""
def Compute_R_Squared(SSE, SST):
    R = 1 - (SSE / SST)
    return R

#---------------LINE_OF_BEST_FIT_CALCULATION---------------#

#Data Arrays
data_X = [1,2,3,4,5,6]
data_Y = [0,7,6,14,11,10]

#Data Sample Means
mean_X = np.mean(data_X)
mean_Y = np.mean(data_Y)

#Data Sample Variances
variance_X = np.var(data_X)
variance_Y = np.var(data_Y)

#Data Linear Regression Equation Variables
n = 6
sumX = sum(data_X)
sumXX = sum(np.power(data_X, 2))
sumY = sum(data_Y)
sumXY = Compute_SumXY(data_X, data_Y)
a = ((sumY * sumXX) - (sumX * sumXY)) / ((n * sumXX) - (sumX)**2)
b = ((n * sumXY) - (sumX * sumY)) / ((n * sumXX) - (sumX)**2)

#Data Coefficent of Determination Variable
lineOfBestFitSquares = Compute_Regression_Slope_Points(data_X, a, b)
SSE = Compute_SSE(data_Y, lineOfBestFitSquares, n)
SST = Compute_SST(data_Y, mean_Y, n)
R = Compute_R_Squared(SSE, SST)

#Print Linear Regression Values & Coefficent of Determination
print("\n")
print("Mean X : " + str(mean_X))
print("Mean Y : " + str(mean_Y))
print("Variance X : " + str(round(variance_X , 2)))
print("Variance Y : " + str(round(variance_Y, 2)))
print("Sum X : " + str(sumX))
print("Sum XX : " + str(sumXX))
print("Sum Y : " + str(sumY))
print("Sum XY : " + str(sumXY))
print("Var a : " + str(a))
print("Var b ; " + str(b))
print("SSE : " + str(SSE))
print("SST : " + str(SST))
print("R^2 : " + str(R))
print("\n")

#Display Linear Regression Graph
plt.scatter(data_X,data_Y, marker = 'd', color = 'blue')
plt.plot(data_X, data_Y, color = 'blue')
plt.scatter(data_X, lineOfBestFitSquares, marker = 's', color = 'red')
plt.plot(data_X, lineOfBestFitSquares, color = 'red')
plt.show()