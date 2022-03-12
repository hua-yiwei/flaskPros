class Foo:

    def fetch(self):
        pass


Foo.fetch(123)

obj = Foo()

print(Foo.fetch)  # 函数
print(obj.fetch)  # 方法
