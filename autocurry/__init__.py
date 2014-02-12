from inspect import getargspec

__all__ = ['autocurry']


class autocurry(object):

    def __init__(self, f, *fargs, **fkwargs):
        self.f = f
        self.fargs = fargs
        self.fkwargs = fkwargs or {}
        self.__name__ = f.__name__

    def __call__(self, *args, **kwargs):
        # merge arguments from previous call with current call
        args = self.fargs + args
        self.fkwargs.update(kwargs)

        # determine number of non-keyword args
        arg_spec = getargspec(self.f)
        num_args = len(arg_spec[0])
        num_args -= len(arg_spec[3]) if arg_spec[3] else 0  # subtract number of arguments which have default values

        # if not enough args are supplied return a curried function
        if len(args) < num_args:
            return autocurry(self.f, *args, **self.fkwargs)
        else:
            return self.f(*args, **self.fkwargs)
