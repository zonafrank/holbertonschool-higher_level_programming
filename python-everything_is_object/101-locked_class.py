#!/usr/bin/python3
class LockedClass:
    """A class that prevents dynamic attribute creation, except for 'first_name'."""
    __slots__ = ["first_name"]

    def __setattr__(self, name, value):
        """Restrict attribute creation to 'first_name'."""
        if name == "first_name":
            super().__setattr__(name, value)
        else:
            raise AttributeError(f"object has no attribute {name}")
