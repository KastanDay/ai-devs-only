#include <stdio.h>

// Function to calculate the integral
float integral(float a, float b, int n, float (*func)(float)) {
    float step = (b-a)/n;
    float area = 0.0;
    for (int i = 0; i < n; i++) {
        area += func(a + (i+0.5)*step) * step;
    }
    return area;
}

// Function to be integrated
float func(float x) {
    return x*x;
}

int main() {
    float a = 0.0, b = 1.0;
    int n = 1000;
    printf("The integral is: %.2f\n", integral(a, b, n, func));
    return 0;
}