def rate_of_change(last, now):


    last = last if last != 0 else 1
    now = now if now != 0 else 1
    
    rate = ((now-last)/last)*100

    return round(rate,2)


def rate(p1, p2):

    p2 = p2 if p2 != 0 else 1
    rate = (p1/p2)*100

    return round(rate,2)

