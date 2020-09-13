from Cli import cli_query
from QueryParser import QueryParser
from ModuleLocator import ModuleLocator
from FunctionsExtract import FunctionsExtract
from FeatureLocator import FeatureLocator
from ModuleImports import ModuleImports

if __name__ == '__main__':
    try:
        userQuery = cli_query()
        parsedQuery = QueryParser(userQuery)
        # print("parsedQuery:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
        # print(parsedQuery)
        modulesFound = ModuleLocator(parsedQuery)
        # print("modulesFound:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
        # print(modulesFound)
        functionsList = FunctionsExtract(modulesFound)
        # print("functionsList:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
        # print(functionsList)
        functionFound = FeatureLocator(parsedQuery, functionsList, modulesFound)
        # print("functionFound:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
        # print(functionFound)
        resFunction = str(modulesFound) + "." + str(functionFound)
        print("COMMAND ::::::::::::::::::::::::::::::" + "\n" + str(resFunction))
        # funcExample = ModExampleGenerator(modulesFound, resFunction)
        # print("EXAMPLES::::::::::::::::::::::::::::::::::" + str(funcExample))
        try:
            keys = []
            values = []
            try:
                ModuleImports(modulesFound)
            except Exception:
                raise ImportError

            try:
                locals()[modulesFound] = __import__(modulesFound)
            except Exception:
                raise ImportError

            each = str(eval(resFunction + '.__doc__'))
            each = "\n\n".join([each.strip() for each in each.split("\n\n") if each])
            each = "\n".join([each.strip() for each in each.split("\n") if each])

            for char in range(len(each)):
                updated_index = 0
                if (each[char] == "\n"):
                    if (char + 1) == len(each):
                        break
                    if each[char + 1] == "-" or each[char + 1] == "=":
                        if each[char + 2] == each[char + 1]:
                            for index in range(char - 1, 0, -1):
                                if each[index] == "\n":
                                    updated_index = index + 1
                                    break
                            keys.append(each[updated_index:char])
                            updated_index = 0
                            values.append(each[char:])

            dictionary = {}
            for each in range(len(keys)):
                dictionary[keys[each]] = values[each]
            examples = dictionary.get('Examples')
            print("EXAMPLES ::::::::::::::::::::::::::::::" + "\n")
            if examples is not None:
                print(examples)
            else:
                print(each)
        except Exception as e:
            print(e)
            print("Module Example Not Found Error!!!")
    except Exception as e:
        print(e)
