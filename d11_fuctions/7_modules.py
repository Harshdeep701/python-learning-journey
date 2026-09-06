 #Two types of modules in Python:
#-build in modules
#- External modules
import math # built in modules
import mymdule
import requests
print(math.sqrt(16)) #.sqrt is the built in function in python 
#Notice it returns 4.0 (a float), not 4 (an integer), because sqrt in Python always gives a floating-point number.

# List of all built in modules: https://docs.python.org/3/py-modindex.html

import os
os.abort
mymdule.hello()
r =requests.get("https://google.com")
print(r.text)