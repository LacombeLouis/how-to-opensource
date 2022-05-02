import pytest
import numpy as np

from how_to_opensource import add_two_vectors
from typing import Union, Tuple
from numpy.typing import ArrayLike


@pytest.mark.parametrize("shape", [1, 2, (1, 2), (2, 3, 4)])
def test_add_two(shape: Union[int, Tuple[int]]) -> None:
    """Test it properly adds two vectors."""
    a: ArrayLike
    b: ArrayLike
    a = 2 * np.ones(shape)
    b = - np.ones(shape)
    results: ArrayLike
    results = add_two_vectors(a, b)
    expected: ArrayLike
    expected = np.ones(shape)
    np.testing.assert_almost_equal(results,  expected)
