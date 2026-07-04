import streamlit as st
from openai import OpenAI
from streamlit_mic_recorder import mic_recorder

# Secrets से API Key लें
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

st.set_page_config(page_title="ACC एआई शिक्षक", page_icon="🎓")

# 10 नियमों का मुख्य निर्देश
SYSTEM_PROMPT = """
तुम स्वरित त्रिपाठी हो, एसीसी हायर सेकेंडरी स्कूल के एक समर्पित एआई शिक्षक।
1. छात्रों के साथ इंसान की तरह बात करो।
2. MP Board (10वीं/12वीं) और JEE Mains (पिछले 11 साल) के विशेषज्ञ हो।
3. छात्र जब तक 'Test' न कहे, सीधे उत्तर न दो, Socratic method (Why/कैसे) से समझाओ।
4. छात्र के डाउट फोटो के रूप में आने पर उसे स्टेप-बाय-स्टेप हिंदी में समझाओ।
5. 10वीं/12वीं की पूरी किताबों के MP बोर्ड पैटर्न पर आधारित ऑब्जेक्टिव सवाल पूछ सकते हो।
6. केवल शिक्षा से संबंधित विषयों पर बात करो।
7. उत्तर अत्यंत तेज गति से दो।
8. JEE Mains के लिए अलग से 'JEE Test' का विकल्प दो।
9. अगर छात्र कहे तो पूरी टेस्ट सीरीज दिखाओ।
10. हमेशा विनम्र और प्रेरक रहो।
"""

st.title("🎓 ACC हायर सेकेंडरी स्कूल एआई शिक्षक")

# वॉइस रिकॉर्डर बटन
st.write("बोलकर सवाल पूछने के लिए नीचे बटन दबाएं:")
audio = mic_recorder(start_prompt="🎙️ रिकॉर्डिंग शुरू करें", stop_prompt="⏹️ रुकें", just_once=True)

if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "system", "content": SYSTEM_PROMPT}]

# चैट इंटरफेस
for message in st.session_state.messages:
    if message["role"] != "system":
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

# इनपुट (फोटो अपलोड और टेक्स्ट)
uploaded_file = st.file_uploader("डाउट की फोटो यहाँ भेजें...", type=["jpg", "png"])
if prompt := st.chat_input("अपना सवाल पूछें..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # OpenAI कॉल (यहाँ gpt-4o-mini का उपयोग किया गया है)
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=st.session_state.messages
    )
    
    answer = response.choices[0].message.content
    with st.chat_message("assistant"):
        st.markdown(answer)
    st.session_state.messages.append({"role": "assistant", "content": answer})
