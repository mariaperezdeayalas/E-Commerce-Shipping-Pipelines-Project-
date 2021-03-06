
import pandas as pd

def load_csv():
    return pd.read_csv("data/Train.csv", encoding = "ISO-8859-1")

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


def loyal_customer(x):
    if x < 5:
        return 'Not Loyal'
    else:
        return 'Loyal'

def customer_rating(x):
    if x < 4:
        return 'Rating 1 - 3'
    else:
        return 'Rating 4 - 5'