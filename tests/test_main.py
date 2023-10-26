from proj.main import pos_or_neg
import pytest

from contextlib import nullcontext as does_not_raise


@pytest.mark.parametrize('x, res, exp', [(25, 'positive', does_not_raise()), (25.5, 'positive', does_not_raise()), (0.05, 'positive', does_not_raise()), (-25, 'negative', does_not_raise()), (-25.5, 'negative', does_not_raise()), (-0.0000000005, 'negative', does_not_raise()), (0, 'zero', does_not_raise()), ('insdfsf', 'Error', pytest.raises(TypeError))])


def test_pon_int(x, res, exp):
	with exp:
		assert pos_or_neg(x) == res