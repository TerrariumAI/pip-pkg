## Example usage
```
import random
from terrariumai import connectRemoteModel, createAction

def randomAction():
    return random.randint(0, 1)
def randomDirection():
    return random.randint(0, 3)

def modelFunc(obsv):
    action = createAction(obsv.id, randomAction(), randomDirection())
    return action


connectRemoteModel(
  # Find your secret key in your dashboard at http://terrarium.ai
  secret='secret-key', 
  modelFunc=modelFunc, 
)
```

## Converting Compiled gRPC Files
When gRPC files are compiled into this package, they need to be edited slightly in order to fit in.  
The import at the top of ```collective_pb2_grpc.py``` must be changed to  

```from . import collective_pb2 as collective__pb2```  

This is because of the way python 3 handles relative imports.  
Any kind of workaround would be appreciated, this is super annoying!