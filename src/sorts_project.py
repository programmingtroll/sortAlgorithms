# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "Juan Carlos Flores"
__date__ = "$Feb 26, 2016 9:19:29 AM$"

import random
import time
import sys
sys.setrecursionlimit(120000)

def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp

def insertionsort( aList ):
  for i in range( 1, len( aList ) ):
    tmp = aList[i]
    k = i
    while k > 0 and tmp < aList[k - 1]:
        aList[k] = aList[k - 1]
        k -= 1
    aList[k] = tmp
    
def selectionsort( aList ):
  for i in range( len( aList ) ):
    least = i
    for k in range( i + 1 , len( aList ) ):
      if aList[k] < aList[least]:
        least = k
 
    exchange( aList, least, i )
 
 
def exchange( A, x, y ):
  tmp = A[x]
  A[x] = A[y]
  A[y] = tmp

def mergeSort(alist):
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

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

def heapsort(a):
    """Run heapsort on a list a
    >>> a = [32,46,77,4344564,7322,3,46,7,32457,7542,4,667,54,]
    >>> heapsort(a)
    >>> print(a)
    [3, 4, 7, 32, 46, 46, 54, 77, 667, 7322, 7542, 32457, 4344564]
    """

    heapify(a, len(a))
    end = len(a)-1
    while end > 0:
        a[end], a[0] = a[0], a[end]
        end -= 1
        sift_down(a, 0, end)

def heapify(a, count):
    start = int((count-2)/2)
    while start >= 0:
        sift_down(a, start, count-1)
        start -= 1

def sift_down(a, start, end):
    root = start
    while (root*2+1) <= end:
        child = root * 2 + 1
        swap = root
        if a[swap] < a[child]:
            swap = child
        if (child + 1) <= end and a[swap] < a[child+1]:
            swap = child+1
        if swap != root:
            a[root], a[swap] = a[swap], a[root]
            root = swap
        else:
            return

#=======================================================================
#  Author: Isai Damier
#  Title: Radix Sort
#  Project: geekviewpoint
#  Package: algorithms
#
#  Statement:
#  Given a disordered list of integers, rearrange them in natural order.
#
#  Sample Input: [18,5,100,3,1,19,6,0,7,4,2]
#
#  Sample Output: [0,1,2,3,4,5,6,7,18,19,100]
#
#  Time Complexity of Solution:
#  Best Case O(kn); Average Case O(kn); Worst Case O(kn),
#  where k is the length of the longest number and n is the
#  size of the input array.
#
#  Note: if k is greater than log(n) then an nlog(n) algorithm would
#  be a better fit. In reality we can always change the radix
#  to make k less than log(n).
#
#  Approach:
#  radix sort, like counting sort and bucket sort, is an integer based
#  algorithm (i.e. the values of the input array are assumed to be
#  integers). Hence radix sort is among the fastest sorting algorithms
#  around, in theory. The particular distinction for radix sort is
#  that it creates a bucket for each cipher (i.e. digit); as such,
#  similar to bucket sort, each bucket in radix sort must be a
#  growable list that may admit different keys.
#
#  For decimal values, the number of buckets is 10, as the decimal
#  system has 10 numerals/cyphers (i.e. 0,1,2,3,4,5,6,7,8,9). Then
#  the keys are continuously sorted by significant digits.
#======================================================================= 
def radixsort( aList ):
  RADIX = 10
  maxLength = False
  tmp , placement = -1, 1
 
  while not maxLength:
    maxLength = True
    # declare and initialize buckets
    buckets = [list() for _ in range( RADIX )]
 
    # split aList between lists
    for  i in aList:
      tmp = i / placement
      buckets[tmp % RADIX].append( i )
      if maxLength and tmp > 0:
        maxLength = False
 
    # empty lists into aList array
    a = 0
    for b in range( RADIX ):
      buck = buckets[b]
      for i in buck:
        aList[a] = i
        a += 1
 
    # move to next digit
    placement *= RADIX

def writeToTxt(stringToAppend):
    file = open('sortResults.txt','a')
    file.write(stringToAppend)
    file.close()

sortsName= ['MergeSort','QuickSort','HeapSort','RadixSort','InsertionSort','SelectionSort','BubbleSort']
sorts = {0:mergeSort,1:quickSort,2:heapsort,3:radixsort,4:insertionsort,5:selectionsort,6:bubbleSort}
inputs = [10,100,1000,10000,100000,1000000]

for key, value in sorts.iteritems():
    writeToTxt(sortsName[key]+" results:" )
    writeToTxt('\n')
    for index in range(0,len(inputs)):
        listToOrder = []
        for x in range(0, inputs[index]):
            listToOrder.append(x)
        resultString = '\n'
        resultString += 'Results for input '+ str(inputs[index])
        resultString += '\n\n'
        sum = 0
        for times in range(0,10):
            random.shuffle(listToOrder)
            start = time.time()
            value(listToOrder)
            end = time.time()
            result = end - start
            sum += result
            resultString += str(inputs[index]) + "," + str(result)
            resultString +='\n'
        avg = sum/10
        resultString +='Average time: '+ str(avg)
        resultString +='\n'
        writeToTxt(resultString)
    writeToTxt('\n')

