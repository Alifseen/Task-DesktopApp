def convert(feet, inches):
    inches_to_meter = ((feet * 12)+inches) / 39.37
    # return f"meters: {inches_to_meter}, inches: {inches}, feet: {feet}"
    return "{:.3f}".format(inches_to_meter)
