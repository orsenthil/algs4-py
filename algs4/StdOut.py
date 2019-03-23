"""
This class provides methods for printing strings and numbers to standard output.

* StdOut coerces the character-set encoding to UTF-8, which is a standard character encoding for Unicode.
* StdOut coerces the locale to {@link Locale#US}, for consistency with {@link StdIn},
  {@link Double#parseDouble(String)}, and floating-point literals.
* StdOut <em>flushes</em> standard output after each call to {@code print()} so that text
  will appear immediately in the terminal.

For additional documentation,
see <a href="https://introcs.cs.princeton.edu/15inout">Section 1.5</a> of
<em>Computer Science: An Interdisciplinary Approach</em>
by Robert Sedgewick and Kevin Wayne.
"""

import locale


class StdOut:

    # force Unicode UTF-8 encoding; otherwise it's system dependent
    CHARSET_NAME = "UTF-8"

    def __init__(self):
        pass

    @classmethod
    def println(cls, x=None):
        """Classmethod for println

        :param x: any object
        :return: prints the output on the console with newline.
        """
        if x is None:
            print("")
        else:
            print(x)

    @classmethod
    def print(cls, x=None):
        """Classmethod for print

        :param x:  any object
        :return: print the output on the console without newline.
        """
        if x is None:
            print("", end="", flush=True)
        else:
            print(x, end='', flush=True)

    @classmethod
    def close(cls):
        """ Calling close() permanently disables standard output;
            subsequent calls to StdOut.println() or System.out.println()
            will no longer produce output on standard output.
        :return:
        """
        print("", flush=True)

    @classmethod
    def printf(cls, format, s, _locale=None):
        """Print the formatted string to stdout.

        :param format: format for the string.
        :param s: string to print
        :param locale: If locale is given, prints using the given locale.
        :return:
        """
        if _locale is not None:
            locale.setlocale(locale.LC_ALL, _locale)
            formatted_s = locale.format_string(format, s)
            print(formatted_s, flush=True)
            locale.resetlocale()
        else:
            print(format % s, flush=True)



if __name__ == '__main__':
    StdOut.print("Test")
    StdOut.println(17)
    StdOut.println(True)
    StdOut.printf("%.6f\n", 1.0/7.0)