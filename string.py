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