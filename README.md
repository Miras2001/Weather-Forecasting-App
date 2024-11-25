# Weather-Forecasting-App


---

## **Description**

The **Weather Forecasting App** is a Python-based command-line application that provides users with real-time weather updates and a 5-day forecast for any city in the world. The app retrieves data from the OpenWeatherMap API and displays the current weather conditions, including temperature and weather descriptions, along with predictions for the coming days.

This project was developed as a final project for the course, showcasing the use of external APIs, Python programming skills, and modular function design. It focuses on clean coding practices, usability, and testing to ensure a robust and reliable user experience.

---

## **Files in the Project**

### **1. `project.py`**
This file is the main script of the application. It contains:
- **`main` Function**:
  - Serves as the entry point of the application.
  - Prompts the user to input a city name and handles the workflow by calling additional functions.
  - Includes error handling for invalid inputs or API errors.

- **`get_weather` Function**:
  - Fetches weather data (current conditions or 5-day forecast) from the OpenWeatherMap API.
  - Accepts the city name and endpoint type (`"weather"` for current weather, `"forecast"` for the 5-day forecast) as parameters.
  - Returns the weather data as a Python dictionary for further processing.

- **`display_weather` Function**:
  - Formats and prints the weather data in a user-friendly way.
  - Displays the current temperature, weather condition, and a 5-day forecast filtered for midday temperatures.

### **2. `test_project.py`**
This file contains unit tests for the functions in `project.py` to ensure the program behaves as expected:
- **`test_get_weather`**:
  - Simulates API responses and verifies that the `get_weather` function processes the data correctly.
  - Uses mocking to avoid real API calls during testing.

- **`test_display_weather`**:
  - Captures and validates the output of the `display_weather` function, ensuring it correctly formats and prints the data.

### **3. `requirements.txt`**
This file lists the dependencies required to run the application:
- **`requests`**: For making HTTP requests to the OpenWeatherMap API.
- **`pytest`**: For running tests to validate functionality.

### **4. `README.md`**
The document you’re reading now, which provides an overview of the project, its functionality, file descriptions, and design decisions.

---

## **How the App Works**
1. The user is prompted to enter a city name.
2. The app:
   - Fetches current weather and a 5-day forecast using the OpenWeatherMap API.
   - Formats and displays the results in a readable format.
3. If the city name is invalid or there’s an API issue, the app informs the user with an error message.

---

## **Design Choices**

### **Why Use OpenWeatherMap API?**
The OpenWeatherMap API was chosen for its comprehensive and reliable weather data. It provides detailed information, including temperature, weather descriptions, and forecasts, making it suitable for the app's functionality.

### **Why Command-Line Interface?**
A command-line interface was selected for simplicity and to focus on core functionality without introducing the complexity of GUI frameworks. This makes the app lightweight and easy to use.

### **Why Modular Functions?**
Each function in `project.py` serves a specific purpose:
- **`main`** handles user input and the overall workflow.
- **`get_weather`** abstracts the API interaction, making the code easier to maintain and test.
- **`display_weather`** focuses solely on formatting and displaying the results.

This modular design ensures the code is clean, reusable, and testable.

---

## **Testing**
Testing is an essential part of this project. The `test_project.py` file ensures that:
- The app behaves correctly under normal and edge-case scenarios.
- API calls are correctly handled without relying on live data (via mocking).
- Output formatting matches the expected results.

---

## **Future Enhancements**
The app can be expanded with the following features:
1. **City Autocomplete**: Allow users to select a city from suggestions when typing.
2. **GUI Version**: Implement a graphical interface for a more user-friendly experience.
3. **Additional Data Points**: Display details like humidity, wind speed, or precipitation probability.
4. **Cache Results**: Store recent searches locally to reduce API calls.

---

## **Setup and Usage**
1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
2. **Run the App**:
   ```bash
   python project.py
   ```
3. **Run Tests**:
   ```bash
   pytest
   ```

---

## **Conclusion**
The Weather Forecasting App is a powerful yet simple tool that showcases Python programming skills, modular design, and the integration of third-party APIs. It provides a strong foundation for further enhancements and demonstrates the application of theoretical knowledge in solving practical problems.


---

This `README.md` includes all the required details: a project overview, file descriptions, design decisions, and usage instructions. Adjust the placeholders (e.g., `<URL HERE>`) and expand on the descriptions as needed to tailor it to your project.
