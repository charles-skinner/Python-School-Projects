from re import I
import sys
import time
i = 0

def main(rows):
    f = open("part2.txt","w")
    start = time.perf_counter()
    for row in range(rows):
        for column in range(row+1):
            f.write(f'{weight_on(row, column):.2f}' + " ")
        f.write("\n")
    end = time.perf_counter()
    f.write("Elapsed time: " + str(end - start) + " seconds\n")
    f.write("Number of function calls: " + str(i) + "\n")

def weight_on(r,c):
    global i
    global j
    i += 1
    
    if((r == 0) and (c == 0)):
        return 0.0
    if(c == 0):
        value = (weight_on(r-1,c)/2 + 100.0)
        return value
    if(r == c):
        value = (weight_on(r-1,c-1)/2 + 100.0)
        return value
    else:
        value = (weight_on(r-1,c)/2 + weight_on(r-1,c-1)/2 + 200.0)
        return value

if __name__ == "__main__":
    main(7)