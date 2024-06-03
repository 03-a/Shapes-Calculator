def CircleCalc(): 
    from math import pi
    r = float(input("Enter the radius (float) of the circle: "))
    d = r * 2
    c = pi * d
    a = pi * (r ** 2)
    print(f"Radius: {r}, diameter: {d}, circumference: {c}, area: {a}")

def SquareCalc(): 
    se = float(input("Enter the side length (float) of the square: "))
    p = se * 4
    a = se ** 2
    print(f"Side: {se}, perimeter: {p}, area: {a}")

def CubeCalc(): 
    ar = float(input("Enter the edge length (float) of the cube: "))
    vol = ar ** 3
    print(f"Edge: {ar}, volume: {vol}")

def RTBCalc(): 
    l, w, h = map(float, input("Enter the length, width and height (float) of the rectangular cube: ").split())
    vol = l * w * h
    print(f"Length: {l}, width: {w}, height: {h}, volume: {vol}")

def RTCalc(): 
    l, w = map(float, input("Enter the length and width (float) of the rectangle: ").split())
    p = (l + w) * 2
    a = l * w
    print(f"Length: {l}, width: {w}, perimeter: {p}, area: {a}")

def ParCalc(): 
    b, s = map(float, input("Enter the base and side (float) of the parallelogram: ").split())
    p = (b + s) * 2
    a = (b + s) / 2
    print(f"Base: {b}, side: {s}, perimeter: {p}, area: {a}")

def TraCalc(): 
    a, b, c, d, h = map(float, input("Enter the bases lengths and height (float) of the trapezoid: ").split())
    p = a + b + c + d
    a = ((a + c) / 2) * h
    print(f"Base: {a, b, c, d}, perimeter: {p}, area: {a}")

def TriCalc(): 
    a, b, c, h = map(float, input("Enter the sides' lengths and height (float) of the triangle: ").split())
    p = a + b + c
    a = 0.5 * c * h
    print(f"Sides: {a, b, c}, perimeter: {p}, area: {a}")

Choose_List = ["CC for Circle", "SC for Square", "CBC for Cube", "RTBC for Rectangular Block", "RTC for Rectangle", "PAC for Parallelogram", "TRA for Trapezoid", "TRI for Triangle"]
print(Choose_List)
ch = input("Type the code for calculation: ")
if ch == "CC": 
    CircleCalc()
elif ch == "SC": 
    SquareCalc()
elif ch == "CBC": 
    CubeCalc()
elif ch == "RTBC": 
    RTBCalc()
elif ch == "RTC": 
    RTCalc()
elif ch == "PAC": 
    ParCalc()
elif ch == "TRA": 
    TraCalc()
elif ch == "TRI": 
    TriCalc()