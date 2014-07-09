def implode(glue, pieces):
    return str(glue).join(map(str, pieces))

#TODO: Negative limit is not yet working
def explode(delimiter, string, limit = None):
    if limit is None:
        return string.split(delimiter)
    else:
        return string.split(delimiter, limit)
            