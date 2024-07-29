def log(file_name=None):
    """ Декоратор для логирования вызовов функции.
    Параметры:
    file_name (str): Название файла для логов. Если не указан, лог выводится в консоль.
     """

    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                message = f"{func.__name__} ok \n"
                if not file_name:
                    print(message)
                else:
                    with open(file_name, "a") as file:
                        file.write(message)
                return result
            except Exception as error:
                message = f"{func.__name__} error: {error}. Inputs: {args} {kwargs}\n "
                if not file_name:
                    print(message)
                else:
                    with open(file_name, "a") as file:
                        file.write(message)

        return wrapper

    return decorator
