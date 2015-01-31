#Copied this from XLindawang http://30daysofgithub.tumblr.com/post/100039983255/day-8
#http://codingbat.com/prob/p148972

'''
int, int, int --> int 

Given 3 int values, a b c, return their sum. However, if one of the values is 
the same as another of the values, it does not count towards the sum. 

a,b,c = 1, 2, 3 → 6
a,b,c = 3, 2, 3 → 2
a,b,c = 3, 3, 3 → 0
'''

if a == b == c:
    print(0)
elif a == b:
    print(c)
elif a == c:
    print(b)
elif b == c:
    print(a)
else:
    print(a + b + c)



