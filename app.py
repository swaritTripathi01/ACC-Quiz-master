v import streamlit as st
import google.generativeai as genai
from streamlit_mic_recorder import mic_recorder

# 1. API Key की जांच करें
if "GOOGLE_API_KEY" not in st.secrets:
    st.error("त्रुटि: Streamlit Secrets में 'GOOGLE_API_KEY' नहीं मिल रहा है। कृपया सेटिंग्स चेक करें।")
    st.stop()

genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
model = genai.GenerativeModel('gemini-1.5-flash')

st.set_page_config(page_title="ACC एआई शिक्षक", page_icon="🎓")

# 2. सिस्टम प्रॉम्प्ट
SYSTEM_INSTRUCTION = """
तुम स्वरित त्रिपाठी हो, एसीसी हायर सेकेंडरी स्कूल के एक समर्पित एआई शिक्षक।
1. छात्रों के साथ इंसान की तरह बात करो।
2. MP Board और JEE Mains के विशेषज्ञ हो।
3. डाउट फोटो आने पर स्टेप-बाय-स्टेप हिंदी में समझाओ।
4. हमेशा विनम्र और प्रेरक रहो।
"""

st.title("🎓 ACC हायर सेकेंडरी स्कूल एआई शिक्षक")

# 3. वॉइस रिकॉर्डर
audio = mic_recorder(start_prompt="🎙️ बोलकर पूछें", stop_prompt="⏹️ रुकें", just_once=True)

if "messages" not in st.session_state:
    st.session_state.messages = []

# चैट हिस्ट्री
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 4. फोटो अपलोडर
uploaded_file = st.file_uploader("डाउट की फोटो भेजें...", type=["jpg", "png"])

# 5. चैट इनपुट
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
        st.error(f"Gemini API एरर: {e}")
