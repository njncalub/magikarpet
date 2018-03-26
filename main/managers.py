from Polygon.Shapes import Rectangle

from main.factories import CarpetFactory


class CarpetManager(object):
    """
    Class to magage the Carpets.
    """
    
    factory = CarpetFactory()
    
    def __init__(self, objects, *args, **kwargs):
        self.objects = objects
    
    def find_all(self, criteria=None):
        """
        Return all carpets by criteria.
        """
        if not criteria: criteria = {}
        
        return (
            self.factory.create(record)
            for record in self.objects.find(criteria)
        )
    
    def get_new_carpets(self, carpet_type=None):
        """
        Return all carpets by type.
        """
        query_string = {"status": "new"}
        if carpet_type:
            query_string["carpet_type"] = carpet_type
        
        return self.find_all(query_string)
    
    def get_cut_carpets(self, carpet_type=None):
        """
        Return all carpets by type.
        """
        query_string = {"status": "cut"}
        if carpet_type:
            query_string["carpet_type"] = carpet_type
        
        return self.find_all(query_string)
    
    def get_carpet_for_cutting(self, carpet_type, side1, side2):
        """
        Return a carpet that can be used for the order.
        """
        
        cut_carpets = self.get_cut_carpets(carpet_type)
        for cut_carpet in cut_carpets:
            # check if client_order will fit
            # otherwise, repeat until generator is exhausted
            if cut_carpet.fits(side1, side2):
                return cut_carpet
        
        new_carpets = self.get_new_carpets(carpet_type)
        new_carpet = None
        for new_carpet in cut_carpets:
            return new_carpet  # return first carpet in generator
        
        if not new_carpet:
            print(f"No more '{carpet_type}' carpet(s).")
            self.restock(carpet_type)
            
            return None
    
    def restock(self, carpet_type, quantity=1):
        """
        Create a new Carpet and save it to the database session.
        """
        
        print(f"Restocking {quantity} '{carpet_type}' carpet(s).")
        
        new_carpet = self.factory.create(carpet_type=carpet_type)
        for _ in range(quantity):
            self.objects.insert_one(new_carpet.as_dict())
