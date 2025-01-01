def list_of_books():
    with open("books.txt", "r", encoding="utf-8") as file:
        for line in file:
            print(line, end="")

def list_checked_out_books():
    with open("books.txt", "r", encoding="utf-8") as file:
        book_list = file.readlines()
        for line in book_list:
            line = line.rstrip()
            book_data = line.split(",")
            if book_data[3] == "T":
                print(line)

def add_new_book():
    ISBN = input("Enter the ISBN number of the book: ")
    book_name = input("Enter the name of the book: ")
    author_name = input("Author's name: ")

    with open("books.txt", "a", encoding="utf-8") as file:
        file.write(ISBN + "," + book_name + "," + author_name + "," + "F" + "," + "0" + "\n")
def search_book_by_ISBN():
    with open("books.txt", "r", encoding="utf-8") as file:
        book_list = file.readlines()
        ISBN = input("Enter the ISBN number: ")
        for line in book_list:
            line = line.rstrip()
            book_data = line.split(",")
            if book_data[0] == ISBN:
                print(f"The ISBN number of the book: {book_data[0]},\nThe name of the book: {book_data[1]},\nAuthor: {book_data[2]},\nThe status of the book: {book_data[3]},\nChecked out times: {book_data[4]}")
                break

def search_book_by_name():
    with open("books.txt", "r", encoding="utf-8") as file:
        book_list = file.readlines()
        name = input("The name of the book: ")
        for line in book_list:
            line = line.rstrip()
            book_data = line.split(",")
            if name.lower() in book_data[1].lower():
                print(line)

def checkout_book():
    with open("books.txt", "r+", encoding="utf-8") as file:
        book_list = file.readlines()
        book_name = input("Enter the name of the book: ")
        student_number = input("Enter student's number: ")
        found = False
        for i in range(len(book_list)):
            line = book_list[i].rstrip()
            book_data = line.split(",")
            if book_data[1].lower() == book_name.lower():
                found = True
                if book_data[3] == "F":  # Kitap mevcutsa
                    book_data[3] = "T"  # Kitap alınmış olarak işaretleniyor
                    book_data[4] = str(int(book_data[4]) + 1)  # Kitap sayısını artır
                    book_list[i] = ",".join(book_data) + "\n"

                    # Öğrencinin aldığı kitabı students.txt'ye yaz
                    with open("students.txt", "a", encoding="utf-8") as student_file:
                        student_file.write(f"{student_number},{book_data[0]}\n")  # Öğrenci numarası ve ISBN kaydediliyor
                    break
                else:
                    print("This book is already checked out.")
                    break

        if not found:
            print("Book not found.")
        else:
            # Güncellenmiş kitap listesini dosyaya yaz
            file.seek(0)
            file.writelines(book_list)
            file.truncate()  # Eski verinin üzerine yazmak için



def list_top_3_books():
    with open("books.txt", "r", encoding="utf-8") as file:
        book_list = file.readlines()
        books = []
        for line in book_list:
            line = line.rstrip()
            books.append(line)
        books_data = []
        for book in books:
            book_data = book.split(",")
            book_data[4] = int(book_data[4])
            books_data.append(book_data)
        sorted_books = sorted(books_data, key=lambda x: x[4], reverse=True)
        for i in range(min(3, len(sorted_books))):
            print(f"ISBN: {sorted_books[i][0]}, Name: {sorted_books[i][1]}, Author: {sorted_books[i][2]}, Status: {sorted_books[i][3]}, Checked Out: {sorted_books[i][4]}")

def list_top_3_students():

    with open("students.txt", "r", encoding="utf-8") as file:
        student_list = file.readlines()
        students_data = []
        for line in student_list:
            line = line.rstrip()
            student_data = line.split(",")
            students_data.append(student_data)
        sorted_students = sorted(students_data, key=lambda x: int(x[1]), reverse=True)
        for i in range(min(3, len(sorted_students))):
            print(f"Student Number: {sorted_students[i][0]}, Books Checked Out: {sorted_students[i][1]}")

def list_students():
    with open("students.txt", "r", encoding="utf-8") as file:
        for line in file:
            print(line, end="")

while True:
    action = input("""\
1- List all books.
2- List checked out books.
3- Add a new book.
4- Search book by ISBN number.
5- Search a book by name.
6- Checkout a book.
7- List all students.
8- List top 3 books.
9- List top 3 students.
10- Exit.
""")

    if action == "1":
        list_of_books()
    elif action == "2":
        list_checked_out_books()
    elif action == "3":
        add_new_book()
    elif action == "4":
        search_book_by_ISBN()
    elif action == "5":
        search_book_by_name()
    elif action == "6":
        checkout_book()
    elif action == "7":
        list_students()
    elif action == "8":
        list_top_3_books()
    elif action == "9":
        list_top_3_students()
    else:
        break
