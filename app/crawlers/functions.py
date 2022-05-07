def char_to_replace(s):

    char_to_replace = {
        '₺': '',
        'TL': '', 
        ',': '.'
        }
    
    for key, value in char_to_replace.items():
        # Replace key character with value character in string
        result = s.replace(key, value)

    return result