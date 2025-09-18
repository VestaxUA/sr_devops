def even_odd_generator():
    toggle = True
    while True:
        if toggle:
            yield "Парне"
        else:
            yield "Непарне"
        toggle = not toggle