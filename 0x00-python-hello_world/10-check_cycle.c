#include <stdio.h>
#include <stdlib.h>
typedef struct listint
{
int n;
struct listint *next;
}
listint_t;
int check_cycle(listint_t *list)
{
listint_t *fast, *slow;
fast = list;
slow = list;
while (fast != NULL && fast->next != NULL)
{
fast = fast->next->next;
slow = slow->next;
if (fast == slow)
return (1);
}
return (0);
}
