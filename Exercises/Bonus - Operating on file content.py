def get_average():
    with open("../files/data.txt", "r") as file:
        data = file.readlines()

    values = data[1:]  #remove the tempratture string
    values = [float(num) for num in values]
    avg = sum(values)/len(values)
    return avg

print(get_average())