

SE 202: High Level Programming I Average: 0.0%
Intro to Week 1
Introduction to Python Programming
Python Basics and Setup
Using the Interpreter
Variables and Data Types
Getting Started with Python
Exercise: Starting out with Python
Project Information
Coding Project: Hello, World
Coding Project: Hello, World

    Weight: 8
    Project will start Jun 28, 2026 5:00 PM, must end by Jul 12, 2026 4:59 PM

Great work on completing the first module! Time to test your learning!

Now move forward to do a check of what you've learnt, before starting out on the coding project!

Quiz questions
Great! You've completed the quiz successfully! Keep going! (Show quiz)
Tasks
0. Run Python File
mandatory

EW_Lesson Header.png

Write a Shell script that runs a Python script.

The Python file name will be saved in the environment variable $PYFILE

guillaume@ubuntu:~/py/0x00$ cat main.py 
#!/usr/bin/python3
print("Best School")

guillaume@ubuntu:~/py/0x00$ export PYFILE=main.py
guillaume@ubuntu:~/py/0x00$ ./0-run
Best School
guillaume@ubuntu:~/py/0x00$ 


EW_Lesson Footer.png

Repo:

    GitHub repository: set-high_level_programming
    Directory: python-hello_world
    File: 0-run

1. Run Inline
mandatory

EW_Lesson Header.png

Write a Shell script that runs Python code.

The Python code will be saved in the environment variable $PYCODE

guillaume@ubuntu:~/py/0x00$ export PYCODE='print(f"Best School: {88+10}")'
guillaume@ubuntu:~/py/0x00$ ./1-run_inline 
Best School: 98
guillaume@ubuntu:~/py/0x00$ 


EW_Lesson Footer.png

Repo:

    GitHub repository: set-high_level_programming
    Directory: python-hello_world
    File: 1-run_inline

2. Hello, print
mandatory

EW_Lesson Header.png

Write a Python script that prints exactly "Programming is like building a multilingual puzzle, followed by a new line.

    Use the function print

guillaume@ubuntu:~/py/0x00$ ./2-print.py 
"Programming is like building a multilingual puzzle
guillaume@ubuntu:~/py/0x00$


EW_Lesson Footer.png

Repo:

    GitHub repository: set-high_level_programming
    Directory: python-hello_world
    File: 2-print.py

3. Print Integer
mandatory

EW_Lesson Header.png

Complete this source code in order to print the integer stored in the variable number, followed by Battery street, followed by a new line.

    You can find the source code here
    The output of the script should be:
        the number, followed by Battery street,
        followed by a new line
    You are not allowed to cast the variable number into a string
    Your code must be 3 lines long
    You have to use f-strings tips

guillaume@ubuntu:~/py/0x00$ ./3-print_number.py
98 Battery street
guillaume@ubuntu:~/py/0x00$ 


EW_Lesson Footer.png

Repo:

    GitHub repository: set-high_level_programming
    Directory: python-hello_world
    File: 3-print_number.py

4. Print Float
mandatory

EW_Lesson Header.png

Complete the source code in order to print the float stored in the variable number with a precision of 2 digits.

    You can find the source code here
    The output of the program should be:
        Float: , followed by the float with only 2 digits
        followed by a new line
    You are not allowed to cast number to string
    You have to use f-strings

guillaume@ubuntu:~/py/0x00$ ./4-print_float.py
Float: 3.14
guillaume@ubuntu:~/py/0x00$ 


EW_Lesson Footer.png

Repo:

    GitHub repository: set-high_level_programming
    Directory: python-hello_world
    File: 4-print_float.py

5. Print String
mandatory

EW_Lesson Header.png

Complete this source code in order to print 3 times a string stored in the variable str, followed by its first 9 characters.

#!/usr/bin/python3
str = "Elmwood Institute"
# YOUR CODE GOES HERE. PLEASE REMOVE THIS LINE

    Copy the source code above and complete it.
    The output of the program should be:
        3 times the value of str
        followed by a new line
        followed by the 9 first characters of str
        followed by a new line
    You are not allowed to use any loops or conditional statement
    Your program should be maximum 5 lines long

guillaume@ubuntu:~/py/0x00$ ./5-print_string.py 
SET SET SET
SET
guillaume@ubuntu:~/py/0x00$ 


EW_Lesson Footer.png

Repo:

    GitHub repository: set-high_level_programming
    Directory: python-hello_world
    File: 5-print_string.py

6. Play with Strings
mandatory

EW_Lesson Header.png

Complete this source code below to print Welcome to Elmwood Institute!

#!/usr/bin/python3
str1 = "Elmwood"
str2 = "Institute"
# YOUR CODE GOES HERE. PLEASE REMOVE THIS LINE
print(f"Welcome to {str1} {str2}!")


    Copy the source code above.
    You are not allowed to use any loops or conditional statements.
    You have to use the variables str1 and str2 in your new line of code
    Your program should be exactly 5 lines long

guillaume@ubuntu:~/py/0x00$ ./6-concat.py
Welcome to SET!
guillaume@ubuntu:~/py/0x00$ wc -l 6-concat.py
5 6-concat.py
guillaume@ubuntu:~/py/0x00$ 


EW_Lesson Footer.png

Repo:

    GitHub repository: set-high_level_programming
    Directory: python-hello_world
    File: 6-concat.py

7. Copy - Cut - Paste
mandatory

EW_Lesson Header.png

Complete this source code:

#!/usr/bin/python3
word = "Elmwood"
# YOUR CODE GOES HERE. PLEASE REMOVE THIS LINE
print(f"First 3 letters: {word_first_3}")
print(f"Last 2 letters: {word_last_2}")
print(f"Middle word: {middle_word}")


    Copy the source code above.
    You are not allowed to use any loops or conditional statements
    Your program should be exactly 8 lines long
    word_first_3 should contain the first 3 letters of the variable word
    word_last_2 should contain the last 2 letters of the variable word
    middle_word should contain the value of the variable word without the first and last letters

guillaume@ubuntu:~/py/0x00$ ./7-edges.py
First 3 letters: Hol
Last 2 letters: on
Middle word: olberto
guillaume@ubuntu:~/py/0x00$ wc -l 7-edges.py
8 7-edges.py
guillaume@ubuntu:~/py/0x00$ 


EW_Lesson Footer.png

Repo:

    GitHub repository: set-high_level_programming
    Directory: python-hello_world
    File: 7-edges.py

8. Create a New Sentence
mandatory

EW_Lesson Header.png

Complete this source code to print object-oriented programming with Python, followed by a new line.

    You can find the source code here
    You are not allowed to use any loops or conditional statements
    Your program should be exactly 5 lines long
    You are not allowed to create new variables
    You are not allowed to use string literals

guillaume@ubuntu:~/py/0x00$ ./8-concat_edges.py
object-oriented programming with Python
guillaume@ubuntu:~/py/0x00$ wc -l 8-concat_edges.py
5 8-concat_edges.py
guillaume@ubuntu:~/py/0x00$ 


EW_Lesson Footer.png

Repo:

    GitHub repository: set-high_level_programming
    Directory: python-hello_world
    File: 8-concat_edges.py

9. Easter Egg
mandatory

EW_Lesson Header.png

Write a Python script that prints "The Zen of Python", by TimPeters, followed by a new line.

    Your script should be maximum 98 characters long (please check with wc -m 9-easter_egg.py)

guillaume@ubuntu:~/py/0x00$ ./9-easter_egg.py
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
guillaume@ubuntu:~/py/0x00$


EW_Lesson Footer.png

Repo:

    GitHub repository: set-high_level_programming
    Directory: python-hello_world
    File: 9-easter_egg.py

10. Linked List Cycle
mandatory

EW_Lesson Header.png

Technical interview preparation:

    You are not allowed to google anything
    Whiteboard first
    This task and all future technical interview prep tasks will include checks for the efficiency of your solution, i.e. is your solution's runtime fast enough, does your solution require extra memory usage / mallocs, etc.

Write a function in C that checks if a singly linked list has a cycle in it.

    Prototype: int check_cycle(listint_t *list);
    Return: 0 if there is no cycle, 1 if there is a cycle

Requirements:

    Only these functions are allowed: write, printf, putchar, puts, malloc, free

carrie@ubuntu:~/0x00$ cat lists.h
#ifndef LISTS_H
#define LISTS_H

#include <stdlib.h>

/**
 * struct listint_s - singly linked list
 * @n: integer
 * @next: points to the next node
 *
 * Description: singly linked list node structure
 * 
 */
typedef struct listint_s
{
	int n;
	struct listint_s *next;
} listint_t;

size_t print_listint(const listint_t *h);
listint_t *add_nodeint(listint_t **head, const int n);
void free_listint(listint_t *head);
int check_cycle(listint_t *list);

#endif /* LISTS_H */

carrie@ubuntu:~/0x00$ cat 10-linked_lists.c
#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * print_listint - prints all elements of a listint_t list
 * @h: pointer to head of list
 * Return: number of nodes
 */
size_t print_listint(const listint_t *h)
{
	const listint_t *current;
	unsigned int n; /* number of nodes */

	current = h;
	n = 0;
	while (current != NULL)
	{
		printf("%i\n", current->n);
		current = current->next;
		n++;
	}

	return (n);
}

/**
 * add_nodeint - adds a new node at the beginning of a listint_t list
 * @head: pointer to a pointer of the start of the list
 * @n: integer to be included in node
 * Return: address of the new element or NULL if it fails
 */
listint_t *add_nodeint(listint_t **head, const int n)
{
	listint_t *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = n;
	new->next = *head;
	*head = new;

	return (new);
}

/**
 * free_listint - frees a listint_t list
 * @head: pointer to list to be freed
 * Return: void
 */
void free_listint(listint_t *head)
{
	listint_t *current;

	while (head != NULL)
	{
		current = head;
		head = head->next;
		free(current);
	}
}

carrie@ubuntu:~/0x00$ cat 10-main.c
#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"

/**
 * main - check the code
 *
 * Return: Always 0.
 */
int main(void)
{
	listint_t *head;
	listint_t *current;
	listint_t *temp;
	int i;

	head = NULL;
	add_nodeint(&head, 0);
	add_nodeint(&head, 1);
	add_nodeint(&head, 2);
	add_nodeint(&head, 3);
	add_nodeint(&head, 4);
	add_nodeint(&head, 98);
	add_nodeint(&head, 402);
	add_nodeint(&head, 1024);
	print_listint(head);

	if (check_cycle(head) == 0)
		printf("Linked list has no cycle\n");
	else if (check_cycle(head) == 1)
		printf("Linked list has a cycle\n");

	current = head;
	for (i = 0; i < 4; i++)
		current = current->next;
	temp = current->next;
	current->next = head;

	if (check_cycle(head) == 0)
		printf("Linked list has no cycle\n");
	else if (check_cycle(head) == 1)
		printf("Linked list has a cycle\n");

	current = head;
	for (i = 0; i < 4; i++)
		current = current->next;
	current->next = temp;

	free_listint(head);

	return (0);
}

carrie@ubuntu:~/0x00$ gcc -Wall -Werror -Wextra -pedantic -std=gnu89 10-main.c 10-check_cycle.c 10-linked_lists.c -o cycle
carrie@ubuntu:~/0x00$$ ./cycle 
1024
402
98
4
3
2
1
0
Linked list has no cycle
Linked list has a cycle
carrie@ubuntu:~/0x00$

    Solving a problem is already a big win! but finding the best and optimal way to solve it, it's way better! Think about the most optimal / fastest way to do it.


EW_Lesson Footer.png

Repo:

    GitHub repository: set-high_level_programming
    Directory: python-hello_world
    File: 10-check_cycle.c, lists.h

Copyright © 2026 SET, All rights reserved.

