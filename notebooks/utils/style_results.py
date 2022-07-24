def style_positive(v, props=''):
    if isinstance(v, str):
        return None
    if (v >= 80): 
        return props
    else:
        return None
    return props 

def style_medium(v, props=''):
    if isinstance(v, str):
        return None
    if (v >= 50 and v < 80): 
        return props
    else:
        return None
    return props 

def style_negative(v, props=''):
    if isinstance(v, str):
        return None
    if (v < 50): 
        return props
    else:
        return None
    return props 

def style_positive_n(v, props=''):
    if isinstance(v, str):
        return None
    if (v <= 10): 
        return props
    else:
        return None
    return props 

def style_medium_n(v, props=''):
    if isinstance(v, str):
        return None
    if (v > 10 and v <= 20): 
        return props
    else:
        return None
    return props 

def style_negative_n(v, props=''):
    if isinstance(v, str):
        return None
    if (v > 20): 
        return props
    else:
        return None
    return props 
