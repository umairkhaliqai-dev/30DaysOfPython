# Definition: requirements.txt is a standard file used to list all the packages 
# and their exact versions needed for a project. 
# You generate it with pip freeze > requirements.txt. 
# Another developer can then recreate the exact environment using 
# pip install -r requirements.txt.

# After activating your environment and installing packages:
# pip freeze > requirements.txt

# This creates a file. Its content will look like:
# requests==2.28.1
# pandas==1.5.0

# To recreate this environment on another machine:
# pip install -r requirements.txt