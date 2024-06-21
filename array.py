# def longest(arr):
#     max=arr[0]
#     for i in range(1,len(arr)):
#         if(arr[i]>max):
#             max=arr[i]
#     return max
# arr=[10,6,7,3,2,4]
# ans=longest(arr)
# print("largest of array is",ans)

# def large(arr,n):
#     arr.sort()
#
#     return arr[n]
# arr=[9,87,65,5,1,0]
# n=len(arr)
# ans=large(arr,n-1)
# print("largest of the numbers is:",ans)


''' secoud largest,smallest
def second(arr,n):
    if(n<2):
        return -1
    seclargest=float('-inf')
    largest=float('-inf')
    for i in range(n):
        if(arr[i]>largest):
            seclargest = largest
            largest=arr[i]
        elif(arr[i]>seclargest and arr[i]!=largest):
            seclargest=arr[i]
    return seclargest
def secsmall(arr,n):
    if(n<2):
        return -1
    ssmall=float('inf')
    small=float('inf')
    for i in range(n):
        if(arr[i]<small):
            ssmall = small
            small=arr[i]
        elif(arr[i]<ssmall and arr[i]!=small):
            ssmall=arr[i]
    return ssmall

arr=[3,7,9,6,5,2,7,1]
n=len(arr)
slargest=second(arr,n)
ssmallest=secsmall(arr,n)
print("Secound Largest=",slargest)
print("Secound smallest=",ssmallest)'''

'''third
def second(arr,n):
    if(n<2):
        return -1
    seclargest=float('-inf')
    largest=float('-inf')
    tlargest = float('-inf')
    for i in range(n):
        if(arr[i]>largest):
            tlargest=seclargest
            seclargest = largest
            largest=arr[i]
        elif(arr[i]>seclargest and arr[i]!=largest and arr[i] != tlargest):
            seclargest=arr[i]
        elif (arr[i] > tlargest and arr[i] != seclargest and arr[i]!=largest):
            tlargest = arr[i]
    return tlargest
arr=[3,7,9,6,5,2,7,1]
n=len(arr)
thlargest=second(arr,n)
print("third Largest=",thlargest)'''



# from typing import List
#
# def removeDuplicates(arr: List[int]) -> int:
#     i = 0
#     for j in range(1, len(arr)):
#         if arr[i] != arr[j]:
#             i += 1
#             arr[i] = arr[j]
#     return i + 1
#
#
# # if __name__ == "__main__":
# arr = [1, 1, 2, 2, 2, 3, 3]
# k = removeDuplicates(arr)
# print("The array after removing duplicate elements is ")
# for i in range(k):
#     print(arr[i], end=" ")


from typing import List
class Solution:
# def removeDuplicates(self, nums: List[int]) -> int:
    def removeDuplicates(self,arr: List[int]) -> int:
        i = 0
        for j in range(1, len(arr)):
            if (arr[i] != arr[j]):
                i += 1
                arr[i] = arr[j]
        return i + 1

if __name__ == "__main__":
    arr = [1, 1, 2, 2, 2, 3, 3]
    k = Solution().removeDuplicates(arr)
    print("duplicates")
    for i in range(k):
        print(arr[i], end=" ")

