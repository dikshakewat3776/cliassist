from nltk.tokenize import word_tokenize
import itertools
import jellyfish

def closeMatchFinder(sentence, words):
    """
     returns a list comprising of the desired sentences most similar to words
    :param sentence:
    :param words:
    :return:
    """
    res = [all([k in s for k in words]) for s in sentence]
    return [sentence[i] for i in range(0, len(res)) if res[i]]


def functionLocator(reducedList: list, query: str):
    """
     returns a function comprising of the most similar function to queries
    :param reducedList:
    :param query:
    :return:
    """
    try:
        scores = {}
        for i in reducedList:
            a = jellyfish.jaro_distance(i, query)
            scores[i] = a
        max_key = max(scores, key=scores.get)
        return max_key
    except Exception as e:
        print(e)
        print("Function Locator Error!!!!")


def FeatureLocator(query: str, functionsList : list,  moduleName : str):
    """
        Function to locate associated features based on preprocessed queries to conclude functions
    """
    try:
        tokens = word_tokenize(query)
        closeMatchList = list()
        for word in tokens:
            matches = closeMatchFinder(functionsList, word)
            closeMatchList.append(matches)
        mergedList = list(itertools.chain.from_iterable(closeMatchList))
        try:
            if moduleName in tokens:
                if moduleName in mergedList:
                    tokens.remove(moduleName)
                    mergedList.remove(moduleName)
                else:
                    pass
            else:
                pass
        except Exception as e:
            print(e)
        funcc = functionLocator(mergedList, query)
        return funcc
    except Exception as e:
        print(e)
        print("Feature Locator Error!!!")


if __name__ == '__main__':
    query: str = "How read csv pandas"
    allfunctions = ['BooleanDtype', 'Categorical', 'CategoricalDtype', 'CategoricalIndex', 'DataFrame', 'DateOffset', 'DatetimeIndex', 'DatetimeTZDtype', 'ExcelFile', 'ExcelWriter', 'Float64Index', 'Grouper', 'HDFStore', 'Index', 'IndexSlice', 'Int16Dtype', 'Int32Dtype', 'Int64Dtype', 'Int64Index', 'Int8Dtype', 'Interval', 'IntervalDtype', 'IntervalIndex', 'MultiIndex', 'NA', 'NaT', 'NamedAgg', 'Period', 'PeriodDtype', 'PeriodIndex', 'RangeIndex', 'Series', 'SparseDtype', 'StringDtype', 'Timedelta', 'TimedeltaIndex', 'Timestamp', 'UInt16Dtype', 'UInt32Dtype', 'UInt64Dtype', 'UInt64Index', 'UInt8Dtype', '__builtins__', '__cached__', '__doc__', '__docformat__', '__file__', '__getattr__', '__git_version__', '__loader__', '__name__', '__package__', '__path__', '__spec__', '__version__', '_config', '_hashtable', '_is_numpy_dev', '_lib', '_libs', '_np_version_under1p16', '_np_version_under1p17', '_np_version_under1p18', '_testing', '_tslib', '_typing', '_version', 'api', 'array', 'arrays', 'bdate_range', 'compat', 'concat', 'core', 'crosstab', 'cut', 'date_range', 'describe_option', 'errors', 'eval', 'factorize', 'get_dummies', 'get_option', 'infer_freq', 'interval_range', 'io', 'isna', 'isnull', 'json_normalize', 'lreshape', 'melt', 'merge', 'merge_asof', 'merge_ordered', 'notna', 'notnull', 'offsets', 'option_context', 'options', 'pandas', 'period_range', 'pivot', 'pivot_table', 'plotting', 'qcut', 'read_clipboard', 'read_csv', 'read_excel', 'read_feather', 'read_fwf', 'read_gbq', 'read_hdf', 'read_html', 'read_json', 'read_orc', 'read_parquet', 'read_pickle', 'read_sas', 'read_spss', 'read_sql', 'read_sql_query', 'read_sql_table', 'read_stata', 'read_table', 'reset_option', 'set_eng_float_format', 'set_option', 'show_versions', 'test', 'testing', 'timedelta_range', 'to_datetime', 'to_numeric', 'to_pickle', 'to_timedelta', 'tseries', 'unique', 'util', 'value_counts', 'wide_to_long']
    modulename = "pandas"
    features = FeatureLocator(query, allfunctions, modulename)
    print(features)
