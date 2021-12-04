def outer():
    x = "local"

    def inner():
        nonlocal x  # we are inheriting the outer function x value
        x = "nonlocal"  # we are assigning value  to the x
        print("inner: ", x)
    inner()
    print("outer: ", x)


outer()
