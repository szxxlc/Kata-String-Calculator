def Add(numbers):
    numbers = numbers.replace("\n", ",")
    if numbers == "":
        return 0
    if numbers[-1] == "," or numbers[0] == ",":
        raise ValueError
    for i in range(len(numbers)):
        if numbers[i] == "," and numbers[i+1] == ",":
            raise ValueError
    else:
        numbers_list = map(int, numbers.split(","))
        if numbers_list:
            return sum(numbers_list)
        else:
            raise ValueError