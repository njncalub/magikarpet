from uuid import uuid4

from Polygon import Polygon
from Polygon.IO import writeSVG
from Polygon.Shapes import Rectangle


def generate_uuid():
   return str(uuid4())


class Carpet(object):
    """
    Base model for all carpets.
    """
    
    DEFAULT_DIMENSIONS = [
      (0, 100),
      (100, 100),
      (100, 0),
      (0, 0),
      (0, 100),
    ]
    
    def __init__(self, carpet_type, dimensions=None, status="new", _id=None,
                 *args, **kwargs):
        if not dimensions:
            dimensions = self.DEFAULT_DIMENSIONS
        
        self._id = _id
        self.carpet_type = carpet_type
        self.dimensions = dimensions
        self.status = status
    
    def as_dict(self):
        return {
            "carpet_type": self.carpet_type,
            "dimensions": self.dimensions,
            "status": self.status,
        }
    
    def pretty_print(self):
        return f"[{self._id}] {self.status} {self.carpet_type}: " + \
               f"{self.dimensions}"
    
    def pointify(self, polygon):
        """
        Convert Polygon back to points.
        """
        
        return tuple(polygon)[0]
    
    def fits(self, x, y, with_orientation=None):
        """
        Check if the rectangle fits in the current carpet.
        """
        
        will_fit = False
        orientation = None
        
        if self.polygon.isInside(x, y):
            will_fit = True
            orientation = "xy"
        if self.polygon.isInside(y, x):
            will_fit = True
            orientation = "yx"
        
        if with_orientation:
            return will_fit, orientation
        
        return will_fit
    
    def cut(self, x, y):
        """
        Cut an area from the Carpet.
        
        Restrictions:
        - @x and @y must be greater than 0.
        - @x and @y should fit inside the current Carpet.
        """
        successful = False
        
        will_fit, orientation = self.fits(x, y, with_orientation=True)
        if will_fit and orientation is "xy":
            self.dimensions = self.pointify(self.polygon - Rectangle(x, y))
            self.status = "cut"
            successful = True
        elif will_fit and orientation is "yx":
            self.dimensions = self.pointify(self.polygon - Rectangle(y, x))
            self.status = "cut"
            successful = True
        else:
            print("Will not fit. Aborting.")
        
        return successful
    
    def save(self, collections):
        """
        Save to the database.
        """
        collections.update_one({
          '_id': self._id
        }, {
          '$set': {
            'dimensions': self.dimensions,
            'status': self.status,
          }
        }, upsert=False)
    
    def save_image(self):
        """
        Save to SVG file.
        """
        file_name = f'generated/{generate_uuid()}.svg'
        writeSVG(file_name, (self.polygon,))
    
    @property
    def polygon(self):
        """
        Returns a Polygon3 Polygon.
        """
        return Polygon(self.dimensions)
    
    @property
    def area(self):
        """
        Returns the area of the contour.
        """
        return Polygon(self.dimensions).area()

class Wool(Carpet):
    """
    Model for a Wool carpet.
    """
    
    TYPE = "wool"
    
    def __init__(self, *args, **kwargs):
        super().__init__(self.TYPE, *args, **kwargs)


class Nylon(Carpet):
    """
    Model for a Nylon carpet.
    """
    
    TYPE = "nylon"
    
    def __init__(self, *args, **kwargs):
        super().__init__(self.TYPE, *args, **kwargs)


class Fiber(Carpet):
    """
    Model for a Fiber carpet.
    """
    
    TYPE = "fiber"
    
    def __init__(self, *args, **kwargs):
        super().__init__(self.TYPE, *args, **kwargs)


class Acrylic(Carpet):
    """
    Model for an Acrylic carpet.
    """
    
    TYPE = "acrylic"
    
    def __init__(self, *args, **kwargs):
        super().__init__(self.TYPE, *args, **kwargs)

