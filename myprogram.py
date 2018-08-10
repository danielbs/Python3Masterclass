#import mymodule
#mymodule.func_in_mymodule()

#the above code works, here is another way 
#which is more user friendly

#import mymodule as mm 
#mm.func_in_mymodule()

#the above code also works
#here is how to import only specific function from mymodule
from mymodule import func_in_mymodule
#if I needed I coulld have imported more functions like 
#from mymodule import func_in_mymodule,anotherfunc,etc
func_in_mymodule()
