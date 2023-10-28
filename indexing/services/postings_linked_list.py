
import json,os,math

final_linked_list={}

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.second_next = None


class Postings_Linked_List:

    def __init__(self):
        self.head=None

    def create_linked_list():

        postings_file = os.path.join(os.path.dirname(__file__), '../helpers/postings.json')
        with open(postings_file, 'r', encoding='utf-8') as json_file:
            postings_data = json.load(json_file)
        for key,value in postings_data.items():

            # Adding Skip Pointers length calculation
            list_length = len(value)
            if math.sqrt(list_length).is_integer():
                skip_length = math.floor(math.sqrt(list_length))-1
            else:
                skip_length = round(math.sqrt(list_length))

            new_list = Postings_Linked_List()
            for each_doc in value:
                new_list.head = new_list.insert(int(each_doc))
            final_linked_list[key] = new_list.head
            if skip_length > 0 :
                final_linked_list[key] = Postings_Linked_List.add_skip_pointers(new_list.head,skip_length)
        
        
      

    def add_skip_pointers(head,skip_length):

        temp_length = skip_length
        temp_head = head
        first_pointer = head
        while head:
            if skip_length == 0:
                first_pointer.second_next = head
                first_pointer = head
                skip_length = temp_length
            skip_length = skip_length - 1
            head = head.next
        return temp_head



    def insert(self,data):
        new_node = Node(data)
        if self.head is None or data < self.head.data:
            new_node.next = self.head
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next and data > current_node.next.data:
                current_node = current_node.next
            
            new_node.next = current_node.next
            current_node.next = new_node

        return self.head
        


    def print_list(head):
        current = head
        while current:
            print(current.data, end =" -> ")
            current = current.second_next
        print("None")



    def print_linked_list():

        for key,value in final_linked_list.items():
            print(key)
            Postings_Linked_List.print_list(value)