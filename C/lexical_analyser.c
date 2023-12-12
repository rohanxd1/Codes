#include <string.h>
#include <ctype.h>
#include <stdio.h>

#define MAX_IDENTIFIER_LENGTH 50

void processKeywordOrIdentifier(const char *str) {
    const char *keywords[] = {"for", "while", "do", "int", "float", "char", "double", "static", "switch", "case"};
    int numKeywords = sizeof(keywords) / sizeof(keywords[0]);

    for (int i = 0; i < numKeywords; ++i) {
        if (strcmp(keywords[i], str) == 0) {
            printf("\n%s is a keyword", str);
            return;
        }
    }

    printf("\n%s is an identifier", str);
}

int main() {
    FILE *f1, *f2, *f3;
    char c;
    int num[100], lineno = 0, tokenvalue = 0, i = 0, j = 0;
    char str[MAX_IDENTIFIER_LENGTH];

    printf("\nEnter the C program: ");
    f1 = fopen("input", "w");
    if (f1 == NULL) {
        printf("Failed to open the file.\n");
        return 1;  // Terminate the program if file opening fails
    }

    while ((c = getchar()) != EOF) {
        putc(c, f1);
    }
    fclose(f1);

    f1 = fopen("input", "r");
    f2 = fopen("identifier", "w");
    f3 = fopen("specialchar", "w");

    while ((c = getc(f1)) != EOF) {
        if (isdigit(c)) {
            tokenvalue = c - '0';
            c = getc(f1);
            while (isdigit(c)) {
                tokenvalue = tokenvalue * 10 + c - '0';
                c = getc(f1);
            }
            num[i++] = tokenvalue;
            ungetc(c, f1);
        } else if (isalpha(c)) {
            int k = 0;
            do {
                if (k < MAX_IDENTIFIER_LENGTH - 1) {
                    str[k++] = c;
                }
                c = getc(f1);
            } while (isdigit(c) || isalpha(c) || c == '_' || c == '$');
            str[k] = '\0';
            fprintf(f2, "%s ", str);
            ungetc(c, f1);
        } else if (c == ' ' || c == '\t') {
            // Do nothing (skip whitespace)
        } else if (c == '\n') {
            lineno++;
        } else {
            putc(c, f3);
        }
    }

    fclose(f2);
    fclose(f3);
    fclose(f1);

    printf("\nThe numbers in the program are: ");
    for (j = 0; j < i; j++) {
        printf("%d ", num[j]);
    }
    printf("\n");

    f2 = fopen("identifier", "r");
    printf("The keywords and identifiers are:");
    while (fscanf(f2, "%s", str) != EOF) {
        processKeywordOrIdentifier(str);
    }
    fclose(f2);

    f3 = fopen("specialchar", "r");
    printf("\nSpecial characters are: ");
    while ((c = getc(f3)) != EOF) {
        printf("%c", c);
    }
    printf("\n");

    fclose(f3);

    printf("Total number of lines: %d", lineno);

    return 0;
}
