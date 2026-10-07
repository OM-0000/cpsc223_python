#Lecture 4: Importing Functions
import math
#from mylib import *   <-- imports every function, doesn't require prepending mylib before function calls. using it a lot can lead to namespace clashes
#import mylib          <-- imports the library, requires prepending function calls with mylib.
#from mylib import mymult as mm     <-- imports the specfic function using an alias
import mylib as ml                  #<-- imports the library using an alias

print(math.gcd(10, 15))

#print(mylib.mymult(3, 5))
#print(mm(3,5))
print(ml.mymult(3,5))