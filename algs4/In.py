import re
import locale


class In:
    """
    Input. This class provides methods for reading strings and numbers from standard input, file input, URLs, and
    sockets.

    The default settings for locale in python are set in users environment for any operating system.

    export LC_ALL=en_US.UTF-8
    export LANG=en_US.UTF-8

    The whitespace match is unicode, and locale aware.

    Like Scanner, reading a token also consumes preceding Java whitespace, reading a full line consumes
    the following end-of-line delimeter, while reading a character consumes nothing extra. Whitespace
    is defined in Character.isWhitespace(char). Newlines consist of \n, \r, \r\n, and Unicode hex code
    points 0x2028, 0x2029, 0x0085; see Scanner.java (NB: Java 6u23 and earlier uses only \r, \r, \r\n).
    """

    # assume Unicode UTF-8 encoding
    CHARSET_NAME = "UTF-8"

    # language = English, country = US for consistency with System.out

    LOCALE = locale.LC_ALL

    WHITESPACE_PATTERN = re.compile(r"""\s  # matches white-space characters
                                     """, re.X | re.UNICODE)

    EMPTY_PATTERN = re.compile("")

    EVERYTHING_PATTERN = re.compile(r"""\A  # Matches only at the start of the string.""", re.X)
