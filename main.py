import sys
import random
from serializationTask import *


def generate_test_case(count=1000, min_val=1, max_val=300, flag=False):
    if flag:
        result = []
        for i in range(count):
            result.append(i//3)
        return result
    else:
        return [random.randint(min_val, max_val) for x in range(count)]


if __name__ == "__main__":
    test_cases = {
        "1": generate_test_case(50, 1, 300),
        "2": generate_test_case(100, 1, 300),
        "3": generate_test_case(500, 1, 300),
        "4": generate_test_case(1000, 1, 300),
        "5": generate_test_case(1000, 1, 9),
        "6": generate_test_case(1000, 10, 99),
        "7": generate_test_case(1000, 100, 300),
        "8": generate_test_case(count=900, flag=True)
    }

    print("Результаты")

    compression_ratios_sum = 0
    for i in range(1, 9):
        print(f"Тестовый случай {i}")
        print(test_cases[f"{i}"])
        simple_ser = simple_serialization(test_cases[f"{i}"])
        print(f"Строка {i} сериализованная без сжатия")
        print(simple_ser)
        ser = serialization(test_cases[f"{i}"])
        print(f"Строка {i} сериализованная cо сжатием")
        print(ser)
        size_simple_ser = sys.getsizeof(simple_ser)
        size_ser = sys.getsizeof(ser)
        compression_ratio = size_simple_ser / size_ser
        print(f"Коэффициент сжатия для строки {i} = {round((compression_ratio - 1) * 100, 2)} %")
        de_ser = deserialization(ser)
        print(f"Десериализованная строка {i}")
        print(de_ser)
        print("\n\n")
        compression_ratios_sum += sys.getsizeof(simple_serialization(test_cases[f"{i}"])) / sys.getsizeof(serialization(test_cases[f"{i}"]))
    avg_compression_ratio = (compression_ratios_sum / 8 - 1) * 100

    print(f"Средний коэффициент сжатия = {round(avg_compression_ratio, 2)} %")
