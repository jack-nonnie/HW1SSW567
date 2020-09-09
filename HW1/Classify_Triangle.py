def classify_Triangle(a, b, c):
    sideCount = 0
    if(a == b):
        sideCount += 1
    if(a == c):
        sideCount += 1
    if(b == c):
        sideCount += 1
    str = ""
    if(sideCount == 3):
        str += "The Triangle is equilateral "
    elif(sideCount == 1):
        str += "The Triangle is isosceles "
    else:
        str += "The Triangle is scalene "
    if((a > b and a > c and a*a == b*b + c*c) or (b > a and b > c and b*b == a*a + c*c) or (c > a and c > b and c*c == a*a + b*b)):
        str += "and the triangle is a right triangle"
    else:
        str += "but the triangle is not a right triangle"
    return str
print(classify_Triangle(6,6,9))