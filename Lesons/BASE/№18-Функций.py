plus  = lambda a, b,*args,**kwargs: a + b + sum(args) % 2



def universal_analyzer(func, calls):
    q = []
    w = []
    for args, kwargs in calls:
        try:
           q.append(func(*args, **kwargs))
        except Exception as e:
            print(f'Ошибка при вызове с args={args}, kwargs={kwargs}: {e}')

    d = {}
    for i in q:
        d[i] = d.get(i, 0) + 1

    result = sorted(d.items(), key=lambda x: x[1], reverse=True)

    print(result)



l = [
    ([1], {}),  # fx(1)
    ([1, 2], {}),  # fx(1, 2)
([2, 3, 4], {}),  # fx(2, 3, 4)
([1], {'b': 2}),  # fx(1, b=2)
([1, 2], {}),  # fx(1, 2)
([2, 3], {}),  # fx(2, 3)
([2], {'b': 3, 'x': 0})]

universal_analyzer(plus,l)
