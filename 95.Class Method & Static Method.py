class Counter:
    count = 0
    
    @classmethod
    def increment(cls):
        cls.count += 1
    
    @staticmethod
    def utility_message():
        print("This is a utility message.")

Counter.increment()
Counter.increment()
print(Counter.count)
Counter.utility_message()