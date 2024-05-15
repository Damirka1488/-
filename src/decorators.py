from functools import wraps
from datetime import datetime
from typing import Callable, Any


def log(func: Callable, filename='') -> Callable:
    """Декоратор, который логирует вызов функции с именем и временем."""

    @wraps(func)
    def wrapper(args: Any, *kwargs: Any) -> Any:
        result_num = func(args, *kwargs)
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        try:
            with open(filename, 'a', encoding='utf-8') as log_file:
                log_file.write(f'{current_time} {func.__name__} ok\n')
        except FileNotFoundError:
            print(f'{current_time} {func.__name__} ok')
        return result_num

    return wrapper


@log
def my_function(element_one: int, element_two: int) -> int:
    """Складывает два элемента."""
    return element_one + element_two


# Пример
result = my_function(3, 4)
