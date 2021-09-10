class FileHandling:

    def file_handle(self):

        f = open("something.txt", "r")
        opening_line = self.get_row(2)

        print(opening_line)
        getting = self.append_row([101, "cat"])
        getting1 = self.append_row(["hello", "something"])
        getting_by_key = self.get_row_key("hello")
        f.close()

    def get_row_key(self, key):

        f = open("something.txt", "r")
        s = f.readlines()
        for line in s:
            if line[0:len(key)] == key and line[len(key)] == ",":
                print(line)



    def no_of_rows(self):
        f = open("something.txt", "r")
        for i,l in enumerate(f):
            pass
        return i+1

    def get_row(self, idx):
        f = open("something.txt", "r")
        getting = f.readlines()
        return getting[idx]

    def append_row(self, elements):

        f = open("something.txt", "a")
        s = ",".join(list(map(lambda x: str(x), elements)))
        f.write(s)
        f.write("\n")

o = FileHandling()
o.file_handle()





