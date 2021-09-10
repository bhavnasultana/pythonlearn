
# val should be int.
def reverse_int(val):
     result = 0
     while val > 0:
         rem = val % 10
         result = result * 10 + rem
         val = val // 10
     return result


def approach_one():
    print('Approach One')
    num1 = int(input())
    num2 = int(input())
    reversed_num1 = reverse_int(num1)
    reversed_num2 = reverse_int(num2)
    sum = reversed_num1 + reversed_num2
    print(sum)


if __name__ == '__main__':
    approach_one()
    import random
    #print(12, 21, 1992, sep='/')
    #print("no newline", end='')
    #print("sum of 5 and 2 is", 5+2)

    #print("Random", random.randint(1,25))
    #print("    Hello    ".rstrip())
    #print("+".join(["Hello", "World"]))
    #print([1,2,3] * 3)

#Fibonacci
    def fib(n):
      i = 0
      x = 0
      y = 1
      if n <= 1e6:
         while i < n-1:
            z = x + y
            x = y
            y = z
            i+=1
      return z

    num = int(input())
    a = fib(num)
    print("The", num, "th number in fibonnaci series is", a)



    sum = 0
    n = int(input())
    while n > 0:
        sum = sum + n
        n = int(input())
    print(sum)

    sampledic = {"Bhavna" : 920, "Hari" : 876, "Ankit" : 987}
    #Parsing a dictionary










  




