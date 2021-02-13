def verifySorted(A):
    for i in range(len(A)-1):
        if A[i] > A[i+1]:
            print(f"A[{i}]=={A[i]} is greater than A[{i+1}]=={A[i+1]}")
            return
    print("Array is sorted!")

def pickPivot(A):
    return(A[-1]) # always use the last value of the array A


def partitionInPlace(A,pivotvalue):
    lowindex = -1
    for i in range(len(A)-1):
        if A[i] <= pivotvalue:
            lowindex+=1
            A[lowindex],A[i] = A[i],A[lowindex]
    A[lowindex+1],A[len(A)-1] = A[len(A)-1],A[lowindex+1]
    return (lowindex+1)
# Input:
#   an array A to be sorted
# Returns:
#   A has been sorted
def quicksort(A):
    # manual sort for small arrays
    if len(A) < 3:
        if len(A) <= 1:
            return A 
        elif A[0] > A[1]:
            A[0],A[1] = A[1],A[0]
        return A
    # set up recursions
    pivotvalue = pickPivot(A)
    partitionindex = partitionInPlace(A,pivotvalue)
    quicksort(A[0:partitionindex])
    quicksort(A[partitionindex+1:]) 







### Driver
def main():
    # create
    import numpy.random
    numpy.random.seed(0)
    A = numpy.random.randint(0,100,100)

    # sort
    quicksort(A)

    # verify
    print(A)
    verifySorted(A)
    

if __name__ == "__main__":
    main()
