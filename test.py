x = {'11A': ('11B', 'XXX'),
     '11B': ('XXX', '11Z')}


print(x.get(x.get("11A")[0])[0])