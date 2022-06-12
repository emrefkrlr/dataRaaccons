def char_to_replace(s):

    char_to_replace = str.maketrans("₺TL,.", "   . ")
    result = s.translate(char_to_replace).strip().replace(' ', '')
    
    return result