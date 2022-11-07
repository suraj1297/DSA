def binary_search(elements, searchElement):
    low = 0
    high = len(elements) - 1

    while low<=high:
        mid = (low+high)//2
        guess = elements[mid]
        if(searchElement == guess ):
            return mid
        elif guess > searchElement:
            high = mid - 1
        else:
            low = mid + 1

    return None

print(binary_search([1,2,3,4,5,6,7,8,9],4))


"""
Binary Search Algorithm:

Suppose we want to find an element in an list of sorted array.
Then there are two ways to do that. Either we can make guess serially
staring from 1, 2, 3,.......... . And if the number we are looking for is 99
then it will take us 99 guess/steps to reach that number. This is simple search
or matbe even we can call it as stupid search.

In Binary search, we guess the middle element, like first we will say 50, as
50 is too low we will drop all numbers from 1 - 50 and because of this in 
one step we elemented 1 - 50 numbers i.e half numbers.
In this way we eliminate half numbers in one step unlike one element in simple search.
2nd step -> 51 - 100 => 75 , too low
3rd step -> 76 - 100 => 88, too low
4th step -> 89 - 100 => 94, too low
5th step -> 95 - 100 => 97, too low
6th step -> 98 - 100 => 99, Element found

We were able to find our element in 6 steps using binary search.
Thats th beauty of binary search. Only thing is we should have sorted list of elements
fir binary search.


The Time complexity of binary search is:

O(n) = log n

n -> number of elements

if we have list of 240,000 elemnts then log 240,000 -> 18. It will takes 18 steps
in worst to find our element.
"""