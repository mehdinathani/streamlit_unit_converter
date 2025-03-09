# Unit Converter

A **Streamlit-based Unit Converter** application that allows you to convert between different units of measurement—specifically Length, Weight, and Temperature. This app not only provides fast and accurate conversions but also enhances user experience with fun animations and voice feedback using the Web Speech API.

## Overview

This project demonstrates how to build a modular unit converter in Python. The core conversion logic is implemented in a separate module (`unit_converter.py`) and then integrated into a dynamic web interface using Streamlit. After a conversion is made, the result is not only displayed on the screen but also read aloud by the system.

## Domain

This application can be useful across various domains, including:
- **Education:** Helping students and teachers quickly convert units during lessons or homework.
- **Engineering & Science:** Assisting engineers, researchers, and scientists with unit conversions required for calculations and experiments.
- **Finance & Business:** Supporting professionals who need to convert units for logistics, inventory management, or technical analysis.
- **Everyday Use:** Serving anyone who needs quick, reliable unit conversions in daily tasks.

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
   git clone https://github.com/yourusername/unit-converter.git
   cd unit-converter
