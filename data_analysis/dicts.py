def create_dict_from_user_input():
    """
    Create a dictionary from user input.

    :return: A dictionary with user-defined keys and values.
    """
    data_input = input("Enter your data as key-value pairs (key:value, key:value): ")
    data_pairs = [pair.strip() for pair in data_input.split(",")]

    result_dict = {}
    for pair in data_pairs:
        if ':' in pair:
            key, value = pair.split(':', 1)
            # convert value to int if it is a number
            try:
                value = int(value.strip())
            except ValueError:
                pass
            result_dict[key.strip()] = value

    return result_dict


if __name__ == "__main__":
    # Example usage
    user_dict = create_dict_from_user_input()
    print(f"User created dictionary: {user_dict} of type {type(user_dict)}")