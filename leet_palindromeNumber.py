def isPalindrome(self, x: int) -> bool:
    if x < 0:
        return False
    
    number = x
    flip = 0
    while x > 0:
        tmp = x % 10
        x //= 10
        flip = flip * 10 + tmp
    return number == flip