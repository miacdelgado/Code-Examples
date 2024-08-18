#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

#define MAX_ATTEMPTS 6
#define WORD_LENGTH 4  // Fixed length for the word

void displayWord(char word[], char guessedLetters[], int wordLength);
int isWordGuessed(char word[], char guessedLetters[], int wordLength);
int isLetterInWord(char letter, char word[], int wordLength);

int main() {
    char word[WORD_LENGTH + 1] = "java";  // Fixed 4-letter word
    char guessedLetters[WORD_LENGTH + 1] = {0};
    char letter;
    int attempts = 0;

    // Provide hints for the word
    printf("Guess the 4-letter word! You have %d attempts.\n", MAX_ATTEMPTS);
    printf("Hint: The word is a popular programming language.\n");

    while (attempts < MAX_ATTEMPTS) {
        displayWord(word, guessedLetters, WORD_LENGTH);
        printf("Enter a letter: ");
        scanf(" %c", &letter);
        letter = tolower(letter);

        if (isLetterInWord(letter, word, WORD_LENGTH)) {
            guessedLetters[strlen(guessedLetters)] = letter;
        } else {
            attempts++;
            printf("Incorrect guess! You have %d attempts left.\n", MAX_ATTEMPTS - attempts);
        }

        if (isWordGuessed(word, guessedLetters, WORD_LENGTH)) {
            printf("Congratulations! You've guessed the word: %s\n", word);
            return 0;
        }
    }

    printf("Sorry, you've run out of attempts. The word was: %s\n", word);
    return 0;
}

void displayWord(char word[], char guessedLetters[], int wordLength) {
    printf("Word: ");
    for (int i = 0; i < wordLength; i++) {
        if (strchr(guessedLetters, word[i])) {
            printf("%c ", word[i]);
        } else {
            printf("_ ");
        }
    }
    printf("\n");
}

int isWordGuessed(char word[], char guessedLetters[], int wordLength) {
    for (int i = 0; i < wordLength; i++) {
        if (!strchr(guessedLetters, word[i])) {
            return 0;
        }
    }
    return 1;
}

int isLetterInWord(char letter, char word[], int wordLength) {
    for (int i = 0; i < wordLength; i++) {
        if (word[i] == letter) {
            return 1;
        }
    }
    return 0;
}