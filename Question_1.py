import math

for i in range(1,9):
    a=math.pi/4
    b=(a/0.785)*45
    s=math.sin(i*a)
    print("The value of sin", round(b*i), "⁰ is :", round(s, 2))
    c=math.cos(i*a)
    print("The value of cos", round(b*i), "⁰ is :", round(c, 2))
    if b==90:
        print("Not defined")
    elif b==270:
        print("Infinity")
    else:
        t=math.tan(i*a)
        print("The value of tan", round(b*i), "⁰ is :", round(t, 2))