from main.models import Acrylic, Carpet, Fiber, Nylon, Wool


class CarpetFactory(object):
    """
    Class to create Carpet objects.
    """
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    def create(self, record=None, carpet_type="default"):
        """
        Create the Appropriate object based on carpet_type.
        """
        models = {
            "acrylic": Acrylic,
            "fiber": Fiber,
            "nylon": Nylon,
            "wool": Wool,
            "default": Carpet,
        }
        
        # If no record was passed, create a new one with carpet_type.
        if not record:
            return models[carpet_type]()
        
        carpet_type = record.pop("carpet_type")
        return models[carpet_type](**record)
