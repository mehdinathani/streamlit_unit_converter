# Unit Converter

A **Streamlit-based Unit Converter** application that allows you to convert between different units of measurement—specifically Length, Weight, and Temperature. This app not only provides fast and accurate conversions but also enhances user experience with fun animations and voice feedback using the Web Speech API.

## Overview

This project demonstrates how to build a modular unit converter in Python. The core conversion logic is implemented in a separate module (`unit_converter.py`) and then integrated into a dynamic web interface using Streamlit. After a conversion is made, the result is not only displayed on the screen but also read aloud by the system.

## Domain

This Unit Converter is designed to serve a wide range of domains:
- **Education:** Ideal for students and educators who need quick, reliable unit conversions for homework, projects, or classroom demonstrations.
- **Engineering & Science:** Useful for professionals and researchers requiring accurate unit conversions during experiments, design calculations, and technical analyses.
- **Everyday Use:** Perfect for individuals who need fast and easy conversions in daily tasks.
- **Finance & Business:** Beneficial for logistics, inventory management, and other business scenarios where unit conversions are frequently required.

Visit the deployed application: [https://unitconverter-mehdinathani.streamlit.app/](https://unitconverter-mehdinathani.streamlit.app/)

## Features

- **Multiple Conversion Types:**
  - **Length:** Convert between meters, kilometers, miles, and feet.
  - **Weight:** Convert between kilograms, grams, pounds, tons, and ounces.
  - **Temperature:** Convert between Celsius, Fahrenheit, and Kelvin.
- **Voice Feedback:**  
  The conversion result is spoken using the browser's Web Speech API.
- **Animations:**  
  Visual effects (such as snowfall) are displayed after successful conversions.
- **User-friendly Interface:**  
  Built with Streamlit, ensuring a clean and responsive user experience.
- **Customizable Voice:**  
  Easily change the voice for text-to-speech by modifying the JavaScript in the `speak_text` function.

## Requirements

- Python 3.7 or higher
- [Streamlit](https://streamlit.io/)
- Internet connection (to load external images, audio files, and for the Web Speech API)

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/mehdinathani/streamlit_unit_converter.git
   cd streamlit_unit_converter
