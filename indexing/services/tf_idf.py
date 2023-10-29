
from indexing.services.postings_linked_list import final_linked_list
import os,json
from collections import Counter
import copy
import math

class Tf_Idf:

    def __init__(self):
        pass

    def calculate_tf_idf():
        resultant_tf_score = {}
        token_file = os.path.join(os.path.dirname(__file__), '../helpers/tokenized_corpus.json')
        with open(token_file, 'r', encoding='utf-8') as json_file:
            token_data = json.load(json_file)
        postings_file = os.path.join(os.path.dirname(__file__), '../helpers/postings.json')
        with open(postings_file, 'r', encoding='utf-8') as json_file:
            postings_data = json.load(json_file)
        for key, value in token_data.items():
            string_counts = Counter(value)
            resultant_tf_score[key]={}
            for string,count in string_counts.items():
                tf = (count/len(token_data[key]))
                resultant_tf_score[key][string]= tf
        tf_score_file = os.path.join(os.path.dirname(__file__), '../helpers/tf_score.json')
        with open(tf_score_file, 'w', encoding='utf-8') as json_file:
            json.dump(resultant_tf_score,json_file, indent=4)


    def daatAndTfIdf(query_tokens,input_json):
        tf_file = os.path.join(os.path.dirname(__file__), '../helpers/tf_score.json')
        with open(tf_file, 'r', encoding='utf-8') as json_file:
            tf_score = json.load(json_file)
        postings_file = os.path.join(os.path.dirname(__file__), '../helpers/postings.json')
        with open(postings_file, 'r', encoding='utf-8') as json_file:
            postings_data = json.load(json_file)
        postings_list = copy.deepcopy(input_json["results"])
        result_json = copy.deepcopy(input_json)
        pairs = []
        tf_idf_score={}
        for each_doc in postings_list:
            cumulative_score=0
            for each_token in query_tokens:
                cumulative_score+=(tf_score[str(each_doc)][each_token])*(len(tf_score.keys())/len(postings_data[each_token]))
            tf_idf_score[str(each_doc)]=cumulative_score

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


    def daatAndSkipTfIdf(query_tokens,input_json):

        tf_file = os.path.join(os.path.dirname(__file__), '../helpers/tf_score.json')
        with open(tf_file, 'r', encoding='utf-8') as json_file:
            tf_score = json.load(json_file)
        postings_file = os.path.join(os.path.dirname(__file__), '../helpers/postings.json')
        with open(postings_file, 'r', encoding='utf-8') as json_file:
            postings_data = json.load(json_file)
        postings_list = copy.deepcopy(input_json["results"])
        result_json = copy.deepcopy(input_json)
        pairs = []
        tf_idf_score={}
        for each_doc in postings_list:
            cumulative_score=0
            for each_token in query_tokens:
                cumulative_score+=(tf_score[str(each_doc)][each_token])*(len(tf_score.keys())/len(postings_data[each_token]))
            tf_idf_score[str(each_doc)]=cumulative_score

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
