STRING_FILEPATH = "todos.txt"


def get_set_todos(bool_get=True, string_todo=None, string_filepath=STRING_FILEPATH):
    if type(bool_get) != bool:
        print("Type of get parameter must be boolean")
    else:
        if bool_get:
            with open(string_filepath, 'r') as file:
                return file.readlines()
        else:
            if string_todo == None:
                print("Todo must be defined")
            with open(string_filepath, 'w') as file:
                file.writelines(string_todo)


def get_todos(filepath=STRING_FILEPATH):
    with open(filepath, 'r') as file:
        todos_local = file.readlines()
    return todos_local


def write_todos(todos_arg, filepath=STRING_FILEPATH):
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)
