# Fonction calculate_average
def calculate_average(numbers):
    total_number = 0

    for number in numbers:
       total_number += number

    return total_number / len(numbers)

# Exemple d'utilisation de la fonction
numbers = [10, 20, 30, 40, 50]
average = calculate_average(numbers)
print("La moyenne est :", average)
