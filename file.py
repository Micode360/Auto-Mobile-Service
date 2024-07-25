import json
import os


# Super class
class File:
    @staticmethod
    def save_to_file(data, filename):
        if not os.path.exists('store'):
            os.makedirs('store')
            
        with open(filename, 'w') as file: # with statement makes sure the file is opened and closed properly
            json.dump(data, file, indent=4) # A function that converts lists or dictionaries into json file and dump it in a file
            # indent=4 means the JSON data will be formatted with an indentation of 4 spaces, making it easier to read

        print(f"Data saved to {filename}") 
     
    @staticmethod
    def load_from_file(filename):
        try: # Exceptional Handling
            with open(filename, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            print(f"file not found {filename}")
            return []
        except json.JSONDecodeError:
            print(f"There is an error decoding the json file structure at {filename}")
            return []

    @staticmethod
    def delete_file(filename):
        if os.path.exists(filename):
            os.remove(filename)
            print(f"{filename} has been deleted.")
        else:
            print(f"{filename} does not exist.")