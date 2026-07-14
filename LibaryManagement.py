from abc import ABC,abstractmethod
class person(ABC):
    def __init__(self,name):
        self._name=name
    @property
    def name(self):
        return self._name
    @abstractmethod
    def role(self):
        pass
class memb(person):
    def __init__(self,name):
        super().__init__(name)
        self._borrowed=[]
    @property
    def borrowed(self):
        return self._borrowed
    def role(self):
        return "memb"
class libarian(person):
    def __init__(self,name):
        super().__init__(name)
    def role(self):
        return "libarian"
class book:
    def __init__(self,title,author,pages):
        self._title=title
        self._author=author
        self._pages=pages
    @property
    def title(self):
        return self._title
    @property
    def author(self):
        return self._author
    @property
    def pages(self):
        return self._pages
    def __str__(self):
        return f"{self._title} by {self._author}"
    def __repr__(self):
        return f"book('{self._title}','{self._author}',{self._pages})"
    def __len__(self):
        return self._pages
    def __eq__(self,other):
        return self._title==other._title
    def __add__(self,other):
        return self._pages+other._pages
class libary:
    def __init__(self,name):
        self._name=name
        self._books=[]
    @property
    def books(self):
        return self._books
    def add_book(self,book):
        self._books.append(book)
        print("book added")
    def remove_book(self,title):
        for book in self._books:
            if book.title==title:
                self._books.remove(book)
                print("removed")
                return
        print("not found")
    def show_books(self):
        if len(self._books)==0:
            print("no books")
        else:
            for book in self._books:
                print(book)
    def __len__(self):
        return len(self._books)
class transaction:
    @staticmethod
    def borrow_book(mem,book):
        mem.borrowed.append(book)
        print(mem.name,"borrowed",book.title)
    @staticmethod
    def return_book(mem,title):
        for book in mem.borrowed:
            if book.title==title:
                mem.borrowed.remove(book)
                print(mem.name,"returned",book.title)
                return
        print("book not found")
def memb_operation(mem):
    while(True):
        print("\n1.show borrowed books")
        print("2.borrow book")
        print("3.return book")
        print("4.exit")
        ch=int(input("enter choice : "))
        if ch==1:
            if len(mem.borrowed)==0:
                print("no books")
            else:
                for book in mem.borrowed:
                    print(book)
        elif ch==2:
            title=input("enter title : ")
            flag=True
            for book in libary.books:
                if book.title==title:
                    transaction.borrow_book(mem,book)
                    flag=False
                    break
            if flag:
                print("not found")
        elif ch==3:
            title=input("enter title : ")
            transaction.return_book(mem,title)
        else:
            break
libary=libary("central")
libary.add_book(book("python","john",300))
libary.add_book(book("java","mike",500))
libary.add_book(book("c","alex",250))
membs=[]
while(True):
    print("\n1.create memb")
    print("2.enter memb")
    print("3.show books")
    print("4.check book")
    print("5.add pages")
    print("6.exit")
    ch=int(input("enter choice : "))
    if ch==1:
        name=input("enter name : ")
        mem=memb(name)
        membs.append(mem)
        print("memb created")
    elif ch==2:
        name=input("enter name : ")
        flag=True
        for mem in membs:
            if mem.name==name:
                print("welcome",mem.name)
                print(mem.role())
                memb_operation(mem)
                flag=False
                break
        if flag:
            print("memb not found")
    elif ch==3:
        print("total books :",len(libary))
        libary.show_books()
    elif ch==4:
        b1=libary.books[0]
        b2=libary.books[1]
        print(b1==b2)
    elif ch==5:
        b1=libary.books[0]
        b2=libary.books[1]
        print("total pages :",b1+b2)
    else:
        break