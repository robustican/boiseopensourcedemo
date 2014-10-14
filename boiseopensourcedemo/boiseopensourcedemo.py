# -*- coding: utf-8 -*-


def a_cool_method(p1):
    """ This method does something cool with p1

    :param p1: an integer

    :raises NotImplementedError: When p1 is not an integer

    :returns: an integer
    """
    if not isinstance(p1, int):
        raise NotImplementedError("You must pass an int")

    return p1 * 5 