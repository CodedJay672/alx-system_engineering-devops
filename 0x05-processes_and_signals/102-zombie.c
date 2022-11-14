#include <unistd.h>
#include <stdlib.h>
#include <sys/types.h>
#include <stdio.h>

int infinite_while(void);

/**
 * main - main entry point
 * Return: Always 0 on success
 */

int main(void)
{
	pid_t child_pr;
	int i = 0;

	while (i <= 4)
	{
		child_pr = fork();
		if (child_pr > 0)
		{
			printf("Zombie process created, PID: %d\n", child_pr);
			sleep(10);
		}
		else
		{
			exit(0);
		}
		i++;
	}

	infinite_while();
	return (0);
}

/**
 * infinite_while -> infinite while loop
 * Return: returns 0 on success
 */

int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}
