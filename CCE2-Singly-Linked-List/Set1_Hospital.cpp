#include <iostream>
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
