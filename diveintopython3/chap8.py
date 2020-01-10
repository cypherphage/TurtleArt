import re
import itertools

def solve(puzzle):
    words = re.findall('[A-Z]+', puzzle.upper())
    unique_characters = set(''.join(words))                 # set doesn't allow duplicates
    assert len(unique_characters) <= 10, 'Too many letters' # if False raises error 'too many letters'
    first_letters = {word[0] for word in words}
    n = len(first_letters)
    sorted_characters = ''.join(first_letters) + ''.join(unique_characters - first_letters)
    characters = tuple(ord(c) for c in sorted_characters)
    digits = tuple(ord(c) for c in '0123456789')
    zero = digits[0]
    for guess in itertools.permutations(digits, len(characters)):
        if zero not in guess[:n]:
            equation = puzzle.translate(dict(zip(characters, guess)))
            if eval(equation):
                return equation
    

if __name__ == '__main__':
    import sys 
    for puzzle in sys.argv[1:]:
        print(puzzle)
        solution = solve(puzzle)
        if solution:
            print(solution)

# .*? looks for shortest possible series of any character
# findall does not return overlapping matches. If two matches overlap, it will return the first one
# 
# python sets don't allow duplicates       
# 
# Using a generator expression instead of a list comprehension can save both cpu and ram. If you’re building an list just to throw it away (e.g. passing it to tuple() or set()), use a generator expression instead!

  