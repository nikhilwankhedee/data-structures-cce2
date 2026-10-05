#include <iostream>
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
