"""
This class demonstrates the differences between a
class method, static method and an instance method
More particularly, static and class method appears to be same

A class can declare class variables(i.e, static variables shared by all objects)
and instance variables. (specific to each object)

"""
class Person:
    species = "Homo sapiens"  # Class variable
    population = 0  # Class variable to track total people

    def __init__(self, name, age):
        self.name = name  # Instance variable
        self.age = age  # Instance variable
        Person.population += 1  # Increment when new person is created

    # STATIC METHOD - doesn't receive self or cls
    @staticmethod
    def is_adult(age):
        """Check if someone is an adult based on age alone"""
        return age >= 18

    # CLASS METHOD - receives cls (the class itself)
    @classmethod
    def get_species(cls):
        """Get the species - accesses class variable"""
        return cls.species

    @classmethod
    def get_population(cls):
        """Get total population - accesses class variable"""
        return cls.population

    @classmethod
    def create_baby(cls, name):
        """Alternative constructor to create a baby (age 0)"""
        return cls(name, 0)  # cls refers to the Person class

    # Regular instance method for comparison
    def introduce(self):
        return f"Hi, I'm {self.name} and I'm {self.age} years old"


# Examples of usage:

print("=== STATIC METHOD EXAMPLES ===")
# Static method - can call on class or instance, doesn't need either
print(Person.is_adult(25))  # True - called on class
print(Person.is_adult(15))  # False - called on class

person1 = Person("Alice", 30)
print(person1.is_adult(20))  # True - called on instance (but doesn't use instance data)

print("\n=== CLASS METHOD EXAMPLES ===")
# Class method - receives the class as first argument
print(Person.get_species())  # "Homo sapiens" - accesses class variable
print(Person.get_population())  # 1 - shows current population

# Class method as alternative constructor
baby = Person.create_baby("Bob")  # Creates Person("Bob", 0)
print(baby.introduce())  # "Hi, I'm Bob and I'm 0 years old"
print(Person.get_population())  # 2 - population increased

print("\n=== KEY DIFFERENCES DEMONSTRATION ===")

# Static method: Cannot access class or instance variables
# This would cause an error in a static method:
# @staticmethod
# def bad_static():
#     return self.name        # ERROR: no 'self'
#     return cls.species      # ERROR: no 'cls'
#     return Person.species   # OK: can access by explicit class name

# Class method: Can access class variables and create instances
print("Species via class method:", Person.get_species())

# Both can be called on class or instance
person2 = Person("Charlie", 25)
print("Static method via instance:", person2.is_adult(30))
print("Class method via instance:", person2.get_species())

print(f"Final population: {Person.get_population()}")