#include <iostream>
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
