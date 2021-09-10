
def file_example():


    with open('random.txt', 'w') as of:
        of.write('this is the first line\n')
        of.write('this is the second line\n')
        of.write('this is the third line')

    def get_row(idx):
        getting = of.readlines()
        return getting[idx]
    with open('random.txt', 'r') as of:
        something = get_row(1)
        print(something)

file_example()











    