# GPA Calculator

## Overview
This program is an interactive GPA Calculator that helps students calculate their academic performance across two semesters. It allows users to input grades, calculate their semester and overall GPA, and even experiment with improvements to see how raising certain grades might affect their final GPA.


---

## Features
- Accepts two semesters of grades (at least 5 per semester).  
- Calculates:
  - GPA for each semester.  
  - Overall cumulative GPA.  
- Compares GPA between semesters and provides feedback.  
- Allows users to set a target GPA.  
- Simulates what would happen if certain grades were improved to a 4.0.  
- Offers the option to restart or set a new target GPA.

---

## Requirements
- Python 3.6+  
- No external libraries are required. This program only uses Python’s built-in functions.

---

## How to Run
1. Save the script as `gpa_calculator.py`.  
2. Open a terminal or command prompt.  
3. Navigate to the folder containing the script.  
4. Run the program using:
   ```bash
   python gpa_calculator.py
## How It Works
```mermaid

flowchart TD

A[Start Program] --> B[Ask for First Semester Grades]
B --> C[Ask for Second Semester Grades]

C --> D{Are both inputs numeric and valid?}
D -- No --> E[Print error and re prompt]
E --> B
D -- Yes --> F{At least 5 grades per semester?}
F -- No --> G[Print warning and re prompt]
G --> B
F -- Yes --> H[Calculate First & Second Semester GPA]

H --> I[Calculate Overall GPA]
I --> J[Display GPAs and Compare Semesters]

J --> K{User wants specific semester GPA?}
K -- Yes --> L[Display selected semester GPA]
K -- No --> M[Skip to target GPA input]

L --> M[Ask for Target GPA]

M --> N{Is Target GPA valid?}
N -- No --> O[Print error and re prompt]
O --> M
N -- Yes --> P{Current GPA >= Target GPA?}

P -- Yes --> Q[Print message: Target achieved!]
P -- No --> R[Simulate raising each grade to 4.0]

R --> S{Any single grade reaches target?}
S -- Yes --> T[Print which classes can reach target]
S -- No --> U[Tell user not reachable by one grade]

U --> V{Try new target GPA?}
V -- Yes --> M
V -- No --> W{Start new GPA calculation?}
W -- Yes --> B
W -- No --> X[Exit Program]

Q --> W
T --> W

```

