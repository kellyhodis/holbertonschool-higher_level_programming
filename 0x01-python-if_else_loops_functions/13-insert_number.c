#include "lists.h"

/**
* insert_node - inserts a number into a sorted singly linked list
* @head: first node of list
* @number: number to insert into list
*
* Return: address of the new node or NULL
*/

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new = malloc(sizeof(listint_t));
	listint_t *trav;

	if (!new)
		return (NULL);
	new->n = number;
	trav = *head;
	while (trav)
	{
		if (number < trav->next->n)
		{
			if (number < trav->n)
			{
				new->next = trav;
				return (new);
			}
			new->next = trav->next;
			trav->next = new;
			return (new);
		}
		trav = trav->next;
	}
	return (NULL);
}
