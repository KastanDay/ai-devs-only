#include <stdio.h>

// Function to calculate the derivative of a function
float derivative(float (*f)(float), float x) {
    float h = 0.00001;
    return (f(x+h) - f(x-h)) / (2*h);
}

int main() {
    // Test the derivative function
    float f(float x) {
        return x*x;
    }
    printf("%f\n", derivative(f, 2));
    return 0;
}