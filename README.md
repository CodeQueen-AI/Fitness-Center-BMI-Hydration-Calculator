# 💪 Fitness Center BMI & Hydration Calculator

A simple Python console program that helps new members calculate **basic health metrics**
It calculates **BMI**, provides the **BMI category**, and recommends **daily water intake** based on weight



## 📌 **Project Overview**

This program helps fitness center members:

* Calculate their **BMI** (Body Mass Index)  
* Understand their **BMI category**: Underweight, Healthy, Overweight, or Obese  
* Get **daily water intake recommendation** based on weight  
* View a **summary** of their health metrics in a clear format  

The program is interactive, supports **multiple members**, and ensures a smooth user experience.



## 💡 **Features**

### ✔ BMI Calculation ⚖️
Uses the formula:

```

BMI = weight (kg) / (height (m))²

```

Calculates and rounds the BMI to **2 decimal places**.

### ✔ BMI Category 🏷️
Classifies BMI as:

* Underweight (<18.5)  
* Healthy (18.5–24.9)  
* Overweight (25–29.9)  
* Obese (30 or more)

### ✔ Daily Water Recommendation 💧
Estimates daily water intake using the formula:

```

Water (liters) = weight × 0.03

````

### ✔ Member Summary 📋
Displays a clear summary including:

* Member’s name  
* BMI value  
* BMI category  
* Daily water intake recommendation  

### ✔ Multi-Member Support 👥
The program runs in a loop allowing **multiple members** to be processed one after another until the user chooses to quit


## 🛠️ **How the Program Works**

1. User chooses to **start** a new member or **quit**.  
2. Inputs member **name**, **weight**, and **height**.  
3. Program calculates:

   * BMI  
   * BMI category  
   * Daily water recommendation  

4. Displays a **formatted summary** for the member.  
5. Repeats for additional members until the user quits.  
6. Prints a **thank you message** when exiting.


## 🎯 **Skills Practiced**

* Functions in Python  
* Conditional statements  
* Loops  
* Input validation  
* Basic arithmetic operations  
* Interactive console programs  


## 📝 **Usage**

1. Run the program:

```bash
index.py
````

2. Follow the prompts:

   * Type `start` to enter a new member
   * Type `q` to quit

3. Input **name**, **weight (kg)**, and **height (m)**.

4. View the summary with BMI, category, and water recommendation.

5. Repeat for multiple members.



## ✅ **Thank You Message**

When quitting, the program displays:

```
Thank you for using the Fitness Center BMI & Hydration Tool! 💪
```


