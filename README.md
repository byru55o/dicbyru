# dicbyru
## Introduction
Generates password lists/dictionaries based on keywords. It uses the keywords and adds capital letters, numbers and special characters to create possible passwords. These passwords are stored in a file with universal formatting, in order to be read and used by a brute-force program such as hydra.  

## Usage
- Run the script with the `python3` interpreter installed on your system:  
For linux-based systems:
```
python3 dicbyru.py
```
For Windows:  
```
python dicbyru.py
```  
- After that, its all pretty self-explanatory, enter the output, keywords and other options when prompted.  

## Options
#### Output
The file where the dictionary will be stored.
#### Keywords
The strings, separated by a `,` that are used to generate the possible passwords.  
**NOTE:** a space after the `,` is **not** needed: `password,pass,mayonnaise`
#### Auto caps
If _auto caps_ equals `1`, every keyword will be reproduced with the firt character in uppercase **and** also with every character in uppercase.
#### Max number
The highest number that is added to a keyword: > if maxnumber 2: `keyword0,keyword1,keyword2`.
#### Special chars
If _special chars_ equals `1`, each of the special characters `,`,`,`,`!`,`?`,`#`,`$`,`@`,`+`,`*`,`=` and `%` will be added to the end of the keyword.

## Dependencies
- PyFiglet:
```
pip install pyfiglet
```
- Colorama:
```
pip install colorama
```

## Additional info
Please, if you encounter a bug, or have a suggestion, report it to [issues](https://github.com/byru55o/dicbyru/issues) or create a [pull request](https://github.com/byru55o/dicbyru/pulls)  
This program was made by [ru55o](https://github.com/byru55o) using [Pop!\_OS](https://pop.system76.com/) and [Gentoo Linux](https://gentoo.org/) machines and [PyCharm](https://www.jetbrains.com/pycharm/) and [micro](https://micro-editor.github.io/) as IDE/editors.  
It is licensed under the GPL (3.0) and is thus _free software_.
