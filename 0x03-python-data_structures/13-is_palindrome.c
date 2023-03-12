#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to head of list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *temp = *head;
	int i = 0, j = 0, k = 0, l = 0, m = 0, n = 0;
	int *arr;

	if (head == NULL || *head == NULL)
		return (1);
	while (temp != NULL)
	{
		temp = temp->next;
		i++;
	}
	arr = malloc(sizeof(int) * i);
	if (arr == NULL)
		return (0);
	temp = *head;
	while (temp != NULL)
	{
		arr[j] = temp->n;
		temp = temp->next;
		j++;
	}
	for (k = 0; k < i; k++)
	{
		if (arr[k] != arr[i - 1 - k])
		{
			free(arr);
			return (0);
		}
	}
	free(arr);
	return (1);
}
