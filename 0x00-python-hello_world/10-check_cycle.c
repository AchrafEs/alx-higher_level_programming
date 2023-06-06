#include "lists.h"

/**
 * check_cycle - A function that checks for cycles
 * @list: a struct
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle.
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *rapid = list;

	if (list == NULL)
	{
		return (0);
	}
	while (rapid != NULL && rapid->next != NULL)
	{
		slow = slow->next;
		rapid = rapid->next->next;
		if (slow == rapid)
		{
			return (1);
		}
	}
	return (0);
}
