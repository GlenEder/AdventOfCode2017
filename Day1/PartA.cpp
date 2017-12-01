#include <stdio.h>
#include <stdlib.h> 
#include <vector>

using namespace std;

int main(int argc, char const *argv[])
{
	if(argc < 2) {
		printf("Usuage: <program> <input filename>\n");
		return 0;
	}

	FILE *file = fopen(argv[1], "r");
	if(file == NULL) {
		printf("Error opening %s\n", argv[1]);
		return 0;
	}

	char c1;
	char c2;
	int firstNumber = 0;
	int i = -1;
	int j = -1;
	int sum = 0;
	while((c2 = (char)fgetc(file)) != EOF) {
		j = c2 - '0';
		printf("%d", j);
		if(i > -1) {
			if(i == j) {
				sum += i;
			}
		}else {
			firstNumber = j;
		}

		i = j;
	}

	if(j == firstNumber) {
		sum += firstNumber;
	}


	printf("The sum of repeating numbers in the input is: %d\n", sum);
	return 0;
}