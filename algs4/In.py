import re
import locale
import urllib.request
import urllib.parse


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

    def __init__(self, fobj=None, url=None):

        if fobj:
            self.fopen = fobj
            self.lines = self.fopen.readlines()
            self.content = "".join(self.lines)

        try:
            self.fopen = urllib.request.urlopen(url)
        except ValueError as e:
            raise e
        else:
            self.lines= self.fopen.readlines()
            self.content = "".join(self.lines)

    def readline(self):
        """Reads and returns the next line in this input stream.

        :return: the next line in this input stream; None if no such line
        """
        try:
            for line in self.lines:
                yield line
        except StopIteration:
            return None

    def exists(self) -> bool:
        """
        Returns true if this input stream exists.

        :return: True if the input stream exists, false otherwise.
        """
        return self.fopen is not None

    def readChar(self) -> int:
        """Reads and returns the next character in this input stream.

        :return: the next in this input stream, throws ValueError if the input stream is empty.
        """
        try:
            for _char in self.content:
                yield _char
        except StopIteration:
            raise ValueError("attempts to read a 'char' value from the input stream, but no more tokens are available")
