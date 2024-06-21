'''s="IX"
m={'I':1,
   'V':5,
   'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000}
dif=0
for i in range(len(s)):
    if(i<len(s)-1 and m[s[i]]<m[s[i+1]]):
        dif-=m[s[i]]
    else:
        dif+=m[s[i]]
print(dif)'''

'''p=input()
def rev(p):
    str=""
    negative=False
    if p[0]=="-":
        negative =True
        p=p[1:]
    for i in p:
        str=i+str
    if(negative==True):
        str="-"+str
    if(str==p):
        print("True")
    else:
        print("False")
rev(p)'''


'''def isPalindrome(x: int) -> bool:
    str = ""
    for i in x:
        str = i + str
    if (str == x):
        return True
    else:
        return False
p="sos"
print(isPalindrome(p))'''

# sum=6 4-1
'''def max_subarray_sum(nums):
    max_sum = float('-inf')  # Initialize with negative infinity
    current_sum = 0

    for num in nums:
        # Update the current sum by adding the current element
        current_sum = max(num, current_sum + num)
        # Update the maximum sum encountered so far
        print(current_sum, end=",")
        max_sum = max(max_sum, current_sum)

    return max_sum'''

num = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
def subarr(num):
    max_num=float('-inf')
    current=0
    for i in num:
        current=max(i,current+i)
        max_num=max(max_num,current)
    return max_num
print(subarr(num))


