#include <stdio.h>

int main() {
  double Mi = 3.986005e+14;
  float constante = 3.0e-1;

  printf("constante gravitacional: %e\n", Mi);
  printf("constante gravitacional: %E\n", Mi);
  printf("constante gravitacional: %g\n", Mi);
  printf("constante gravitacional: %e\n", constante);
  printf("constante gravitacional: %E\n", constante);
  printf("constante gravitacional: %g\n", constante);

  return 0;
}
