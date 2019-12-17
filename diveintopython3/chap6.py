# square brackets mean "match excatly one of these characters"

import re

'''
def plural(noun):
    if re.search('[sxz]$', noun):
        return re.sub('$','es',noun)
    elif re.search('[^aeioudgkprt]h$',noun): # The ^ as the first character inside the square brackets means something special: negation. [^abc] means “any single character except a, b, or c”
        return re.sub('$', 'es', noun)
    elif re.search('[^aeiou]y$', noun):
        return re.sub('$','ies',noun)
    else:
        return noun + 's'
'''
# re.sub replaces all of the matches 
'''
def match_sxz(noun):
    return re.search('[sxz]$', noun)

def apply_sxz(noun):
    return re.sub('$','es',noun)

def match_h(noun):
    return re.search('[^aeioudgkprt]h$',noun)

def apply_h(noun):
    return re.sub('$','es',noun)

def match_y(noun):
    return re.search('[^aeiou]y$', noun)

def apply_y(noun):
    return re.sub('y$','ies',noun)

def match_default(noun);
    return True

def apply_default(noun):
    return noun + 's'

rules = ((match_sxz, apply_sxz),
        (match_h, apply_h),
        (match_y, apply_h),
        (match_default, apply_default)
        )


'''
def build_match_and_apply_functions(pattern, search, replace):
    def matches_rule(word):
        return re.search(pattern, word)
    def apply_rule(word):
        return re.sub(search, replace, word)
    return (matches_rule, apply_rule)

# This technique of using the values of outside parameters within a dynamic function is called closures.
'''
patterns = \
    (
        ('[sxz]$',              '$',    'es'),
        ('[^aeioudgkprt]h$',    '$',    'es'),
        ('qu|[^aeiou]y$',       'y$',   'es'),
        ('$',                   '$',    's')
    )

rules = [build_match_and_apply_functions(pattern, search, replace) for (pattern, search, replace) in patterns]
'''
def plural(noun):
    for matches_rule, apply_rule in rules:
        if matches_rule(noun):
            return apply_rule(noun)

rules = []
with open('plural4-rules.txt', encoding='utf-8') as pattern_file: # The with statement creates what’s called a context
    for line in pattern_file:
        pattern, search, replace = line.split(None, 2)
        rules.append(build_match_and_apply_functions(pattern, search, replace))


# yield pauses a function and saves its state, next() resums where it left off

# The Fibonacci sequence is a sequence of numbers where each number is the sum of the two numbers before it.
def fib(max):
    a, b = 0, 1
    while a < max:
        yield a
        a, b = b, a + b

print(list(fib(100)))