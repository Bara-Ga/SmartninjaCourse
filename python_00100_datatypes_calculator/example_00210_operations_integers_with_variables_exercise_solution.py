# nehme 2 und 10 und weise variablen zu und dividiere sie
# printe das ergebnis
x = 2.0
y = 10.0
ergebnis = x/y
print ergebnis

# nehme deinen Vor- und Nachnamen als Strings,
# addiere sie zu einer neuen Variable
# printe sie
vorname = "xyz"
nachname = "abc"
print vorname + " " + nachname


# divide a number by 0, what happens?
5/0

try:
    5/0
except ZeroDivisionError:
    print "Do not divide by zero"


try:
    int("abc")
except ValueError:
    print "Please enter a number"

try:
    int("abc")
except Exception:
    print "Please enter a number"
