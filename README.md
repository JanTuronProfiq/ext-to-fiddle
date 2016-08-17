# Merge all ExtJS project files to one

This can be very useful when you want to show your project at https://fiddle.sencha.com/#home

## Usage
```
python merge.py path/to/my/root/folder
```

```
optional arguments:
  -h, --help            show this help message and exit
  -v, --verbose         Print additional info
  -nrc                  Do not remove SA comments
  -o OUTPUT, --output OUTPUT
                        Define the output file, output.js is default
```

### Requirements
- python3


##### TODO
- Create Fiddle connector (automatic upload)
- Create NodeJS version