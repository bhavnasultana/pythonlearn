def file_handle():

    f = open("example.txt", "r")
    #opening_line = get_row(2)

    #print(opening_line)
    #getting = append_row([101, "cat"])
    #getting1 = append_row(["hello", "something"])
    getting_by_key = get_row_key("hello")
    f.close()

def get_row_key(key):

    f = open("example.txt", "r")
    s = f.readlines()
    for line in s:
        if line[0:len(key)] == key and line[len(key)] == ",":
            print(line)


    #count the number of lines in a file = sum(1 for line in open("example.txt"))


def no_of_rows():
    f = open("example.txt", "r")
    for i,l in enumerate(f):
        pass
    return i+1

def get_row(idx):
    f = open("example.txt", "r")
    getting = f.readlines()
    return getting[idx]

def append_row(elements):

    f = open("example.txt", "a")
    s = ",".join(list(map(lambda x: str(x), elements)))
    f.write(s)
    f.write("\n")


file_handle()
