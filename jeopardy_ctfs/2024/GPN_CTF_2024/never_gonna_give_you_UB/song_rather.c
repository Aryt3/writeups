#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

void scratched_record() {
	printf("Oh no, your record seems scratched :(\n");
	printf("Here's a shell, maybe you can fix it:\n");
	execve("/bin/sh", NULL, NULL);
}

extern char *gets(char *s);

int main() {
	printf("Song rater v0.1\n-------------------\n\n");
	char buf[0xff];
	printf("Please enter your song:\n");
	gets(buf);
	printf("\"%s\" is an excellent choice!\n", buf);
	return 0;
}
