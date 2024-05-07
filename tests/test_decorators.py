from src.decorators import my_function

def test_my_function() -> None:
    assert my_function(3, 4) == 7
    assert my_function(4, 5) == 9
    assert my_function(1, 2) == 3
