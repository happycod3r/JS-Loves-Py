import json
import os

class Py:
    def __init__(self) -> None:
        self.NOTE = None
    
    def send_note_to_js(self, note_object: dict, path: str):
        try:
            with open(path, 'x') as note:
                json.dump(note_object, note)
                note.close()
        except FileNotFoundError as e:
            print(repr(e))
        except IOError as e:
            print(repr(e))

    def get_note_from_js(self, path: str) -> (dict | None):
        note_from_js = path
        try:
            with open(note_from_js, "r") as note:
                note_text = json.load(note)
                note.close()
                return note_text
        except FileNotFoundError as e:
            print(repr(e))
            return None
        except IOError as e:
            print(repr(e))
            return None
            
    def check_for_note(self, path: str, file: str) -> (bool | None):
        """
        Watches the folder specified by path for the existence of
        a file specified by file by recursively checking for its 
        existence.  
        """
        try:
            got_note = False
            note_path = os.path.join(path, file)
            while not got_note:
                if os.path.exists(note_path):
                    note = self.get_note_from_js(note_path)
                    self.NOTE = note
                    got_note = True
                else: print("Checking ...")
            return True
        except TypeError as e:
            print(repr(e))
            return False

py = Py()

if py.check_for_note(".", "note_from_js.json"):
    print("Got the note from JavaScript!!!")

# py.send_note_to_js({
#     "name": "python",
#     "text": "Hello JavaScript!"
# }, "note_from_py.json")
