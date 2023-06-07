#include "lists.h"
#include <stdio.h>
#include <stdlib.h>
#include <stddef.h>

/**
 * insert_node - A function in C that inserts a number into
 * a sorted singly linked list.
 * @head: the head of the list
 * @number: an integer
 *
 * Return: (success) new node, or NULL if failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *newNode, *current, *prev;

	if (head == NULL)
		return (NULL);
	current = *head;
	prev = NULL;
	while (current != NULL && current->n < number)
	{
		prev = current;
		current = current->next;
	}
	newNode = malloc(sizeof(listint_t));
	if (newNode == NULL)
		return (NULL);
	newNode->n = number;
	if (prev == NULL)
	{
		newNode->next = *head;
		*head = newNode;
	}
	else
	{
		newNode->next = current;
		prev->next = newNode;
	}
	return newNode;
}
