from subprocess import call


def ModuleImports(module_name : str):
    statement_import = "\n" "import" + " " + module_name
    file = open("myFile.py", "a+")
    file.write(statement_import)
    file.close()
    if call(["python3", "myFile.py"]):
        return True
    else:
        return False

