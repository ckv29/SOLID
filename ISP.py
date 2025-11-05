from abc import ABC, abstractclassmethod


class Printable(ABC):
    @abstractclassmethod
    def print_document(self, document):
        pass


class Scannable(ABC):
    @abstractclassmethod
    def scan_document(self):
        pass


class Faxable(ABC):
    @abstractclassmethod
    def fax_document(self, document):
        pass


class Copyable(ABC):
    @abstractclassmethod
    def copy_document(self):
        pass


class MultiFunctionDevice(Printable, Scannable,Faxable,Copyable):
    def print_document(self, document):
        print(f"Printing: {document}")
        
    def scan_document(self):
        print(f"Scanning")
        
    def fax_document(self, document):
        print(f"Faxing: {document}")
        
    def copy_document(self):
        print(f"Copying:")


class SimplePrinter(Printable):
    def print_document(self, document):
        print(f"Printing: {document}")
        
        
   

sp = SimplePrinter()
sp.print_document("doc1")

mfd = MultiFunctionDevice()
mfd.scan_document()
mfd.copy_document()
mfd.fax_document("doc2")
