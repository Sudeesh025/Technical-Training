#
# def romanToInt(s):
#     roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
#     num = 0
#     last_value = 0
#     for char in reversed(s):
#         value = roman_dict[char]
#         if value < last_value:
#             num -= value
#         else:
#             num += value
#         last_value = value
#     return num

# s = "CIX"
# print(romanToInt(s))  # Output: 5





# def bubbleSort(arr,c):
#     n = len(arr)
#     # optimize code, so if the array is already sorted, it doesn't need
#     # to go through the entire process
#     # Traverse through all array elements
#     c = 0
#     for i in range(n-1):
#
#         # range(n) also work but outer loop will
#         # repeat one time more than needed.
#         # Last i elements are already in place
#         swapped = False   #flag
#         for j in range(0, n-i-1):
#
#             # traverse the array from 0 to n-i-1
#             # Swap if the element found is greater
#             # than the next element
#             if arr[j] > arr[j + 1]:
#                 swapped = True
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
#
#             c = c + 1
#
#         if not swapped:
#             # if we haven't needed to make a single swap, we
#             # can just exit the main loop.
#             return
#
#
# # Driver code to test above
# arr = [64, 34, 25, 12, 22, 11, 90]
# c=0
# bubbleSort(arr,0)
#
# print("Sorted array is:")
# print(c)
# for i in range(len(arr)):
#     print("% d" % arr[i], end=" ")


# def add_digits(num):
#     # Convert the number to a string
#     num_str = str(num)
#
#     # Initialize the sum to 0
#     sum = 0
#
#     # Iterate over each character in the string
#     for char in num_str:
#         # Convert the character back to an integer and add it to the sum
#         sum += int(char)
#     return sum
# def prime(num):
#     for i in range(2, num):
#         if (num % i == 0):
#             return("not prime")
#         else:
#             return("prime")
# sum=add_digits(201)
# print(sum)
# print(prime(sum))

#203---5



'''def search(n,m,f):
    str = list(n)
    for i in n:
        if(n=="m"):
            print("0")
        elif(n>="m"):
            print(m)
        else:
            print(f)
n = input()
search(n,0,0)'''





# s="leet**cod*e"
# b=[]
# for i in s:
#     if(i!="*"):
#         b.append(i)
#     else:
#         b.pop()
# print("".join(b))


s="p**suy"
l=[]
for i in s:
    if(i!="*"):
        l.append(i)
    # else:
    #     l.pop()
print("".join(l))


