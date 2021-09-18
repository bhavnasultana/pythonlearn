import time

def mydecorator(fn):
    def innerfunction():
        initial_value = time.time()
        fn()
        final_value = time.time()
        print("time taken by my function", final_value - initial_value)
    return innerfunction

@mydecorator
def hello_world():
    print("saying hello world and then sleeping")
    time.sleep(2)

if __name__ == "__main__":
    hello_world()



