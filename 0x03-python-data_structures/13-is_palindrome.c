#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to the first node of the list
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
    listint_t *fast = *head;
    listint_t *slow = *head;
    listint_t *prev = NULL;
    int result = 1;

    if (*head == NULL)
        return (1);

    while (fast != NULL && fast->next != NULL)
    {
        fast = fast->next->next;

        listint_t *next = slow->next;
        slow->next = prev;
        prev = slow;
        slow = next;
    }

    if (fast != NULL)
        slow = slow->next;

    while (slow != NULL)
    {
        if (prev->n != slow->n)
        {
            result = 0;
            break;
        }
        slow = slow->next;
        prev = prev->next;
    }

    return (result);
}
