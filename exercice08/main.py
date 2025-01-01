def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Appel de la fonction {func.__name__} avec les arguments {args} et {kwargs}")
        result = func(*args, **kwargs)
        print(f"Résultat de la fonction {func.__name__} : {result}")
        return result

    return wrapper
 
@log_decorator
def function_test():
    print("Cette fonction ne prend pas d'arguments.")

function_test()
