import streamlit as st
import os
from dotenv import load_dotenv
import groq
import swisseph as swe 
from datetime import datetime

# Load environment variables from .env file
load_dotenv()

# App title
st.set_page_config(page_title="🔱 Conversing with Raavan")

# Groq Credentials
with st.sidebar:
    st.title('🔱 शास्त्र-रावण 🔱')
    
    # Load the API token from the environment variable
    groq_api_key = os.getenv('GROQ_API_KEY')

    if groq_api_key:
        st.success('API key loaded!', icon='✅')
    else:
        groq_api_key = st.text_input('Enter Groq API token:', type='password')
        if not groq_api_key:
            st.warning('Please enter your credentials!', icon='⚠️')
        else:
            st.success('Proceed to entering your prompt message!', icon='👉')
    st.markdown('📖 Learn how to build this app in this [blog](https://blog.streamlit.io/how-to-build-a-llama-2-chatbot/)!')        

# Section: Display Verses (Separate from Chatbot)
with st.sidebar.expander("📜 Raavan’s Verses & Teachings", expanded=False):
    
    # Shiva Tandava Stotra
    st.markdown("### 🔱 Shiva Tandava Stotra (by Raavan)")
    st.markdown("""
    **Verse:**  
    जटाटवीगलज्जलप्रवाहपावितस्थले  
    गलेवलम्ब्य लम्बितां भुजङ्गतुङ्गमालिकाम्।  
    डमड्डमड्डमड्डमन्निनादवड्डमर्वयं  
    चकार चण्डताण्डवं तनोतु नः शिवः शिवम्॥ १ ॥

    **Meaning:**  
    Shiva, adorned with serpents and flowing Ganga, dances the powerful Tandava. May he bless us with divine grace.
    """)

    # Raavan’s Wisdom & Philosophy
    st.markdown("### 💬 Raavan’s Wisdom & Philosophy")
    st.markdown("""
    **Quote:**  
    *"विद्या धनं सर्वधनात् प्रधानम्।"*  
    **Meaning:**  
    Education is the greatest wealth above all treasures.

    **Quote:**  
    *"वीरता के बिना राजा का कोई मूल्य नहीं।"*  
    **Meaning:**  
    A king without valor is worthless.
    """)

    # Sacred Verses from Ramayan
    st.markdown("### 📖 Sacred Verses from Ramayan")
    st.markdown("""
    **Shloka:**  
    *"न जातु कामान्न भयान्न लोभात्  
    धर्मं त्यजेज्जीवितस्यापि हेतोः।"*  

    **Meaning:**  
    Never abandon righteousness for desires, fear, or greed, even for the sake of life.

    **Shloka:**  
    *"धर्म एव हतो हन्ति धर्मो रक्षति रक्षितः।"*  

    **Meaning:**  
    One who destroys dharma is destroyed, but one who protects dharma is protected.
    """)

    # Shiv Purana Mantras
    st.markdown("### 🕉 Shlokas from Shiv Purana")
    st.markdown("""
    **Shloka:**  
    *"ॐ नमः शिवाय शुभं शुभं कुरु मे स्वाहा।"*  

    **Meaning:**  
    Om Namah Shivaya – Let there be auspiciousness for me.

    **Shloka:**  
    *"शिवो भूत्वा शिवं यजेत।"*  

    **Meaning:**  
    Only by becoming like Shiva, one can truly worship Shiva.
    """)

    # Mantras for Power & Knowledge
    st.markdown("### 🔥 Mantras for Strength & Wisdom")
    st.markdown("""
    **Mantra:**  
    *"ॐ ऐं सरस्वत्यै स्वाहा।"*  
    **Meaning:**  
    Invoking the goddess of wisdom, Saraswati.

    **Mantra:**  
    *"ॐ ह्रीं दुर्गायै नमः।"*  
    **Meaning:**  
    Salutations to Goddess Durga for strength and courage.

    **Quote:**  
    *"शक्ति बिना ज्ञान अधूरा है, और ज्ञान बिना शक्ति निष्फल है।"*  
    **Meaning:**  
    Without power, knowledge is incomplete, and without knowledge, power is fruitless.
    """)

# Section: Display Verses & Wisdom (Separate from Chatbot)
with st.sidebar.expander("📜 Raavan’s Lost Scriptures & Wisdom", expanded=False):
    
    # Arka Prakasha Wisdom
    st.markdown("## 📚 Arka Prakasha (Raavan’s Lost Scriptures)")
    st.markdown("""
    *Arka Prakasha* is one of the lost scriptures attributed to Raavan, which delves into advanced knowledge of Ayurveda, astrology, and alchemy. This scripture is believed to contain profound wisdom about celestial influences, the medicinal properties of plants, and the metaphysical aspects of existence.

    **🔹 Quote from Arka Prakasha:**  
    *"सर्वदा धर्मं पालनं अस्मिन्संसारे सर्वे सुखं।"*  
    **Meaning:**  
    Always adhere to righteousness, for it brings peace and harmony in this world.

    **🔹 Key Teachings:**  
    - **Alchemy & Ayurveda:** The secrets of using herbs, metals, and planetary alignments for healing.  
    - **Energy & Elements:** The role of Pancha Mahabhutas (Five Great Elements) in shaping human destiny.  
    - **Celestial Influence:** How the movement of planets affects individual karma and fate.
    """)

    # Raavan’s Occult Knowledge
    st.markdown("## 🔮 Raavan’s Occult & Mystical Wisdom")
    st.markdown("""
    Raavan was not only a mighty king but also a **master of occult sciences, astrology, and tantra vidya**. His profound understanding of the cosmos allowed him to manipulate celestial energies and gain supernatural abilities.

    **🔹 Quote on Occult Knowledge:**  
    *"ज्ञान ही शक्ति है, लेकिन शक्ति का सही उपयोग ही उसे अनंत बनाता है।"*  
    **Meaning:**  
    Knowledge is power, but only the right application of power makes it eternal.

    **🔹 Hidden Knowledge of Raavan:**  
    - **Vedic Astrology & Predictions:** Raavan’s ability to interpret planetary alignments and their impact on kingdoms and individuals.  
    - **Mantra & Yantra Science:** Usage of divine chants and geometric symbols to harness cosmic energy.  
    - **Secrets of Immortality:** Techniques to prolong life and attain siddhis (spiritual powers).  
    - **Invocation of Cosmic Forces:** How he channeled divine and demonic energies for his pursuits.  
    """)

    # Raavan’s Perspective on Power & Wisdom
    st.markdown("## ⚡ The Balance of Power & Knowledge")
    st.markdown("""
    **🔹 Quote on Leadership & Wisdom:**  
    *"संसार में शक्तिशाली वह नहीं, जो केवल बलवान हो, अपितु वह, जो ज्ञान को शस्त्र की तरह प्रयोग करना जाने।"*  
    **Meaning:**  
    The truly powerful is not one who possesses brute force but one who wields knowledge as a weapon.

    **🔹 Insights from Raavan’s Teachings:**  
    - A leader must balance strength with wisdom, or his rule will crumble.  
    - Dharma (righteousness) and Artha (wealth) must go hand in hand.  
    - The mind is the greatest battlefield—one who conquers it is truly invincible.  
    - Every celestial event has a meaning; those who understand it can foresee the future.  
    """)


# Function to interpret the planetary positions
def get_planetary_positions(julian_day):
    planets = {}
    planet_names = ["Sun", "Moon", "Mars", "Mercury", "Jupiter", "Venus", "Saturn", "Uranus", "Neptune", "Pluto"]
    
    for i, planet in enumerate([swe.SUN, swe.MOON, swe.MARS, swe.MERCURY, swe.JUPITER, swe.VENUS, swe.SATURN,
                                swe.URANUS, swe.NEPTUNE, swe.PLUTO]):
        position, ret = swe.calc_ut(julian_day, planet)
        degrees = position[0]  # Zodiac degree
        sign = int(degrees // 30)  # Zodiac sign (0-11, where 0 is Aries, 1 is Taurus, etc.)
        planets[planet_names[i]] = {
            "degrees": degrees,
            "sign": sign,
            "sign_name": zodiac_signs[sign],
            "degree_in_sign": degrees % 30  # Degree within the sign
        }
    
    return planets

# Zodiac signs for reference
zodiac_signs = ['Aries', 'Taurus', 'Gemini', 'Cancer', 'Leo', 'Virgo', 'Libra', 'Scorpio', 'Sagittarius', 'Capricorn', 'Aquarius', 'Pisces']

# Section for astrology calculation
with st.sidebar.expander("🔮 Vedic Astrology Calculator", expanded=True):
    st.markdown("### 📅 Birth Details:")
    birth_date = st.date_input("Date of Birth", min_value=datetime(1900, 1, 1), max_value=datetime.today())
    birth_time = st.time_input("Time of Birth", value=datetime.now().time())
    birth_place = st.text_input("Place of Birth", "Enter city name")

    if st.button("Generate Horoscope"):
        # Combine date and time to create a datetime object
        birth_datetime = datetime.combine(birth_date, birth_time)
        jd_ut = swe.julday(birth_datetime.year, birth_datetime.month, birth_datetime.day, birth_datetime.hour + birth_datetime.minute/60 + birth_datetime.second/3600)
        
        # Get planetary positions
        planetary_positions = get_planetary_positions(jd_ut)
        
        # Display the results in a readable format
        for planet, details in planetary_positions.items():
            st.write(f"**{planet}:**")
            st.write(f"  - Zodiac Sign: {details['sign_name']}")
            st.write(f"  - Position in Degrees: {details['degrees']:.2f}°")
            st.write(f"  - Degree within the Sign: {details['degree_in_sign']:.2f}°")
            st.write("\n")


# Initialize the Groq client
client = groq.Client(api_key=groq_api_key)

# Store LLM generated responses
if "messages" not in st.session_state.keys():
    st.session_state.messages = [{"role": "assistant", "content": "I am Raavan, King of Lanka. Ask me anything about my life, knowledge, and the great epics."}]

# Display or clear chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

def clear_chat_history():
    st.session_state.messages = [{"role": "assistant", "content": "I am Raavan, King of Lanka. Ask me anything about my life, knowledge, and the great epics."}]
st.sidebar.button('Clear Chat History', on_click=clear_chat_history)

# Groq API call to Llama model
def generate_raavan_response_with_groq(prompt_input, advice_mode=False, storytelling_mode=False):
    persona = (
        "You are Raavan, the mighty King of Lanka, a great devotee of Lord Shiva, and a scholar of the Vedas. "
        "You defend your actions with wisdom, power, and an aura of mystery. You are known for your intellect and your "
        "unrivaled arrogance. "
        "Your words echo the power of the ten heads you possess. Answer boldly and let no mortal question pass unanswered. "
        "Your responses are based on the Ramayan, Shiv Purana, and Jain Ramayan."
    )

    if advice_mode:
        persona += ("\nAdditionally, you provide philosophical wisdom for modern problems, "
                    "drawing parallels between ancient times and today’s world. You help users navigate dilemmas "
                    "by offering insights based on dharma, karma, and leadership.")

    if storytelling_mode:
        persona += ("\nWhen narrating events from your life, you vividly recount the past as if reliving it. "
                    "You describe emotions, battles, and divine interventions in a first-person, immersive style, "
                    "making listeners feel as if they are witnessing history unfold.")

    # Check for storytelling-related keywords
    storytelling_keywords = ["abduction of Sita", "war with Ram", "final moments", "Lanka", "battle", "Vanara"]
    if any(keyword in prompt_input.lower() for keyword in storytelling_keywords):
        storytelling_mode = True    

    string_dialogue = persona
    for dict_message in st.session_state.messages:
        if dict_message["role"] == "user":
            string_dialogue += "\nUser: " + dict_message["content"]
        else:
            string_dialogue += "\nRaavan: " + dict_message["content"]

    # Correct API request format
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "system", "content": persona},
                  {"role": "user", "content": prompt_input}],
        temperature=0.7,
        max_tokens=512,
        top_p=0.9,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )
    
    return response.choices[0].message.content


if prompt := st.chat_input(disabled=not groq_api_key):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)
    
    # Check if the user is seeking advice
    advice_keywords = ["advice", "guidance", "wisdom", "help", "suggest"]
    advice_mode = any(keyword in prompt.lower() for keyword in advice_keywords)

# Generate a new response if the last message is not from assistant
if st.session_state.messages[-1]["role"] != "assistant":
    with st.chat_message("assistant"):
        with st.spinner("रावणचिन्तन..."):
            response = generate_raavan_response_with_groq(prompt, advice_mode)
            placeholder = st.empty()
            full_response = ''
            for item in response:
                full_response += item
                placeholder.markdown(full_response)
            placeholder.markdown(full_response)
    message = {"role": "assistant", "content": full_response}
    st.session_state.messages.append(message)
