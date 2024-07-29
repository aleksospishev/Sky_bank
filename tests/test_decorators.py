from src.decorators import log


@log()
def function_error() -> None:
    raise Exception("Ошибка")


@log()
def function_int() -> int:
    return 5


@log(file_name="test_1.txt")
def function_file() -> str:
    return "Hello"


def test_log_decorator(capsys) -> None:
    function_error()
    captured = capsys.readouterr()
    assert captured.out == "function_error error: Ошибка. Inputs: () {}\n \n"


def test_log_decorator_int(capsys) -> None:
    function_int()
    captured = capsys.readouterr()
    assert captured.out == "function_int ok \n\n"


def test_decorator_file() -> None:
    function_file()
    with open("test_1.txt", "r", encoding='utf-8') as file:
        result = file.read()
        assert result == "function_file ok \n"
    with open("test_1.txt", "w") as file:
        file.write('')
