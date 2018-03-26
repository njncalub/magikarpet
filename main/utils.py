from .models import (
    Acrylic,
    Fiber,
    Nylon,
    Wool,
)

def populate_collection(collection):
    # TODO: use random.randint and random.choice here
    
    acrylic = [Acrylic().as_dict() for _ in range(1)]
    fiber = [Fiber().as_dict() for _ in range(1)]
    nylon = [Nylon().as_dict() for _ in range(2)]
    wool = [Wool().as_dict() for _ in range(2)]
    
    # add a "cut" carpet
    nylon.append(Nylon(
        dimensions=[
          [0, 100],
          [100, 100],
          [100, 0],
          [50, 0],
          [50, 50],
          [0, 50],
          [0, 100],
        ],
        status="cut"
    ).as_dict())
    
    carpets = acrylic + fiber + nylon + wool
    
    collection.insert_many(carpets)


def purge_collection(collection):
    collection.remove( { } )
