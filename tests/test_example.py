import random

import pytest

from rye_template import fermat_primality_test

random.seed(42)


@pytest.mark.parametrize(
    "n, k, expected",
    [
        (2, 100, True),
        (3, 100, True),
        (4, 100, False),
        (5, 100, True),
        (6, 100, False),
        (7, 100, True),
        (8, 100, False),
        (9, 100, False),
        (10, 100, False),
        (11, 100, True),
        (12, 100, False),
        (13, 100, True),
        (14, 100, False),
        (15, 100, False),
        (16, 100, False),
        (17, 100, True),
        (18, 100, False),
        (19, 100, True),
        (20, 100, False),
        (21, 100, False),
        (22, 100, False),
        (23, 100, True),
        (24, 100, False),
        (25, 100, False),
        (26, 100, False),
        (27, 100, False),
        (28, 100, False),
        (29, 100, True),
        (30, 100, False),
        (31, 100, True),
        (32, 100, False),
        (33, 100, False),
        (34, 100, False),
        (35, 100, False),
        (36, 100, False),
        (37, 100, True),
        (38, 100, False),
        (39, 100, False),
        (40, 100, False),
        (41, 100, True),
        (42, 100, False),
        (43, 100, True),
        (44, 100, False),
        (45, 100, False),
        (46, 100, False),
        (47, 100, True),
        (48, 100, False),
        (49, 100, False),
        (50, 100, False),
        (51, 100, False),
        (52, 100, False),
        (53, 100, True),
        (54, 100, False),
        (55, 100, False),
    ],
)
def test_fermat_primality_test(n, k, expected):
    assert fermat_primality_test(n, k) == expected
