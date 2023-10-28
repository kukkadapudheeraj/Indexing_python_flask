
from indexing.services.postings_linked_list import final_linked_list
import os,json
from collections import Counter
import copy
import math

class Tf_Idf:

    def __init__(self):
        pass

    def calculate_tf_id():
        resultant_tf_score = {}
        token_file = os.path.join(os.path.dirname(__file__), '../helpers/tokenized_corpus.json')
        with open(token_file, 'r', encoding='utf-8') as json_file:
            token_data = json.load(json_file)
        postings_file = os.path.join(os.path.dirname(__file__), '../helpers/postings.json')
        with open(postings_file, 'r', encoding='utf-8') as json_file:
            postings_data = json.load(json_file)
        for key, value in token_data.items():
            string_counts = Counter(value)
            cumulative_score = 0
            for string,count in string_counts.items():
                tf = (count/len(value))
                idf_score = 0
                for each_doc in postings_data[string]:
                    each_doc_counter = Counter(token_data[each_doc])
                    idf_score+=each_doc_counter[string]
                idf_score = len(token_data.keys())/idf_score
                cumulative_score+=tf*idf_score
            resultant_tf_score[key] = cumulative_score
        tf_idf_score_file = os.path.join(os.path.dirname(__file__), '../helpers/tf_idf_score.json')
        with open(tf_idf_score_file, 'w', encoding='utf-8') as json_file:
            json.dump(resultant_tf_score,json_file, indent=4)


    def daatAndTfIdf(query,input_json):
        tf_idf_file = os.path.join(os.path.dirname(__file__), '../helpers/tf_idf_score.json')
        with open(tf_idf_file, 'r', encoding='utf-8') as json_file:
            tf_idf_score = json.load(json_file)
        postings_list = copy.deepcopy(input_json["results"])
        result_json = copy.deepcopy(input_json)
        pairs = []
        for each_doc in postings_list:
            temp_list=[]
            temp_list.append(each_doc)
            temp_list.append(tf_idf_score[str(each_doc)])
            pairs.append(temp_list)
        sorted_pairs = sorted(pairs, key=lambda x: x[1],reverse=True)
        result_postings = []
        for each_post in sorted_pairs:
            result_postings.append(each_post[0])
        result_json["results"] = result_postings
        return result_json


    def daatAndSkipTfIdf(query,input_json):
        tf_idf_file = os.path.join(os.path.dirname(__file__), '../helpers/tf_idf_score.json')
        with open(tf_idf_file, 'r', encoding='utf-8') as json_file:
            tf_idf_score = json.load(json_file)
        postings_list = copy.deepcopy(input_json["results"])
        result_json = copy.deepcopy(input_json)
        pairs = []
        for each_doc in postings_list:
            temp_list=[]
            temp_list.append(each_doc)
            temp_list.append(tf_idf_score[str(each_doc)])
            pairs.append(temp_list)
        sorted_pairs = sorted(pairs, key=lambda x: x[1],reverse=True)
        result_postings = []
        for each_post in sorted_pairs:
            result_postings.append(each_post[0])
        result_json["results"] = result_postings
        return result_json