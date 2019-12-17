# FIRST PYTHON PROGRAM
SUFFIXES = {1000: ['KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB'],
            1024: ['KiB', 'MiB', 'GiB', 'TiB', 'PiB', 'EiB', 'ZiB', 'YiB']}

def approximate_size(size, a_kilobyte_is_1024_bytes=True):
    '''Convert a file size to human-readable form.

    Keyword arguments:
    size -- file size in bytes
    a_kilobyte_is_1024_bytes -- if True(default), use multiples of 1024
                                if False, use multples of 1000

    Returns: String

    '''

    if size < 0:
        raise ValueError('number must be non-negative')

    multiple = 1024 if a_kilobyte_is_1024_bytes else 1000
    
    for suffix in SUFFIXES[multiple]:
        size = size / multiple
        if size < multiple:
            return f'{size:.1f} {suffix}'

    raise ValueError('number too large')

if __name__ == '__main__': # when you run module as a standalone program, __name__ gets a default value as __main__   ....If  you are import the module then __name__ is the module's filename
    print(approximate_size(1000000000000,False))
    print(approximate_size(1000000000000))

# Every Python function returns a value; if the function ever executes a return statement, it will return that value, otherwise it will return None, the Python null value.

# As soon as you have a named argument, all arguments to the right of that need to be named arguments, too

# Once you import a Python module, you access its functions with module.function

# Everything in Python is an object, and everything can have attributes and methods.

# Python uses try...except blocks to handle exceptions, and the raise statement to generate them. Java and c++ use try...catch blocks to handle exceptions, and the throw statement to generate them.

