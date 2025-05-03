from DocumentType import DocumentType 
class Employee:
    def __init__(self, id: int, first_name: str, last_name: str, email: str, salary: int, document: str,document_type: DocumentType):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.salary= salary
        self.document=document
        self.document_type = document_type