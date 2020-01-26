def handle_error_by_throwing_exception():
    raise Exception("Really useful description.")


def handle_error_by_returning_none(input_data):
    value = None

    try:
        value = int(input_data)
    
    finally:    
        return value


def handle_error_by_returning_tuple(input_data):
    operation_successful = False
    value = input_data

    try:
        value = int(input_data)
        operation_successful = True
    
    finally:
        return (operation_successful, value)


def filelike_objects_are_closed_on_exception(filelike_object):
    try:
        filelike_object.do_something()

    finally:
        filelike_object.close()
