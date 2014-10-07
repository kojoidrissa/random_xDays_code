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
names = ["John", "Jon", "Jonny", "Juan", "Johan"]

for n in names:
    hash_object = hashlib.sha1(bytes(n, encoding='utf-8'))
    hex_dig = hash_object.hexdigest()
    print (hex_dig)