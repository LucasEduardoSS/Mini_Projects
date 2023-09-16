def calc_media_pesos(tasks: list):
    """Return the average of a list."""

    if len(tasks) > 0:
        # List comprehension systas: newlist = [expression for item in iterable if condition == True]
        return sum([peso["Peso"] for peso in tasks], 0)/len(tasks)
    else:
        return 'Lista vazia'
