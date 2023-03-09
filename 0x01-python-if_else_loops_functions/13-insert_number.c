#include <stdlib.h>
/**
* insert_node - inserts a number into a sorted singly linked list
* @head: pointer to pointer to head of list
* @number: number to insert into list
*
* Return: pointer to new node, or NULL if failed
*/
listint_t *insert_node(listint_t **head, int number)
{
listint_t *node = NULL, *current = *head;
node = malloc(sizeof(listint_t));
if (!node)
return (NULL);
node->n = number;
node->next = NULL;
if (*head == NULL)
{
*head = node;
return (node);
}
if (number < current->n)
{
node->next = current;
*head = node;
return (node);
}
while (current->next)
{
if (number >= current->n && number <= current->next->n)
{
node->next = current->next;
current->next = node;
return (node);
}
current = current->next;
}
current->next = node;
return (node);
}
