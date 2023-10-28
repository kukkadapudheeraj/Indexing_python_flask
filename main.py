from indexing import create_app
from indexing.services.preprocessing import preProcess
from indexing.services.postings import Postings
from indexing.services.postings_linked_list import Postings_Linked_List
from indexing.services.tf_idf import Tf_Idf

app = create_app()

if __name__ == '__main__':

    preProcess.clean()
    Postings.create_postings()
    Postings_Linked_List.create_linked_list()
    Tf_Idf.calculate_tf_id()
    # Postings_Linked_List.print_linked_list()
    app.run(host='127.0.0.1',port=9999,debug=True)


