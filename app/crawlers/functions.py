def char_to_replace(s):

    char_to_replace = str.maketrans("₺TL,.", "   . ")
    
    result = s.translate(char_to_replace).strip().replace(' ', '')
    
    return result if result != '' else 0


def char_to_replace_separated_by_dots(s):
    
    char_to_replace = str.maketrans("₺TL,", "   .")
    
    result = s.translate(char_to_replace).strip().replace(' ', '')
    
    return result


def clear_price_text(s):

    remove_list = [" ", "\n", "Sepette", "Satış fiyatı", "YENİ", "Satışfiyatı", "/Kg", "/KG", "/kg", "KG", "Kg", "kg", "2Al1Öde", "YeniÜrün", "2si%70", "2si%50", "3Al2Öde", "6Al5Öde", "2si%36", "4Al3Öde", "2si%50", "Hediyeli", "'2si%50'"]

    for remove in remove_list:

        s = s.replace(remove, "")

    result = s
    
    return result


def clear_text(s):
    result = ""
    t = s.replace("\n", "")
    l = t.split(" ")
    
    for i in l:
        if i:
            result += i.strip() + ' '


    return result


def get_image_on_css(s, main_url):

    c = s.split("'")
    
    image_url = c[1]
    return main_url + image_url

def set_image_size(s, size):
    
    result = s.format(width = size)
    
    
    return result


def clear_price(s):

    price = s.split("\n")

    return char_to_replace_separated_by_dots(price[0])



def get_image_url(s):

    att = s.split('" ')
    for i in att:
        if "data-srcset" in i:
            src_set = i.split(", ")
            image_url = src_set[0].split(" ")
            
            return image_url[0].replace('data-srcset="', '')
    
    
    