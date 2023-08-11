const fs = require('fs')
const path = require('path')

class JS {
    /**
     * Creates a Json file with the given object to be picked up 
     * by the Python Py object. 
     */
    constructor() {

        this.NOTE = null
        this.JSON_PATH = null

        this.sendNoteToPy = (note_object, path) => {
            try {
                fs.writeFileSync(path, JSON.stringify(note_object))
            }
            catch (err) {
                console.info(err.message)
            }
        }

        this.getNoteFromPy = () => {
            try {
                let note_from_py = JSON.parse(fs.readFileSync(this.JSON_PATH))
                return note_from_py
            }
            catch(err) {
                console.info(err.message)
            }
        }

        this.checkForNote = (path) => {
            if (path) {
                try {
                    let got_note = false
                    const note_path = path + '/' + "note_from_py.json"
                    this.JSON_PATH = note_path
        
                    while (!got_note) {
                        if (fs.existsSync(note_path)) {
                            let note = this.getNoteFromPy()
                            this.NOTE = note
                            got_note = true;
                        } else {
                            console.log('Checking ...')
                        }
                    }
                    return true
                } catch (error) {
                    console.error(error)
                    return null
                }
            }
        }
    }
};

//Example usage

// Listen for and get an object from JS. 

// const js = new JS()
// if (js.checkForNote(".")) {
//     console.log("Data available!!!")
//     console.log(js.NOTE)
// }

// Send an object to JS.

// js.sendNoteToPy({
//     "name": "javascript",
//     "text": "Hello Python!"
// }, "note_from_js.json")

