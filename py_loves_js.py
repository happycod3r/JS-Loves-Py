import json
import os

class Py:
    def __init__(self) -> None:
        self.NOTE = None
        self.JSON_PATH = None
    
    def send_note_to_js(self, note_object: dict, path: str):
        try:
            with open(path, 'x') as note:
                json.dump(note_object, note)
                note.close()
        except FileNotFoundError as e:
            print(repr(e))
        except IOError as e:
            print(repr(e))

    def get_note_from_js(self) -> (dict | None):
        try:
            with open(self.JSON_PATH, "r") as note:
                note_data = json.load(note)
                note.close()
                return note_data
        except FileNotFoundError as e:
            print(repr(e))
            return None
        except IOError as e:
            print(repr(e))
            return None
        except TypeError as e:
            print(repr(e))
            return None
            
    def check_for_note(self, path: str) -> (bool | None):
        """
        Watches the folder specified by path for the existence of
        a file specified by file by recursively checking for its 
        existence.  
        """
        try:
            got_note = False
            note_path = os.path.join(path, "note_from_js.json")
            self.JSON_PATH = note_path
            print(note_path)
            while not got_note:
                if os.path.exists(note_path):
                    note = self.get_note_from_js()
                    self.NOTE = note
                    got_note = True
                else: print("Checking ...")
            return True
        except TypeError as e:
            print(repr(e))
            return False

py = Py()

if py.check_for_note("."):
    print("Data available!")
    print(py.NOTE)

# py.send_note_to_js({
#     "name": "python",
#     "text": "Hello JavaScript!"
# }, "note_from_py.json")
