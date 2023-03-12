#include <stdio.h>
#include <stdlib.h>

typedef struct listint_s
{
    int n;
    struct listint_s *next;
} listint_t;

int is_palindrome(listint_t **head)
{
    int count = 0;
    listint_t *current = *head;
    listint_t *temp = *head;

    // Count the number of nodes in the list
    while (current != NULL)
    {
        current = current->next;
        count++;
    }

    // If the list has no elements, it is a palindrome
    if (count == 0)
        return 1;

    // Set current to the head of the list
    current = *head;
    int mid = count / 2;
    int i;

    // Iterate up to the middle of the list
    for (i = 0; i < mid; i++)
        current = current->next;

    // Reverse the second half of the list
    listint_t *prev = NULL;
    listint_t *next = NULL;
    while (current != NULL)
    {
        next = current->next;
        current->next = prev;
        prev = current;
        current = next;
    }

    // Compare the first and second half of the list
    while (prev != NULL)
    {
        if (temp->n != prev->n)
            return 0;

        prev = prev->next;
        temp = temp->next;
    }

    return 1;
}
