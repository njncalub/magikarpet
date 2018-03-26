# magikarpet
Carpet inventory system using [Polygon 3](https://www.j-raedler.de/projects/polygon/) and [MongoDB](https://www.mongodb.com/download-center).

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

### Description
1. To add a new carpet to the inventory, create a new document with a "status" of "new". You can also specify the "carpet_type". The "dimensions" is an array of point tuples and will default to 100m x 100m.
2. To cut from a roll of carpet, we need to get the difference of two 2D polygons (p-q). This can be done using [Polygon 3](https://www.j-raedler.de/projects/polygon/). The resulting array of point tuples will then be stored as the new "dimensions" of the document and the "status" will be changed to "cut".
3. We need to iterate through all the carpets with a "status" of "cut" until we can find one that meets the requirement (e.g. a 85m x 85m rectangle should fit inside the bigger polygon). If there are no "cut" carpets left to choose from, we will then loop through all the "new" carpets. If there are still none, we can call the restock() method.

### Requirements
* Python >=3.5.x
* MongoDB >=3.6.x

### Recommended
I recommend installing the [pyenv](https://github.com/pyenv/pyenv) to make your life easier.

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

### Things To Do
* Cutting the Carpet works but it still cuts even if the area is very little.
    * Need to modify carpet.fits()
* Write unit tests.

### Licensing
MIT. Take, adapt, use. A link back to this repo is appreciated.
