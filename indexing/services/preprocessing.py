import re
import json
import os
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
nltk.download('stopwords')


class preProcess:
    def __init__(self):
        return self
    
    def clean(query=""):
        if query == "":
            text_file = os.path.join(os.path.dirname(__file__), '../input_corpus.txt')
            text_data = open(text_file, 'r').readlines()
            tokenized_json = {}
            for each_line in text_data:
                each_line = re.split(r'\t+', each_line.rstrip('\t'))
                doc_id = each_line[0]
                line =  each_line[1].rstrip('\n')
                line = preProcess.lowerCase(line)
                line = preProcess.trim_extra_characters(line)
                tokenized_line = preProcess.whitespace_tokenize(line)
                token_list = preProcess.trim_stop_words(tokenized_line)
                stemmed_tokens = preProcess.porters_stemming(token_list)
                tokenized_json[doc_id]=stemmed_tokens
            token_file = os.path.join(os.path.dirname(__file__), '../helpers/tokenized_corpus.json')
            with open(token_file, 'w', encoding='utf-8') as json_file:
                json.dump(tokenized_json,json_file, indent=4)
            return []
        else:
            query = preProcess.lowerCase(query)
            line = preProcess.trim_extra_characters(query)
            tokenized_line = preProcess.whitespace_tokenize(line)
            token_list = preProcess.trim_stop_words(tokenized_line)
            stemmed_tokens = preProcess.porters_stemming(token_list)
            return stemmed_tokens

    def lowerCase(text):
        return text.lower()
    
    def trim_extra_characters(input_string):
        trimmed_string = re.sub(r'[^a-zA-Z0-9\s]', ' ', input_string)
        trimmed_string = re.sub(r'\s+', ' ', trimmed_string)
        return trimmed_string
    
    def whitespace_tokenize(input_string):
        temp_list = input_string.split(' ')
        for each_word in temp_list:
            if len(each_word)>0 and each_word!=' ':
                pass
            else:
                temp_list.remove(each_word)
        return temp_list
    
    def trim_stop_words(token_list):
        stopwords_list = stopwords.words('english')
        output_token_list = []
        for word in token_list:
            if word not in stopwords_list:
                output_token_list.append(word)
        return output_token_list
    
    def porters_stemming(token_list):
        ps = PorterStemmer()
        resultant_list = []
        for token in token_list:
            token = ps.stem(token)
            resultant_list.append(token)
        return resultant_list
    

    def calculate_tf_idf(token_list):
        pass
