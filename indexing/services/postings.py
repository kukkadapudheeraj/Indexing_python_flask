import json
import os
from indexing.services.postings_linked_list import final_linked_list
class Postings:

    def __init__(self):
        pass

    def create_postings():
        token_file = os.path.join(os.path.dirname(__file__), '../helpers/tokenized_corpus.json')
        with open(token_file, 'r', encoding='utf-8') as json_file:
            token_data = json.load(json_file)
        token_set = set()
        for each_list in token_data.values():
            for each_token in each_list:
                token_set.add(each_token)

        postings_list = {}

        for each_token in token_set:
            postings_list[each_token] = []
            for doc_id,each_list in token_data.items():
                if each_token in each_list:
                    postings_list[each_token].append(doc_id)

        Postings.calculate_length(postings_list)

        postings_file = os.path.join(os.path.dirname(__file__), '../helpers/postings.json')
        with open(postings_file, 'w', encoding='utf-8') as json_file:
            json.dump(postings_list,json_file, indent=4)


    def calculate_length(postings_json):
        postings_lengths = {}
        for key,value in postings_json.items():
            postings_lengths[key] = len(value)
        postings_length_file = os.path.join(os.path.dirname(__file__), '../helpers/postings_lengths.json')
        with open(postings_length_file, 'w', encoding='utf-8') as json_file:
            json.dump(postings_lengths,json_file, indent=4)

    def getPostings(result_json,token_list):
        for each_token in token_list:
            token_linked_list = final_linked_list[each_token]
            result_json["postingsList"][each_token]=[]
            while token_linked_list:
                result_json["postingsList"][each_token].append(token_linked_list.data)
                token_linked_list = token_linked_list.next
        return result_json
    

    def getPostingsSkip(result_json,token_list):
        for each_token in token_list:
            token_linked_list = final_linked_list[each_token]
            result_json["postingsListSkip"][each_token]=[]
            while token_linked_list:
                result_json["postingsListSkip"][each_token].append(token_linked_list.data)
                token_linked_list = token_linked_list.second_next
        return result_json

        
