from math import sqrt
def main(a):
    """check that the number "a" is a perfect square.
    Args:
        a: int
    Returns:
        bool
    """
    # Write your code here
    return sqrt(a)==a and a>0
print(main(7))