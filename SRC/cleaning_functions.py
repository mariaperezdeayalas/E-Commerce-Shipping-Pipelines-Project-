
def percentage_range(x):
    if x > 0 and x <= 20:
        return '(0% - 20%)'
    elif x > 20 and x <= 40:
        return '(21% - 40%)'
    elif x > 40 and x <= 60:
        return '(41% - 60%)'
    elif x > 60 and x <= 80:
        return '(61% - 80%)'
    else:
        return '(81% - 100%)'

        