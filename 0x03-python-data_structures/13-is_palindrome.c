#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
* is_palindrome - checks if a singly linked list is a palindrome
* @head: pointer to the head of the list
*
* Return: 0 if it is not a palindrome, 1 if it is a palindrome
*/
int is_palindrome(listint_t **head)
{
listint_t *slow, *fast, *prev;
int result = 1;
if (head == NULL || *head == NULL || (*head)->next == NULL)
return (1);
slow = *head;
fast = *head;
while (fast != NULL && fast->next != NULL)
{
fast = fast->next->next;
prev = slow;
slow = slow->next;
}
if (fast != NULL)
slow = slow->next;
prev->next = NULL;
while (slow != NULL)
{
if ((*head)->n != slow->n)
result = 0;
slow = slow->next;
head = &(*head)->next;
}
return (result);
}
