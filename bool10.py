from math import sqrt
def main(a):
    """check that the number "a" is a perfect square.
    Args:
        a: int
    Returns:
        bool
    """
    # Write your code here
    b = sqrt(a)
    return int(b**2) == a
print(main(25))
