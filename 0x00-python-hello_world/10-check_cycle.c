#include "lists.h"

/**
* check_cycle - checks if a singly linked list has a cycle in it
* @list: singly linked list to check
*
* Return: 0 if no cycle or 1 if cycle
*/

int check_cycle(listint_t *list)
{
	listint_t *slow, *fast;

	slow = list;
	fast = list;

	while (slow && fast)
	{
		if (fast->next)
			fast = fast->next->next;
		else
			break;
		slow = slow->next;
		if (slow == fast)
			return (1);
	}
	return (0);
}
