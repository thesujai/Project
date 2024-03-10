try:
    print(1/0)
except ZeroDivisionError as e:
    print(e.with_traceback(None))