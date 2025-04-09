 
from feedback_entry import collect_feedback
from score_calculator import calculate_average

def test_collect_feedback():
    assert isinstance(collect_feedback(), str)  # Basic type check

def test_calculate_average():
    assert calculate_average([70, 80, 90]) == 90.0
    assert calculate_average([]) == 0