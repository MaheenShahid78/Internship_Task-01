# Continuous Scientific Calculator

This task is a simple console-based scientific calculator developed in Python. It performs standard arithmetic operations and basic trigonometric calculations. The calculator runs continuously in a loop until the user chooses to exit by typing **end**.

## Contents

- Basic Arithmetic Operations
- Trigonometric Functions
- Degree and Radian Support
- Division by Zero Handling
- Infinite Loop for Continuous Calculations
- User-Friendly Console Interface

## Getting Started

Follow these instructions to set up and run the project on your local machine.

### Prerequisites

Ensure you have the following installed:

- Python 3.x
- Visual Studio Code or any Python IDE

## Installation

1. Clone the repository:

```bash
git clone https://github.com/MaheenShahid78/Internship_Task-01.git
```

2. Navigate to the project folder:

```bash
cd Internship_Task-01
```

3. Run the Python file:

```bash
python Task.py
```

## Usage

1. Run the program.
2. Choose an operation:
   - Addition (+)
   - Subtraction (-)
   - Multiplication (*)
   - Division (/)
   - Sine (sin)
   - Cosine (cos)
3. Enter the required number(s).
4. For **sin** and **cos**, specify whether the angle is:
   - **d** for degrees
   - **r** for radians
5. To exit the calculator, type:

```text
end
```

## Task Structure

```
Internship_Task-01/
│── Task.py
│── README.md
```

## Features

- Performs addition, subtraction, multiplication, and division.
- Prevents division by zero.
- Calculates sine and cosine values.
- Supports both degree and radian inputs for trigonometric functions.
- Uses an infinite `while` loop for continuous calculations.
- Terminates only when the user enters **end**.
- Provides simple and beginner-friendly console interaction.

## Technologies Used

- Python 3
- Python Math Module

## Example Output

```text
Choose an operation (+, -, *, /, sin, cos) or type 'end' to exit: +

Enter your first number: 10
Enter your second number: 5

Result: 15
```

```text
Choose an operation (+, -, *, /, sin, cos) or type 'end' to exit: sin

Enter your number: 90
Enter d for degrees or r for radians: d

Result: 1.0
```

```text
Choose an operation (+, -, *, /, sin, cos) or type 'end' to exit: end

Calculator shutting down
```

## Concepts Used

- Infinite While Loop
- Conditional Statements (`if`, `elif`, `else`)
- User Input
- Python `math` Module
- Trigonometric Functions
- Division by Zero Validation

## Author

**Maheen Shahid**

## Contact

Feel free to reach out if you have any questions or suggestions.

**Email:** maheenshahid0302@gmail.com
