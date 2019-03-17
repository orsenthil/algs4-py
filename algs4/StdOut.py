"""
This class provides methods for printing strings and numbers to standard output.

* StdOut coerces the character-set encoding to UTF-8, which is a standard character encoding for Unicode.
* StdOut coerces the locale to {@link Locale#US}, for consistency with {@link StdIn},
  {@link Double#parseDouble(String)}, and floating-point literals.
* StdOut <em>flushes</em> standard output after each call to {@code print()} so that text
  will appear immediately in the terminal.

"""


class StdOut:

    # force Unicode UTF-8 encoding; otherwise it's system dependent
    CHARSET_NAME = "UTF-8"

    def __init__(self):
        pass

    @classmethod
    def println(cls, x):
        """Classmethod for println

        :param x: any object
        :return: prints the output on the console with newline.
        """
        print(x)