def parse(measurement):
    ft_inch_list = measurement.split(" ")
    feet = float(ft_inch_list[0])
    inches = float(ft_inch_list[1])
    return feet, inches
