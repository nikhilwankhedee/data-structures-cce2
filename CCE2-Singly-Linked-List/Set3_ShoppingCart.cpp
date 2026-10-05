#include <iostream>
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
