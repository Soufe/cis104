import math
def output_decorator(f):
    def wrapper(w, h):
        rectangle_area = f(w, h)
        formatted_area = round(rectangle_area)
        return f"Rectangle Area = {formatted_area}"
    return wrapper
def find_rectangle_area(w, h):
    return w * h
print(find_rectangle_area(3, 4))