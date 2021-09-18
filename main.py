# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


def revision_for_loops():
    # Print numbers from 1 to 20
    for x in range(20):
        print(x)

    # Print numbers from 7 to 10
    # [7, 10)
    for x in range(7, 10):
        print(x)

    # Print odd numbers from 5 to 10.
    for x in range(5, 10, 2):
        print(x)

    # Print odd numbers from 6 to 10.
    for x in range(6, 10):
        if x % 2 == 1:
            print(x)


def revision_lists():
    l = []
    another_way = list()
    l.append(10)
    l.append(20)
    l.append(30)
    print(l[0])
    print(l[1])

    print(l[-1])
    print(l[-2])

    # Print elements of list between indices [1, 3)
    print(l[1:3])
    print(l[0:2])

    result = l[1:3]
    print(result[0])
    result[0] = -1
    print(l)
    print(result)

    # Iterate over list elements.
    for x in l:
        print(x)

    # Another way.
    for idx in range(len(l)):
        print(l[idx])


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print_hi('PyCharm')
    # revision_for_loops()
    revision_lists()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
