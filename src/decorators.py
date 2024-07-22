def log(file_name=None):
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
