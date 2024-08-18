
# Snack Center Billing System

## Overview

The Snack Center Billing System is a desktop application built using Python and Tkinter. It allows users to create bills for various snack items, save transactions to a CSV file, view past transactions, and print invoices. The system features a simple and intuitive graphical user interface (GUI) for ease of use.

## Features

- **Calculate Bill:** Allows users to enter the quantity of various snack items and calculates the total amount.
- **Save Transaction:** Saves the details of each transaction to a CSV file for record-keeping.
- **View Transactions:** Displays a list of all previous transactions.
- **Print Invoice:** Provides an option to print the generated invoice.
- **Reset Form:** Clears the quantities entered by the user for a fresh start.

## Installation

To run this application, you need Python installed on your system. You can download Python from the [official website](https://www.python.org/downloads/).

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/PATILYASHH/Snacks-Billing-System
   ```

2. **Navigate to the Project Directory:**

   ```bash
   cd Snacks-Billing-System
   ```

3. **Install Dependencies:**

   This project uses standard Python libraries, so no additional dependencies are required.

## Usage

1. **Run the Application:**

 
2. **Interacting with the Application:**

   - Enter the quantity of each snack item in the provided fields.
   - Click on "Calculate Bill" to generate the bill.
   - Click on "View Transactions" to see a list of all recorded transactions.
   - Click on "Reset" to clear the entered quantities.
   - Click on "Print Bill" to print the generated invoice.

## Code Structure

- **`calculate_bill()`**: Calculates the total amount based on the quantities and prices of the items.
- **`save_transaction(items, total)`**: Saves the details of the transaction to a CSV file.
- **`reset()`**: Resets the quantity fields to zero.
- **`view_transactions()`**: Displays all recorded transactions.
- **`display_invoice(invoice)`**: Displays the invoice in a new window.
- **`print_bill()`**: Prints the invoice text.
- **`print_invoice_text(text)`**: Simulates printing by outputting text to the console.

## Contributing

If you want to contribute to this project, feel free to fork the repository and submit a pull request. Your contributions and suggestions are welcome!

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

