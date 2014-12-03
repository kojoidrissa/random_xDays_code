#!/anaconda/bin/python
import hashlib
#print hashlib.algorithms

# hash_object = hashlib.sha1(b'Hello World')
# hex_dig = hash_object.hexdigest()
# print('"hex_dig" is of the type: ', type(hex_dig))
# print(hex_dig)
# print(len(hex_dig))
# print(\n)
# print("New EXAMPLE")
"""
New approach to testing this idea
1. create a sequence of numbers, approximateing the number of names/records
2. hash each number
3. make list of  first 5 char of each hash; search it for duplicates
4. repeat step 4 with 1st and 2nd 5 char of each hash (simulate personal, family name)
"""
names = ["John", "Jon", "Jonny", "Juan", "Johan"]

for n in names:
    hash_object = hashlib.sha1(bytes(n, encoding='utf-8'))
    hex_dig = hash_object.hexdigest()
    print (hex_dig, "; ", len(hex_dig))


