'''
Example test
'''
from module import total
import pytest
import sys

@pytest.mark.skipif(sys.version_info > (3,8), reason="Do not test for python 3.8 and higher")
def test_total_empty() -> None:
    assert total([]) == 0.0

@pytest.mark.skip(reason = 'reason of skip')
def test_total_single_item() -> None:
    assert total([110]) == 110.0

def test_total_many_items() -> None:
    assert total([1,2,3]) == 6.0

@pytest.mark.parametrize('testlist, result',
                        [
                            ([], 0.0),
                            ([110], 110.0),
                            ([1,2,3], 6.0)
                        ]
                        )
def test_total(testlist, result):
    assert total(testlist) == result