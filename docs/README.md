# JS ❤️ PY

> JS Loves Py is a set of scripts that will allow you to easily pass data back and forth between JavaScript and Python using Json.

## [Table Of Contents](#table-of-contents)

- [Table of Contents](#table-of-contents)
- [About](#about)
- [Contributing](#contributing)
- [Security](#security)
- [Contacts](#contacts)
---

# [About](#about)
JS loves Py contains two classes. One in JavaScript called `JS()` and the other in Python call `Py()`. These two classes are identical other than the fact that one is written in Python and the other in JavaScript. Both classes allow you to pass an object back and forth between Python and JavaScript easily using Json. Each class creates a Json file which it will store the data being passed in. The Json files created by both classes are called `from_js.json` and `from_py.json` respectively.

Since Json, a JavaScript object and a Python dictionary are all written out the same this can be leveraged to easily pass objects back and forth between Python and JavaScript. On top of that you can create listeners to automate getting the data being passed as I have here with the `JS.checkForNote()` and `Py.check_for_note()` methods.
All you have to do is specify the path to the place where the ***from_js.json*** and ***from_py.json*** files will be created by passing it to whichever listener is being used or both.

[**Json (JavaScript Object Notation)**](#json)
```json
{
    "name": "json",
    "msg": "Hello, world I'm Json"
}
```
[**Python Dictionary {}**](#python-dict)
```python
note = {
    "name": "python",
    "msg": "Hello, world I'm Python"
}
```

[**JavaScript Object {}**](#javascript-object)
```javascript
let note = {
    "name": "javascript",
    "msg": "Hello, world I'm JavaScript"
}
```
---

## [Usage](#usage)

Both the `JS` and the `Py` classes have the exact same functionality and contain the same methods and properties as follows:

### [JS Class Methods](#js)
- `JS.NOTE` - This is where the retieved data from Py is stored
- `JS.PATH` - This will store the path passed to checkForNote()
- `JS.sendNoteToPy(note_object, path)`
- `JS.getNoteFromPy(path)`
- `JS.checkForNote(path)`


### [Py Class Methods](#py)
- `Py.NOTE` - This is where the retieved data from JS is stored
- `Py.PATH` - This will store the path passed to check_for_note()
- `Py.send_note_to_js(self, note_object: dict, path: str)`
- `Py.get_note_from_js(self, path: str)`
- `Py.check_for_note(self, path: str, file: str)`

---

To get an object from JavaScript to Python do the following:

1) In your Python program create a new instance of the **Py** class and then call the `check_for_note()` method passing in the path to watch and let it run.
```python
py = Py()
py.check_for_note("C:\\MyPyApp\\")
``` 
   
> \* NOTE * The `Py.check_for_note` and `JS.checkForNote` methods both have the ability to detect the object/dict being sent from one another, so you can have the `Py.checkForNote` or the `JS.checkForNote` method running already and when the object is sent and it will detect the json file, get the data object, and store it for you.


2) Now in your JavaScript program create a new instance of the **JS** class and then call the `sendNoteToPy()` method passing in the object containing whatever data you want as the first argument.
```javascript
const js = new JS()
sendNoteToPy({
     "title": "Note to Py from JS",
     "text": "Hello Python!"
}, "note_from_js.json")
```

Once the `sendNoteToPy()` method is called the object you passed in will be stored in the ***note_from_js.json*** file at the specified path and this will automatically be picked up on the Python side by the running `Py.check_for_note()` method from step 1. The data will be stored in `Py.NOTE` and accessible from there.

![Example Usage](./pyjsex.gif)

## [Contributing](#contributing)

If you have any feature requests, suggestions or general questions you can 
reach me via any of the methods listed below in the [Contacts](#contacts) section.

---

## [Security](#security)

### Reporting a vulnerability or bug?

**Do not submit an issue or pull request**: A general rule of thumb is to 
never publicly report bugs or vulnerabilities because you might inadvertently 
reveal it to unethical people who may use it for bad. Instead, you can email 
me directly at: [paulmccarthy676@gmail.com](mailto:paulmccarthy676@gmail.com). 
I will deal with the issue privately and submit a patch as soon as possible.

---

## [Contacts](#contacts)

**Author:** Paul M.

* Email: [paulmccarthy676@gmail.com](mailto:paulmccarthy676@gmail.com)
* Github: [https://github.com/happycod3r](https://github.com/happycod3r)
* Linkedin: [https://www.linkedin.com/in/paul-mccarthy-89165a269/]( https://www.linkedin.com/in/paul-mccarthy-89165a269/)
* Facebook: [https://www.facebook.com/paulebeatz]( https://www.facebook.com/paulebeatz)

---

