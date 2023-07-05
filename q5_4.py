class IDIterator:
    """
    Iterator class that generates valid ID numbers within a specified range.
    """

    def __init__(self, id_number):
        """
        Initializes the IDIterator object with the starting ID number.

        Args:
        :param self: self value
        :param id_number: id_number value
        :type self: object
        :type id_number: int
        :return:none
        """
        self.id_ = id_number

    def __iter__(self):
        """
        Returns the iterator object itself.

        return: IDIterator- The iterator object.
        rtype : object .
        
        """
        return self

    def __next__(self):
        """
        Generates the next valid ID number.

        return: The next valid ID number.
        rtype : int.
        Raises: StopIteration - If the ID number reaches the maximum limit.
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
    :param id_number: id_number value .
    :type id_number: int
    :return: The ID number to be checked.
    :rtype: bool: True if the ID number is valid, False otherwise.
    """
    id_str = str(id_number)
    if len(id_str) != 9:                # Check if ID number has 9 digits
        return False
    if not id_str.isdigit():            # Check if ID number contains only digits
        return False
    if id_number < 100000000:           # Check if ID number is greater than or equal to 100000000
        return False

    id_digits = [int(digit) for digit in id_str]     # Convert ID number to a list of digits
    multiplied_digits = [digit * (2 if i % 2 == 0 else 1) for i, digit in enumerate(id_digits)]     # Multiply digits by 1 or 2 based on their positions
    summed_digits = [digit // 10 + digit % 10 if digit > 9 else digit for digit in multiplied_digits]     # Sum the digits of numbers greater than 9
    return sum(summed_digits) % 10 == 0      # Check if the sum is divisible by 10 (valid ID number)


def id_generator(id_number):
        """    
      Generator function that yields the next valid ID number.    
    :param id_number: id_number value .
    :type id_number: int

    Yields:
        int: The next valid ID number.
    """
    while id_number < 999999999:
        id_number += 1
        if check_id_valid(id_number):
            yield id_number


def main():
    """
    Main program that generates and prints new ID numbers based on user input.
    """
    id_number = int(input("Enter ID: "))
    generator_type = input("Generator or Iterator? (gen/it)? ")

    if generator_type == "it":
        iterator = IDIterator(id_number)
        id_list = [next(iterator) for _ in range(10)]
    elif generator_type == "gen":
        generator = id_generator(id_number)
        id_list = [next(generator) for _ in range(10)]
    else:
        print("Invalid input.")
        return

    for id_num in id_list:
        print(id_num)


if __name__ == "__main__":
    main()
