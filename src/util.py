def checkint(s,up,low):
    try :
        d = int(s)
        if d > up:
            return False
        if d < low :
            return False
        return True
    except ValueError:
        return False
