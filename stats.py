def get_num_words(content):
    return len(content.split())

def get_char_count(content):
    obj = {}

    for x in content:
        key = x.lower()
        if key not in obj:
            obj[key] = 1
        else:
            obj[key] += 1
    
    return obj

def get_sorted_list(chars_dict):
    chars_list = []
    for key in chars_dict:
        chars_list.append({
            'label': key,
            'count': chars_dict[key]
        })

    chars_list.sort(reverse=True, key=lambda x: x['count'])

    return chars_list