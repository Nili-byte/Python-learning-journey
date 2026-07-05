
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


