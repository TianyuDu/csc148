def hello(n):
    print("h:",n)
    if n < 2:
        r = world(n, n + 1)
        print("back from world", r, n)
        return r
    else:
        r = hello(n - 1)
        print("back from hello", r, n)
        return r

def world(x, y):
    # here
    print("world:", x, y)
    return x + y

if __name__ == "__main__":
    print("main")
    r = hello(2)
    print("back from hello", r)