class Person:
    """The base 'package' for all hospital entities - think of this as our python3-minimal installation"""
    
    def __init__(self, name: str, age: int):
        self._name = name  # Protected attribute (like a sudo-protected file)
        self._age = age
    
    @property
    def name(self):
        """Encapsulation in action! This is your sudo permission to read name"""
        return self._name
    
    @name.setter
    def name(self, value):
        """Now THAT'S proper encapsulation - no root access needed!"""
        if not value:
            raise ValueError("Name cannot be empty - this isn't a /dev/null entry!")
        self._name = value