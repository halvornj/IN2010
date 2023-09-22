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

    yInsertComps = []
    
    N:Final = 0
    INSERTION_CMP = 1
    INSERTION_SWAPS=2
    INSERTION_TIME = 3
    MERGE_CMP = 4
    MERGE_SWAPS = 5
    MERGE_TIME = 6
    #! change these when plotting a new file
    outputFile = "swap_compare_time_insertion"
    TITLE ="antall sammenligninger og swaps / tid"


    with open(filename, 'r') as csvfile:
        lines = csv.reader(csvfile, delimiter=',')
        headers = next(lines)
        for row in lines:
            #use the constants defined above to determine what gets plotted.
            #!remember to change axis-titles. too lazy to program that in, this is already overkill when i could just screenshot excel...
            x.append(int(row[INSERTION_TIME]))
            #yMerge.append(int(row[3]))
            yInsert.append(int(row[INSERTION_SWAPS]))
            yInsertComps.append(int(row[INSERTION_CMP]))

    #plt.plot(x,yMerge, color='g', label="Merge")
    plt.plot(x, yInsert, color='r', label="Insertion swaps")
    plt.plot(x, yInsertComps, color='g', label="insertion compares")

    plt.xlabel("time (μs)")
    plt.ylabel('antall')
    plt.title(TITLE)
    plt.grid()
    plt.legend()

    plt.savefig("../output_graphs/"+outputFile)
    
    plt.show()


if sys.argv[1] == None:
    print("error: run plot-program with the path to a csv-file containing sorting algorithm-data as argument.")
    exit(1)
plot(sys.argv[1])