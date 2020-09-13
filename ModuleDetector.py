import importlib

def ModuleDetector(package_name : str):
  try:
    mymodule = importlib.import_module(package_name)
    modCheck = str(mymodule).startswith("<module ")
    if modCheck ==  True:
      decision = "Module"
    else:
      decision = "Not a Module"
    return decision
  except Exception as e:
    raise ModuleNotFoundError


if __name__ == '__main__':
  mod = ModuleDetector("numpy")
  print(mod)