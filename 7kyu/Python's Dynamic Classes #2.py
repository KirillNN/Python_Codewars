class ReNameAbleClass(object):
    @classmethod
    def change_class_name(cls, new_name):
        if not new_name:
            raise Exception()
        if not new_name[0].isupper():
            raise Exception()
        if ' ' in new_name or '!' in new_name:
            raise Exception()
        cls.__name__ = new_name

    @classmethod
    def __str__(cls):
        return f'Class name is: {cls.__name__}'

