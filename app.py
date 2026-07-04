import streamlit as st
import google.generativeai as genai
from streamlit_mic_recorder import mic_recorder

# API सेटअप
genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
model = genai.GenerativeModel('gemini-1.5-flash')

st.set_page_config(page_title="ACC एआई शिक्षक", page_icon="🎓")

SYSTEM_INSTRUCTION = """
तुम स्वरित त्रिपाठी हो, एसीसी हायर सेकेंडरी स्कूल के एक समर्पित एआई शिक्षक।
1. छात्रों के साथ इंसान की तरह बात करो।
2. MP Board और JEE Mains के विशेषज्ञ हो।
3. डाउट फोटो आने पर स्टेप-बाय-स्टेप हिंदी में समझाओ।
4. हमेशा विनम्र और प्रेरक रहो।
"""

st.title("🎓 ACC हायर सेकेंडरी स्कूल एआई शिक्षक")

audio = mic_recorder(start_prompt="🎙️ बोलकर पूछें", stop_prompt="⏹️ रुकें", just_once=True)

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

uploaded_file = st.file_uploader("डाउट की फोटो भेजें...", type=["jpg", "png"])

if prompt := st.chat_input("अपना सवाल पूछें..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    try:
        response = model.generate_content(SYSTEM_INSTRUCTION + prompt)
        with st.chat_message("assistant"):
            st.markdown(response.text)
        st.session_state.messages.append({"role": "assistant", "content": response.text})
    except Exception as e:
        st.error("तकनीकी समस्या, कृपया रीबूट करें।")
