import math
def process_data(data: list, /, operation="sum"):
    if operation=="sum":
        result = math.fsum(data)
    elif operation=="product":
        result = math.prod(data)
    else:
        result = "No such operation"
    return result

print(process_data([1,2,3], "product"))