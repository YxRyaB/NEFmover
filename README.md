#The script for the distribution of catalogs digital negative "NEF"
The script for the distribution of "Digital Negative Specification", namely "NEF" - which is used exclusively with cameras Nikon.
#Options
```
Usage: NEFmover.py [options] arg1 ...

Options:
  -h, --help            show this help message and exit
  -d PATH_TO_DIR, --dir=PATH_TO_DIR
                        The directory path to digital negatives (NEF)(default:
                        path to script)
  -p PREFIX, --prefix=PREFIX
                        Prefix applicable to similar files (default : date and
                        time_{ file })
```
#NEFmover.rar
The script is compiled for Windows users.
#Example:
##Before
```
.
├── test1
│   ├── 1.jpg
│   └── 1.NEF
├── test2
│   ├── 1.jpg
│   ├── 1.NEF
│   └── NEF
│       └── 1.NEF
└── test3
    ├── 1.jpg
    ├── 1.NEF
    └── NEF
        ├── 1.NEF
        └── new_1.NEF
```
##After
```
.
├── test1
│   ├── 1.jpg
│   └── NEF
│       └── 1.NEF
├── test2
│   ├── 1.jpg
│   └── NEF
│       ├── 1.NEF
│       └── 2015-08-03 11:38_1.NEF
└── test3
    ├── 1.jpg
    └── NEF
        ├── 1.NEF
        ├── new_2015-08-03 11:38_1.NEF
        └── new_1.NEF
```