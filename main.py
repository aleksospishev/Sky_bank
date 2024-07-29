from src.decorators import log


@log()
def main(x, y):
    res = x / y


if __name__ == "__main__":
    main(6
         )
