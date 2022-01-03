#include "lists.h"
/**
 * is_palindrome - checks if a linked list is a palindrome
 * @head: double pointer to the linked list
 *
 * Return: 1 if it is, 0 if not
 */
int is_palindrome(listint_t **head)
{
	listint_t *tmp1 = *head, *tmp2 = *head;
	int i = 1, j = 0, k = 0, l = 1;

	if (*head == NULL || (*head)->next == NULL)
		return (1);
	while (tmp1->next)
	{
		tmp1 = tmp1->next;
		i++;
	}
	tmp1 = *head;
	if (i % 2 == 0)
		k = i;
	else
		k = i + 1;
	j = i;
	while (i >= k / 2)
	{
		while (j > l)
		{
			tmp1 = tmp1->next;
			j--;
		}
		if (tmp1->n != tmp2->n)
			return (0);
		i--;
		j = i;
		l++;
		tmp2 = tmp2->next;
		tmp1 = tmp2;
	}
	return (1);
}
