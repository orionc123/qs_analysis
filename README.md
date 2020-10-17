# Quicksort Analysis
The Quicksort algorithm is rather interesting. Its worst-case time complexity is
O(n<sup>2</sup>), and its best-case time complexity is O(nlgn), but on average Quicksort runs in Θ(nlgn). I used
this module to compare the time complexity of Quicksort, Mergesort, and Selectionsort for random inputs of varying sizes. Here I will discuss my experiment to determine how well Quicksort performs on average.
## Quicksort Explained
Quicksort is a divide and conquer algorithm. That is, we partition the original problem
into two subproblems, and sort each subproblem using recursion. What makes the best-case and
the worst-case so drastically different is the way in which we partition. In the worst case, our pivot
element will be either the largest or the smallest element in the array. This causes all of the
elements to be placed into only one of the two subarrays, and we must recurse on the entire array
(n<sup>2</sup>) instead of two equal subarrays (nlgn). In the best case, our pivot element will be the median
of the array.
## Recurrence Relation
An easy way to analyze this is to assume that the average partition will divide the
problem into sizes 3n/4 and n/4. This is reasonable because it’s halfway between the best case
and the worst case. This gives us the recurrence relation: T(n) = T(3n/4) + T(n/4) + n. At each
level of the recurrence tree, we do n work, and there are log<sub>4/3</sub>(n) levels. Because the n/4 path of
the tree ends before the 3n/4 path, we know the total work is less than log<sub>4/3</sub>(n), and this makes the
average time complexity for Quicksort O(nlgn).
## Testing the Theory
We’re able to evaluate the average time complexity of Quicksort theoretically, but that
isn’t enough. We need evidence. In my Python module, I’ve implemented three sorting
algorithms: Quicksort, Mergesort, and Selectionsort. Mergesort has a Θ(nlgn) time complexity,
and Selectionsort has a Θ(n<sup>2</sup>) time complexity. Run the module for yourself to compare the sorting algorithms.
## Conclusion
As we can see, as n gets larger, the time it takes to run Selectionsort (n<sup>2</sup>) increases exponentially
faster than Mergesort or Quicksort. Quicksort seems to run significantly better than Mergesort
(nlgn) for the smaller inputs, but as n increases, they become very similar. Another thing to note
is that the max runtime for Quicksort never comes close to the minimum runtime for the n<sup>2</sup>
algorithm even though the worst case for Quicksort is O(n<sup>2</sup>). I find this to be quite shocking; I
thought I would see more cases of Quicksort running in n<sup>2</sup> time, but it seems that Quicksort runs
consistently in nlgn time. From this experiment, I’ve discovered that Quicksort has a
time complexity of Θ(nlgn) on average--performing much more consistently than I had originally thought.
