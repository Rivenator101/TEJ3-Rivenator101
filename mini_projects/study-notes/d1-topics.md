

# **Day 1 – Unit Converter: How it Works & Syntax Explanation**
(sources: w3 schools, mit open course ware lecture notes, standerd c++)

### 1️**Headers and Namespaces**

```cpp
#include <iostream>
using namespace std;
```

* `#include <iostream>` -> includes the Input/Output library so we can use `cin` and `cout`.
* `using namespace std;` -> allows us to write `cout` instead of `std::cout`.

*This is standard setup for any progrm that uses input and output in C++.*

---

### 2️**Function Prototypes**

```cpp
void lengthConverter();
void tempConverter();
void energyConverter();
```

* A **function prototype** tells the compiler: “I’ll define this function later.”
* `void` -> the function doesn’t return a value.

*We declare these functions at the top so the main function can call them before they are defined.*

---

### 3️**The Main Function**

```cpp
int main() {
    int choice;
    ...
    return 0;
}
```

* `int main()` -> the starting point of the program.
* `return 0;` -> signals that the program finished successfully.
* `int choice;` -> creates a variable to store the user’s menu selection.

*All C++ programs start with `main()`. Variables inside `main` store user input or temporary data.*

---

### 4️**Input and Output (`cin` / `cout`)**

```cpp
cout << "Choose an option (1-4): ";
cin >> choice;
```

* `cout` -> prints text or results to the screen.
* `cin` -> waits for the user to type something and stores it in a variable.

*We use these to create an interactive menu and get user input.*

---

### 5️**Conditionals and Switch**

```cpp
switch (choice) {
    case 1: lengthConverter(); break;
    case 2: tempConverter(); break;
    case 3: energyConverter(); break;
    case 4: cout << "Exiting..." << endl; break;
    default: cout << "Invalid option." << endl;
}
```

* `switch` -> checks a variable and executes code for the matching `case`.
* `break;` -> stops the program from continuing to the next case.
* `default` -> runs if no cases match.

*We use `switch` to select which conversion function to run based on the user’s menu choice.*

---

### 6️**Functions**

Example: **Length Converter**

```cpp
void lengthConverter() {
    double value;
    int option;
    ...
    switch(option) {
        case 1: cout << value / 100 << " m"; break;
        ...
    }
}
```

* `void lengthConverter()` -> defines a function for length conversions.
* Local variables `value` and `option` exist ony inside this function.
* `switch` selects the type of length conversion.

*Functions allow us to organize code into sections that do specific tasks. This makes the program easier to read and maintain.*

---

### 7️**Math in Conversions**

Examples:

```cpp
value / 100        // cm → m
(value * 9/5) + 32 // C → F
value / 4.184      // Joules → calories
```

* Standard arithmetic operators are used:

  * `/` → divide
  * `*` → multiply
  * `+` → add
*These formulas perform the actual unit conversion. We input a value and output the converted result.*

---

### 8️**Putting it All Together**

* **Main function** -> shows the menu, gets the user’s choice, calls the correct function.
* **Functions** -> handle specific conversions and print the results.
* **Input/output** -> lets the user interact with the program.
* **Switch** -> makes decision-making easier than using multiple `if/else`.
* **Math formulas** -> perform the actual conversions.

*The program first shows a menu and asks the user what they want to convertt. Using `switch`, it calls the appropriate function. Inside each function, we ask for a value, do the conversion with math formulass, and print the result using `cout`. This teaches us about input/output, variables, decision-making, functions, and math in C++.*

---


