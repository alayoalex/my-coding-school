import json

my_mapping = {'a': 23, 'b': 42, 'c': 0xc0ffee}
print(my_mapping)

# The "json" module can do a much better job:
print(json.dumps(my_mapping, indent=4, sort_keys=True))

# Note this only works with dicts containing
# primitive types (check out the "pprint" module):
json.dumps({all: 'yup'})