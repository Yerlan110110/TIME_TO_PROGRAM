class Dog:
    def send_bark(self):
        print("WOOF I'm a bit you")
layka = Dog()
layka.send_bark()
Dog.send_bark(Dog())
