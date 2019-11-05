# translateVoid

Very simple sentence/comment/post/string processing script that will re-generate the input with mixed characters in order to circumvent common "Translate" functions on the Internet.

```
usage: translateVoid.py [-h] [-s SENTENCE] [-c] [-r]

Welcome to translateVoid.py

optional arguments:
  -h, --help            show this help message and exit
  -s SENTENCE, --string SENTENCE
                        Passing an escaped strings
  -c, --clipboard       Grab a string from the clipboard
  -r, --reverse         Substitute characters from string based on cyrilic
                        characters
```

# Installation

Installation is done via the Makefile.

```
sudo make install
```

and it can be promptly un-installed via `clean`

```
sudo make clean
```

# Usage 

```
!?master ~/translateVoid $ translateVoid -r -s "Това е за тест"
ТoBa e зa TecT
!?master ~/translateVoid $ translateVoid -s "This is a test"
Тhis is а tеst
```

# To do:

- Add a `Grab from clipboard` functionality
- Create a cross platform simple GUI

