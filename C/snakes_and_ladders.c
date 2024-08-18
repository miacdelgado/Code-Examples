#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define WIN_POSITION 100
#define START_POSITION 1
#define NUM_SNAKES 5
#define NUM_LADDERS 5

int snakes[NUM_SNAKES][2] = {{16, 6}, {47, 26}, {49, 11}, {56, 53}, {62, 19}};
int ladders[NUM_LADDERS][2] = {{1, 38}, {7, 14}, {15, 26}, {28, 84}, {21, 42}};

void printBoard(int playerPosition) {
    printf("Player is at position: %d\n", playerPosition);
}

int rollDice() {
    return (rand() % 6) + 1;
}

int movePlayer(int playerPosition, int diceRoll) {
    playerPosition += diceRoll;
    if (playerPosition > WIN_POSITION) {
        playerPosition = WIN_POSITION - (playerPosition - WIN_POSITION);
    }
    return playerPosition;
}

int checkSnakesLadders(int position) {
    for (int i = 0; i < NUM_SNAKES; i++) {
        if (snakes[i][0] == position) {
            printf("Player landed on a snake! Sliding down from %d to %d.\n", position, snakes[i][1]);
            return snakes[i][1];
        }
    }
    for (int i = 0; i < NUM_LADDERS; i++) {
        if (ladders[i][0] == position) {
            printf("Player landed on a ladder! Climbing up from %d to %d.\n", position, ladders[i][1]);
            return ladders[i][1];
        }
    }
    return position;
}

int main() {
    srand(time(NULL));
    int playerPosition = START_POSITION;
    int diceRoll;

    printf("Welcome to Snakes and Ladders!\n");

    while (playerPosition < WIN_POSITION) {
        printBoard(playerPosition);
        printf("Press Enter to roll the dice...");
        getchar(); // Wait for user to press Enter

        diceRoll = rollDice();
        printf("You rolled a %d!\n", diceRoll);

        playerPosition = movePlayer(playerPosition, diceRoll);
        playerPosition = checkSnakesLadders(playerPosition);

        printf("\n");
    }

    printBoard(playerPosition);
    printf("Congratulations! You have reached position %d and won the game!\n", WIN_POSITION);
    return 0;
}