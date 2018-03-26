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
```

### Sample Output
```
Listing all carpets in inventory:
- [5ab8c2c1921fdb50b9c16617] new acrylic: [[0, 100], [100, 100], [100, 0], [0, 0], [0, 100]]
- [5ab8c2c1921fdb50b9c16618] new fiber: [[0, 100], [100, 100], [100, 0], [0, 0], [0, 100]]
- [5ab8c2c1921fdb50b9c16619] new nylon: [[0, 100], [100, 100], [100, 0], [0, 0], [0, 100]]
- [5ab8c2c1921fdb50b9c1661a] new nylon: [[0, 100], [100, 100], [100, 0], [0, 0], [0, 100]]
- [5ab8c2c1921fdb50b9c1661b] cut nylon: [[0, 100], [100, 100], [100, 0], [50, 0], [50, 50], [0, 50], [0, 100]]
- [5ab8c2c1921fdb50b9c1661c] new wool: [[0, 100], [100, 100], [100, 0], [0, 0], [0, 100]]
- [5ab8c2c1921fdb50b9c1661d] new wool: [[0, 100], [100, 100], [100, 0], [0, 0], [0, 100]]
----------------------------------------------------------------------------------------------------
Finding all 'nylon' carpets in stock:
- [5ab8c2c1921fdb50b9c16619] new nylon: [[0, 100], [100, 100], [100, 0], [0, 0], [0, 100]]
- [5ab8c2c1921fdb50b9c1661a] new nylon: [[0, 100], [100, 100], [100, 0], [0, 0], [0, 100]]
- [5ab8c2c1921fdb50b9c1661b] cut nylon: [[0, 100], [100, 100], [100, 0], [50, 0], [50, 50], [0, 50], [0, 100]]
----------------------------------------------------------------------------------------------------
Finding all new 'nylon' carpets in stock:
- [5ab8c2c1921fdb50b9c16619] new nylon: [[0, 100], [100, 100], [100, 0], [0, 0], [0, 100]]
- [5ab8c2c1921fdb50b9c1661a] new nylon: [[0, 100], [100, 100], [100, 0], [0, 0], [0, 100]]
----------------------------------------------------------------------------------------------------
Finding all cut 'nylon' carpets in stock:
- [5ab8c2c1921fdb50b9c1661b] cut nylon: [[0, 100], [100, 100], [100, 0], [50, 0], [50, 50], [0, 50], [0, 100]]
----------------------------------------------------------------------------------------------------
Finding a 'nylon' carpet that will fit an 85x85 order:
- [5ab8c2c1921fdb50b9c1661b] cut nylon: [[0, 100], [100, 100], [100, 0], [50, 0], [50, 50], [0, 50], [0, 100]]
----------------------------------------------------------------------------------------------------
Cutting a 'nylon' carpet that will fit an 85x85 order:
Generated carpet image at generated/c77766a2-56d1-44db-bf10-d55d7d4c5290.svg.
----------------------------------------------------------------------------------------------------
Adding additional 'nylon' carpets to the inventory:
Restocking 5 'nylon' carpet(s).
----------------------------------------------------------------------------------------------------
Listing all carpets in inventory:
- [5ab8c2c1921fdb50b9c16617] new acrylic: [[0, 100], [100, 100], [100, 0], [0, 0], [0, 100]]
- [5ab8c2c1921fdb50b9c16618] new fiber: [[0, 100], [100, 100], [100, 0], [0, 0], [0, 100]]
- [5ab8c2c1921fdb50b9c16619] new nylon: [[0, 100], [100, 100], [100, 0], [0, 0], [0, 100]]
- [5ab8c2c1921fdb50b9c1661a] new nylon: [[0, 100], [100, 100], [100, 0], [0, 0], [0, 100]]
- [5ab8c2c1921fdb50b9c1661b] cut nylon: [[100.0, 0.0], [85.0, 0.0], [85.0, 85.0], [0.0, 85.0], [0.0, 100.0], [100.0, 100.0]]
- [5ab8c2c1921fdb50b9c1661c] new wool: [[0, 100], [100, 100], [100, 0], [0, 0], [0, 100]]
- [5ab8c2c1921fdb50b9c1661d] new wool: [[0, 100], [100, 100], [100, 0], [0, 0], [0, 100]]
- [5ab8c2c1921fdb50b9c1661e] new nylon: [[0, 100], [100, 100], [100, 0], [0, 0], [0, 100]]
- [5ab8c2c1921fdb50b9c1661f] new nylon: [[0, 100], [100, 100], [100, 0], [0, 0], [0, 100]]
- [5ab8c2c1921fdb50b9c16620] new nylon: [[0, 100], [100, 100], [100, 0], [0, 0], [0, 100]]
- [5ab8c2c1921fdb50b9c16621] new nylon: [[0, 100], [100, 100], [100, 0], [0, 0], [0, 100]]
- [5ab8c2c1921fdb50b9c16622] new nylon: [[0, 100], [100, 100], [100, 0], [0, 0], [0, 100]]
----------------------------------------------------------------------------------------------------
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

### Things To Do
* Cutting the Carpet works but it still cuts even if the area is very little.
    * Need to modify carpet.fits()
* Write unit tests.

### Licensing
MIT. Take, adapt, use. A link back to this repo is appreciated.
