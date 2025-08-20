def combine_and_sort_lists(list1: list, list2: list, list3: list):
    """
    Combines three lists into one.

    Args:
        list1 (list): First list.
        list2 (list): Second list.
        list3 (list): Third list.

    Returns:
        list: Combined list.
    """
    combined_list = list1 + list2 + list3
    return sorted(combined_list)

def course_list_operations() -> list:
    # add a loop to operate as menu asking user for desired operation, possible operations:
    # 1. Add a course
    # 2. Remove a course
    # 3. Display all courses in cappital letters
    # 4. Display all courses in lowercase letters
    # 5. Display all courses in reverse order
    # 6. Display all courses in sorted order
    # 7. Count the number of course entries
    # 8. Exit the program
    courses = []
    while True:
        print("\nCourse List Operations:")
        print("1. Add a course")
        print("2. Remove a course")
        print("3. Display all courses in capital letters")
        print("4. Display all courses in lowercase letters")
        print("5. Display all courses in reverse order")
        print("6. Display all courses in sorted order")
        print("7. Count the number of course entries")
        print("8. Exit the program")

        choice = input("Enter your choice (1-8): ")

        if choice == '1':
            course = input("Enter the course name to add: ")
            courses.append(course)
            print(f"Course '{course}' added.")
        elif choice == '2':
            course = input("Enter the course name to remove: ")
            if course in courses:
                courses.remove(course)
                print(f"Course '{course}' removed.")
            else:
                print(f"Course '{course}' not found.")
        elif choice == '3':
            print("Courses in capital letters:", [c.upper() for c in courses])
        elif choice == '4':
            print("Courses in lowercase letters:", [c.lower() for c in courses])
        elif choice == '5':
            print("Courses in reverse order:", list(reversed(courses)))
        elif choice == '6':
            print("Courses in sorted order:", sorted(courses))
        elif choice == '7':
            course = input("Enter the course name to count: ")
            if course in courses:
                x = courses.count(course)
            else:
                print(f"Course '{course}' not found.")
            print(f"Number of course entries: {x}")
        elif choice == '8':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice, please try again.")
    return courses

if __name__ == "__main__":
    # Example usage of course_list_operations
    print("Final course list:", course_list_operations())

