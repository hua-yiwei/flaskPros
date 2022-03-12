"""
能使用 obj["key"] = "value" 这种形式的，必定是对象中有__setitem__方法，要嘛就是继承的父类中有__setitem__方法
"""
class Foo(object):
    pass


class Foo2(object):
    def __setitem__(self, key, value):
        pass


class Foo3(dict):
    pass


if __name__ == '__main__':
    obj = Foo()
    # obj["name"] = "w"    # 会报错

    obj2 = Foo2()
    obj2["name"] = "这是2"  # 不报错

    obj3 = Foo3()
    obj3["name"] = "这是3"  # 不报错
