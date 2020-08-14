import sys

def mergeSort(items):
    n = len(items)
    if(n == 1):
        return items
    fhalfend = int(n/2)
    shalfstart = int((n/2))
    fhalf = items[:fhalfend]
    shalf = items[shalfstart:]
    fhalf = mergeSort(fhalf)
    shalf = mergeSort(shalf)
    return merge(fhalf, shalf)
    
def merge(list1, list2):
    
    newarr = []
    while len(list1) > 0 and len(list2) > 0:
        if list1[0] > list2[0]:
            newarr.append(list2[0])
            list2.pop(0)
        else:
            newarr.append(list1[0])
            list1.pop(0)
    while len(list1) > 0:
        newarr.append(list1[0])
        list1.pop(0)
        
    while len(list2) > 0:
        newarr.append(list2[0])
        list2.pop(0)
    return newarr

if __name__ == "__main__":

    num_items = 0
    items = []

    for line in sys.stdin:

        print("Given this input: " + str(line))
        items = line.split()

        items = [ int(x) for x in items ]
        items = mergeSort(items)
        print("This is the output: " + str(items))

