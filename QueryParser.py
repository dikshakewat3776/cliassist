import string
import nltk
from nltk.corpus import stopwords


def QueryParser(query : str):
    """
    Function to preprocess text based queries and extract necessary features
    """
    try:
        all_punctuations = string.punctuation + '‘’,:”][],'

        # Method to remove punctuation marks from the data
        def punc_remover(query):
            no_punct = "".join([i for i in query if i not in all_punctuations])
            return no_punct

        # Method to remove stopwords from the data
        def stopword_remover(no_punc_text):
            words = no_punc_text.split()
            no_stp_words = " ".join([i for i in words if i not in stopwords.words('english')])
            return no_stp_words

        # Method to lemmatize the words in the data
        # lemmer = nltk.stem.WordNetLemmatizer()

        # def lem(words):
        #     return " ".join([lemmer.lemmatize(word, 'v') for word in words.split()])

        # Method to perform a complete cleaning
        def text_cleaner(raw):
            cleaned_text = stopword_remover(punc_remover(raw))
            return cleaned_text

        clean_query = text_cleaner(query)
        return clean_query
    except Exception as e:
        print(e)
        print("Pre-processing Query Error!!!")


if __name__ == '__main__':
    query: str = "How to read csv in pandas?"
    r = QueryParser(query)
    print(r)
    print(type(r))
