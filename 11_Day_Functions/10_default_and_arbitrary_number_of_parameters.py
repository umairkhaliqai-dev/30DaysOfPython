# You can mix *args with regular parameters. *args must come after fixed parameters.
def info(country, *cities):
    print(f"Country: {country}")
    print(f"Cities: {cities}")

info("UK", "London", "Manchester")
# Country: UK | Cities: ('London', 'Manchester')