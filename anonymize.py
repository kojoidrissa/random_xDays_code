#!/anaconda/bin/python
import hashlib
import random as rnd
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
1. create a sequence of numbers, approximating a number of unique records: DONE
2. hash each number: DONE
3. make list of  first 5 char of each hash; search it for duplicates
4. repeat step 4 with 1st and 2nd 5 char of each hash (simulate personal, family name)
"""
names = []

for n in range(0, 500):
    names.append(n)

personal_name =[]
family_name = []

for n in names:
    hash_object = hashlib.sha1(bytes(n, encoding='utf-8'))
    hex_dig = hash_object.hexdigest()
    #I don't need to print this anymore
    #also, doesn't version control mean I can DELETE instead of comment out?
    # print (hex_dig, ";", len(hex_dig), ";", type(hex_dig))
    personal_name.append(hex_dig[:5])
    family_name.append(hex_dig[5:12])

#Change this to calculate percentages?
print("There are ", len(personal_name), "personal names; ", 
    '{:.2%}'.format(len(set(personal_name))/len(personal_name)), "are unique")
print("There are ", len(family_name), "family names; ", 
    '{:.2%}'.format(len(set(family_name))/len(personal_name)), "are unique")

full_name = []
print("full_name has", len(full_name), "elements")

for i in family_name:
    new_name = [i, personal_name[family_name.index(i)]]
    full_name.append(new_name)

print("full_name now has", len(full_name), "elements.")
'''
since set uses hashes and I can't hash a list, how do I test to see
if full_name is made up of unique elements? Does it matter, if each
element in it's constituent lists is unique AND I know those lists aren't
equal? This is where I need more formal math/CS. :-/
'''

#printing 10 random `full_name` entries, to see what they look like
print("\n")
print(str.upper("ten random full names"))
for i in range(0,10):
    rnd_index = rnd.randint(0,(len(full_name)-1))
    print(rnd_index, full_name[rnd_index])

##Trying a treacherous live demo. I failed. :-(
print(personal_name[0])

hash_object = hashlib.sha1(bytes(n, encoding='utf-8'))

