#include <stdio.h>
#include <stdlib.h>

void get_ages(int *ages, int *total_ages_ref);
void show_ages(int *ages, int *total_ages_ref);
float get_mean(int *ages, int *total_ages_ref);

int main(){
  
  int total_ages = 0;
  int *total_ages_ref = &total_ages;
  int *ages = malloc((total_ages + 1) * sizeof(int));

  get_ages(ages, total_ages_ref);
  show_ages(ages, total_ages_ref);

  float ages_mean = get_mean(ages, total_ages_ref);

  printf("Ages mean: %.1f", ages_mean);
  
  return 0;
}

void get_ages(int *ages, int *total_ages_ref){
  puts("Digite as idades ou 0 para sair!");

  int age;

  do {
    scanf("%d", &age);
    if(age){
      ages[*total_ages_ref] = age;
      (*total_ages_ref)++;
    }
  }while (age);

}

void show_ages(int *ages, int *total_ages_ref){
  puts("\nIdades inseridas: ");
  int i;
  for(i = 0; i < *total_ages_ref; i++)
      printf("%d ", ages[i]);
}

float get_mean(int *ages, int *total_ages_ref){
  float total_of_ages = *total_ages_ref;
  float total_ages_sum = 0;

  int i;
  for(i = 0; i < total_of_ages; i++)
      total_ages_sum += ages[i];

  return total_ages_sum / total_of_ages;
}
