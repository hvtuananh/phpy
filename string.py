def explode(delimiter, string, limit = None):
    if limit is None:
        return string.split(delimiter)
    else:
        if limit < 0:
            return string.split(delimiter, limit)[:limit]
        else:
            return string.split(delimiter, limit)
            
def implode(glue, pieces):
    return str(glue).join(map(str, pieces))

def join(glue, pieces):
    return implode(glue, pieces)
    
def ltrim(string, character_mask = " \t\n\r\0\x0B"):
    return string.lstrip(character_mask)

def rtrim(string, character_mask = " \t\n\r\0\x0B"):
    return string.rstrip(character_mask)
        
def strlen(string):
    return len(string)
    
def trim(string, character_mask = " \t\n\r\0\x0B"):
    return string.strip(character_mask)