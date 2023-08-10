const fs = require('fs')
const path = require('path')

class JS {
    constructor() {

        this.NOTE = null

        this.sendNoteToPy = (note_object, path) => {
            try {
                fs.writeFileSync(path, JSON.stringify(note_object))
            }
            catch (err) {
                console.info(err.message)
            }
        }

        this.getNoteFromPy = (path) => {
            try {
                let note_from_py = JSON.parse(fs.readFileSync(path))
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
                    const note_path = path
        
                    while (!got_note) {
                        if (fs.existsSync(note_path)) {
                            let note = this.getNoteFromPy(note_path)
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

const js = new JS()
if (js.checkForNote("note_from_py.json")) {
    console.log("Got the note from Python!!!")
}

// Example usage
// sendNoteToPy({
//     "name": "javascript",
//     "text": "Hello Python!"
// }, "note_from_js.json")

//console.info(getNoteFromPy())
