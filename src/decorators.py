def log(file_name: str = None) -> None:
    """Декоратор для логирования вызовов функции.
    Параметры:
    file_name (str): Название файла для логов. Если не указан, лог выводится в консоль.
    """

    def decorator(func) -> None:
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                message = f"{func.__name__} ok \n"
            except Exception as error:
                message = f"{func.__name__} error: {error}. Inputs: {args} {kwargs}\n "
                result = None
            if not file_name:
                print(message)
            else:
                with open(file_name, "a") as file:
                    file.write(message)
            return result

        return wrapper

    return decorator
