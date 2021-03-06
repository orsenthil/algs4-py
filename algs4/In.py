"""
Input. This class provides methods for reading strings and numbers from standard input, file input, URLs, and sockets.

The Locale used is: language = English, country = US. This is consistent with the formatting conventions with Java
floating-point literals, command-line arguments (via {@link Double#parseDouble(String)}) and standard output.

For additional documentation, see <a href="https://introcs.cs.princeton.edu/31datatype">Section 3.1</a> of
<i>Computer Science: An Interdisciplinary Approach</i> by Robert Sedgewick and Kevin Wayne.

Like {@link Scanner}, reading a token also consumes preceding Java whitespace, reading a full line consumes
the following end-of-line delimeter, while reading a character consumes nothing extra.

Whitespace is defined in {@link Character#isWhitespace(char)}. Newlines consist of \n, \r, \r\n, and Unicode hex code
points 0x2028, 0x2029, 0x0085;
"""
import re
import locale
import urllib.request
import urllib.parse
from typing import Iterator


class InputMismatchException(Exception):
    pass


class NoSuchElementException(Exception):
    pass


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
    CHARSET_NAME = "utf-8"

    # language = English, country = US for consistency with System.out

    LOCALE = locale.LC_ALL

    WHITESPACE_PATTERN = re.compile(r"""\s+  # matches white-space characters
                                     """, re.X | re.UNICODE)

    EMPTY_PATTERN = re.compile("")

    EVERYTHING_PATTERN = re.compile(r"""\A  # Matches only at the start of the string.""", re.X)

    def __init__(self, fobj=None, url=None):

        if fobj:
            self.fopen = fobj
            self.lines = self.fopen.readlines()
            self.content = "".join(self.lines)
            self.scanned_contents = re.split(self.WHITESPACE_PATTERN, self.content)

        try:
            self.fopen = urllib.request.urlopen(url)
        except ValueError as e:
            raise e
        else:
            self.lines= self.fopen.readlines()
            self.content = "".join(self.lines)
            self.scanned_contents = re.split(self.WHITESPACE_PATTERN, self.content)

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

    def readAll(self) -> str:
        """
        Reads and returns the remainder of this input stream, as a string.

        :return:
        """
        result = self.fopen.read()
        return result


    def readString(self) -> str:
        """Reads the next token from this input stream and returns it as a String.

        :return: str
        """
        try:
            yield self.readline()
        except StopIteration:
            raise ValueError("attempts to read a 'String' value from the input stream, but no more tokens are available")

    def readInt(self) -> int:
        """Reads the next token from this input stream, parses it as a int,
        and returns the int.

        @throws NoSuchElementException if the input stream is empty
        @throws InputMismatchException if the next token cannot be parsed as an int
        :return: the next int in this input stream
        """

        if not self.scanned_contents:
            raise NoSuchElementException("attemps to read an 'int' value from the input stream, "
                                         + "but no more tokens are available")

        for token in self.scanned_contents:
            try:
                yield int(token)
            except ValueError:
                raise InputMismatchException("attempts to read an 'int' value from the input stream, "
                                             + "but the next token is \"" + token + "\"")


    def readDouble(self) -> float:
        """Reads the next token from this input stream, parses it as a float,
        and returns the float.

        @throws NoSuchElementException if the input stream is empty
        @throws InputMismatchException if the next token cannot be parsed as an int
        :return: the next int in this input stream
        """

        if not self.scanned_contents:
            raise NoSuchElementException("attemps to read an 'float' value from the input stream, "
                                         + "but no more tokens are available")

        for token in self.scanned_contents:
            try:
                yield float(token)
            except ValueError:
                raise InputMismatchException("attempts to read an 'int' value from the input stream, "
                                             + "but the next token is \"" + token + "\"")

    def readFloat(self) -> float:
        """Reads the next token from this input stream, parses it as a float,
        and returns the float.

        @throws NoSuchElementException if the input stream is empty
        @throws InputMismatchException if the next token cannot be parsed as an float
        :return: the next float in this input stream
        """
        return self.readDouble()

    def readLong(self) -> int:
        """Reads the next token from this input stream, parses it as a long,
        and returns the long.

        @throws NoSuchElementException if the input stream is empty
        @throws InputMismatchException if the next token cannot be parsed as an long
        :return: the next long in this input stream
        """

        return self.readInt()

    def readShort(self) -> int:
        """Reads the next token from this input stream, parses it as a {@code short},
        and returns the {@code short}.
        @return the next {@code short} in this input stream
        @throws NoSuchElementException if the input stream is empty
        @throws InputMismatchException if the next token cannot be parsed as a {@code short}
        :return:  the next short in this input stream.
        """
        return self.readInt()


    def readByte(self) -> bytes:
        """Reads the next token from this input stream, parses it as a {@code byte}, and returns the {@code byte}.
        <p>
        To read binary data, use {@link BinaryIn}.

        @return the next {@code byte} in this input stream
        @throws NoSuchElementException if the input stream is empty
        @throws InputMismatchException if the next token cannot be parsed as a {@code byte}
        :return:
        """
        if not self.scanned_contents:
            raise NoSuchElementException("attemps to read an 'byte' value from the input stream, "
                                         + "but no more tokens are available")

        for token in self.scanned_contents:
            try:
                yield bytes(token, encoding=self.CHARSET_NAME)
            except ValueError:
                raise InputMismatchException("attempts to read an 'byte' value from the input stream, "
                                             + "but the next token is \"" + token + "\"")


    def readAllStrings(self) -> list:
        """Reads all remaining tokens from this input stream and returns them as an array of strings.

        :return: all remaining tokens in this input stream, as an array of strings
        """
        return re.split(self.WHITESPACE_PATTERN, self.content)

    def readAllLines(self) -> str:
        """
        Reads and returns all the lines of hte input.

        :return: List of Lines.
        """

        return self.lines

    def readAllInts(self) -> Iterator[int]:
        """Reads all remaining tokens from this input stream, parses them as integers, and returns them as an
        array of integers.

        :return: all remaining lines in this input stream, as an array of integers
        """
        tokens = self.readAllStrings()
        return list(map(int, tokens))

    def readAllLongs(self) -> Iterator[int]:
        """Reads all remaining tokens from this input stream, parses them as longs, and returns them as an
        array of longs.

        :return: All remaining lines in this input stream, as an array of longs
        """
        return self.readAllInts()

    def readAllDoubles(self) -> Iterator[float]:
        """Reads all remaining tokens from this input stream, parses them as doubles, and returns them as an
        array of doubles.

        :return: All remaining lines in this input stream, as an array of doubles
        """
        tokens = self.readAllStrings()
        return list(map(float, tokens))

    def close(self):
        """Close the stream.

        :return: None.
        """
        self.fopen.close()
