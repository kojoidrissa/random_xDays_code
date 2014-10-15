#Copied this from XLindawang http://30daysofgithub.tumblr.com/post/100039983255/day-8
#http://codingbat.com/prob/p148972

def loneSum(a, b, c):

    '''
    int, int, int --> int 

    Given 3 int values, a b c, return their sum. However, if one of the values is the same as another of the values, it does not count towards the sum. 

    loneSum(1, 2, 3) → 6
    loneSum(3, 2, 3) → 2
    loneSum(3, 3, 3) → 0
    '''

    if a == b == c:
        return 0
    elif a == b:
        return c
    elif a == c:
        return b
    elif b == c:
        return a
    else:
        return a + b + c



