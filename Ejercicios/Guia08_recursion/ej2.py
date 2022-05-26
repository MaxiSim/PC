def digit_count(num, digits = 0) -> int:
    if num == 0:
        if digits != 0:
            return digits
        else:
            return 1
    else:
        return digit_count(num // 10, digits +1)
print(digit_count(128))