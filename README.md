# Quicksort Analysis
The Quicksort algorithm is a rather interesting one. Its worst-case time complexity is
O(n2), and its best-case time complexity is O(nlgn), but on average Quicksort runs in Θ(nlgn). In
the following write-up, I will discuss my experiment to determine how well Quicksort performs on average.


Quicksort is a divide and conquer algorithm. That is, we partition the original problem
into two subproblems, and sort each subproblem using recursion.What makes the best-case and
the worst-case so drastically different is the way we partition. In the worst case, our pivot
element will be either the largest or the smallest element in the array. This causes all of the
elements to be placed into only one of the two subarrays, and we must recurse on the entire array
(n2
) instead of two equal subarrays (nlgn). In the best case, our pivot element will be the median
of the array.
An easy way to analyze this is to assume that the average partition will divide the
problem into sizes 3n/4 and n/4. This is reasonable because it’s halfway between the best case
and the worst case. This gives us the recurrence relation: T(n) = T(3n/4) + T(n/4) + n. At each
level of the recurrence tree, we do n work, and there are log4/3n levels. Because the n/4 path of
the tree ends before the 3n/4 path, we know the total work is less than log4/3n, and this makes the
average time complexity for Quicksort O(nlgn).
We’re able to evaluate the average time complexity of Quicksort theoretically, but that
isn’t enough. We need evidence. In my Python module, I’ve implemented three sorting
algorithms: Quicksort, Mergesort, and Selectionsort. Mergesort has a Θ(nlgn) time complexity,
and Selectionsort has a Θ(n2
) time complexity. We will compare the time it takes to run both of
these sorting algorithms to the time it takes to run Quicksort on varying input sizes. Here are my
results for n = 300, 1000, 5000, and 10000:
Max Quicksort time for n=300: 0.0020012855529785156
Min Quicksort time for n=300: 0.0
Median Quicksort time for n=300: 0.000997304916381836
Max Selectionsort time for n=300: 0.007992982864379883
Min Selectionsort time for n=300: 0.0030028820037841797
Median Selectionsort time for n=300: 0.004999399185180664
Max Mergesort time for n=300: 0.005999565124511719
Min Mergesort time for n=300: 0.0009136199951171875
Median Mergesort time for n=300: 0.0019986629486083984
Max Quicksort time for n=1000: 0.005938529968261719
Min Quicksort time for n=1000: 0.0019257068634033203
Median Quicksort time for n=1000: 0.0029997825622558594
Max Selectionsort time for n=1000: 0.09506106376647949
Min Selectionsort time for n=1000: 0.04599928855895996
Median Selectionsort time for n=1000: 0.0540088415145874
Max Mergesort time for n=1000: 0.011928796768188477
Min Mergesort time for n=1000: 0.0049896240234375
Median Mergesort time for n=1000: 0.006006479263305664
Max Quicksort time for n=5000: 0.023999452590942383
Min Quicksort time for n=5000: 0.015987634658813477
Median Quicksort time for n=5000: 0.01799464225769043
Max Selectionsort time for n=5000: 1.4611501693725586
Min Selectionsort time for n=5000: 1.230051040649414
Median Selectionsort time for n=5000: 1.2914831638336182
Max Mergesort time for n=5000: 0.04591989517211914
Min Mergesort time for n=5000: 0.03592228889465332
Median Mergesort time for n=5000: 0.03800153732299805
Max Quicksort time for n=10000: 0.04798579216003418
Min Quicksort time for n=10000: 0.03393101692199707
Median Quicksort time for n=10000: 0.03899025917053223
Max Selectionsort time for n=10000: 6.166844129562378
Min Selectionsort time for n=10000: 4.907277584075928
Median Selectionsort time for n=10000: 5.070969223976135
Max Mergesort time for n=10000: 0.04591989517211914
Min Mergesort time for n=10000: 0.03592228889465332
Median Mergesort time for n=10000: 0.03800153732299805
As we can see, as n gets larger, the time it takes to run Selectionsort (n2
) increases exponentially
faster than Mergesort or Quicksort. Quicksort seems to run significantly better than Mergesort
(nlgn) for the smaller inputs, but as n increases, they become very similar. Another thing to note
is that the max runtime for Quicksort never comes close to the minimum runtime for the n2
algorithm even though the worst case for Quicksort is O(n2
). I find this to be quite shocking; I
thought I would see more cases of Quicksort running in n2
 time, but it seems that Quicksort runs
consistently in nlgn time. From this experiment, I’ve discovered that Quicksort has, on average, a
time complexity of Θ(nlgn). I’ll surely consider the Quicksort algorithm when I need something
sorted in the future, especially on smaller inputs; it performs much more consistently than I had
originally thought.
