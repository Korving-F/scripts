# Scripts, Configs etc.

### hibpwned.py
This script checks the [pwned passwords API](https://haveibeenpwned.com/API/v2) by haveibeenpwned.com for compromised passwords.
 ``` bash
$ python hibpwned.py $PWD
 ```

### euribor
Calls API for current EURIBOR rates

### emacs
Personal config files for emacs, to be used in combination with prelude.

 ``` bash
$ git clone git@github.com:Korving-F/scripts-configs.git
$ cp scripts-configs/emacs/* ~/.emacs.d/personal/
 ```

### GPG Converter
Meh script to convert GPG keys produced by QtPass to CSV file for import into 3rd party password manager. Also an excuse to learn about click / jinja2 etc.
``` bash
$ python converter.py --help
```

