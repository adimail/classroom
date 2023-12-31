#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

namespace ll{

    template <typename T>
    struct Node {
        T data;          // Data stored in the node
        Node* next;      // Pointer to the next node
    };


    template <typename T>
    class LinkedList {
    private:
        Node<T>* head;  // Pointer to the head of the list

    public:
        LinkedList() : head(nullptr) {}

        // Method to insert a new node at the beginning of the list
        void insertAtStart(T data) {
            Node<T>* newNode = new Node<T>;
            newNode->data = data;
            newNode->next = head;
            head = newNode;
        }

        // Method to traverse and print the linked list
        void display() {
            Node<T>* current = head;
            while (current != nullptr) {
                cout << current->data << " ";
                current = current->next;
            }
            cout << endl;
        }
        // Add more methods like insertAtEnd, delete, search, etc. as needed
    };

}
