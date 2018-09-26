"""
The StdIn class provides static methods for reading strings and numbers from standard input.

These functions fall into one of four categories:

* Those for reading individual tokens from standard input, one at a time, and converting each to a number, string, or boolean
* Those for reading characters from standard input, one at a time
* Those for reading lines from standard input, one at a time

* Those for reading a sequence of values of the same type from standard input, and returning the values in an array

Generally, it is best not to mix functions from the different categories in the same program.

Reading tokens from standard input and converting to numbers and strings.
You can use the following methods to read numbers, strings, and booleans
from standard input one at a time:

isEmpty()
readInt()
readDouble()
readString()
readShort()
readLong()
readFloat()
readByte()
readBoolean()

The first method returns true if standard input has more tokens. Each other method skips over any
input that is whitespace. Then, it reads the next token and attempts to convert it into a value of the
specified type. If it succeeds, it returns that value; otherwise, it throws an InputMismatchException.

Whitespace includes spaces, tabs, and newlines; the full definition
is inherited from Character.isWhitespace(char).

A token is a maximal sequence of non-whitespace characters.

The precise rules for describing which tokens can be converted to
integers and floating-point numbers are inherited from

using the locale Locale_US; the rules for floating-point numbers are slightly different
from those in Double.valueOf(String), but unlikely to be of concern to most programmers.

As an example, the following code fragment reads integers from standard input,
one at a time, and prints them one per line.

::

    while (!StdIn.isEmpty()) {
        double value = StdIn.readDouble();
        StdOut.println(value);
    }
    StdOut.println(sum);


Reading characters from standard input.

You can use the following two methods to read characters from standard input one at a time:

#hasNextChar()
#readChar()

The first method returns true if standard input has more input (including whitespace).
The second method reads and returns the next character of input on standard
input (possibly a whitespace character).

As an example, the following code fragment reads characters from standard input,
one character at a time, and prints it to standard output.

while (StdIn.hasNextChar()) {
    char c = StdIn.readChar();
    StdOut.print(c);
}

Reading lines from standard input.
You can use the following two methods to read lines from standard input:

#hasNextLine()
#readLine()

The first method returns true if standard input has more input (including whitespace).
The second method reads and returns the remaining portion of
the next line of input on standard input (possibly whitespace),
discarding the trailing line separator.

A line separator is defined to be one of the following strings:

`\n` (Linux), `\r` (old Macintosh),
`\r\n` (Windows),
`\u2028`, `\u2029`, or `\u0085`.

As an example, the following code fragment reads text from standard input,
one line at a time, and prints it to standard output.

::

    while (StdIn.hasNextLine()) {
        String line = StdIn.readLine();
        StdOut.println(line);
    }

Reading a sequence of values of the same type from standard input.

You can use the following methods to read a sequence numbers, strings,
or booleans (all of the same type) from standard input:

#readAllDoubles()
#readAllInts()
#readAllLongs()
#readAllStrings()
#readAllLines()
#readAll()

The first three methods read of all of remaining token on standard input
and converts the tokens to values of
the specified type, as in the corresponding

readDouble, readInt, and readString() methods.

The readAllLines() method reads all remaining lines on standard
input and returns them as an array of strings.

The readAll() method reads all remaining input on standard
input and returns it as a string.

As an example, the following code fragment reads all of the remaining
tokens from standard input and returns them as an array of strings.


String[] words = StdIn.readAllStrings();

Differences with Scanner.

StdIn and Scanner are both designed to parse
tokens and convert them to primitive types and strings.
The main differences are summarized below:

StdIn is a set of static methods and reads
     reads input from only standard input. It is suitable for use before
     a programmer knows about objects.
     See In for an object-oriented version that handles
     input from files, URLs,
     and sockets.

StdIn uses whitespace as the delimiter pattern
     that separates tokens.
     Scanner supports arbitrary delimiter patterns.

StdIn coerces the character-set encoding to UTF-8,
     which is the most widely used character encoding for Unicode.

StdIn coerces the locale to Locale#US,
     for consistency with StdOut, Double#parseDouble(String),
     and floating-point literals.

StdIn has convenient methods for reading a single
     character; reading in sequences of integers, doubles, or strings;
     and reading in all of the remaining input.

Historical note: StdIn preceded Scanner; when
Scanner was introduced, this class was re-implemented to use Scanner.

Using standard input.

Standard input is fundamental operating system abstraction, on Mac OS X,
Windows, and Linux.

The methods in StdIn are <em>blocking</em>, which means that they
will wait until you enter input on standard input.

If your program has a loop that repeats until standard input is empty,
you must signal that the input is finished.

To do so, depending on your operating system and IDE,
use either <Ctrl-d> or <Ctrl-z>, on its own line.

If you are redirecting standard input from a file, you will not need
to do anything to signal that the input is finished.

Known bugs.

Java's UTF-8 encoding does not recognize the optional
<a href = "http://bugs.sun.com/bugdatabase/view_bug.do?bug_id=4508058">byte-order mask</a>.
If the input begins with the optional byte-order mask, {@code StdIn}
will have an extra character \uFEFF at the beginning.


"""

import re

from In import NoSuchElementException, InputMismatchException


class StdIn:

    WHITESPACE_PATTERN = re.compile(r"""\s+  # matches white-space characters
                                     """, re.X | re.UNICODE)

    def __init__(self, fobj=None):

        if fobj:
            self.fopen = fobj
            self.lines = self.fopen.readlines()
            self.content = "".join(self.lines)
            self.scanned_contents = re.split(self.WHITESPACE_PATTERN, self.content)

    def isEmpty(self):
        return len(self.lines) == 0

    def hasNextLine(self):
        """Returns true if standard input has a next line.
        Use this method to know whether the next call to {@link #readLine()} will succeed. This method
        is functionally equivalent to {@link #hasNextChar()}.

        :return: if standard input has more input (including whitespace); , False, otherwise
        """
        return bool(self.lines)

    def hasNextChar(self):
        all_lines = " ".join(self.lines)
        _chars = all_lines.split(" ")
        return bool(_chars)

    def readLine(self):
        """Reads and returns the next line, excluding the line separator if present.

        :return: @return the next line, excluding the line separator if present; {@code null} if no such line
        """
        try:
            for line in self.lines:
                yield line
        except StopIteration:
            return None

    def readChar(self):
        """Reads and returns the next character.

        :return: char if available, else None.
        """
        chars = list(" ".join(self.lines))
        try:
            for c in chars:
                yield c
        except StopIteration:
            return None


    def readAll(self):
        """Reads and returns the remainder of the input, as a string.

        :return: the remainder of the input, as a string
        """
        contents = " ".join(self.lines)
        return contents

    def readString(self):
        """Reads and returns the next String, excluding the line separator if present.

        :return: @return the next line, or raise a NoSuchElementException if the next line is not present.
        """
        try:
            for line in self.lines:
                yield line
        except StopIteration:
            raise NoSuchElementException


    def readInt(self) -> int:
        """Reads the next token from this input stream, parses it as a int,
        and returns the int.

        @throws NoSuchElementException if the input stream is empty
        @throws InputMismatchException if the next token cannot be parsed as an int
        :return: the next int in this input stream
        """

        contents = list(" ".join(self.lines))

        if not contents:
            raise NoSuchElementException("attemps to read an 'int' value from the input stream, "
                                         + "but no more tokens are available")

        for token in contents:
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

        contents = list(" ".join(self.lines))

        if not contents:
            raise NoSuchElementException("attemps to read an 'float' value from the input stream, "
                                         + "but no more tokens are available")

        for token in contents:
            try:
                yield float(token)
            except ValueError:
                raise InputMismatchException("attempts to read an 'int' value from the input stream, "
                                             + "but the next token is \"" + token + "\"")
