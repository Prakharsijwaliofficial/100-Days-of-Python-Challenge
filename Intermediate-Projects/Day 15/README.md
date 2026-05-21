# Day 15 - Coffee Machine Project

## 📌 Project

A Python-based virtual Coffee Machine simulation. The program manages internal inventory (water, milk, coffee), processes coin payments (quarters, dimes, nickels, pennies), tracks total profits, and dispenses espresso, latte, or cappuccino based on resource availability.

## 💬 What I Learned

*   **Global Variables & State Management**: Managing and updating a central machine state (`profit`, `resources`, `machine_on`) across multiple functions.
*   **Modular Programming**: Breaking down a complex process into dedicated, reusable functions (`is_resource_sufficient`, `process_coins`, `is_transaction_successful`, `make_coffee`).
*   **While Loops & Control Flow**: Building a continuous operational loop with specific secret administrative keywords (`off`, `report`) alongside regular customer inputs.
*   **Nested Dictionary Manipulation**: Reading complex, nested drink data structures to dynamic retrieve costs and ingredient lists.
*   **User Input Processing**: Taking unstructured text input, converting it to lowercase, validating the choice against existing menus, and converting coin counts into precise decimal currency values.

## 🚀 How to Run

1. Run the code in any standard Python 3 environment (like PyCharm, VS Code, or Replit).
2. Enter `espresso`, `latte`, or `cappuccino` to purchase a drink.
3. Type `report` to view current resource levels and machine profits.
4. Type `off` to shut down the coffee machine simulator.
