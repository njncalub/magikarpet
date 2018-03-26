# magikarpet
Carpet inventory system using [Polygon 3](https://www.j-raedler.de/projects/polygon/) and [MongoDB](https://www.mongodb.com/download-center).

### Requirements
* Python >=3.5.x
* MongoDB >=3.6.x

### Recommended
I recommend installing the following version managers to make your life easier:
* [pyenv](https://github.com/pyenv/pyenv)

### Running
```
# navigate to the project directory
$ cd <project directory>/

# install dependencies
$ pip install -r requirements/local.txt

# make sure mongodb is running
$ mongod

# run the program
$ ./app.py

# check generated image
$ open generated/
```

### Carpet Document Schema
```
{
    "_id"          : ObjectId("123456789abcdef"),
    "carpet_type"  : "wool",
    "status"       : "new"
    "dimensions"   : [ [ 0, 100 ],
                       [ 100, 100 ],
                       [ 100, 0 ],
                       [ 0, 0 ],
                       [ 0, 100 ]
    ]
}
```

### Licensing
MIT. Take, adapt, use. A link back to this repo is appreciated.
