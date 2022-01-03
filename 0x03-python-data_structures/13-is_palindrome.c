#include "lists.h"
/**
 * is_palindrome - checks if a linked list is a palindrome
 * @head: double pointer to the linked list
 *
 * Return: 1 if it is, 0 if not
 */
int is_palindrome(listint_t **head)
{
	listint_t *first_node = *head;
	listint_t *last_node = *head;
	listint_t *carry_node = NULL;
	int i = 0, count = 0;

	if (*head == NULL || (*head)->next == NULL)
		return (1);
	while (last_node->next != NULL)
	{
		last_node = last_node->next;
		count += 1;
	}
	if (count % 2 != 0)
	{
		count -= 1;
	}
	while (i < count / 2)
	{
		if (first_node->n != last_node->n)
		{
			return (0);
		}
		first_node = first_node->next;
		carry_node = first_node;
		while (carry_node->next != last_node)
		{
			carry_node = carry_node->next;
		}
		last_node = carry_node;
		i++;
	}
	return (1);
}
