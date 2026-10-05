#include <iostream>
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
