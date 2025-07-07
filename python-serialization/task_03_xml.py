import xml.etree.ElementTree as ET

def serialize_to_xml(dictionary, filename):
    """
    Serialize a Python dictionary to an XML file.

    Parameters:
    dictionary (dict): The dictionary to serialize.
    filename (str): The filename of the output XML file.
    """
    root = ET.Element("data")

    for key, value in dictionary.items():
        child = ET.Element(key)
        child.text = str(value)
        root.append(child)

    tree = ET.ElementTree(root)
    tree.write(filename)

def deserialize_from_xml(filename):
    """
    Deserialize an XML file to a Python dictionary.

    Parameters:
    filename (str): The filename of the input XML file.

    Returns:
    dict: The deserialized dictionary.
    """
    try:
        tree = ET.parse(filename)
        root = tree.getroot()
        return {child.tag: child.text for child in root}
    except Exception as e:
        print(f"Error deserializing XML file: {e}")
        return None

# Sample Test
if __name__ == "__main__":
    sample_dict = {
        'name': 'John',
        'age': '28',
        'city': 'New York'
    }

    xml_file = "data.xml"
    serialize_to_xml(sample_dict, xml_file)
    print(f"Dictionary serialized to {xml_file}")

    deserialized_data = deserialize_from_xml(xml_file)
    print("\nDeserialized Data:")
    print(deserialized_data)
