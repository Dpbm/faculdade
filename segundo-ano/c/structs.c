#include <stdio.h>

typedef struct{
  char name[20];
  int age;
}Person;

int main(){
  Person person;
  
  gets(person.name);
  scanf("%d", &person.age);

  printf("Name: %s\nAge: %d", person.name, person.age);

  return 0;
}
