# File: IAT.py
# Description: Print out my initials in stylized large block letters.
# Assignment Number: 1
#
# Name: Isaac Agbozo Tetteh
# STUDENT ID:  <2425403781>
# Email: <ikeagbozo17@gmail.com>
# Grader: <Isaac>
#5
# On my honor, Isaac Agbozo Tetteh, this programming assignment is my own work
# and I have not provided this code to any other student.


def main():
    # Prints initials I.A.T in small form then as large 12x10 block letters with period markers

    # blank line before the small initials
    print()

    # small initials line: three dots then initials with no spaces
    print("...IAT")

    # blank line between small and large initials
    print()

    # -----------------------------------------------------------------------
    # Each large letter is 12 chars wide and 10 chars tall
    # Layout per row: ...I(12)...*(2)...A(12)...*(2)...T(12)...*(2)
    # The period marker (4 asterisks total) is a 2x2 block on the last 2 rows
    # Three dots separate each letter/period item; no trailing separator after last period
    # -----------------------------------------------------------------------

    # row 0 - top bar of I, top bar of T, A peak begins
    print("...IIIIIIIIIIII...  ...    AAAA    ...  ...TTTTTTTTTTTT...")

    # row 1 - second top bar of I, second top bar of T, A widens
    print("...IIIIIIIIIIII...  ...   AAAAAA   ...  ...TTTTTTTTTTTT...")

    # row 2 - I narrows to stem, A shoulders form
    print("...     II     ...  ...  AA    AA  ...  ...     TT     ...")

    # row 3 - I stem, A legs spread wider, T stem continues
    print("...     II     ...  ... AA      AA ...  ...     TT     ...")

    # row 4 - I stem, A crossbar (top of bar), T stem
    print("...     II     ...  ...AAAAAAAAAAAA...  ...     TT     ...")

    # row 5 - I stem, A crossbar (bottom of bar), T stem
    print("...     II     ...  ...AAAAAAAAAAAA...  ...     TT     ...")

    # row 6 - I stem, A lower legs, T stem
    print("...     II     ...  ...AA        AA...  ...     TT     ...")

    # row 7 - I stem, A lower legs, T stem
    print("...     II     ...  ...AA        AA...  ...     TT     ...")

    # row 8 - bottom bar of I, A lower legs, T stem, period markers appear (**) 2x2 block row 1
    print("...IIIIIIIIIIII...**...AA        AA...**...     TT     ...**")

    # row 9 - second bottom bar of I, A lower legs, T stem, period markers 2x2 block row 2
    print("...IIIIIIIIIIII...**...AA        AA...**...     TT     ...**")

    # blank line after the large initials
    print()


main()