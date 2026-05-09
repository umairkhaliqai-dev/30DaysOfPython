# Definition: You use the pip install command followed by the package name to download and install a package from PyPI. You can also specify a version.
# In your terminal, you'd run:
# pip install numpy
# Then you can import it in your code
# import numpy as np
# print("NumPy version:", np.__version__)  # This would work after installation
print()
# But i am getting an issue as it is not allowing me to intall numpy using pip intall numpy directly 
# rather i need to create virtual enviroment or need to use sudo apt install python3-numpy.
# So i am going to try virtual enviroment by using : cd ~/Python.pyFile-01-04-26 python3 -m venv venv
# Activating venv as source venv/bin/activate
# Then i asked to pip install requests numpy pandas matplotlib seaborn
# to deactivate later " deactivate "
# verify installation by " pip list"

# Test 1: Check Python
# python --version
# Should show: Python 3.12.3

# Test 2: Check pip
# pip --version
# Should show: pip 24.0 from .../venv/lib/...

# Test 3: Import numpy
# python -c "import numpy as np; print(f'NumPy: {np.__version__}')"

# Test 4: Start interactive shell
# python
# >>> import numpy as np
# >>> print("Working!")
# >>> exit()
print()
# Type this and press Enter
# import numpy as np

# Then type this
# arr = np.array([1, 2, 3, 4, 5])

# Then type this
# print(arr)

# Then type this
# print(arr.mean())

# Then type this
# print("NumPy is working!")

# When you're done, type this to exit
# exit()
