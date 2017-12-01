#include <stdio.h>
#include <stdlib.h> 

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

	fseek(file, 0, SEEK_END);
	int length = ftell(file);
	printf("File length: %d", length);
	fseek(file, 0, SEEK_SET);

	char c;
	int numbers[length];
	int i = 0;
	int j = -1;
	int sum = 0;

	while((c = (char)fgetc(file)) != EOF) {
		j = c - '0';
		numbers[i] = j;
		i++;
	}

	
	for(int k = 0; k < length; k++) {
		printf("Number at %d: %d\n", k, numbers[k]);
	}
	

	int posToCheck = 0;
	for(int k = 0; k < length; k++) {
		posToCheck = k + (length / 2);

		if(posToCheck >= length) {
			posToCheck -= length;
		}

		printf("Position to check: %d\n", posToCheck);

		if(numbers[k] == numbers[posToCheck]) {
			sum += numbers[k];
		}
	}

	


	printf("The sum of repeating numbers in the input is: %d\n", sum);
	return 0;
}