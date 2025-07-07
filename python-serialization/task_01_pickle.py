
import pickle

class CustomObject:
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Serialize the current instance to a file using pickle.

        Parameters:
        filename (str): The filename of the output pickle file.
        """
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self, file)
        except Exception as e:
            print(f"Error serializing object: {e}")

    @classmethod
    def deserialize(cls, filename):
        """
        Deserialize an instance from a file using pickle.

        Parameters:
        filename (str): The filename of the input pickle file.

        Returns:
        CustomObject: The deserialized instance, or None if an error occurs.
        """
        try:
            with open(filename, 'rb') as file:
                obj = pickle.load(file)
            return obj
        except Exception as e:
            print(f"Error deserializing object: {e}")
            return None

# Sample Test
if __name__ == "__main__":
    # Create an instance of CustomObject
    obj = CustomObject(name="John", age=25, is_student=True)
    print("Original Object:")
    obj.display()

    # Serialize the object
    obj.serialize("object.pkl")

    # Deserialize the object into a new instance
    new_obj = CustomObject.deserialize("object.pkl")
    if new_obj:
        print("\nDeserialized Object:")
        new_obj.display()
