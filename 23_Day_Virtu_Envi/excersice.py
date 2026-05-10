# 1. Create a practice folder
# mkdir requirements_practice
# cd requirements_practice

# 2. Create a virtual environment
# python -m venv myenv

# 3. Activate it
# On Windows:
# myenv\Scripts\activate
# On macOS/Linux:
# source myenv/bin/activate

## 4. Install some packages (notice no sudo/--user needed!)
# pip install requests
# pip install pandas
# pip install numpy
# pip install flask

# 5. See what's installed (with versions)
# pip list

# 6. Generate requirements.txt (THIS IS THE KEY COMMAND)
# pip freeze > requirements.txt

# 7. View the file content
# cat requirements.txt  # On Linux/Mac
# OR
# type requirements.txt  # On Windows

# (myenv) umair@umair-HP:~/Python.pyFile-01-04-26/requirements_practice$ pip list
# Package            Version
# ------------------ -----------
# blinker            1.9.0
# certifi            2026.4.22
# charset-normalizer 3.4.7
# click              8.3.3
# Flask              3.1.3
# idna               3.13
# itsdangerous       2.2.0
# Jinja2             3.1.6
# MarkupSafe         3.0.3
# numpy              2.4.4
# pandas             3.0.2
# pip                24.0
# python-dateutil    2.9.0.post0
# requests           2.33.1
# six                1.17.0
# urllib3            2.7.0
# Werkzeug           3.1.8

print()
print()
# after requirements call: 
# myenv) umair@umair-HP:~/Python.pyFile-01-04-26/requirements_practice$ cat requirements.txt 
# blinker==1.9.0
# certifi==2026.4.22
# charset-normalizer==3.4.7
# click==8.3.3
# Flask==3.1.3
# idna==3.13
# itsdangerous==2.2.0
# Jinja2==3.1.6
# MarkupSafe==3.0.3
# numpy==2.4.4
# pandas==3.0.2
# python-dateutil==2.9.0.post0
# requests==2.33.1
# six==1.17.0
# urllib3==2.7.0
# Werkzeug==3.1.8

### Machine-Readable vs Human-Readable
# bash
# pip list output - CAN'T be used directly:
# pip install requests        2.31.0  ❌ This will FAIL!

# pip freeze output - CAN be used directly:
# pip install requests==2.31.0  ✅ This works perfectly!

### # You: "Hey team, I built a cool data app!"
# You send them: requirements.txt with just "pandas"

# Your teammate tries:
# pip install -r requirements.txt
# Installs: pandas==latest (maybe 2.1.0)

# But YOUR app used pandas==1.8.3 (old version)
# Their pandas 2.1.0 has DIFFERENT syntax
# 🔥 YOUR APP BREAKS ON THEIR MACHINE! 🔥

# But if you used pip freeze:
# numpy==1.22.0
# pandas==1.8.3  # <-- EXACT version you used
# python-dateutil==2.8.2
# pytz==2021.3
# six==1.16.0
#### Think of it this way:

# pip list is like a grocery list ("buy milk, eggs") - vague

# pip freeze is like a recipe ("250g organic whole milk, 2 large free-range eggs") - precise and reproducible

# That precision is everything in professional development! 🚀

