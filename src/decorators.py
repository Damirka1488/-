from datetime import datetime
from functools import wraps
from typing import Any, Callable


def log(filename: str | None = None) -> Callable:
    """Декоратор, который логирует вызов функции с именем и временем."""

    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                result = func(*args, **kwargs)
                current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                log_message = f"{current_time} {func.__name__} ok"
                if filename:
                    with open(filename, "a", encoding="utf-8") as log_file:
                        log_file.write(f"{log_message}\n")
                else:
                    print(log_message)
                return result
            except Exception as e:
                current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                error_message = f"{current_time} {func.__name__} error: {type(e).__name__}. Inputs: {args}, {kwargs}"
                if filename:
                    with open(filename, "a", encoding="utf-8") as log_file:
                        log_file.write(f"{error_message}\n")
                else:
                    print(error_message)
                raise

        return wrapper

    return decorator


@log("mylog.txt")
def my_function(element_one: int, element_two: int) -> int:
    """Складывает два элемента."""
    return element_one + element_two


my_function(3, 4)
