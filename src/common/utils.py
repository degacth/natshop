def remove_list(src, l):
    reduce(lambda last, i: src.remove(i), l)
    return src
