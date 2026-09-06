def func1(*args, **kwargs):
    print(args)
    print(kwargs)

func1(1, 2, 4, 5, jack=34, jill=32, marie=31)
# you have to pass the args first then the kwargs this is the rule of that keep remember that in future code 