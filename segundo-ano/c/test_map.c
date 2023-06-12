#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

#define PLAYER_CHAR '#'

#define MAP_CHAR '.'
#define MAP_COLS 100
#define MAP_ROWS 15

int player_x_pos = 3;
int player_y_pos = 4;

void createMap(int cols, int rows);
bool samePositionAsPlayer(int i, int j, int x, int y);
void updateUserPos(char command);

int main(){
  char command;

  do{
    system("clear");
    createMap(MAP_COLS, MAP_ROWS);
    printf("Command: ");
    scanf("%c", &command);
    updateUserPos(command);
    printf("\n");
  }while(command != 'x');

  return 0;
}

void createMap(int cols, int rows){
  for(int i = 0; i < rows; i++){
    for(int j = 0; j < cols; j++)
      if(samePositionAsPlayer(i, j, player_x_pos, player_y_pos))
        printf("%c", PLAYER_CHAR);
      else
        printf("%c", MAP_CHAR);
    printf("\n");
  }
}

bool samePositionAsPlayer(int i, int j, int x, int y){
  return (i == x) && (j == y);
}

void updateUserPos(char command){
  switch (command) {
    case 'd':
      if(player_y_pos < MAP_COLS-1)
        player_y_pos ++;
      break;
    case 'a':
      if(player_y_pos > 0)
        player_y_pos --;
      break;
    case 'w':
      if(player_x_pos > 0)
        player_x_pos --;
      break;
    case 's':
      if(player_x_pos < MAP_ROWS-1)
        player_x_pos ++;
      break;
  }
}
