import numpy as np
import matplotlib.pyplot as plt

def estimatePi(n):
    x = generateX(n)
    y = generateY(n)

    insideX, insideY = x[(x*x+y*y)<=1],y[(x*x+y*y)<=1]
    outsideX, outsideY = x[(x*x+y*y)>1],y[(x*x+y*y)>1]

    generatePlot(insideX, insideY, outsideX, outsideY)


def generateX(n):
    x = 1-2*np.random.random(int(n))
    return x

def generateY(n):
    y = 1-2*np.random.random(int(n))
    return y

def generatePlot(i_x,i_y,o_x,o_y):
    plt.title('Monte Carlo Cirle Plot')
    plt.scatter(i_x, i_y, c='b', alpha=0.8, edgecolor=None)
    plt.scatter(o_x, o_y, c='r', alpha=0.8, edgecolor=None)
    plt.axis('scaled')
    plt.show()

if __name__ == '__main__':
    estimatePi(1000)