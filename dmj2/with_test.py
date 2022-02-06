class TestWith():
    def __enter__(self):
        print('run------')
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_tb is None:
            print("没有异常，正常结束-------")
        else:
            print("代码出现异常： %s" %exc_tb)

with TestWith():
    print("Test is runing")
    raise  NameError('testNameError')