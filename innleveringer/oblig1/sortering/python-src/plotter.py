import sys
import matplotlib.pyplot as plt
import sort_runner
import csv  
from typing import Final


def plot(filename):
    x = []
    yMerge = []
    yInsert = []
    headers: str = ""
    
    N:Final = 0
    INSERTION_CMP = 1
    INSERTION_SWAPS=2
    INSERTION_TIME = 3
    MERGE_CMP = 4
    MERGE_SWAPS = 5
    MERGE_TIME = 6

    with open(filename, 'r') as csvfile:
        lines = csv.reader(csvfile, delimiter=',')
        headers = next(lines)
        for row in lines:
            #use the constants defined above to determine what gets plotted.
            #!remember to change axis-titles. too lazy to program that in, this is already overkill when i could just screenshot excel...
            x.append(int(row[N]))
            yInsert.append(int(row[INSERTION_TIME]))
            yMerge.append(int(row[MERGE_TIME]))

    plt.plot(x,yMerge, color='g',marker='o', label="Merge")
    plt.plot(x, yInsert, color='r', marker='o', label="Insertion")

    plt.xlabel('number of elements (n)')
    plt.ylabel('time (μs)')
    plt.title("tid/elementer (nearly sorted) (n=10000)")
    plt.grid()
    plt.legend()
    plt.show()


if sys.argv[1] == None:
    print("error: run plot-program with the path to a csv-file containing sorting algorithm-data as argument.")
    exit(1)
plot(sys.argv[1])