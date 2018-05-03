#!/usr/bin/env python
# -*- coding: utf-8 -*-


def singleton(cls, *args, **kwargs):
    """make your the class in singleton design pattern.

    Args:
        cls: the class

    Examples:

        @singleton
        class TestClass(object):
            pass

        # the old way to declare an object
        obj_1 = TestClass()
        obj_2 = TestClass()
    """
    instances = {}

    def _singleton(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)

        return instances[cls]

    return _singleton


if __name__ == '__main__':

    @singleton
    class TestClass(object):
        pass

    obj_test_1 = TestClass()
    obj_test_2 = TestClass()
    print 'obj_test_1', obj_test_1, id(obj_test_1)
    print 'obj_test_2', obj_test_2, id(obj_test_2)
    print 'obj_test_1 is obj_test_2', obj_test_1 is obj_test_2
