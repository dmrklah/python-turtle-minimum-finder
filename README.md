# Minimum Value Finder — Python & Turtle Graphics

**Module:** Algorithms and Problem Solving using Python  
**Degree:** BSc Computer Science and Digitization

---

## Overview

A Python program that accepts three numbers from the user, identifies the smallest value using Python's built-in `min()` function, and displays the result inside a coloured circle using the Turtle graphics module.

---

## Features

- User input with float conversion (supports integers and decimals)
- Minimum value detection using `min()`
- Turtle graphics visualisation — light blue filled circle with black border
- Result displayed at the centre of the circle
- Error handling with `try/except` for invalid (non-numeric) inputs
- Modular design — input, logic, and visualisation separated into functions

---

## How It Works

1. User is prompted to enter three numbers (X, Y, Z)
2. Program finds the minimum using `min(x, y, z)`
3. A Turtle graphics window opens showing a light blue circle
4. The minimum value is displayed at the centre of the circle
5. If invalid input is entered, an error message is shown

**Example:**  
Input: `33`, `23`, `5.6` → Output: circle displaying `Min: 5.6`

---

## How to Run

```bash
python minimum_finder.py
```

No additional packages needed — uses Python standard library only (`turtle` is built-in).

> Note: Turtle graphics requires a display. Run locally or use an IDE like Thonny or IDLE.

---

## Files

| File | Description |
|------|-------------|
| `minimum_finder.py` | Python program with turtle graphics visualisation |
| `report.pdf` | Full assignment report with algorithm explanation and output |

---

## Technologies

- Python · Turtle Graphics · try/except error handling
