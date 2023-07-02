#Aufgabe 2.1
wort=input('word:')
i=0
for b in wort:
    i+=1
print(i)

#Aufgabe 2.2
figur=input('Figur:')
if figur=='Kreis':
    r=float(input('radius(cm):'))
    print(3.14*r**2, 'cm2')
elif figur=='Quadrat':
    l=float(input('Seite(cm):'))
    print(1**2, 'cm2')
elif figur=='Rechteck':
    l1=float(input('Seite1'))
    l2=float(input('Seite2'))
    print(11*12, 'cm2')
else:
    print('nicht bekannt')
             
#Aufgabe 2.3
# menge=int(input('wie viele Zahlen? '))
# summe=0
# i=0
# while i < menge:
#     for i in range(menge):
#         z=float(input('zahl eingeben:'))
#         summe+=z
#         i+=1
# durchscnitt= summe / menge
# print('Durchschnitt: ', durchscnitt)

#Aufgabe 2.5
wort=input('word:')
for letter in wort:
    print(letter)

#Aufgabe 2.6
number= int(input('Zahlen: '))
i=0
while i<number:
    i+=1
    if i %2 == 1:
        print(i)

#Aufgabe 2.7
number=int(input('Zahlen: '))
i=1
while i<=number:
    print('*'*1)
    i+=1
#Andere Lösung
i=1
while i<5:
    print(i*'*')
    i+=1

#Aufgabe 2.8
number=int(input('Zahlen: '))
while number>0:
    print('*' *number)
    number=number-1
#Andere Lösung
i=4
while i>1:
    print(i* '*')
    i=i-1

#Aufgabe 2.9
h=int(input('Die Höhe ist: '))
b=int(input('Die Breite ist:'))
for i in range(h):
    print('*' *b)