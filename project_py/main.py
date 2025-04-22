import gc

class ExampleClass:
    def __init__(self, name, value):
        self.name = name  # Public attribute
        self._value = value  # Protected attribute
        self.__secret = "This is private"  # Private attribute

    def public_method(self):
        """A public method."""
        return f"Public method called. Name: {self.name}, Value: {self._value}"

    def _protected_method(self):
        """A protected method."""
        return f"Protected method called. Value: {self._value}"

    def __private_method(self):
        """A private method."""
        return f"Private method called. Secret: {self.__secret}"

    def access_private_method(self):
        """Access the private method from within the class."""
        return self.__private_method()


class SubExampleClass(ExampleClass):
    def __init__(self, name, value, extra):
        super().__init__(name, value)
        self.extra = extra  # Additional attribute for the subclass

    def public_method(self):
        """Override the public method."""
        return f"Overridden public method. Name: {self.name}, Extra: {self.extra}"

    # Not overriding the _protected_method, so it will use the parent's implementation
    def access_protected_method(self):
        """Access the protected method from the subclass."""
        return self._protected_method()

    def access_private_method(self):
        """Attempt to access the private method from the subclass."""
        # Cannot directly access __private_method because it's name-mangled
        return "Cannot access private method directly from subclass."


# Example usage
if __name__ == "__main__":
    # Create an object of the parent class
    parent_obj = ExampleClass("ParentObject", 42)
    print(parent_obj.public_method())
    print(parent_obj._protected_method())
    print(parent_obj.access_private_method())

    # Create an object of the subclass
    child_obj = SubExampleClass("ChildObject", 99, "ExtraValue")
    print(child_obj.public_method())  # Calls the overridden method
    print(child_obj.access_protected_method())  # Accesses the inherited protected method
    print(child_obj.access_private_method())  # Demonstrates inability to directly access private method

    # Delete the objects and force garbage collection
    del parent_obj, child_obj
    gc.collect()
    print("Objects deleted and garbage collected.")