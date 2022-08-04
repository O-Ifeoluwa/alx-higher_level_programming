#include "lists.h"
#include <stdlib.h>
#include <string.h>
#include <stdio.h>

/**
 * insert_node -  inserts a number into a sorted singly linked list
 * @head: singly list head
 * @number: number to insert
 * Return: the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *ptr1, *ptr2, *new;

	new = malloc(sizeof(listint_t));

	if (new == NULL)
		return (NULL);
	new->n = number;

	if (head == NULL)
		return (new);

	ptr1 = *head;
	while ((ptr1->n < number) && ptr1->next != NULL)
	{
		ptr2 = ptr1;
		ptr1 = ptr1->next;
	}

	if (ptr1->next == NULL)
		ptr1->next = new;
	else if (ptr2 == *head)
	{
		if (ptr2->n < new->n)
			ptr2->next = new;
		else
			new->next = ptr2;
	}
	else
	{
		ptr2->next = new;
		new->next = ptr1;
	}

	return (new);
}
