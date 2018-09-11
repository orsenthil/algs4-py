"""
The {@code StdIn} class provides static methods for reading strings and numbers from standard input.
These functions fall into one of four categories:

<ul>
<li>those for reading individual tokens from standard input, one at a time,
    and converting each to a number, string, or boolean
<li>those for reading characters from standard input, one at a time
<li>those for reading lines from standard input, one at a time
<li>those for reading a sequence of values of the same type from standard input,
    and returning the values in an array
</ul>

<p>
Generally, it is best not to mix functions from the different
categories in the same program.
<p>

<b>Reading tokens from standard input and converting to numbers and strings.</b>
You can use the following methods to read numbers, strings, and booleans
from standard input one at a time:

<ul>
<li> {@link #isEmpty()}
<li> {@link #readInt()}
<li> {@link #readDouble()}
<li> {@link #readString()}
<li> {@link #readShort()}
<li> {@link #readLong()}
<li> {@link #readFloat()}
<li> {@link #readByte()}
<li> {@link #readBoolean()}
</ul>

<p>
The first method returns true if standard input has more tokens.
Each other method skips over any input that is whitespace. Then, it reads
the next token and attempts to convert it into a value of the specified
type. If it succeeds, it returns that value; otherwise, it
throws an {@link InputMismatchException}.
<p>

<em>Whitespace</em> includes spaces, tabs, and newlines; the full definition
is inherited from {@link Character#isWhitespace(char)}.

A <em>token</em> is a maximal sequence of non-whitespace characters.
The precise rules for describing which tokens can be converted to
integers and floating-point numbers are inherited from
<a href = "http://docs.oracle.com/javase/7/docs/api/java/util/Scanner.html#number-syntax">Scanner</a>,
using the locale {@link Locale#US}; the rules
for floating-point numbers are slightly different
from those in {@link Double#valueOf(String)},
but unlikely to be of concern to most programmers.

<p>
As an example, the following code fragment reads integers from standard input,
one at a time, and prints them one per line.

<pre>
while (!StdIn.isEmpty()) {
    double value = StdIn.readDouble();
    StdOut.println(value);
}
StdOut.println(sum);
</pre>


<p>
<b>Reading characters from standard input.</b>
You can use the following two methods to read characters from standard input one at a time:
<ul>
<li> {@link #hasNextChar()}
<li> {@link #readChar()}
</ul>
<p>
The first method returns true if standard input has more input (including whitespace).
The second method reads and returns the next character of input on standard
input (possibly a whitespace character).
<p>
As an example, the following code fragment reads characters from standard input,
one character at a time, and prints it to standard output.
<pre>
while (StdIn.hasNextChar()) {
    char c = StdIn.readChar();
    StdOut.print(c);
}
</pre>
<p>
<b>Reading lines from standard input.</b>
You can use the following two methods to read lines from standard input:
<ul>
<li> {@link #hasNextLine()}
<li> {@link #readLine()}
</ul>
<p>
The first method returns true if standard input has more input (including whitespace).
The second method reads and returns the remaining portion of
the next line of input on standard input (possibly whitespace),
discarding the trailing line separator.
<p>
A <em>line separator</em> is defined to be one of the following strings:
{@code \n} (Linux), {@code \r} (old Macintosh),
{@code \r\n} (Windows),
{@code \}{@code u2028}, {@code \}{@code u2029}, or {@code \}{@code u0085}.
<p>
As an example, the following code fragment reads text from standard input,
one line at a time, and prints it to standard output.
<pre>
while (StdIn.hasNextLine()) {
    String line = StdIn.readLine();
    StdOut.println(line);
}
</pre>
<p>
<b>Reading a sequence of values of the same type from standard input.</b>
You can use the following methods to read a sequence numbers, strings,
or booleans (all of the same type) from standard input:
<ul>
<li> {@link #readAllDoubles()}
<li> {@link #readAllInts()}
<li> {@link #readAllLongs()}
<li> {@link #readAllStrings()}
<li> {@link #readAllLines()}
<li> {@link #readAll()}
</ul>
<p>
The first three methods read of all of remaining token on standard input
and converts the tokens to values of
the specified type, as in the corresponding
{@code readDouble}, {@code readInt}, and {@code readString()} methods.
The {@code readAllLines()} method reads all remaining lines on standard
input and returns them as an array of strings.
The {@code readAll()} method reads all remaining input on standard
input and returns it as a string.
<p>
As an example, the following code fragment reads all of the remaining
tokens from standard input and returns them as an array of strings.
<pre>
String[] words = StdIn.readAllStrings();
</pre>
<p>
<b>Differences with Scanner.</b>
{@code StdIn} and {@link Scanner} are both designed to parse
tokens and convert them to primitive types and strings.
The main differences are summarized below:
<ul>
<li> {@code StdIn} is a set of static methods and reads
     reads input from only standard input. It is suitable for use before
     a programmer knows about objects.
     See {@link In} for an object-oriented version that handles
     input from files, URLs,
     and sockets.
<li> {@code StdIn} uses whitespace as the delimiter pattern
     that separates tokens.
     {@link Scanner} supports arbitrary delimiter patterns.
<li> {@code StdIn} coerces the character-set encoding to UTF-8,
     which is the most widely used character encoding for Unicode.
<li> {@code StdIn} coerces the locale to {@link Locale#US},
     for consistency with {@link StdOut}, {@link Double#parseDouble(String)},
     and floating-point literals.
<li> {@code StdIn} has convenient methods for reading a single
     character; reading in sequences of integers, doubles, or strings;
     and reading in all of the remaining input.
</ul>
<p>
Historical note: {@code StdIn} preceded {@code Scanner}; when
{@code Scanner} was introduced, this class was re-implemented to use {@code Scanner}.
<p>
<b>Using standard input.</b>
Standard input is fundamental operating system abstraction, on Mac OS X,
Windows, and Linux.
The methods in {@code StdIn} are <em>blocking</em>, which means that they
will wait until you enter input on standard input.
If your program has a loop that repeats until standard input is empty,
you must signal that the input is finished.
To do so, depending on your operating system and IDE,
use either {@code <Ctrl-d>} or {@code <Ctrl-z>}, on its own line.
If you are redirecting standard input from a file, you will not need
to do anything to signal that the input is finished.
<p>
<b>Known bugs.</b>
Java's UTF-8 encoding does not recognize the optional
<a href = "http://bugs.sun.com/bugdatabase/view_bug.do?bug_id=4508058">byte-order mask</a>.
If the input begins with the optional byte-order mask, {@code StdIn}
will have an extra character {@code \}{@code uFEFF} at the beginning.
<p>

"""
class StdIn:

    def __init__(self):
        pass
