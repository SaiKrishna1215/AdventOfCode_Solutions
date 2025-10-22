
def compute_area(dim):
    l, w, h = dim
    area = [l*w, w*h, h*l]
    total = 2*sum(area)
    least = min(area)
    return total + least

def compute_ribbon(dim):
    perimeter = 2*sum(dim) - 2*max(dim)
    bow = dim[0]*dim[1]*dim[2]
    return perimeter + bow

total = 0
ribbon = 0

dims = []

with open("input.txt") as f:
    for dim in f:
        dims.append([int(d) for d in dim.split('x')])



for dim in dims:
    total += compute_area(dim)
    ribbon += compute_ribbon(dim)

print(total, ribbon)
