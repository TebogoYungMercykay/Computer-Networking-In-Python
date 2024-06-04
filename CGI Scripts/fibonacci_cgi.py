#!/usr/bin/env python
import os
import cgi
import warnings

warnings.filterwarnings("ignore", category=DeprecationWarning)

def calculate_next_fibonacci(f0, f1, f2):

    next_number = f1 + f2 if f1 is not None and f2 is not None else None

    return f1, f2, next_number

def calculate_previous_fibonacci(f0, f1, f2):

    if f0 == 0 and f1 == 1 and f2 == 1:
        return '###', 0, 1

    previous_number = (f1 - f0) if f1 is not None and f2 is not None else None

    return previous_number, f0, f1

def print_html(f0, f1, f2, show_prev=True):
    print("Content-type: text/html\n")
    print("<!DOCTYPE html")
    print("<html>")
    print("<head>")
    print("<title>Fibonacci Sequence</title>")
    print("</head>")
    print("<body>")
    print(f"<p>{f0}, {f1}, {f2}</p>")

    if show_prev:
        print("<a href=\"/cgi-bin/fibonacci_cgi.py?action=prev\">Previous</a> ")

    print("<a href=\"/cgi-bin/fibonacci_cgi.py?action=next\">Next</a>")
    print("</body>")
    print("</html>")

def main():
    filename = 'fibonacci_numbers.txt'

    with open(filename, 'r') as file:
        fib_numbers = [int(num) if num.strip() != '###' else None for num in file.readline().split(',')]

    f0, f1, f2 = fib_numbers

    action = cgi.FieldStorage().getvalue('action')

    if action == 'prev' and not (f0 == '###' and f1 == 0 and f2 == 1):
        f0, f1, f2 = calculate_previous_fibonacci(f0, f1, f2)
        show_prev = False if f0 is None else True
    elif action == 'next':
        f0, f1, f2 = calculate_next_fibonacci(f0, f1, f2)
        show_prev = True
    else:
        show_prev = False

    with open(filename, 'w') as file:
        file.write(f'{f0},{f1},{f2}')

    print_html(f0, f1, f2, show_prev)

if __name__ == "__main__":
    main()
