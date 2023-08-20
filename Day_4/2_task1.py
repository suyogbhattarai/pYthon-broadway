a = [(4, 12, 5), (6, 1), (11, 12), (6, 7, 8)]

def get_last_element(element):
    return element[-1]

a.sort(key=get_last_element)
print(a)



