"""
This class provides methods for printing strings and numbers to standard output.
<p>
<b>Getting started.</b>
To use this class, you must have {@code StdOut.class} in your
Java classpath. If you used our autoinstaller, you should be all set.
Otherwise, either download
<a href = "https://introcs.cs.princeton.edu/java/code/stdlib.jar">stdlib.jar</a>
and add to your Java classpath or download
<a href = "https://introcs.cs.princeton.edu/java/stdlib/StdOut.java">StdOut.java</a>
and put a copy in your working directory.
<p>
Here is an example program that uses {@code StdOut}:
<pre>
 public class TestStdOut {
     public static void main(String[] args) {
         int a = 17;
         int b = 23;
         int sum = a + b;
         StdOut.println("Hello, World");
         StdOut.printf("%d + %d = %d\n", a, b, sum);
     }
}
</pre>
<p>
<b>Differences with System.out.</b>
The behavior of {@code StdOut} is similar to that of {@link System#out},
but there are a few technical differences:
<ul>
<li> {@code StdOut} coerces the character-set encoding to UTF-8,
     which is a standard character encoding for Unicode.
<li> {@code StdOut} coerces the locale to {@link Locale#US},
     for consistency with {@link StdIn}, {@link Double#parseDouble(String)},
     and floating-point literals.
<li> {@code StdOut} <em>flushes</em> standard output after each call to
     {@code print()} so that text will appear immediately in the terminal.
</ul>
<p>
<b>Reference.</b>
For additional documentation,
see <a href="https://introcs.cs.princeton.edu/15inout">Section 1.5</a> of
<em>Computer Science: An Interdisciplinary Approach</em>
by Robert Sedgewick and Kevin Wayne.

@author Robert Sedgewick
@author Kevin Wayne

"""