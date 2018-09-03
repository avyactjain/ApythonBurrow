import sys
import re

if (sys.hexversion < 0x03000000):
    import os
    sys.stdin = os.fdopen(sys.stdin.fileno(), 'rU', 0)
else:    
    sys.stdin = open(sys.stdin.fileno(), 'r', newline=None)
            
def writeln(x=''):
    if sys.hexversion < 0x03000000:
        x = unicode(x)
        x = x.encode('utf-8')
    else:
        x = str(x)
    sys.stdout.write(x)
    sys.stdout.write('\n')
    sys.stdout.flush()


def write(x=''):
    if (sys.hexversion < 0x03000000):
        x = unicode(x)
        x = x.encode('utf-8')
    else:
        x = str(x)
    sys.stdout.write(x)
    sys.stdout.flush()

#-----------------------------------------------------------------------

def writef(fmt, *args):
    x = fmt % args
    if sys.hexversion < 0x03000000:
        x = unicode(x)
        x = x.encode('utf-8')
    sys.stdout.write(x)
    sys.stdout.flush()

#=======================================================================
# Reading functions
#=======================================================================

_buffer = ''

#-----------------------------------------------------------------------

def _readRegExp(regExp):
    
    global _buffer
    if isEmpty():
        raise EOFError()
    compiledRegExp = re.compile(r'^\s*' + regExp)
    match = compiledRegExp.search(_buffer)
    if match is None:
        raise ValueError()
    s = match.group()
    _buffer = _buffer[match.end():]
    return s.lstrip()

#-----------------------------------------------------------------------

def isEmpty():
    
    global _buffer
    while _buffer.strip() == '':
        line = sys.stdin.readline()
        if sys.hexversion < 0x03000000:
            line = line.decode('utf-8')
        if line == '':
            return True
        _buffer += line
    return False

#-----------------------------------------------------------------------

def readInt():
   
    s = _readRegExp(r'[-+]?(0[xX][\dA-Fa-f]+|0[0-7]*|\d+)')
    radix = 10
    strLength = len(s)
    if (strLength >= 1) and (s[0:1] == '0'): radix = 8
    if (strLength >= 2) and (s[0:2] == '-0'): radix = 8
    if (strLength >= 2) and (s[0:2] == '0x'): radix = 16
    if (strLength >= 2) and (s[0:2] == '0X'): radix = 16
    if (strLength >= 3) and (s[0:3] == '-0x'): radix = 16
    if (strLength >= 3) and (s[0:3] == '-0X'): radix = 16
    return int(s, radix)

#-----------------------------------------------------------------------

def readAllInts():
    
    strings = readAllStrings()
    ints = []
    for s in strings:
        i = int(s)
        ints.append(i)
    return ints

#-----------------------------------------------------------------------

def readFloat():
    
    s = _readRegExp(r'[-+]?(\d+(\.\d*)?|\.\d+)([eE][-+]?\d+)?')
    return float(s)

#-----------------------------------------------------------------------

def readAllFloats():
    
    strings = readAllStrings()
    floats = []
    for s in strings:
        f = float(s)
        floats.append(f)
    return floats

#-----------------------------------------------------------------------

def readBool():
    """
    Discard leading white space characters from standard input. Then
    read from standard input a sequence of characters comprising a bool.
    Convert the sequence of characters to a bool, and return the
    bool.  Raise an EOFError if no non-whitespace characters remain
    in standard input. Raise a ValueError if the next characters to be
    read from standard input cannot comprise a bool.

    These character sequences can comprise a bool:
    -- True
    -- False
    -- 1 (means true)
    -- 0 (means false)
    """
    s = _readRegExp(r'(True)|(False)|1|0')
    if (s == 'True') or (s == '1'):
        return True
    return False

#-----------------------------------------------------------------------

def readAllBools():
    """
    Read all remaining strings from standard input, convert each to
    a bool, and return those bools in an array. Raise a ValueError if
    any of the strings cannot be converted to a bool.
    """
    strings = readAllStrings()
    bools = []
    for s in strings:
        b = bool(s)
        bools.append(b)
    return bools

#-----------------------------------------------------------------------

def readString():
    """
    Discard leading white space characters from standard input. Then
    read from standard input a sequence of characters comprising a
    string, and return the string. Raise an EOFError if no
    non-whitespace characters remain in standard input.
    """
    s = _readRegExp(r'\S+')
    return s

#-----------------------------------------------------------------------

def readAllStrings():
    """
    Read all remaining strings from standard input, and return them in
    an array.
    """
    strings = []
    while not isEmpty():
        s = readString()
        strings.append(s)
    return strings

#-----------------------------------------------------------------------

def hasNextLine():
    """
    Return True if standard input has a next line. Otherwise return
    False.
    """
    global _buffer
    if _buffer != '':
        return True
    else:
        _buffer = sys.stdin.readline()
        if sys.hexversion < 0x03000000:
            _buffer = _buffer.decode('utf-8')
        if _buffer == '':
            return False
        return True

#-----------------------------------------------------------------------

def readLine():
    """
    Read and return as a string the next line of standard input.
    Raise an EOFError is there is no next line.
    """
    global _buffer
    if not hasNextLine():
        raise EOFError()
    s = _buffer
    _buffer = ''
    return s.rstrip('\n')

#-----------------------------------------------------------------------

def readAllLines():
    """
    Read all remaining lines from standard input, and return them as
    strings in an array.
    """
    lines = []
    while hasNextLine():
        line = readLine()
        lines.append(line)
    return lines

#-----------------------------------------------------------------------

def readAll():
    """
    Read and return as a string all remaining lines of standard input.
    """
    global _buffer
    s = _buffer
    _buffer = ''
    for line in sys.stdin:
        if sys.hexversion < 0x03000000:
            line = line.decode('utf-8')
        s += line
    return s

#=======================================================================
# For Testing
#=======================================================================

def _testWrite():
    writeln()
    writeln('string')
    writeln(123456)
    writeln(123.456)
    writeln(True)
    write()
    write('string')
    write(123456)
    write(123.456)
    write(True)
    writeln()
    writef('<%s> <%8d> <%14.8f>\n', 'string', 123456, 123.456)
    writef('formatstring\n')

#-----------------------------------------------------------------------

def _main():
    """
    For testing. The command-line argument should be the name of the
    function that should be called.
    """

    map = {
        'readInt':    readInt,    'readAllInts':    readAllInts,
        'readFloat':  readFloat,  'readAllFloats':  readAllFloats,
        'readBool':   readBool,   'readAllBools':   readAllBools,
        'readString': readString, 'readAllStrings': readAllStrings,
        'readLine':   readLine,   'readAllLines' :  readAllLines,
        'readAll':    readAll }

    testId = sys.argv[1]

    if testId == 'write':
        _testWrite()
    else:
        writeln(map[testId]())

if __name__ == '__main__':
    _main()
