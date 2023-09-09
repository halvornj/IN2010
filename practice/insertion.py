
def sort(array:list) ->list:
    for i in range(1, len(array)):
        j = i
        while j>0 and array[j-1] > array[j]:
            array[j-1], array[j] = array[j], array[j-1]
            j = j-1




def main():
    tester = [1,4,3,2,6,4]
    print(tester)
    sort(tester)
    print(tester)

main()
