import importlib


def FunctionsExtract(module_name : str):
    mymodule = importlib.import_module(module_name)
    all_functions = dir(mymodule)
    return all_functions


if __name__ == '__main__':
    module_name = "pandas"
    functionsList = FunctionsExtract(module_name)
    print(functionsList)
