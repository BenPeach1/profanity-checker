# Python Profanity Checker

This is a simple Python application that reads a source text file and then subsequently passes it into a Google site that check's for profanity.

## Input / Source

- The input text for the profanity checker is added in the _**profanity-check.txt**_ file.
- This file is stored locally in the project directory (e.g., /Users/[name]/Documents/Udacity/Projects/intro-to-python/profanity-checker/source/profanity-check.txt)

## Output

Depending on the presence or absence of profanity in the source text file, the output of this program (via customizable message), will display one of the three following outcomes:
- Profanity identified
- No profanity identified
- Source file could not be read

These output messages can be customized by modifying the string within the print() command in the code snippet below:
```
if b"true" in output:
        print("Slow down buddy, this has some profanity in it!")
    elif b"false" in output:
        print("Carry on my friend, you're profanity free!")
    else:
        print("Houston, we have a problem --- we couldn't read your document")
```
