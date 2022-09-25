import random
import argparse

def estimate(n):
    circlePoints = 0
    outsidePoints = 0

    for i in range(n**2):
        x = random.uniform(-1,1)
        y = random.uniform(-1,1)

        if((x*x+y*y)<=1):
            circlePoints += 1
        
        outsidePoints += 1

        pi = 4 * circlePoints / outsidePoints

    print(pi)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--num', type=int, default=100)
    options = parser.parse_args()

    estimate(options.num)