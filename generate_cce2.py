from pathlib import Path
import subprocess
import shutil

PROJECT_NAME = "CCE2-Singly-Linked-List"

files = {
    "Set1_Hospital.cpp": r'''#include <iostream>
#include <string>
using namespace std;

struct Node
{
    int patientID;
    string patientName;
    Node* next;
};

Node* head = NULL;

void addPatient(int id, string name)
{
    Node* newNode = new Node;
    newNode->patientID = id;
    newNode->patientName = name;
    newNode->next = NULL;

    if (head == NULL)
    {
        head = newNode;
        return;
    }

    Node* temp = head;

    while (temp->next != NULL)
    {
        temp = temp->next;
    }

    temp->next = newNode;
}

void deletePatient(int id)
{
    if (head == NULL)
    {
        cout << "Patient list is empty." << endl;
        return;
    }

    // If the first node is the node to delete
    if (head->patientID == id)
    {
        Node* temp = head;
        head = head->next;
        delete temp;

        cout << "Patient deleted successfully." << endl;
        return;
    }

    Node* temp = head;

    while (temp->next != NULL && temp->next->patientID != id)
    {
        temp = temp->next;
    }

    if (temp->next == NULL)
    {
        cout << "Patient not found." << endl;
        return;
    }

    Node* del = temp->next;
    temp->next = del->next;
    delete del;

    cout << "Patient deleted successfully." << endl;
}

void displayPatients()
{
    if (head == NULL)
    {
        cout << "Patient list is empty." << endl;
        return;
    }

    Node* temp = head;

    while (temp != NULL)
    {
        cout << "Patient ID: " << temp->patientID << endl;
        cout << "Patient Name: " << temp->patientName << endl;
        cout << "------------------------" << endl;

        temp = temp->next;
    }
}

int main()
{
    addPatient(101, "Rahul");
    addPatient(102, "Amit");
    addPatient(103, "Sneha");

    cout << "PATIENT LIST" << endl;
    cout << "============" << endl;
    displayPatients();

    cout << endl;
    cout << "Deleting Patient ID 102..." << endl;
    deletePatient(102);

    cout << endl;
    cout << "PATIENT LIST AFTER DELETION" << endl;
    cout << "===========================" << endl;
    displayPatients();

    return 0;
}
''',

    "Set2_Student.cpp": r'''#include <iostream>
#include <string>
using namespace std;

struct Node
{
    int rollNo;
    string studentName;
    float marks;
    Node* next;
};

Node* head = NULL;

void insertStudent(int roll, string name, float marks)
{
    Node* newNode = new Node;

    newNode->rollNo = roll;
    newNode->studentName = name;
    newNode->marks = marks;

    // Insert at beginning
    newNode->next = head;
    head = newNode;
}

void searchStudent(int roll)
{
    Node* temp = head;

    while (temp != NULL)
    {
        if (temp->rollNo == roll)
        {
            cout << "Student Found!" << endl;
            cout << "Roll Number: " << temp->rollNo << endl;
            cout << "Student Name: " << temp->studentName << endl;
            cout << "Marks: " << temp->marks << endl;
            return;
        }

        temp = temp->next;
    }

    cout << "Student not found." << endl;
}

void displayStudents()
{
    if (head == NULL)
    {
        cout << "Student list is empty." << endl;
        return;
    }

    Node* temp = head;

    while (temp != NULL)
    {
        cout << "Roll Number: " << temp->rollNo << endl;
        cout << "Student Name: " << temp->studentName << endl;
        cout << "Marks: " << temp->marks << endl;
        cout << "------------------------" << endl;

        temp = temp->next;
    }
}

int main()
{
    insertStudent(101, "Rahul", 85);
    insertStudent(102, "Amit", 90);
    insertStudent(103, "Sneha", 88);

    cout << "STUDENT RECORDS" << endl;
    cout << "===============" << endl;
    displayStudents();

    cout << endl;
    cout << "Searching for Roll Number 102..." << endl;
    searchStudent(102);

    return 0;
}
''',

    "Set3_ShoppingCart.cpp": r'''#include <iostream>
#include <string>
using namespace std;

struct Node
{
    int productID;
    string productName;
    float price;
    Node* next;
};

Node* head = NULL;

void addProduct(int id, string name, float price)
{
    Node* newNode = new Node;

    newNode->productID = id;
    newNode->productName = name;
    newNode->price = price;
    newNode->next = NULL;

    if (head == NULL)
    {
        head = newNode;
        return;
    }

    Node* temp = head;

    while (temp->next != NULL)
    {
        temp = temp->next;
    }

    temp->next = newNode;
}

void deleteProduct(int id)
{
    if (head == NULL)
    {
        cout << "Shopping cart is empty." << endl;
        return;
    }

    if (head->productID == id)
    {
        Node* temp = head;
        head = head->next;
        delete temp;

        cout << "Product deleted successfully." << endl;
        return;
    }

    Node* temp = head;

    while (temp->next != NULL && temp->next->productID != id)
    {
        temp = temp->next;
    }

    if (temp->next == NULL)
    {
        cout << "Product not found." << endl;
        return;
    }

    Node* del = temp->next;
    temp->next = del->next;
    delete del;

    cout << "Product deleted successfully." << endl;
}

void displayCart()
{
    if (head == NULL)
    {
        cout << "Shopping cart is empty." << endl;
        return;
    }

    Node* temp = head;

    while (temp != NULL)
    {
        cout << "Product ID: " << temp->productID << endl;
        cout << "Product Name: " << temp->productName << endl;
        cout << "Price: " << temp->price << endl;
        cout << "------------------------" << endl;

        temp = temp->next;
    }
}

int main()
{
    addProduct(1, "Laptop", 55000);
    addProduct(2, "Mouse", 800);
    addProduct(3, "Keyboard", 1500);

    cout << "SHOPPING CART" << endl;
    cout << "=============" << endl;
    displayCart();

    cout << endl;
    cout << "Deleting Product ID 2..." << endl;
    deleteProduct(2);

    cout << endl;
    cout << "SHOPPING CART AFTER DELETION" << endl;
    cout << "============================" << endl;
    displayCart();

    return 0;
}
''',

    "Set4_Library.cpp": r'''#include <iostream>
#include <string>
using namespace std;

struct Node
{
    int bookID;
    string bookName;
    string authorName;
    Node* next;
};

Node* head = NULL;

void insertBook(int id, string book, string author)
{
    Node* newNode = new Node;

    newNode->bookID = id;
    newNode->bookName = book;
    newNode->authorName = author;

    // Insert at beginning
    newNode->next = head;
    head = newNode;
}

void searchBook(int id)
{
    Node* temp = head;

    while (temp != NULL)
    {
        if (temp->bookID == id)
        {
            cout << "Book Found!" << endl;
            cout << "Book ID: " << temp->bookID << endl;
            cout << "Book Name: " << temp->bookName << endl;
            cout << "Author Name: " << temp->authorName << endl;
            return;
        }

        temp = temp->next;
    }

    cout << "Book not found." << endl;
}

void displayBooks()
{
    if (head == NULL)
    {
        cout << "Library is empty." << endl;
        return;
    }

    Node* temp = head;

    while (temp != NULL)
    {
        cout << "Book ID: " << temp->bookID << endl;
        cout << "Book Name: " << temp->bookName << endl;
        cout << "Author Name: " << temp->authorName << endl;
        cout << "------------------------" << endl;

        temp = temp->next;
    }
}

int main()
{
    insertBook(101, "C++ Programming", "Bjarne Stroustrup");
    insertBook(102, "Data Structures", "Mark Allen");
    insertBook(103, "Algorithms", "Thomas Cormen");

    cout << "LIBRARY BOOKS" << endl;
    cout << "=============" << endl;
    displayBooks();

    cout << endl;
    cout << "Searching for Book ID 102..." << endl;
    searchBook(102);

    return 0;
}
''',

    "Set5_Contact.cpp": r'''#include <iostream>
#include <string>
using namespace std;

struct Node
{
    int contactID;
    string name;
    string phoneNumber;
    Node* next;
};

Node* head = NULL;

void addContact(int id, string name, string phone)
{
    Node* newNode = new Node;

    newNode->contactID = id;
    newNode->name = name;
    newNode->phoneNumber = phone;
    newNode->next = NULL;

    if (head == NULL)
    {
        head = newNode;
        return;
    }

    Node* temp = head;

    while (temp->next != NULL)
    {
        temp = temp->next;
    }

    temp->next = newNode;
}

void deleteContact(int id)
{
    if (head == NULL)
    {
        cout << "Contact list is empty." << endl;
        return;
    }

    if (head->contactID == id)
    {
        Node* temp = head;
        head = head->next;
        delete temp;

        cout << "Contact deleted successfully." << endl;
        return;
    }

    Node* temp = head;

    while (temp->next != NULL && temp->next->contactID != id)
    {
        temp = temp->next;
    }

    if (temp->next == NULL)
    {
        cout << "Contact not found." << endl;
        return;
    }

    Node* del = temp->next;
    temp->next = del->next;
    delete del;

    cout << "Contact deleted successfully." << endl;
}

void displayContacts()
{
    if (head == NULL)
    {
        cout << "Contact list is empty." << endl;
        return;
    }

    Node* temp = head;

    while (temp != NULL)
    {
        cout << "Contact ID: " << temp->contactID << endl;
        cout << "Name: " << temp->name << endl;
        cout << "Phone Number: " << temp->phoneNumber << endl;
        cout << "------------------------" << endl;

        temp = temp->next;
    }
}

int main()
{
    addContact(1, "Rahul", "9876543210");
    addContact(2, "Amit", "9876501234");
    addContact(3, "Sneha", "9123456780");

    cout << "CONTACT LIST" << endl;
    cout << "============" << endl;
    displayContacts();

    cout << endl;
    cout << "Deleting Contact ID 2..." << endl;
    deleteContact(2);

    cout << endl;
    cout << "CONTACT LIST AFTER DELETION" << endl;
    cout << "===========================" << endl;
    displayContacts();

    return 0;
}
''',

    "Set6_Movie.cpp": r'''#include <iostream>
#include <string>
using namespace std;

struct Node
{
    int movieID;
    string movieName;
    Node* next;
};

Node* head = NULL;

void addMovie(int id, string name)
{
    Node* newNode = new Node;

    newNode->movieID = id;
    newNode->movieName = name;
    newNode->next = NULL;

    if (head == NULL)
    {
        head = newNode;
        return;
    }

    Node* temp = head;

    while (temp->next != NULL)
    {
        temp = temp->next;
    }

    temp->next = newNode;
}

void deleteMovie(int id)
{
    if (head == NULL)
    {
        cout << "Watchlist is empty." << endl;
        return;
    }

    if (head->movieID == id)
    {
        Node* temp = head;
        head = head->next;
        delete temp;

        cout << "Movie deleted successfully." << endl;
        return;
    }

    Node* temp = head;

    while (temp->next != NULL && temp->next->movieID != id)
    {
        temp = temp->next;
    }

    if (temp->next == NULL)
    {
        cout << "Movie not found." << endl;
        return;
    }

    Node* del = temp->next;
    temp->next = del->next;
    delete del;

    cout << "Movie deleted successfully." << endl;
}

void displayMovies()
{
    if (head == NULL)
    {
        cout << "Watchlist is empty." << endl;
        return;
    }

    Node* temp = head;

    while (temp != NULL)
    {
        cout << "Movie ID: " << temp->movieID << endl;
        cout << "Movie Name: " << temp->movieName << endl;
        cout << "------------------------" << endl;

        temp = temp->next;
    }
}

int main()
{
    addMovie(101, "Inception");
    addMovie(102, "Interstellar");
    addMovie(103, "The Dark Knight");

    cout << "MOVIE WATCHLIST" << endl;
    cout << "===============" << endl;
    displayMovies();

    cout << endl;
    cout << "Deleting Movie ID 102..." << endl;
    deleteMovie(102);

    cout << endl;
    cout << "MOVIE WATCHLIST AFTER DELETION" << endl;
    cout << "==============================" << endl;
    displayMovies();

    return 0;
}
'''
}


def find_compiler():
    """Find g++ on the system."""
    compiler = shutil.which("g++")
    if compiler:
        return compiler

    compiler = shutil.which("clang++")
    if compiler:
        return compiler

    return None


def main():
    project_dir = Path(PROJECT_NAME)
    project_dir.mkdir(exist_ok=True)

    print(f"Creating project: {project_dir.resolve()}")
    print()

    # Create all C++ files
    for filename, code in files.items():
        filepath = project_dir / filename
        filepath.write_text(code.strip() + "\n", encoding="utf-8")
        print(f"[CREATED] {filename}")

    print()
    print("All source files created.")

    # Validate compilation
    compiler = find_compiler()

    if compiler is None:
        print()
        print("[WARNING] g++/clang++ was not found.")
        print("Files were created successfully, but automatic compilation could not be checked.")
        return

    print()
    print(f"Compiler found: {compiler}")
    print("Checking all programs...")
    print()

    build_dir = project_dir / "build"
    build_dir.mkdir(exist_ok=True)

    failed = []

    for filename in files:
        source = project_dir / filename
        executable_name = source.stem

        # Windows needs .exe; Linux/macOS doesn't.
        executable = build_dir / executable_name

        result = subprocess.run(
            [
                compiler,
                "-std=c++17",
                "-Wall",
                "-Wextra",
                "-pedantic",
                str(source),
                "-o",
                str(executable)
            ],
            capture_output=True,
            text=True
        )

        if result.returncode == 0:
            print(f"[PASS] {filename}")
        else:
            print(f"[FAIL] {filename}")
            print(result.stderr)
            failed.append(filename)

    print()
    print("=" * 50)

    if not failed:
        print("SUCCESS: All 6 programs compiled successfully.")
        print("=" * 50)
        print()
        print(f"Project created at:")
        print(project_dir.resolve())
    else:
        print("COMPILATION ERRORS FOUND:")
        for filename in failed:
            print(f" - {filename}")
        print("=" * 50)


if __name__ == "__main__":
    main()
