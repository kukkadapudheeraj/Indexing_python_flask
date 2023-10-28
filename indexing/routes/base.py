from flask import Blueprint,request
from indexing.services.preprocessing import preProcess
from indexing.services.daat import Daat
from indexing.services.tf_idf import Tf_Idf
from indexing.services.postings import Postings
import time

base = Blueprint('base',__name__)

@base.route('/',methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return "Hello , Hope you are doing great... !! Please use POST method to get valid results"
    elif request.method == 'POST':
        start_time = time.time()
        split_query = request.data.decode('utf-8').splitlines()
        result_json = {}
        query_token_list=[]
        for each_query in split_query:
            if result_json.get("daatAnd") is None:
                result_json["daatAnd"]={}
            if result_json.get("daatAndSkip") is None:
                result_json["daatAndSkip"]={}
            if result_json.get("daatAndTfIdf") is None:
                result_json["daatAndTfIdf"]={}
            if result_json.get("daatAndSkipTfIdf") is None:
                result_json["daatAndSkipTfIdf"]={}
            if result_json.get("postingsList") is None:
                result_json["postingsList"]={}
            if result_json.get("postingsListSkip") is None:
                result_json["postingsListSkip"]={}
            query_token_list = preProcess.clean(each_query)
            result_json["daatAnd"][each_query]= Daat.daatAnd(query_token_list)
            result_json["daatAndSkip"][each_query] = Daat.daatAndSkip(query_token_list)
            result_json["daatAndTfIdf"][each_query] = Tf_Idf.daatAndTfIdf(each_query,result_json["daatAnd"][each_query])
            result_json["daatAndSkipTfIdf"][each_query] = Tf_Idf.daatAndSkipTfIdf(each_query,result_json["daatAndSkip"][each_query])
            result_json = Postings.getPostings(result_json,query_token_list) 
            result_json = Postings.getPostingsSkip(result_json,query_token_list) 
        final_result={}
        final_result["Response"] = result_json
        final_result["time_taken"] =  str(time.time() - start_time)
        return final_result
