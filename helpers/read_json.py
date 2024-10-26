import json

def read_json(file_path):
    """
    Reads JSON data from a file and returns it as a Python dictionary.

    :param file_path: str, path to the JSON file
    :return: dict, the data read from the JSON file
    """
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except json.JSONDecodeError:
        print(f"Error: Failed to decode JSON from the file '{file_path}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")