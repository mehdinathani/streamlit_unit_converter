import streamlit as st
from unit_converter import UnitConverter

import streamlit.components.v1 as components

import streamlit.components.v1 as components

def speak_text(text):
    # Escape any quotes in the text
    text_escaped = text.replace('"', '\\"')
    html_str = f"""
    <html>
    <body>
    <script>
        function speakWithVoice() {{
            var msg = new SpeechSynthesisUtterance("{text_escaped}");
            var voices = window.speechSynthesis.getVoices();
            // Example: Select a voice by name; adjust the name based on available voices.
            for (var i = 0; i < voices.length; i++) {{
                if (voices[i].name === "Google US English") {{
                    msg.voice = voices[i];
                    break;
                }}
            }}
            // If the desired voice isn't found, msg.voice will remain default.
            window.speechSynthesis.speak(msg);
        }}

        // Ensure voices are loaded (some browsers may need a delay)
        if (window.speechSynthesis.getVoices().length === 0) {{
            window.speechSynthesis.addEventListener('voiceschanged', speakWithVoice);
        }} else {{
            speakWithVoice();
        }}
    </script>
    </body>
    </html>
    """
    components.html(html_str, height=0, width=0)

def main():
    st.set_page_config(

        page_title="Unit Converter", page_icon=":bar_chart:", layout="wide"
    )
    st.title("Unit Converter")
    st.write("This app allows you to convert between different units of measurement.")

    # Create an instance of the converter
    converter = UnitConverter()

    # Sidebar for selecting the conversion type
    conversion_type = st.sidebar.selectbox(
        "Select Conversion Type", ["Length", "Weight", "Temperature"]
    )
    
    if conversion_type == "Length":
        st.header("Length Conversion")
        value = st.number_input("Enter Value", value=0.0)
        from_unit = st.selectbox("From Unit", list(converter.length_factors.keys()))
        to_unit = st.selectbox("To Unit", list(converter.length_factors.keys()))
        if st.button("Convert Length"):
            result = converter.convert_length(value, from_unit, to_unit)
            if result is not None:
                message = f"{value} {from_unit} is equal to {result:.2f} {to_unit}"
                st.success(message)
                speak_text(message)
                # You can also add an animation and sound for weight conversion if desired
                st.snow()
                # st.image("https://media.giphy.com/media/xT9IgzoKnwFNmISR8I/giphy.gif", width=200)
                # st.audio("https://www.soundjay.com/button/beep-07.mp3", format="audio/mp3")
            else:
                st.error("Error in length conversion. Please check your inputs.")

    elif conversion_type == "Weight":  # Use "Weight" with capital W to match the sidebar option
        st.header("Weight Conversion")
        value = st.number_input("Enter Value", value=0.0)
        from_unit = st.selectbox("From Unit", list(converter.weight_factors.keys()))
        to_unit = st.selectbox("To Unit", list(converter.weight_factors.keys()))
        if st.button("Convert Weight"):
            result = converter.convert_weight(value, from_unit, to_unit)
            if result is not None:
                message = f"{value} {from_unit} is equal to {result:.2f} {to_unit}"
                st.success(message)
                speak_text(message)
                # You can also add an animation and sound for weight conversion if desired
                st.snow()
                # st.image("https://media.giphy.com/media/xT9IgzoKnwFNmISR8I/giphy.gif", width=200)
                # st.audio("https://www.soundjay.com/button/beep-07.mp3", format="audio/mp3")
            else:
                st.error("Error in weight conversion. Please check your inputs.")

    elif conversion_type == "Temperature":
        st.header("Temperature Conversion")
        value = st.number_input("Enter Value", value=0.0)
        # Use fixed options for temperature units instead of converter.convert_temperature
        from_unit = st.selectbox("From Unit",list(converter.temperature_units))
        to_unit = st.selectbox("To Unit", list(converter.temperature_units))
        if st.button("Convert Temperature"):
            result = converter.convert_temperature(value, from_unit, to_unit)
            if result is not None:
                message = f"{value} {from_unit} is equal to {result:.2f} {to_unit}"
                st.success(message)
                speak_text(message)
                # You can also add an animation and sound for weight conversion if desired
                st.snow()
                # st.image("https://media.giphy.com/media/xT9IgzoKnwFNmISR8I/giphy.gif", width=200)
                # st.audio("https://www.soundjay.com/button/beep-07.mp3", format="audio/mp3")
            else:
                st.error("Error in temperature conversion. Please check your inputs.")


if __name__ == "__main__":
    main()

# Footer with social media links
st.markdown("""
    <hr>
    <div style="text-align: center;">
        <p style="font-size: 16px;">👨‍💻 Developed by <strong>Mehdi Abbas Nathani</strong></p>
        <p>📢 Connect with me:</p>
        <a href="https://www.linkedin.com/in/mehdinathani/" target="_blank">
            <img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" width="30">
        </a>
        &nbsp;&nbsp;
        <a href="https://github.com/mehdinathani" target="_blank">
            <img src="https://cdn-icons-png.flaticon.com/512/25/25231.png" width="30">
        </a>
        &nbsp;&nbsp;
        <a href="https://www.fiverr.com/sellers/mehdinathani/" target="_blank">
            <img src="https://cdn.worldvectorlogo.com/logos/fiverr-1.svg" width="30">
        </a>
    </div>
""", unsafe_allow_html=True)
