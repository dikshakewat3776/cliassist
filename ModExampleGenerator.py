from ModuleImports import ModuleImports


def ModExampleGenerator(module_name : str, function_name : str):
    try:
        keys = []
        values = []
        try:
            ModuleImports(module_name)
        except Exception:
            raise ImportError

        try:
            locals()[module_name] = __import__(module_name)
        except Exception:
            raise ImportError
        print(function_name + '.__doc__')
        each = str(eval(function_name + '.__doc__'))
        # print(each)
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
        if examples is not None:
            return examples
        else:
            return each
    except Exception as e:
        print(e)
        print("Module Example Not Found Error!!!")


if __name__ == '__main__':
    module_name = "requests"
    function_name = "requests.post"
    funcExample = ModExampleGenerator(module_name, function_name)
    print(funcExample)


