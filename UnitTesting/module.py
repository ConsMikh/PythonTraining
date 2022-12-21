
from typing import List

def total(xs: List[float]) -> float:
    result: float = 0.0
    for x in xs:
        result += x
    return result