from autocurry import autocurry


# noinspection PyMethodMayBeStatic,PyCallingNonCallable
class TestAutocurryDecorator(object):

    def test_positional_arguments(self):
        @autocurry
        def add(a, b, c):
            return a + b + c

        assert add(1, 2, 3) == 6
        assert add(1, 2)(3) == 6
        assert add(1)(2, 3) == 6
        assert add(1)(2)(3) == 6

    def test_named_arguments(self):
        @autocurry
        def add(a, b, c=0):
            return a + b + c

        assert add(2, 3) == 5
        assert add(2)(3) == 5
        assert add(1, 1, c=3) == 5
        assert add(1)(1, c=3) == 5
        assert add(c=3)(1, 1) == 5
        assert add(c=3)(1)(1) == 5

    def test_argument_lists(self):
        @autocurry
        def add(a, b, *args):
            return a + b + sum(args)

        assert add(1, 2) == 3
        assert add(1)(2) == 3
        assert add(1)(2, 3, 4) == 10
        assert add(1, 2, *[3, 4]) == 10
        assert add(1)(2, *[3, 4]) == 10