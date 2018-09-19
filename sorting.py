# Bubble sorting fuction                                              
import time
from random import randrange
import sys
sys.setrecursionlimit(1500)

def bubbleSort(aList):
	for i in range (len(aList)):
	    for j in range(len(aList)):
	        if aList[i] <= aList[j]:
	            t = aList[i]
	            aList[i] = aList[j]
	            aList[j] = t

def quickSort(alist):
   quickSortHelper(alist,0,len(alist)-1)

def quickSortHelper(alist,first,last):
   if first<last:

       splitpoint = partition(alist,first,last)

       quickSortHelper(alist,first,splitpoint-1)
       quickSortHelper(alist,splitpoint+1,last)


def partition(alist,first,last):
   pivotvalue = alist[first]

   leftmark = first+1
   rightmark = last

   done = False
   while not done:

       while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
           leftmark = leftmark + 1

       while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
           rightmark = rightmark -1

       if rightmark < leftmark:
           done = True
       else:
           temp = alist[leftmark]
           alist[leftmark] = alist[rightmark]
           alist[rightmark] = temp

   temp = alist[first]
   alist[first] = alist[rightmark]
   alist[rightmark] = temp


   return rightmark



def mergeSort(alist):
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]
        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1


miLista = []

for i in range (250):
    miLista.append(randrange(0,1000))


start_time = time.clock()
bubbleSort(miLista)
print ("Bubble Sorting-->",time.clock() - start_time)

start_time = 0

start_time = time.clock()
quickSort(miLista)
print ("Quick Sorting-->",time.clock() - start_time)

start_time = 0

start_time = time.clock()
mergeSort(miLista)
print ("Merge Sorting-->",time.clock() - start_time)


