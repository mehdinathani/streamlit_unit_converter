# unit_converter.py

class UnitConverter:
    def __init__(self):
        # Define conversion factors for length relative to meter (base unit)
        self.length_factors = {
            "meter": 1.0,
            "kilometer": 0.001,   # 1 meter = 0.001 kilometers
            "mile": 0.000621371,  # 1 meter = 0.000621371 miles
            "foot": 3.28084       # 1 meter = 3.28084 feet
        }
        # Define conversion factors for weight relative to kilogram (base unit)
        self.weight_factors = {
            "kilogram": 1.0,
            "gram": 1000.0,       # 1 kilogram = 1000 grams
            "pound": 2.20462,     # 1 kilogram = 2.20462 pounds
            "ton": 0.00110231,    # 1 kilogram = 0.00110231 tons
            "ounce": 35.274       # 1 kilogram = 35.274 ounces
        }
        self.temperature_units = ["Celsius", "Fahrenheit", "Kelvin"]


    def convert_length(self, value, from_unit, to_unit):
        """
        Convert length from one unit to another.
        Steps:
          1. Normalize the input value to the base unit (meter).
          2. Convert the base value to the target unit.
        """
        try:
            base_value = value / self.length_factors[from_unit]
            result = base_value * self.length_factors[to_unit]
            return result
        except Exception as e:
            print("Error in length conversion:", e)
            return None

    def convert_weight(self, value, from_unit, to_unit):
        """
        Convert weight from one unit to another.
        Steps:
          1. Normalize the input value to the base unit (kilogram).
          2. Convert the base value to the target unit.
        """
        try:
            base_value = value / self.weight_factors[from_unit]
            result = base_value * self.weight_factors[to_unit]
            return result
        except Exception as e:
            print("Error in weight conversion:", e)
            return None

    def convert_temperature(self, value, from_unit, to_unit):
        """
        Convert temperature between Celsius, Fahrenheit, and Kelvin.
        Steps:
          1. Convert the input value to Celsius.
          2. Convert from Celsius to the target unit.
        """
        try:
            # Convert the input value to Celsius
            if from_unit.lower() == "celsius":
                celsius = value
            elif from_unit.lower() == "fahrenheit":
                celsius = (value - 32) * 5 / 9
            elif from_unit.lower() == "kelvin":
                celsius = value - 273.15
            else:
                raise ValueError("Unsupported temperature unit: " + from_unit)
            
            # Convert from Celsius to the target unit
            if to_unit.lower() == "celsius":
                return celsius
            elif to_unit.lower() == "fahrenheit":
                return (celsius * 9 / 5) + 32
            elif to_unit.lower() == "kelvin":
                return celsius + 273.15
            else:
                raise ValueError("Unsupported temperature unit: " + to_unit)
        except Exception as e:
            print("Error in temperature conversion:", e)
            return None

# Quick test when running this file directly
if __name__ == "__main__":
    converter = UnitConverter()
    # Testing length conversion
    print("5 kilometers in meters:", converter.convert_length(5, "kilometer", "meter"))
    
    # Testing weight conversion
    print("5 kilograms in grams:", converter.convert_weight(5, "kilogram", "gram"))
    print("5 kilograms in pounds:", converter.convert_weight(5, "kilogram", "pound"))
    
    # Testing temperature conversion
    print("32 Fahrenheit in Celsius:", converter.convert_temperature(32, "fahrenheit", "celsius"))
