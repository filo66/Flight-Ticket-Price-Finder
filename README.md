# ✈️ Cheapest Flight Ticket Finder

A Python desktop application that helps users find affordable flight tickets by searching real-time flight offers through the **Amadeus API**. Built with **CustomTkinter**, the application provides a modern, intuitive interface for searching flights and viewing essential travel information.

🎥 **Video Demo:** https://youtu.be/Zvuwv0HAhn0

---

# 📖 Description

**Cheapest Flight Ticket Finder** is a Python GUI application that allows users to search for flight tickets between two airports for a specific departure date.

The application combines several important programming concepts, including:

* 🖥️ Graphical User Interface (GUI) development with **CustomTkinter**
* 🌐 REST API integration using the **Amadeus API**
* ✅ User input validation
* ⚠️ Exception handling
* 🧪 Unit testing with assertions

Users simply enter:

* 🛫 Origin airport (IATA code)
* 🛬 Destination airport (IATA code)
* 📅 Departure date
* 👥 Number of adult passengers

The application then communicates with the **Amadeus API** to retrieve available flight offers and displays the cheapest available option, including:

* 💲 Ticket price
* ✈️ Airline
* 🔢 Flight number
* 🕒 Departure time
* 🕓 Arrival time

---

# ✨ Features

* 🔍 Search for flight tickets using airport IATA codes
* 💵 Display the cheapest available flight
* 📅 Validate departure date format
* 🛫 Verify airport codes using a local airport database
* 👥 Validate the number of adult passengers
* ⚠️ Display clear error messages for invalid input
* 🎨 Modern desktop interface built with CustomTkinter

---

# 📂 Project Structure

### 📄 `project.py`

The main application containing all core functionality.

Functions included:

* `main()` – Initializes the application and configures the GUI.
* `input_frame()` – Displays the form for entering flight information.
* `new_frame()` – Displays the retrieved flight details.
* `send_data()` – Collects and validates user input before searching.
* `get_data()` – Connects to the Amadeus API and retrieves flight information.
* `check_the_input()` – Validates airport codes, departure date, and passenger count.

---

### 🧪 `test_project.py`

Contains unit tests for the project's core functions.

The tests use Python's `assert` statements to verify that the application's logic behaves correctly and satisfy the CS50P project requirements.

---

### 📋 `requirements.txt`

Lists all required Python packages needed to run the application:

* `amadeus`
* `customtkinter`

---

### 🗂️ `airports.csv`

Contains a database of airports and their IATA airport codes. The application uses this file to validate the origin and destination airport codes entered by the user.

---

# 🚀 Installation

1. Clone the repository.

```bash
git clone https://github.com/your-username/Flight-Ticket-Price-Finder.git
```

2. Install the required packages.

```bash
pip install -r requirements.txt
```

3. Obtain your **Amadeus API** credentials and replace the `client_id` and `client_secret` values inside `project.py`.

4. Run the application.

```bash
python project.py
```

---

# 🛠️ Technologies Used

* Python
* CustomTkinter
* Amadeus API
* Tkinter
* Datetime

---

# 📌 Notes

* Airport codes must be valid **IATA** codes (e.g., `CAI`, `JFK`, `LHR`).
* Departure dates must follow the format:

```text
YYYY-MM-DD
```

* Internet access is required to retrieve live flight offers from the Amadeus API.

---

# 📄 License

This project is licensed under the **MIT License**.

---

## 👨‍💻 Author

Developed as the final project for **CS50's Introduction to Programming with Python (CS50P)**.
