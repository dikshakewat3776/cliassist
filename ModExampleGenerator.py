from nltk.tokenize import word_tokenize
import  importlib
import pandas
import subprocess


def ModuleLocator(query : str):
    """
        Function to locate modules/ packages in environment and map them to preprocessed queries
    """
    # try:
    #     try:
    #         from pip._internal.operations import freeze
    #     except ImportError:  # pip < 10.0
    #         from pip.operations import freeze



        # x = freeze.freeze()
        # a = list()
        #----------------------------------------
        # for p in x:
        #     mod = p.split("==")
        #     mod_without_version = mod.pop(0)
        #     a.append(mod_without_version)
        # print(a)
        # --------------------------------
        # with open("pack.csv", "w") as fp:
        #     for i in a:
        #         fp.write(i + "\n")



    try:
        package_data = pandas.read_csv("pack.csv")
        package_name = None
        flag = 0

        tokens = word_tokenize(query)
        # print(tokens)
        for index, row in package_data.iterrows():
            for each in row:
                if each in tokens:
                    package_name = each
                    break
        if package_name is None:
            for i in tokens:
                if flag == 1:
                    break
                try:
                    importlib.import_module(i)
                    break
                except Exception as e:
                    while True:
                        package_name = input("Please input correct package name: ")
                        try:
                            if importlib.import_module(package_name):
                                print("Installed {}".format(package_name))
                                # subprocess.call("python3 -m pip install {}".format(package_name))
                                if package_name not in package_data:
                                    with open("pack.csv", "a+") as fp:
                                        fp.write(package_name + "\n")
                                    flag = 1
                                return package_name
                        except Exception as e:
                            print(e)
                            print("No Package with {} Found. Please Check and try again".format(package_name))
                            try:
                                subprocess.call("python3 -m pip install {}".format(package_name))
                                return package_name
                            except Exception as e:
                                print(e)
        return package_name
    except Exception as e:
        print(e)

    #         print(tokens)
    #         loc = None
    #         for i in tokens:
    #             if i not in a:
    #
    #                 loc = None
    #             else:
    #                 loc = i
    #         if loc is None:
    #             raise ModuleNotFoundError
    #         return loc
    #     except Exception as e:
    #         print(e)
    #         print("Tokenizing Error!!!")
    # except Exception as e:
    #     print(e)
    #     print("Module Locator Error!!!")





if __name__ == '__main__':
    query: str = "How read csv pandas"
    mymodule = ModuleLocator(query)
    print(mymodule)

