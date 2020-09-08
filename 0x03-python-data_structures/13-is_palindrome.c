#include "lists.h"

/**
 *is_palindrome - checks if a singly linked list is a palindrome.
 *@head: head pointer
 *Return: 0.
 */

int is_palindrome(listint_t **head)
{
	listint_t *slow = *head, *fast = *head, *prev = *head;
	listint_t *second = NULL, *mid = NULL;
	int res = 0;

	if (!fast || !fast->next)
		return (1);
	while (fast && fast->next)
	{
		fast = fast->next->next;
		prev = slow;
		slow = slow->next;
	}

	if (fast)
	{
		mid = slow;
		slow = slow->next;
	}
	second = slow;
	prev->next = NULL;
	reverse_linked_list(&second);
	res = compare_linked_list(*head, second);
	reverse_linked_list(&second);
	if (mid)
	{
		prev->next = mid;
		mid->next = second;
	} else
		prev->next = second;
	return (res);
}

/**
 *reverse_linked_list - reverse linked list
 *@head: head list.
 */

void reverse_linked_list(listint_t **head)
{
	listint_t *prev = NULL;
	listint_t *current = *head;
	listint_t *next;

	while (current)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
	*head = prev;
}

/**
 *compare_linked_list - compare linked list.
 *@head1: head first list.
 *@head2: head second list.
 *Return: 0.
 */

int compare_linked_list(listint_t *head1, listint_t *head2)
{
	listint_t *temp1 = head1;
	listint_t *temp2 = head2;

	while (temp1 && temp2)
	{
		if (temp1->n == temp2->n)
		{
		temp1 = temp1->next;
		temp2 = temp2->next;
		}
		else
			return (0);
	}
	if (temp1 == NULL && temp2 == NULL)
		return (1);
	return (0);
}
