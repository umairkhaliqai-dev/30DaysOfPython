# Given list
names = ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland', 'Estonia', 'Russia']

# Unpack the first five countries into nordic_countries
# Store Estonia and Russia in es and ru respectively
*nordic_countries, es, ru = names

# Print results to verify
print(f"Nordic Countries: {nordic_countries}")
print(f"Estonia: {es}")
print(f"Russia: {ru}")