# $ "end of the string"
# ^ "start of the string"

#raw string tells python that nothing in this string should be escaped
print(r'\tshak')

# \b "a word boundary must occur here"

# re.sub('regex', 'replacement', string)

# ? makes a pattern optional


import re

pattern = r'^M?M?M?(CM|CD|D?C?C?C?)(XC|XL|L?X?X?X?)(IX|IV|V?I?I?I?)$'

found = re.search(pattern, 'MM')

print(found)

# {n,m} matches from n and m occurrences of a pattern

pattern_new = r'^M{0,3}(CM|CD|D?L{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$'

#Verbose regular expression

pattern_verbose = r'''
    ^                   # beginning of string
    M{0,3}              # thousands - 0 to 3 Ms
    (CM|CD|D?C{0,3})    # hundreds - 900 (CM), 400 (CD), 0-300 (0 to 3 Cs),
                        #            or 500 - 800 (D, followed by 0 to 3 Cs)
    (XC|XL|L?X{0,3})    # tens - 90 (XC), 40 (XL), 0-30 (0 to 3 Xs),
                        #       or 50-80 (L, followed by 0 to 3 Xs)
    (IX|IV|V?I{0,3})    # ones - 9 (IX), 4 (IV), 0-3 (0 to 3 Is),
                        #        or 5-8 (V, followed by 0 to 3 Is)
    $                   # end of string
'''

re.search(pattern_verbose, 'M', re.VERBOSE)
# Python assumes every regular expression is compact unless you explicitly state that it is verbose.

# \d matches any numeric digit (0–9). \D matches anything but digits.

phone_pattern = re.compile(r'(\d{3})\D*(\d{3})\D*(\d{4})\D*(\d*)$')

# + means one or more
# * means zero or more












