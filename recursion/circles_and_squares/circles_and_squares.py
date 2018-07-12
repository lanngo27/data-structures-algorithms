import math

def count_circles_and_squares(length, circles, squares):
    #Write your code here
    if length > 1 or math.isclose(length,1):
        circles += 1

    if length > math.sqrt(2) or math.isclose(length,math.sqrt(2)):
        squares += 1
        return count_circles_and_squares(length/math.sqrt(2), circles, squares)
    return circles, squares


def main():
    length = 2
    circles, squares = count_circles_and_squares(length, 0, 0)
    print("Circles:", circles, "Squares:", squares)


if __name__ == "__main__":    
    main()
