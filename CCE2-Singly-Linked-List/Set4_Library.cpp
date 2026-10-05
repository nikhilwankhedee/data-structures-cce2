#include <iostream>
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
