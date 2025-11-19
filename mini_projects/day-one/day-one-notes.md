
# Day 1 – C++ Unit Converter Project Summary + Reflection

### By Riven ;3

## What I Learned Today

To build a simple Unit Converter in C++, I needed to understand five core concepts:

* **Input and output** (`cin` and `cout`)
* **Variables** (`int`, `double`, `string`)
* **Conditionals** (`if/else`, `switch`)
* **Functions** (creating my own reusable sections of code)
* **Basic math formulas** (for unit conversions)

---

## notes for Each Conceptt

### **Input / Output**

* `cout` prints text onto the screen
* `cin` lets the user type into the program.
  This is how the program communicates with the user.

### **Variables**

Variables store information.

* `int` → whole numbers
* `double` → decimals
* `string` → text

Most unit conversions use `double` because the values often contain decimals.

### **Conditionals**

* `if/else` lets the program make decisions.
* `switch` is good for menus because it runs different code based on the user’s choice.

### **Functions**

Functions act like mini-programs inside the main program and help organize code.

For this project, I created three functions:

* `lengthConverter()`
* `tempConverter()`
* `energyConverter()`

---

## Math Formulas I Used

### **Length**

* cm → m: divide by 100
* m → cm: multiply by 100
* m → km: divide by 1000
* km → m: multiply by 1000

### **Temperature**

* C → F: `(C * 9/5) + 32`
* F → C: `(F - 32) * 5/9`

### **Energy**

* Joules → calories: divide by 4.184
* Calories → joules: multiply by 4.184

---

## How the Project Works

1. The program starts by showing a menu.
2. The user chooses what type of conversion they want (length, temperature, or energy).
3. A `switch` statementt calls the correct function.
4. Inside each function, there is a smaller menu for specific conversions.
5. The user inputs a value.
6. The program applies the correct formula and prints the result.

---

## Skills Gained

* Using `cin` and `cout`
* Creating and storin values in variables
* Making decisions using `if/else` and `switch`
* Writing and calling functions
* Doing math with user input
* Organizing a C++ program into clear sections

This covers everything needed to understand and create the Day 1 Unit Converter tool in C++.

---


