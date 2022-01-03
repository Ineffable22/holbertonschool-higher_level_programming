#include "lists.h"
/**
 * is_palindrome - checks if a linked list is a palindrome
 * @head: double pointer of the linked list
 *
 * Return: 1 if it is, 0 if not
 */
int is_palindrome(listint_t **head)
{
	if (head == NULL || *head == NULL)
		return (1);
	return (checker(head, *head));
}

/**
 * checker - function to check if the list is palindrome
 * @head: double pointer of the linked list
 * @last: ptr to the end of the list
 *
 * Return: 1 if it is, 0 if not
 */
int checker(listint_t **head, listint_t *last)
{
	if (last == NULL)
		return (1);
	if (checker(head, last->next) && (*head)->n == last->n)
	{
		*head = (*head)->next;
		return (1);
	}
	return (0);
}
