#include <math.h>
#include <vector>
#include <iostream>

#include "baekjoon.h"

int 
sol1002(int x1, int y1, int r1, int x2, int y2, int r2) {
  double distanse = sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2));
  double subtract = r1 > r2 ? r1 - r2 : r2 - r1;

  if (distanse == 0 && r1 == r2) {
    return  -1;
  } else if (distanse < r1 + r2 && (subtract < distanse)) {
    return 2;
  } else if (distanse == r1 + r2 || distanse == subtract) {
    return 1;
  }
  return 0;
}