#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * reverse_list - reverses a linked list
 * @head: pointer to pointer to the head of the list
 */
void reverse_list(listint_t **head)
{
	listint_t *prev = NULL;
	listint_t *current = *head;
	listint_t *next = NULL;

	while (current != NULL) {
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}

	*head = prev;
}

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to pointer to the head of the list
 * Return: 1 if the list is a palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow_ptr = *head;
	listint_t *fast_ptr = *head;
	listint_t *prev_slow_ptr = *head;
	listint_t *mid_node = NULL;
	int is_palindrome = 1;

	if (*head != NULL && (*head)->next != NULL) {
		while (fast_ptr != NULL && fast_ptr->next != NULL) {
			fast_ptr = fast_ptr->next->next;
			prev_slow_ptr = slow_ptr;
			slow_ptr = slow_ptr->next;
		}

		if (fast_ptr != NULL) {
			mid_node = slow_ptr;
			slow_ptr = slow_ptr->next;
		}

		reverse_list(&slow_ptr);

		while (slow_ptr != NULL) {
			if ((*head)->n != slow_ptr->n) {
				is_palindrome = 0;
				break;
			}
			(*head) = (*head)->next;
			slow_ptr = slow_ptr->next;
		}

		reverse_list(&mid_node);

		if (mid_node != NULL) {
			prev_slow_ptr->next = mid_node;
		} else {
			prev_slow_ptr->next = NULL;
		}
	}

	return is_palindrome;
}

