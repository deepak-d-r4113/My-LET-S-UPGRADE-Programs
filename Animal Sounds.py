# Step 1: Create a base class Animal with a method make_sound().
class Animal:
    def make_sound(self):
        print("Generic animal sound")

# Step 2: Create two subclasses Dog and Cat, each inheriting from the Animal class.
class Dog(Animal):
    def make_sound(self):
        super().make_sound()  # Calling the base class's make_sound() method
        print("Bark!")

class Cat(Animal):
    def make_sound(self):
        super().make_sound()  # Calling the base class's make_sound() method
        print("Meow!")

# Step 4: Implement a function called animal_sound_in_zoo() that takes an animal object as a parameter and calls its make_sound() method.
def animal_sound_in_zoo(animal):
    animal.make_sound()

# Step 5: Create instances of Dog and Cat classes and call the animal_sound_in_zoo() function with these instances as arguments to observe their unique sounds.
if __name__ == "__main__":
    dog_instance = Dog()
    cat_instance = Cat()

    print("Dog in the zoo:")
    animal_sound_in_zoo(dog_instance)

    print("\nCat in the zoo:")
    animal_sound_in_zoo(cat_instance)
