def naturals(value, stop):
    if(value > stop):
        return

    if(value <= stop):
        print(value, end=" ")
        naturals(value + 1, stop)

naturals(1, 50)