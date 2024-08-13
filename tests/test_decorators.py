from src.decorators import log


@log()
def function_error() -> None:
    """Тест с ошибкой."""
    raise Exception("Ошибка")


@log()
def function_int() -> int:
    """Тест возвращаем Int."""
    return 5


@log(file_name="test_1.txt")
def function_file() -> str:
    """Тест чтение из файла."""
    return "Hello"


def test_log_decorator(capsys) -> None:
    """Тест чтение логов из консоли ошибка."""
    function_error()
    captured = capsys.readouterr()
    assert captured.out == "function_error error: Ошибка. Inputs: () {}\n \n"


def test_log_decorator_int(capsys) -> None:
    """Чтение из консоли функция ок."""
    function_int()
    captured = capsys.readouterr()
    assert captured.out == "function_int ok \n\n"


def test_decorator_file() -> None:
    """Чтение логов из файла."""
    function_file()
    with open("test_1.txt", "r", encoding="utf-8") as file:
        result = file.read()
        assert result == "function_file ok \n"
    with open("test_1.txt", "w") as file:
        file.write("")
