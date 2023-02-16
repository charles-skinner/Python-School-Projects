#Group members: Charlie Skinner, Batmunkh Munkhjargal
from timeit import default_timer as timer
import time as _time

class Timedec():
    def __init__(self,func):
        self.func = func
        self.times = []
    def __call__(self,*args):
        start = timer()
        self.func(*args)
        end = timer()
        result = end - start
        self.times.append(result)

@Timedec
def fun1(seconds):
    _time.sleep(seconds)
    
def main():
    for t in [.1, .2, .3, .4, .5, .6, .7, .8, .9]:
        fun1(t)
    print(fun1.times)
    print(", ".join(['{:.2f}'.format(t) for t in fun1.times]))

if __name__ == "__main__":
    main()