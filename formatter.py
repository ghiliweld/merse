from query import query


def formatter(g, w, r):
    return f'🔵 Google \n   {g} \n' + f'⚪  Wikipedia \n    {w} \n' + f'🔶Reddit \n    {r} \n'


print(formatter(**query('bitcoin')))
