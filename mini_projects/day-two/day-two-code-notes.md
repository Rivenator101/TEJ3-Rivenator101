
---

# Day 2 – C++ Password Strength Checker Project Summary + Reflection

### By Riven ;3

## What I Learned Today

To build a Password Strength Checker in C++, I needed to understand four core concepts:

* **Input and output** (`cin` and `cout`)
* **Variables** (`string`, `bool`)
* **Loops** (`for`)
* **Conditionals** (`if/else`)
* **Boolean flags** (true/false markers to track conditions)

---

## Notes for Each Concept

### **Input / Output**

* `cout` prints text onto the screen.
* `cin` lets the user type into the program.
  This is how the program interacts with the user.

### **Variables**

Variables store information.

* `string` → stores the password text.
* `bool` → stores true/false values for conditions (like hasUpper, hasDigit, hasSpecial).

Boolean flags are used to remember if a password contains numbers, uppercase letters, or special characters.

### **Loops**

* A `for` loop is used to go through each character in the password.
* This allows the program to check every character individually.

Example:

```cpp
for (int i = 0; i < password.length(); i++) { /* check password[i] */ }
```

### **Conditionals**

* `if/else` statements are used to check each condition:

  * Does the password have an uppercase letter?
  * Does it have a number?
  * Does it have a special character?
  * Is the length >= 8?
* Based on these checks, the program prints the result.

---

## How the Project Works

1. The program shows a simple menu: “Check password” or “Exit.”
2. The user selects to check a password.
3. The program asks the user to enter a password.
4. A loop goes through each character in the password.
5. Boolean flags track whether the password contains:

   * At least one uppercase letter
   * At least one number
   * At least one special character
6. The program prints a check for each condition.
7. If all conditions are met and the length >= 8, the password is **STRONG**; otherwise, it is **WEAK**.

---

## Skills Gained

* Using `cin` and `cout` for user interaction
* Creating and storing values in `string` and `bool` variables
* Using loops (`for`) to iterate over data
* Using `if/else` to make decisions
* Combining multiple conditions to evaluate password strength
* Organizing a program into a clear, reusable function

This covers everything needed to understand and create the Day 2 Password Strength Checker tool in C++.

---



