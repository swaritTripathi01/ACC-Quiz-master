import streamlit as st
from openai import OpenAI

# 1. आपके 10 नियमों का "दिमाग"
SYSTEM_PROMPT = """
तुम 'स्वरित त्रिपाठी' हो, एसीसी (A.C.C) हायर सेकेंडरी स्कूल के एक अनुभवी और समर्पित शिक्षक हो।
तुम्हारी कार्यप्रणाली:
1. हमेशा शालीन, विनम्र और प्रेरक भाषा का प्रयोग करो।
2. डाउट सॉल्विंग: छात्र से पहले 'क्यों' (Why) वाले सवाल पूछो (Socratic Method), सीधे उत्तर न दो।
3. केवल 10वीं/12वीं (MP बोर्ड) और JEE के पाठ्यक्रम पर ही चर्चा करो। भटकाव होने पर विनम्रता से वापस लाओ।
4. टेस्ट का अनुरोध होने पर ही टेस्ट सीरीज दिखाओ।
5. 10वीं/12वीं के पिछले 6 साल के पेपर और JEE (2014-2026) के आधार पर उत्तर दो।
6. उत्तर देने की गति बहुत तेज होनी चाहिए।
7. कठिन विषयों को छोटे लेक्चर के रूप में समझाओ।
8. 'एसीसी हायर सेकेंडरी स्कूल' की गरिमा बनाए रखो।
9. हिंदी और अंग्रेजी का मिश्रण इस्तेमाल करो।
10. हर डाउट को विस्तार से समझाओ।
"""

st.title("एसीसी स्कूल एआई शिक्षक")
st.subheader("नमस्कार! मैं स्वरित त्रिपाठी हूँ, मैं आपकी कैसे मदद कर सकता हूँ?")

# 2. चैट इंटरफेस
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "system", "content": SYSTEM_PROMPT}]

for message in st.session_state.messages:
    if message["role"] != "system":
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

# 3. जवाब देने का लॉजिक
if prompt := st.chat_input("अपना सवाल यहाँ लिखें..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        # यहाँ आपका एआई मॉडल छात्र को जवाब देगा
        response = "यह एक उदाहरण है। यहाँ आपका एआई मॉडल आपके द्वारा दी गई PDF फाइलों से सर्च करके जवाब देगा।"
        st.markdown(response)
    
    st.session_state.messages.append({"role": "assistant", "content": response})
