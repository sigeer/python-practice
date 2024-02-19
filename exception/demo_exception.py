try:
    print("try start")
    # raise相当于throw
    raise Exception("python.raise = CSharp.throw")
    print("try end")
# except 相当于 catch
except Exception as ex:
    print(f'err: {ex}')
finally:
    print("finally")