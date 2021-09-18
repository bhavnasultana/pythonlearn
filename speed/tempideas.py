a = [2,4]
b = [16,32,96]
x = [x for x in range(4,17)]
y = []
z = []
for elem in a:
    y.append(list(filter(lambda x: x%elem == 0, x)))
for element in b:
    z.append(list(filter(lambda x: element%x == 0, x)))
import operator
x = dict()
y = []
something = [4,4,2,1,1]
something.sort()
for elem in something:
    x[elem] = something.count(elem)
print(x)
keyMax = max(x.items(), key = operator.itemgetter(1))[0]
print(keyMax)

# import numpy as np
# weight = [11,12,13,14]
# np_weight = np.array(weight)
# np_lbs = np_weight * 2.2
# print(np_lbs)
# print(np_lbs[np_lbs > 25])

y = {1:2, 2:4, 3:3, 4:2, 5:1}
z = max(y, key = lambda x: y[x])


something = "what"
print(something.upper())



