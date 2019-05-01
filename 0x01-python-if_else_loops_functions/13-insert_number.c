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
	listint_t *new;
	listint_t *trav;

	new = malloc(sizeof(listint_t));
	if (!new || !head)
		return (NULL);
	new->n = number;
	trav = *head;
	if (number < trav->n || !trav)
	{
		new->next = trav->next;
		*head = new;
		return (new);
	}
	while (trav->next)
	{
		if (number < trav->next->n)
		{
			new->next = trav->next;
			trav->next = new;
			return (new);
		}
		trav = trav->next;
	}
	new->next = trav->next;
	trav->next = new;
	return (new);
}
