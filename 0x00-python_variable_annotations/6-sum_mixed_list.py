#!/usr/bin/env python3
'''Complex types - mixed list'''

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    '''retun sum of the list'''
    return float(sum(mxd_lst))
