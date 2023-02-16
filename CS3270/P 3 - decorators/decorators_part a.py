#Group members: Charlie Skinner, Batmunkh Munkhjargal
from timeit import default_timer as timer
import time as _time

def timedec(some_function):
    def timedec_wrapper(seconds):
        start = timer()
        result = some_function(seconds)
        end = timer()
        print(f"function ran in {'{:.2f}'.format(end - start)} seconds")
        return result
    return timedec_wrapper

@timedec
def fun1(seconds):
    _time.sleep(seconds)
    
def main():
    fun1(2.5)

if __name__ == "__main__":
    main()
