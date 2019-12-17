class Fib:
    '''iterator that yields numbers in the fibonacci sequence'''

    def __init__(self,max): # Calling Fib(max) is really creating an instance of the class and calling its __init__() method with max
        self.max = max  # self.max is global to the instance

    def __iter__(self):
        self.a = 0
        self.b = 1
        return self

    def __next__(self):
        fib = self.a
        if fib > self.max:
            raise StopIteration
        self.a, self.b = self.b, self.a + self.b
        return fib

# The first argument of every class method is always a reference to the current instance of the class, by convention named self

# An iterator is just a class that defines an __iter__() method.

class LazyRules:
    rules_filename = 'plural6-rules.txt'

    def __init__(self):
        self.pattern_file = open(self.rules_filename, encoding='utf-8')
        self.cache = []

    def __iter__(self): # the one thing that every __iter__() method must do is return an iterator.In thi case, it returns self, which signals that this class defines a __next__() method which will take care of returning values throughout the iteration.
        self.cache_index = 0
        return self

    def __next__(self):
        self.cache_index += 1
        if len(self.cache) >= self.cache_index:
            return self.cache[self.cache_index - 1]

        if self.pattern_file.closed:
            raise StopIteration

        line = self.pattern_file.readline()
        if not line:
            self.pattern_file.close()
            raise StopIteration

        pattern, search, replace = line.split(None, 2)
        funcs = build_match_and_apply_functions(pattern, search, replace)
        self.cache.append(funcs)
        return funcs

def build_match_and_apply_functions(pattern, search, replace):
    def matches_rule(word):
        return re.search(pattern, word)
    def apply_rule(word):
        return re.sub(search, replace, word)
    return (matches_rule, apply_rule)

rules = LazyRules()


#changing the class attributes at run time doesn't change the overridden attributes 

