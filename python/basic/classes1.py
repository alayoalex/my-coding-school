# @classmethod vs @staticmethod vs "plain" methods
# What's the difference?

class MyClass:
    def method(self):
        """
        Instance methods need a class instance and
        can access the instance through `self`.
        """
        return 'instance method called', self

    @classmethod
    def classmethod(cls):
        """
        Class methods don't need a class instance.
        They can't access the instance (self) but
        they have access to the class itself via `cls`.
        """
        return 'class method called', cls

    @staticmethod
    def staticmethod():
        """
        Static methods don't have access to `cls` or `self`.
        They work like regular functions but belong to
        the class's namespace.
        """
        return 'static method called'


# All methods types can be
# called on a class instance:
obj = MyClass()
print(obj.method())
print(obj.classmethod())
print(obj.staticmethod())

# Calling instance methods fails
# if we only have the class object:
print(MyClass.classmethod())
print(MyClass.staticmethod())
print(MyClass.method())   #wrong
print(MyClass.method(obj))   #righ