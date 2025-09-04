def create_tuple(name: str, data: list) -> tuple:
    """
    Create a tuple with a name and a list of data.

    :param name: The name to be included in the tuple.
    :param data: The list of data to be included in the tuple.
    :return: A tuple containing the name and the data.
    """
    return name, *data

def create_tuple_from_user_input():
    """
    Create a tuple from user input.

    :return: A tuple containing the user's name and their data.
    """
    data_input = input("Enter your data (comma-separated): ")
    data = [int(x.strip()) for x in data_input.split(",") if x]
    return tuple(data)

if __name__ == "__main__":
    # Example usage
    name = "Example"
    data = [1, 2, 3]
    result = create_tuple(name, data)
    print(f"Created tuple: {result}")

    # Create tuple from user input
    user_tuple = create_tuple_from_user_input()
    print(f"User created tuple: {user_tuple} of type {type(user_tuple)}")