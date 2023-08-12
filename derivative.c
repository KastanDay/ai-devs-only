#include <stdio.h>

// Function to calculate the derivative of a function
float derivative(float (*f)(float), float x) {
    float h = 0.00001;
    return (f(x+h) - f(x-h)) / (2*h);
}

// Function to calculate the second derivative of a function
float second_derivative(float (*f)(float), float x) {
    return derivative(derivative(f, x), x);
}

int main() {
    // Test the derivative function
    float f(float x) {
        return x*x;
    }
    printf("%f\n", derivative(f, 2));
    printf("%f\n", second_derivative(f, 2));
    return 0;
}