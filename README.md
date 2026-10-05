# CCE2 — Singly Linked List in C++

A complete collection of **Scenario-Based Singly Linked List programs in C++** for CCE2 preparation.

This repository contains all 6 expected scenario patterns:

1. Hospital Patient Management
2. Student Record Management
3. Online Shopping Cart
4. Library Book Management
5. Contact List Management
6. Movie Watchlist

The main purpose of this repository is **not to memorize six different programs**.

Almost all six programs are built using the **same few Singly Linked List patterns**.

Once you understand those patterns, you can solve almost any similar CCE question by simply changing:

- Node fields
- Function names
- Comparison field
- Display statements

---

# Table of Contents

- [1. Repository Structure](#1-repository-structure)
- [2. Generate Everything Automatically](#2-generate-everything-automatically)
- [3. What Is a Singly Linked List?](#3-what-is-a-singly-linked-list)
- [4. What Is a Node?](#4-what-is-a-node)
- [5. Understanding `head`](#5-understanding-head)
- [6. Understanding `next`](#6-understanding-next)
- [7. Basic Structure of a Node](#7-basic-structure-of-a-node)
- [8. How Memory Works](#8-how-memory-works)
- [9. Creating a New Node](#9-creating-a-new-node)
- [10. Pattern 1 — Insert at Beginning](#10-pattern-1--insert-at-beginning)
- [11. Pattern 2 — Insert at End](#11-pattern-2--insert-at-end)
- [12. Pattern 3 — Display / Traversal](#12-pattern-3--display--traversal)
- [13. Pattern 4 — Search](#13-pattern-4--search)
- [14. Pattern 5 — Delete by ID](#14-pattern-5--delete-by-id)
- [15. Why Deleting the Head Is Special](#15-why-deleting-the-head-is-special)
- [16. Understanding `temp`](#16-understanding-temp)
- [17. Understanding `new` and `delete`](#17-understanding-new-and-delete)
- [18. All Six CCE Sets](#18-all-six-cce-sets)
- [19. The Important Pattern Grouping](#19-the-important-pattern-grouping)
- [20. How to Identify the Pattern in the Exam](#20-how-to-identify-the-pattern-in-the-exam)
- [21. Complete Operation Cheat Sheet](#21-complete-operation-cheat-sheet)
- [22. Time Complexity](#22-time-complexity)
- [23. Common Mistakes](#23-common-mistakes)
- [24. Viva Questions and Answers](#24-viva-questions-and-answers)
- [25. Frequently Asked Code Questions](#25-frequently-asked-code-questions)
- [26. How to Modify a Program](#26-how-to-modify-a-program)
- [27. Exam Strategy](#27-exam-strategy)
- [28. Final Cheat Sheet](#28-final-cheat-sheet)

---

# 1. Repository Structure

```text
CCE2-Singly-Linked-List/
│
├── README.md
├── generate_cce2.py
│
├── Set1_Hospital.cpp
├── Set2_Student.cpp
├── Set3_ShoppingCart.cpp
├── Set4_Library.cpp
├── Set5_Contact.cpp
└── Set6_Movie.cpp
```

### Files

| File | Scenario | Operations |
|---|---|---|
| `Set1_Hospital.cpp` | Hospital Patient Management | Add at End, Delete, Display |
| `Set2_Student.cpp` | Student Record Management | Insert at Beginning, Search, Display |
| `Set3_ShoppingCart.cpp` | Online Shopping Cart | Add at End, Delete, Display |
| `Set4_Library.cpp` | Library Book Management | Insert at Beginning, Search, Display |
| `Set5_Contact.cpp` | Contact List Management | Add at End, Delete, Display |
| `Set6_Movie.cpp` | Movie Watchlist | Add at End, Delete, Display |
| `generate_cce2.py` | Code Generator | Creates all C++ programs automatically |

---

# 2. Generate Everything Automatically

You **do not need to manually create all six C++ files**.

The repository includes:

```text
generate_cce2.py
```

Run:

```bash
python generate_cce2.py
```

The Python script will automatically:

1. Create the project directory.
2. Create all six `.cpp` files.
3. Put the complete C++ code inside them.
4. Find `g++` or `clang++`.
5. Compile all six programs.
6. Check for compilation errors.
7. Create a `build/` directory containing the compiled programs.

So:

```text
One Python command
       ↓
All 6 C++ programs
       ↓
Automatic compilation
       ↓
Ready for practice
```

### Example output

```text
[CREATED] Set1_Hospital.cpp
[CREATED] Set2_Student.cpp
[CREATED] Set3_ShoppingCart.cpp
[CREATED] Set4_Library.cpp
[CREATED] Set5_Contact.cpp
[CREATED] Set6_Movie.cpp

Compiler found: g++

[PASS] Set1_Hospital.cpp
[PASS] Set2_Student.cpp
[PASS] Set3_ShoppingCart.cpp
[PASS] Set4_Library.cpp
[PASS] Set5_Contact.cpp
[PASS] Set6_Movie.cpp

SUCCESS: All 6 programs compiled successfully.
```

### Requirements

You need:

- Python 3
- A C++ compiler such as `g++` or `clang++`

The Python script is only a **generator and validator**.

The actual CCE programs are the `.cpp` files.

---

# 3. What Is a Singly Linked List?

A **Singly Linked List** is a linear data structure where elements are stored in separate nodes.

Each node contains:

1. Data
2. Address of the next node

Conceptually:

```text
+---------+---------+      +---------+---------+      +---------+---------+
|  Data   |  next   | ---> |  Data   |  next   | ---> |  Data   |  NULL   |
+---------+---------+      +---------+---------+      +---------+---------+
```

For example:

```text
10 → 20 → 30 → NULL
```

Every node points to the next node.

The final node points to:

```cpp
NULL
```

which means:

> There is no next node.

---

# 4. What Is a Node?

A **node** is the basic building block of a linked list.

For example:

```cpp
struct Node
{
    int id;
    string name;
    Node* next;
};
```

This node contains:

```text
id       → actual data
name     → actual data
next     → address of next node
```

For the Student problem:

```cpp
struct Node
{
    int rollNo;
    string studentName;
    float marks;
    Node* next;
};
```

For the Hospital problem:

```cpp
struct Node
{
    int patientID;
    string patientName;
    Node* next;
};
```

The **data changes depending on the scenario**.

The `next` pointer remains.

---

# 5. Understanding `head`

`head` is a pointer that stores the address of the **first node**.

```cpp
Node* head = NULL;
```

Initially:

```text
head
 ↓
NULL
```

After inserting one node:

```text
head
 ↓
[101 | NULL]
```

After inserting another:

```text
head
 ↓
[101 | •] → [102 | NULL]
```

After another:

```text
head
 ↓
[101 | •] → [102 | •] → [103 | NULL]
```

The `head` pointer always points to the first node.

---

# 6. Understanding `next`

`next` is a pointer inside every node.

It stores the address of the next node.

Example:

```cpp
newNode->next = head;
```

This means:

> Make the new node point to whatever `head` is currently pointing to.

Another example:

```cpp
temp = temp->next;
```

This means:

> Move `temp` to the next node.

This line is extremely important.

---

# 7. Basic Structure of a Node

The general structure is:

```cpp
struct Node
{
    // Data
    int id;
    string name;

    // Pointer to next node
    Node* next;
};
```

Think of it as:

```text
Node
┌─────────────────────┐
│ Data                │
│                     │
│ next ───────────────┼──────→ next Node
└─────────────────────┘
```

---

# 8. How Memory Works

When we write:

```cpp
Node* newNode = new Node;
```

we dynamically create a node in memory.

For example:

```text
newNode
   ↓
┌───────────────┐
│ id            │
│ name          │
│ next          │
└───────────────┘
```

The variable `newNode` stores the address of this node.

When the node is no longer required:

```cpp
delete newNode;
```

releases its dynamically allocated memory.

---

# 9. Creating a New Node

The standard pattern is:

```cpp
Node* newNode = new Node;

newNode->id = id;
newNode->name = name;
newNode->next = NULL;
```

Breakdown:

### Step 1

```cpp
Node* newNode = new Node;
```

Create a new node.

### Step 2

```cpp
newNode->id = id;
```

Store the ID.

### Step 3

```cpp
newNode->name = name;
```

Store the name.

### Step 4

```cpp
newNode->next = NULL;
```

Initially, the new node does not point to another node.

---

# 10. Pattern 1 — Insert at Beginning

This is one of the easiest linked-list operations.

Suppose:

```text
head
 ↓
10 → 20 → 30 → NULL
```

We want to insert `5`.

First create:

```text
5 → ?
```

Then:

```cpp
newNode->next = head;
```

Now:

```text
5 → 10 → 20 → 30 → NULL
```

Then:

```cpp
head = newNode;
```

Final structure:

```text
head
 ↓
5 → 10 → 20 → 30 → NULL
```

### The two lines to memorize

```cpp
newNode->next = head;
head = newNode;
```

That's the entire insertion-at-beginning logic.

### Complete pattern

```cpp
void insertNode(int id, string name)
{
    Node* newNode = new Node;

    newNode->id = id;
    newNode->name = name;

    newNode->next = head;
    head = newNode;
}
```

### Complexity

```text
O(1)
```

Because we do not traverse the list.

---

# 11. Pattern 2 — Insert at End

Suppose:

```text
head
 ↓
10 → 20 → 30 → NULL
```

We want:

```text
40
```

We first create:

```text
40 → NULL
```

Then start from `head`.

```cpp
Node* temp = head;
```

Move until the last node:

```cpp
while (temp->next != NULL)
{
    temp = temp->next;
}
```

When the loop finishes:

```text
temp
 ↓
30 → NULL
```

Then:

```cpp
temp->next = newNode;
```

Final list:

```text
10 → 20 → 30 → 40 → NULL
```

### Complete pattern

```cpp
Node* newNode = new Node;

newNode->id = id;
newNode->name = name;
newNode->next = NULL;

if (head == NULL)
{
    head = newNode;
}
else
{
    Node* temp = head;

    while (temp->next != NULL)
    {
        temp = temp->next;
    }

    temp->next = newNode;
}
```

### Why check `head == NULL`?

Because if the list is empty:

```text
head → NULL
```

there is no node to traverse.

So the new node itself becomes `head`.

### Complexity

```text
O(n)
```

because we may have to travel through the entire list.

---

# 12. Pattern 3 — Display / Traversal

Suppose:

```text
10 → 20 → 30 → NULL
```

We want to visit every node.

Start:

```cpp
Node* temp = head;
```

Then:

```cpp
while (temp != NULL)
```

Inside:

```cpp
cout << temp->id;
```

Then move:

```cpp
temp = temp->next;
```

### Complete pattern

```cpp
Node* temp = head;

while (temp != NULL)
{
    cout << temp->id << endl;

    temp = temp->next;
}
```

### Why `temp`?

We should **not move `head`**.

If we did:

```cpp
head = head->next;
```

we would lose the beginning of our list.

Instead, use:

```cpp
Node* temp = head;
```

and move `temp`.

### Complexity

```text
O(n)
```

because every node is visited.

---

# 13. Pattern 4 — Search

Suppose:

```text
101 → 102 → 103 → NULL
```

We want to search for:

```text
102
```

Start:

```cpp
Node* temp = head;
```

Then:

```cpp
while (temp != NULL)
```

Compare:

```cpp
if (temp->id == id)
```

If found, print the information:

```cpp
cout << "Found!";
```

Then:

```cpp
return;
```

If the loop finishes without finding anything:

```cpp
cout << "Not found.";
```

### Complete pattern

```cpp
void searchStudent(int roll)
{
    Node* temp = head;

    while (temp != NULL)
    {
        if (temp->rollNo == roll)
        {
            cout << "Student Found!" << endl;
            cout << "Roll Number: " << temp->rollNo << endl;
            cout << "Name: " << temp->studentName << endl;
            cout << "Marks: " << temp->marks << endl;

            return;
        }

        temp = temp->next;
    }

    cout << "Student not found." << endl;
}
```

### Important

A search loop by itself does **not automatically print anything**.

This:

```cpp
while (temp != NULL)
{
    if (temp->id == id)
    {
        return;
    }

    temp = temp->next;
}
```

only searches.

If the question expects output, you must explicitly use:

```cpp
cout
```

---

# 14. Pattern 5 — Delete by ID

Deletion is the most important pattern to understand properly.

Suppose:

```text
101 → 102 → 103 → NULL
```

We want to delete:

```text
102
```

We need to make:

```text
101 → 103 → NULL
```

We therefore need access to the node **before** the node being deleted.

```text
temp
 ↓
101 → 102 → 103
      ↑
     delete
```

We find the previous node using:

```cpp
while (temp->next != NULL && temp->next->id != id)
{
    temp = temp->next;
}
```

Now:

```text
temp
 ↓
101 → 102 → 103
      ↑
     del
```

Then:

```cpp
Node* del = temp->next;
```

Now `del` points to `102`.

Connect `101` directly to `103`:

```cpp
temp->next = del->next;
```

Finally:

```cpp
delete del;
```

### Complete pattern

```cpp
Node* temp = head;

while (temp->next != NULL && temp->id != id)
{
    temp = temp->next;
}
```

However, the safer beginner-friendly version used in these programs is:

```cpp
Node* temp = head;

while (temp->next != NULL && temp->next->id != id)
{
    temp = temp->next;
}

if (temp->next == NULL)
{
    cout << "Not found." << endl;
}
else
{
    Node* del = temp->next;
    temp->next = del->next;
    delete del;
}
```

---

# 15. Why Deleting the Head Is Special

Suppose:

```text
head
 ↓
101 → 102 → 103 → NULL
```

We want to delete `101`.

There is no node before `101`.

Therefore, we cannot use:

```cpp
temp->next
```

to find its previous node.

Instead:

```cpp
Node* temp = head;
head = head->next;
delete temp;
```

Result:

```text
head
 ↓
102 → 103 → NULL
```

### Standard pattern

```cpp
if (head->id == id)
{
    Node* temp = head;
    head = head->next;
    delete temp;
    return;
}
```

This is one of the most important special cases in linked-list deletion.

---

# 16. Understanding `temp`

`temp` means temporary pointer.

It is normally used for traversal.

Example:

```cpp
Node* temp = head;
```

Suppose:

```text
head
 ↓
10 → 20 → 30 → NULL
```

Initially:

```text
temp → 10
```

After:

```cpp
temp = temp->next;
```

we get:

```text
temp → 20
```

Again:

```cpp
temp = temp->next;
```

Now:

```text
temp → 30
```

Again:

```cpp
temp = temp->next;
```

Now:

```text
temp → NULL
```

The standard traversal pattern is:

```cpp
Node* temp = head;

while (temp != NULL)
{
    // Work with temp

    temp = temp->next;
}
```

Memorize this pattern.

You will use it constantly.

---

# 17. Understanding `new` and `delete`

## `new`

Used for dynamic memory allocation.

```cpp
Node* newNode = new Node;
```

Creates a node dynamically.

## `delete`

Used to release dynamically allocated memory.

```cpp
delete temp;
```

or:

```cpp
delete del;
```

### Why use them?

Linked lists dynamically create and remove nodes.

For example:

```cpp
Node* newNode = new Node;
```

creates a node.

When that node is deleted:

```cpp
delete newNode;
```

its dynamically allocated memory is released.

---

# 18. All Six CCE Sets

## Set 1 — Hospital Patient Management

### Node

```cpp
struct Node
{
    int patientID;
    string patientName;
    Node* next;
};
```

### Operations

- Add patient at end
- Delete patient by Patient ID
- Display patients

### Pattern

```text
Insert End
+
Delete
+
Display
```

---

## Set 2 — Student Record Management

### Node

```cpp
struct Node
{
    int rollNo;
    string studentName;
    float marks;
    Node* next;
};
```

### Operations

- Insert student at beginning
- Search by Roll Number
- Display students

### Pattern

```text
Insert Beginning
+
Search
+
Display
```

---

## Set 3 — Online Shopping Cart

### Node

```cpp
struct Node
{
    int productID;
    string productName;
    float price;
    Node* next;
};
```

### Operations

- Add product at end
- Delete product by Product ID
- Display cart

### Pattern

```text
Insert End
+
Delete
+
Display
```

---

## Set 4 — Library Book Management

### Node

```cpp
struct Node
{
    int bookID;
    string bookName;
    string authorName;
    Node* next;
};
```

### Operations

- Insert book at beginning
- Search by Book ID
- Display books

### Pattern

```text
Insert Beginning
+
Search
+
Display
```

---

## Set 5 — Contact List Management

### Node

```cpp
struct Node
{
    int contactID;
    string name;
    string phoneNumber;
    Node* next;
};
```

### Operations

- Add contact at end
- Delete contact by Contact ID
- Display contacts

### Pattern

```text
Insert End
+
Delete
+
Display
```

---

## Set 6 — Movie Watchlist

### Node

```cpp
struct Node
{
    int movieID;
    string movieName;
    Node* next;
};
```

### Operations

- Add movie at end
- Delete movie by Movie ID
- Display movies

### Pattern

```text
Insert End
+
Delete
+
Display
```

---

# 19. The Important Pattern Grouping

This is probably the most important section for exam preparation.

You do **NOT** have six completely different programs.

There are basically **two major program patterns**.

## Pattern A

Used by:

- Set 1
- Set 3
- Set 5
- Set 6

Operations:

```text
Insert at End
Delete by ID
Display
```

That means:

```text
Set 1 = Pattern A
Set 3 = Pattern A
Set 5 = Pattern A
Set 6 = Pattern A
```

Only the data fields and names change.

---

## Pattern B

Used by:

- Set 2
- Set 4

Operations:

```text
Insert at Beginning
Search
Display
```

That means:

```text
Set 2 = Pattern B
Set 4 = Pattern B
```

Again, the actual linked-list logic remains almost identical.

---

# 20. How to Identify the Pattern in the Exam

Do not panic when the examiner gives you a new scenario.

The scenario might be:

> Hospital Management

or:

> Library Management

or:

> Employee Management

or:

> Product Management

The story does not matter.

Look only at the **operations**.

### If the question says:

> Insert at beginning

Immediately think:

```cpp
newNode->next = head;
head = newNode;
```

---

### If it says:

> Add at end

Immediately think:

```cpp
while (temp->next != NULL)
{
    temp = temp->next;
}

temp->next = newNode;
```

---

### If it says:

> Search by ID

Immediately think:

```cpp
while (temp != NULL)
{
    if (temp->id == id)
    {
        // found
    }

    temp = temp->next;
}
```

---

### If it says:

> Delete by ID

Immediately think:

```text
1. Check empty list
2. Check whether head must be deleted
3. Find previous node
4. Bypass target
5. delete target
```

---

### If it says:

> Display all records

Immediately think:

```cpp
Node* temp = head;

while (temp != NULL)
{
    // cout

    temp = temp->next;
}
```

---

# 21. Complete Operation Cheat Sheet

## Create Node

```cpp
Node* newNode = new Node;
```

---

## Assign Data

```cpp
newNode->id = id;
newNode->name = name;
```

---

## Initialize Next

```cpp
newNode->next = NULL;
```

---

## Insert at Beginning

```cpp
newNode->next = head;
head = newNode;
```

---

## Insert at End

```cpp
Node* temp = head;

while (temp->next != NULL)
{
    temp = temp->next;
}

temp->next = newNode;
```

Remember the empty-list case:

```cpp
if (head == NULL)
{
    head = newNode;
}
```

---

## Traverse

```cpp
Node* temp = head;

while (temp != NULL)
{
    temp = temp->next;
}
```

---

## Search

```cpp
Node* temp = head;

while (temp != NULL)
{
    if (temp->id == id)
    {
        // Found
        return;
    }

    temp = temp->next;
}

// Not found
```

---

## Delete Head

```cpp
Node* temp = head;
head = head->next;
delete temp;
```

---

## Delete Middle/Last Node

```cpp
Node* del = temp->next;
temp->next = del->next;
delete del;
```

---

# 22. Time Complexity

| Operation | Complexity |
|---|---:|
| Insert at Beginning | O(1) |
| Insert at End | O(n) |
| Search | O(n) |
| Display | O(n) |
| Delete by ID | O(n) |

### Why is insertion at beginning O(1)?

Because we immediately modify:

```cpp
newNode->next = head;
head = newNode;
```

No traversal is required.

### Why is insertion at end O(n)?

Because we have to find the last node:

```cpp
while (temp->next != NULL)
```

### Why is search O(n)?

Because the required element may be the last node or may not exist at all.

### Why is deletion O(n)?

Because we may have to search through the list to find the node.

---

# 23. Common Mistakes

## Mistake 1 — Forgetting `next`

Wrong:

```cpp
struct Node
{
    int id;
    string name;
};
```

Correct:

```cpp
struct Node
{
    int id;
    string name;
    Node* next;
};
```

---

## Mistake 2 — Forgetting `new`

Wrong:

```cpp
Node* newNode;
```

Correct:

```cpp
Node* newNode = new Node;
```

---

## Mistake 3 — Forgetting to initialize `next`

For insertion at end:

```cpp
newNode->next = NULL;
```

---

## Mistake 4 — Forgetting the empty-list case

Always consider:

```cpp
if (head == NULL)
```

especially during insertion at end and deletion.

---

## Mistake 5 — Destroying `head`

Do not traverse like this:

```cpp
while (head != NULL)
{
    head = head->next;
}
```

unless you intentionally want to destroy the reference to the list.

Instead:

```cpp
Node* temp = head;

while (temp != NULL)
{
    temp = temp->next;
}
```

---

## Mistake 6 — Forgetting to move `temp`

Wrong:

```cpp
while (temp != NULL)
{
    cout << temp->id;
}
```

This creates an infinite loop.

Correct:

```cpp
while (temp != NULL)
{
    cout << temp->id;

    temp = temp->next;
}
```

---

## Mistake 7 — Search without output

This:

```cpp
if (temp->id == id)
{
    return;
}
```

does not display anything.

If the question expects the record:

```cpp
cout << "Found!" << endl;
cout << temp->id << endl;
```

---

## Mistake 8 — Incorrect deletion

Never simply do:

```cpp
temp = temp->next;
```

and assume the node has been deleted.

That only moves a pointer.

Actual deletion requires:

```cpp
Node* del = temp->next;
temp->next = del->next;
delete del;
```

---

## Mistake 9 — Forgetting the head deletion case

This can cause incorrect behavior or crashes.

Always handle:

```cpp
if (head->id == id)
```

before searching for a previous node.

---

# 24. Viva Questions and Answers

## Q1. What is a linked list?

A linked list is a linear data structure consisting of nodes where each node contains data and a pointer to the next node.

---

## Q2. What is a node?

A node is an individual element of a linked list containing data and a pointer to another node.

---

## Q3. What is `head`?

`head` is a pointer that stores the address of the first node in the linked list.

---

## Q4. What does `NULL` mean?

`NULL` indicates that a pointer does not point to another valid node.

In a linked list, the last node's `next` usually contains `NULL`.

---

## Q5. Why do we use `Node* next`?

It stores the address of the next node, allowing nodes to be connected.

---

## Q6. Why use dynamic memory allocation?

The number of nodes can change during program execution, so nodes can be dynamically created using `new`.

---

## Q7. What does `new` do?

`new` dynamically allocates memory and returns the address of the allocated object.

---

## Q8. What does `delete` do?

`delete` releases dynamically allocated memory.

---

## Q9. What is traversal?

Traversal means visiting each node of the linked list sequentially.

Example:

```cpp
Node* temp = head;

while (temp != NULL)
{
    temp = temp->next;
}
```

---

## Q10. Why do we use `temp`?

`temp` allows us to traverse the list without modifying the `head` pointer.

---

## Q11. Why is insertion at beginning O(1)?

Because it requires only two pointer changes:

```cpp
newNode->next = head;
head = newNode;
```

---

## Q12. Why is insertion at end O(n)?

Because we normally need to traverse the list to find the last node.

---

## Q13. Why is search O(n)?

Because in the worst case, every node must be checked.

---

## Q14. Why is deleting the first node different?

The first node has no previous node, so `head` itself must be updated.

---

## Q15. What happens if the linked list is empty?

```cpp
head == NULL
```

There are no nodes in the list.

---

## Q16. What happens when we insert into an empty list?

The new node becomes:

```cpp
head = newNode;
```

---

## Q17. What happens to the last node's `next`?

It points to:

```cpp
NULL
```

---

## Q18. What is the difference between an array and a linked list?

### Array

- Usually fixed-size or requires resizing
- Contiguous memory
- Direct indexing
- Insertion/deletion can be expensive

### Linked List

- Dynamic size
- Non-contiguous memory
- Sequential access
- Insertion/deletion can be efficient when the relevant position is known

---

# 25. Frequently Asked Code Questions

## What does `->` mean?

For a pointer to a structure:

```cpp
temp->id
```

means:

> Access the `id` member of the object pointed to by `temp`.

It is equivalent to:

```cpp
(*temp).id
```

but `->` is much cleaner.

---

## What does this mean?

```cpp
Node* temp = head;
```

It means:

> Create a pointer named `temp` and make it point to the same node that `head` currently points to.

---

## What does this mean?

```cpp
temp = temp->next;
```

It means:

> Move `temp` to the next node.

---

## What does this mean?

```cpp
newNode->next = head;
```

It means:

> Make the new node point to the current first node.

---

## What does this mean?

```cpp
head = newNode;
```

It means:

> Make the new node the first node.

---

## What does this mean?

```cpp
temp->next = newNode;
```

It means:

> Connect the current node to the new node.

---

## What does this mean?

```cpp
temp->next = del->next;
```

It means:

> Skip over the node being deleted and connect the previous node directly to the node after it.

For:

```text
101 → 102 → 103
```

it changes the links to:

```text
101 → 103
```

---

# 26. How to Modify a Program

The best way to prepare is to understand how to convert one scenario into another.

Suppose you know the Student program:

```cpp
struct Node
{
    int rollNo;
    string studentName;
    float marks;
    Node* next;
};
```

Now the question becomes:

> Employee Management — Employee ID, Employee Name, Salary.

You only need to change the data:

```cpp
struct Node
{
    int employeeID;
    string employeeName;
    float salary;
    Node* next;
};
```

Then change:

```cpp
temp->rollNo
```

to:

```cpp
temp->employeeID
```

and:

```cpp
temp->studentName
```

to:

```cpp
temp->employeeName
```

The linked-list logic remains the same.

---

# 27. Exam Strategy

When you receive the question, do this:

## Step 1 — Identify the fields

Example:

```text
Patient ID
Patient Name
```

Create:

```cpp
struct Node
{
    int patientID;
    string patientName;
    Node* next;
};
```

---

## Step 2 — Identify the operations

Example:

```text
Add at end
Delete by ID
Display
```

Immediately recognize:

```text
PATTERN A
```

---

## Step 3 — Write the standard skeleton

```cpp
#include <iostream>
#include <string>
using namespace std;

struct Node
{
    // fields
    Node* next;
};

Node* head = NULL;
```

---

## Step 4 — Write the required functions

For Pattern A:

```text
add()
delete()
display()
```

For Pattern B:

```text
insert()
search()
display()
```

---

## Step 5 — Write `main()`

Create a few sample records.

Call the required functions.

---

## Step 6 — Check edge cases

At minimum think about:

```text
Empty list
First node
Middle node
Last node
Element not found
```

---

# 28. Final Cheat Sheet

If you remember nothing else before the exam, remember these patterns.

## Node

```cpp
struct Node
{
    int id;
    string name;
    Node* next;
};
```

## Head

```cpp
Node* head = NULL;
```

## New Node

```cpp
Node* newNode = new Node;
```

## Insert Beginning

```cpp
newNode->next = head;
head = newNode;
```

## Insert End

```cpp
newNode->next = NULL;

if (head == NULL)
{
    head = newNode;
}
else
{
    Node* temp = head;

    while (temp->next != NULL)
    {
        temp = temp->next;
    }

    temp->next = newNode;
}
```

## Traversal

```cpp
Node* temp = head;

while (temp != NULL)
{
    // process node

    temp = temp->next;
}
```

## Search

```cpp
Node* temp = head;

while (temp != NULL)
{
    if (temp->id == id)
    {
        // Found
        return;
    }

    temp = temp->next;
}
```

## Delete Head

```cpp
Node* temp = head;
head = head->next;
delete temp;
```

## Delete Other Node

```cpp
Node* del = temp->next;
temp->next = del->next;
delete del;
```

---

# The Entire CCE in One Table

| Question | Pattern |
|---|---|
| Hospital | Insert End + Delete + Display |
| Student | Insert Beginning + Search + Display |
| Shopping Cart | Insert End + Delete + Display |
| Library | Insert Beginning + Search + Display |
| Contact List | Insert End + Delete + Display |
| Movie Watchlist | Insert End + Delete + Display |

Therefore:

```text
                    SINGLY LINKED LIST
                           │
             ┌─────────────┴─────────────┐
             │                           │
        PATTERN A                    PATTERN B
             │                           │
      Insert at End             Insert at Beginning
      Delete by ID              Search by ID
      Display                   Display
             │                           │
       Sets 1, 3, 5, 6               Sets 2, 4
```

## The real goal

Don't memorize:

```text
Set 1
Set 2
Set 3
Set 4
Set 5
Set 6
```

Memorize:

```text
INSERT BEGINNING
INSERT END
SEARCH
DELETE
DISPLAY
```

Then adapt the fields to whatever scenario appears in the CCE.

**Understand the pointer movement, and the scenario becomes almost irrelevant.**