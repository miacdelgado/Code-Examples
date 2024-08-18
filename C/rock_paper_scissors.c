#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int generateRandomNumber(int n) {
    return rand() % n;
}

int main() {
    int playerScore = 0, computerScore = 0;
    char playerName[50];
    int playerChoice, computerChoice;

    srand(time(NULL));

    printf("Enter your name: ");
    fflush(stdout); // Ensure the output buffer is flushed
    scanf("%s", playerName);
    printf("Name entered: %s\n", playerName);
    fflush(stdout); // Ensure the output buffer is flushed

    for (int i = 0; i < 3; i++) {
        printf("\nRound %d\n", i + 1);
        fflush(stdout); // Ensure the output buffer is flushed
        printf("Choose: 0 for Rock, 1 for Paper, 2 for Scissors: ");
        fflush(stdout); // Ensure the output buffer is flushed

        if (scanf("%d", &playerChoice) != 1 || playerChoice < 0 || playerChoice > 2) {
            printf("Invalid input. Please enter 0, 1 or 2.\n");
            fflush(stdout); // Ensure the output buffer is flushed
            i--;
            while (getchar() != '\n'); // Clear the input buffer
            continue;
        }

        printf("Player choice: %d\n", playerChoice); // Debug statement
        fflush(stdout); // Ensure the output buffer is flushed

        computerChoice = generateRandomNumber(3);
        printf("Computer chose: %d\n", computerChoice);
        fflush(stdout); // Ensure the output buffer is flushed

        if (playerChoice == computerChoice) {
            printf("It's a draw!\n");
        } 
        else if ((playerChoice == 0 && computerChoice == 2) ||
                   (playerChoice == 1 && computerChoice == 0) ||
                   (playerChoice == 2 && computerChoice == 1)) {
            printf("%s wins this round!\n", playerName);
            playerScore++;
        } 
        else {
            printf("Computer wins this round!\n");
            computerScore++;
        }
        fflush(stdout); // Ensure the output buffer is flushed
    }

    printf("\nFinal Scores:\n");
    printf("%s: %d\n", playerName, playerScore);
    printf("Computer: %d\n", computerScore);
    fflush(stdout); // Ensure the output buffer is flushed

    if (playerScore > computerScore) {
        printf("Congratulations %s, you won the game!\n", playerName);
    } 
    else if (computerScore > playerScore) {
        printf("Sorry %s, you lost the game!\n", playerName);
    } 
    else {
        printf("It's a draw!\n");
    }
    fflush(stdout); // Ensure the output buffer is flushed

    return 0;
}