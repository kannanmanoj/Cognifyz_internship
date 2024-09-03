#include <stdio.h>

// Function to convert Celsius to Fahrenheit
float celsius_to_fahrenheit(float celsius) {
    return (celsius * 9/5) + 32; //formula for this coversion this is the key part of the function
}

// Function to convert Fahrenheit to Celsius
float fahrenheit_to_celsius(float fahrenheit) {
    return (fahrenheit - 32) * 5/9; // as usual same conversion
}

int main() {
    int choice; // user choices
    float temperature, converted;

    printf("Temperature Converter\n");
    printf("1. Celsius to Fahrenheit\n");
    printf("2. Fahrenheit to Celsius\n");
    printf("Choose conversion direction (1 or 2): ");
    scanf("%d", &choice);

    if (choice == 1) {
        printf("Enter temperature in Celsius: ");
        scanf("%f", &temperature);//read
        converted = celsius_to_fahrenheit(temperature);//conversion part
        printf("%.2f°C is equal to %.2f°F\n", temperature, converted);// result
    } else if (choice == 2) {
        printf("Enter temperature in Fahrenheit: ");
        scanf("%f", &temperature);
        converted = fahrenheit_to_celsius(temperature);
        printf("%.2f°F is equal to %.2f°C\n", temperature, converted);
    } else {
        printf("Invalid choice. Please select 1 or 2.\n");
    }

    return 0;
}
