def rate_of_change(current, previous):


    previous = previous if previous != 0 else 0.0000001
    current = current if current != 0 else 0.0000001
    
    rate = ((current-previous)/previous)*100

    return round(rate,2)


def rate(divisor, base):

    base = base if base != 0 else 1
    rate = (divisor/base)*100

    return round(rate,2)

