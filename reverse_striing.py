# First Loop based approch to reverse a string 

def reverse_string(s):
    left = 0
    right = len(s) - 1

    s = list(s)

    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1

    return ''.join(s)


# Recursion based approch to reverse a string

def _recusion_reverse(s, left, right):
    if left > right:
        return

    s[left], s[right] = s[right], s[left]
    _recusion_reverse(s, left + 1, right - 1)

def reverse_withRecusion(s):

    s = list(s)

    _recusion_reverse(s, 0, len(s) - 1)

    return ''.join(s)


if __name__== "__main__":
    print(reverse_string("Saurabh"))
    print("-"*20)
    print(reverse_withRecusion("Shashank"))
