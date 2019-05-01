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

	if (!new || !head)
		return (NULL);
	new->n = number;
	trav = *head;
	if (number < trav->n || !trav)
	{
		new->next = trav;
		*head = new;
		return (new);
	}
	while (trav)
	{
		if ((trav->next && number <= trav->next->n) || !trav->next)
		{
			new->next = trav->next;
			trav->next = new;
			return (new);
		}
		trav = trav->next;
	}
	free(new);
	return (NULL);
}
