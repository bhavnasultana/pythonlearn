if __name__ == '__main__':
    print("Hello")
#divisible by 3 list
# def divby3(sample):
#     o = []
#     for x in sample:
#         if x%3 == 0:
#             o.append(x)
#     return o

# sample = [1,2,6,8,6,9,8,10,12,10]
# sample = filter(lambda x: x%3 != 0, sample)
# print(list(sample))
# print(list(j))
    # divby3(sample)
# print(j)
# print(sample)

#sorting a list
# something = [1,2,6,8,6,9,8,10,12,10]
# something.sort()
# print(something)
#
# returning kth smallest element in the list
# something = [1,2,6,8,8,6,9,8,10,12,10]
# print("Enter k")
# k = int(input())
# something.sort()
# result = (lambda x:
# print(something)
# print(something[k])
#
#converting list of elements to a string
# x =[1,2,3,4,5,6]
# y = map(lambda i: str(i), x)
# print(list(y))


# #converting keys to values
# sampledic = {0:1, 1:2, 2:3, 3:9, 4:10}
# reverse_dic = map(lambda x, sampledic)
# reverse_dic = {values:keys for keys, values in sampledic.items()}
# print(reverse_dic)

#
#
# s = [1,2,3,4,5,6,7,8,9]
# result = filter(lambda x: x % 2 == 0, s)
# anotheresult = filter(lambda x: x% 2 != 0,s )
# print(list(result))
# print(list(anotheresult))
#
# #implementing map here
# something = map(lambda x, y: x*y, [1,2], [3,4])
# print(list(something))
#
# #here's what lambda does
# x = (lambda x,y,z: x*y*z)
# print(x(1,2,3))

x = input("Enter any number")
print(x[::-1])

for animal in ["dog", "cat", "mouse"]:
    # You can use format() to interpolate formatted strings
    print("{} is a mammal".format(animal))

animals = ["dog", "cat", "mouse"]
for i, value in enumerate(animals):
    print(i, value)

print([x for x in [3, 4, 5, 6, 7] if x > 5])

# y = set()
# nums = [1,2,3,3,2,1,1,1,6,7,4,3,3,3]
# for x in nums:
#     y.add(nums.count(x))
# majority = max(y)
# i = {}
# i = nums
# print(i)

# nums = [1,2,3,3,2,1,1,1,1,6,7,4,3,3,2]
# x = dict()
# for i, value in enumerate(nums):
#     x.add(( value, (nums.count(value))))
# majority_freq = max(x, key=x.get)
# print(majority_freq)
#
# nums = [1,2,3,3,2,1,1,1,1,6,7,4,3,3,2]
# y = {}
# for x in nums:
#     y[nums.count(x)] = x
# print(y)
# majority = max(y, key=y.get)
# print(majority)

# first = "abcd"
# second = "bcad"
# first = list()
# first.sort()
# print(first)
#
#
# first = []
#         second = []
#         for x in s:
#             first.append(x)
#         for y in goal:
#             second.append(y)
#         for i in first

# first = ["a","b","c"]
# second = ["a","c","b"]
# count = 0
# compare = []
# for i in first, second:
#     if first[i] != second[i]:
#         count +=1
#         compare.append(i)
# if count == 2:
#
#     first = []
#     second = []
#     count = 0
#     i = len(first)
#     j = len(second)
#     if i != j:
#         return False
#     comparison = []
#     for x in s:
#         first.append(x)
#     for y in goal:
#         second.append(y)
#     for i in range(first):
#         if first[i] != second[i]:
#             count += 1
#             i += 1
#             comparison.append(i)
#     a = comparison[0]
#     b = comparison[1]
#     if count == 2:
#         if first[a] == second[b] and first[b] == second[a]:
#             return True
#         else:
#             return False
#     else:
#         return False

    def isHappy(self, n: int) -> bool:
        sumofsquare = 0
       
        flag = 0
        while n>0:
            rem = n%10
            n = n//10
            sumofsquare = sumofsquare + rem**2
            passing = sumofsquare
            if passing == 1:
                flag = 1
                break
        if flag == 1:
            return True
        else:
            isHappy(passing)







# a = map(lambda x,y: x == y, first, second)
# print(list(a))



















