class IDIterator:
    """
    Iterator class that generates valid ID numbers within a specified range.
    """

    def __init__(self, id_number):
        """
        Initializes the IDIterator object with the starting ID number.

        :param id_number: The starting ID number.
        :type id_number: int
        """
        self.id_ = id_number

    def __iter__(self):
        """
        Returns the iterator object itself.

        :return: The iterator object.
        """
        return self

    def __next__(self):
        """
        Generates the next valid ID number.

        :return: The next valid ID number.
        """
        if self.id_ >= 999999999:
            raise StopIteration
        self.id_ += 1
        while not check_id_valid(self.id_):
            self.id_ += 1
        return self.id_


def check_id_valid(id_number):
    """
    Checks the validity of an ID number.

    :param id_number: The ID number to check.
    :type id_number: int
    :return: True if the ID number is valid, False otherwise.
    :rtype: bool
    """
    id_str = str(id_number)
    if len(id_str) != 9:
        return False
    if not id_str.isdigit():
        return False
    if id_number < 100000000 or id_number > 999999999:
        return False
    id_digits = [int(digit) for digit in id_str]
    multiplied_digits = [digit * (2 if i % 2 == 0 else 1) for i, digit in enumerate(id_digits)]
    summed_digits = [digit // 10 + digit % 10 if digit > 9 else digit for digit in multiplied_digits]
    return sum(summed_digits) % 10 == 0


def main():
    id_number = int(input("Enter ID: "))
    iterator = IDIterator(id_number)
    id_list = [next(iterator) for _ in range(10)]
    for id_num in id_list:
        print(id_num)


if __name__ == "__main__":
    main()
