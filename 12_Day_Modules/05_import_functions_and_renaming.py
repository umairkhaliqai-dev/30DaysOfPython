# Use 'as' to give a module or function a shorter alias — very common with libraries like numpy (np) or pandas (pd).
from mymodule import greet as g, add as a

print(g('World'))   # → Hi, World!
print(a(2, 8))       # → 10

# or rename the whole module:
import mymodule as mm
print(mm.greet('Dev'))  # → Hi, Dev!