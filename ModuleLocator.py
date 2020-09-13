from nltk.tokenize import word_tokenize


def ModuleLocator(query : str):
    """
        Function to locate modules/ packages in environment and map them to preprocessed queries
    """
    try:
        try:
            from pip._internal.operations import freeze
        except ImportError:  # pip < 10.0
            from pip.operations import freeze

        x = freeze.freeze()
        a = list()

        for p in x:
            mod = p.split("==")
            mod_without_version = mod.pop(0)
            a.append(mod_without_version)
        try:
            tokens = word_tokenize(query)
            loc = None
            for i in tokens:
                if i not in a:
                    loc = None
                else:
                    loc = i
            if loc is None:
                raise ModuleNotFoundError
            return loc
        except Exception as e:
            print(e)
            print("Tokenizing Error!!!")
    except Exception as e:
        print(e)
        print("Module Locator Error!!!")


if __name__ == '__main__':
    query: str = "How read csv pandas"
    mymodule = ModuleLocator(query)
    print(mymodule)

