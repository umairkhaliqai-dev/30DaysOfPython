# The sys module gives access to Python interpreter details — like command-line arguments, Python version, and the module search path.
import sys

print(sys.version)       # Python version string
print(sys.path)          # list of module search paths
print(sys.argv)          # command-line arguments list
# sys.exit()            # exits the program

# to exit sys
sys.exit()
# To know the largest integer variable it takes
sys.maxsize
# To know environment path
sys.path
# To know the version of python you are using
sys.version