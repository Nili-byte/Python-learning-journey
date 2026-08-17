
def step(Maal):
    def start():
        print("WE WOKE")
        Maal()
        print("WE SLEEP")
    return start




@step
def grind():
    print("WE GRIND")


grind()


def start(func):
    def wrap():
        print("Salam")
        func()
        print("walekum salam")

    return wrap





@start
def f():
    print("wassup")


f()




