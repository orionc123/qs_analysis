import random
import time
import statistics

#   Author: Orion Carroll
#   Date: 10/20/2018
#   Purpose: Verify the average runtime of the quicksort algorithm.

# Selectionsort serves as our O(n^2) sorting algorithm. We must see how Quicksort compares to n^2.
class Selectionsort:
    def sort(self,A):
        for fill in range(len(A)-1, 0, -1):
            maxPos = 0
            for loc in range(1,fill+1):
                if A[loc] > A[maxPos]:
                    maxPos = loc
            
            temp = A[fill]
            A[fill] = A[maxPos]
            A[maxPos] = temp

# Mergesort serves as our theta(nlgn) sorting algorithm. We must see how Quicksort compares to nlgn.
class Mergesort:
    def sort(self,A):
        self.ms(A,0,len(A)-1)

    def ms(self,A,p,r):
        if p<r:
            q = (p+r)//2
            self.ms(A,p,q)
            self.ms(A,q+1,r)
            self.merge(A,p,r)
    
    def merge(self,A,p,r):
        if p<r:
            q = (p+r)//2
            s1 = q-p + 1
            s2 = r-q
            #Create 2 temporary subarrays
            L = [0] * (s1)
            R = [0] * (s2)

            for i in range(s1):
                L[i] = A[p+i]
            for j in range(s2):
                R[j] = A[q+1+j]
            
            i = 0
            j = 0
            k = p
            #Merge the 2 arrays back into A
            while i < s1 and j < s2:
                if L[i] <= R[j]:
                    A[k] = L[i]
                    i += 1
                else:
                    A[k] = R[j]
                    j += 1
                k += 1
            
            while i < s1:
                A[k] = L[i]
                i += 1
                k += 1

            while j < s2:
                A[k] = R[j]
                j += 1
                k += 1
            
# Quicksort is our algorithm to evaluate.
class Quicksort:
    def qs(self,A,p,r):
        if p<r:
            q = self.partition(A,p,r)
            self.qs(A,p,q-1)
            self.qs(A,q+1,r)

    def partition(self, A, p, r):
        x = A[r]
        i = p-1
        for j in range(p, r-1):
            if A[j] <= x:
                i = i + 1
                temp = A[i]
                A[i] = A[j]
                A[j] = temp
        temp = A[i + 1]
        A[i + 1] = A[r]
        A[r] = temp
        return i + 1
        
    def sort(self, A):
        self.qs(A,0,len(A)-1)

# instantiate sorting classes
select = Selectionsort()
quick = Quicksort()
merge = Mergesort()

#create lists of runtimes
#n = 300
qs300 = list()
ss300 = list()
ms300 = list()
for x in range(1000):
    #for each sorting algorithm, time the sort x times, and report valuable data
    listn300 = random.sample(range(301), 300)
    start = time.time()
    quick.sort(listn300)
    end = time.time()
    qs300.append(end - start)

    start1 = time.time()
    select.sort(listn300)
    end1 = time.time()
    ss300.append(end1 - start1)

    start2 = time.time()
    merge.sort(listn300)
    end2 = time.time()
    ms300.append(end2 - start2)

print("Max Quicksort time for n=300: ", max(qs300))
print("Min Quicksort time for n=300: ", min(qs300))
print("Median Quicksort time for n=300: ", statistics.median(qs300))

print("Max Selectionsort time for n=300: ", max(ss300))
print("Min Selectionsort time for n=300: ", min(ss300))
print("Median Selectionsort time for n=300: ", statistics.median(ss300))

print("Max Mergesort time for n=300: ", max(ms300))
print("Min Mergesort time for n=300: ", min(ms300))
print("Median Mergesort time for n=300: ", statistics.median(ms300))

#n = 1000
qs1k = list()
ss1k = list()
ms1k = list()
for x in range(500):
    listn1k = random.sample(range(1001), 1000)
    start = time.time()
    quick.sort(listn1k)
    end = time.time()
    qs1k.append(end - start)

    start1 = time.time()
    select.sort(listn1k)
    end1 = time.time()
    ss1k.append(end1 - start1)

    start2 = time.time()
    merge.sort(listn1k)
    end2 = time.time()
    ms1k.append(end2 - start2)

print("Max Quicksort time for n=1000: ", max(qs1k))
print("Min Quicksort time for n=1000: ", min(qs1k))
print("Median Quicksort time for n=1000: ", statistics.median(qs1k))

print("Max Selectionsort time for n=1000: ", max(ss1k))
print("Min Selectionsort time for n=1000: ", min(ss1k))
print("Median Selectionsort time for n=1000: ", statistics.median(ss1k))

print("Max Mergesort time for n=1000: ", max(ms1k))
print("Min Mergesort time for n=1000: ", min(ms1k))
print("Median Mergesort time for n=1000: ", statistics.median(ms1k))

#n = 5000
qs5k = list()
ss5k = list()
ms5k = list()
for x in range(100):
    listn5k = random.sample(range(5001), 5000)
    start = time.time()
    quick.sort(listn5k)
    end = time.time()
    qs5k.append(end - start)

    start1 = time.time()
    select.sort(listn5k)
    end1 = time.time()
    ss5k.append(end1 - start1)

    start2 = time.time()
    merge.sort(listn5k)
    end2 = time.time()
    ms5k.append(end2 - start2)

print("Max Quicksort time for n=5000: ", max(qs5k))
print("Min Quicksort time for n=5000: ", min(qs5k))
print("Median Quicksort time for n=5000: ", statistics.median(qs5k))

print("Max Selectionsort time for n=5000: ", max(ss5k))
print("Min Selectionsort time for n=5000: ", min(ss5k))
print("Median Selectionsort time for n=5000: ", statistics.median(ss5k))

print("Max Mergesort time for n=5000: ", max(ms5k))
print("Min Mergesort time for n=5000: ", min(ms5k))
print("Median Mergesort time for n=5000: ", statistics.median(ms5k))

#n = 10000
qs10k = list()
ss10k = list()
ms10k = list()
for x in range(100):
    listn10k = random.sample(range(10001), 10000)
    start = time.time()
    quick.sort(listn10k)
    end = time.time()
    qs10k.append(end - start)

    start1 = time.time()
    select.sort(listn10k)
    end1 = time.time()
    ss10k.append(end1 - start1)

    start2 = time.time()
    merge.sort(listn10k)
    end2 = time.time()
    ms10k.append(end2 - start2)

print("Max Quicksort time for n=10000: ", max(qs10k))
print("Min Quicksort time for n=10000: ", min(qs10k))
print("Median Quicksort time for n=10000: ", statistics.median(qs10k))

print("Max Selectionsort time for n=10000: ", max(ss10k))
print("Min Selectionsort time for n=10000: ", min(ss10k))
print("Median Selectionsort time for n=10000: ", statistics.median(ss10k))

print("Max Mergesort time for n=10000: ", max(ms5k))
print("Min Mergesort time for n=10000: ", min(ms5k))
print("Median Mergesort time for n=10000: ", statistics.median(ms5k))