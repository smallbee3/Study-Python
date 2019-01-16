class Test:
    test23 = "static"

    def __init__(self):
        pass

    @classmethod
    def test(cls):
        return "hello"

    @property
    def test3(self):

        return self.test() + self.test2()

    def test2(self):
        return "hi"


# 1) class method test
print(Test.test())

# 2) instance method cannot be access through Class because it lacks 'self' parameter
# Test.test2()

# 3) @property test
# Test.test3() # -> TypeError: 'property' object is not callable
print(Test.test3)  # -> Just address <property object at 0x10d79ff48>

t1 = Test()
print(t1.test3)  # -> hellohi
