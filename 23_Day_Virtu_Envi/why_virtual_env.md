# Definition: Virtual environments prevent dependency conflicts, keep your global Python clean, allow you to test different library versions safely, and make your project reproducible. It is an essential practice for any Python development beyond simple scripts.

# Scenario: You are on Day 23 and start a web project.
# Instead of: pip install django (global)
# Best Practice:
# 1. python -m venv django_project_env
# 2. source django_project_env/bin/activate
# 3. pip install django==3.2

# If the project fails and you need to switch to Django 4.1:
# 4. deactivate
# 5. rm -rf django_project_env (delete old env)
# 6. Create new env and pip install django==4.1

# Your system Python and other projects remain unaffected.