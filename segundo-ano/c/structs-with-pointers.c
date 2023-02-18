#include <stdio.h>

typedef struct{
  char name[20];
  int age;
} Person;

int main(){
  Person person;
  Person *p;

  p = &person;

  gets(person.name);
  scanf("%d", &person.age);

  printf("Name: %s\nAge: %d", p->name, p->age);

  return 0;

}
