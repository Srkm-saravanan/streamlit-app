import streamlit as st
import random
import time

# Set up page with a vibrant theme
st.set_page_config(page_title="AI Assistants Hub", layout="wide")

# Custom CSS for colorful styling
st.markdown(
    """
    <style>
        body {
            background-image: url("https://source.unsplash.com/1600x900/?artificial-intelligence,technology");
            background-size: cover;
            background-attachment: fixed;
            color: white;
        }
        .main {
            background-color: rgba(40, 42, 54, 0.8);  /* Semi-transparent dark background */
            padding: 20px;
            border-radius: 10px;
        }
        h1, h2, h3 {color: #ff79c6;}
        .stButton>button {background-color: #bd93f9; color: white; border-radius: 10px;}
        .stRadio > div {background-color: #6272a4; padding: 10px; border-radius: 5px;}
    </style>
    """,
    unsafe_allow_html=True,
)

# Header
st.title("Assitent Corner")
st.subheader("A vibrant platform to explore AI-powered tools!")

# AI Assistant Categories
st.sidebar.header("🔍 Categories")
categories = ["Chatbots", "Image Generators", "Code Assistants", "Voice AI", "Video AI", "Other AI Tools", "AI Learning Platforms"]
search_query = st.sidebar.text_input("🔎 Search AI Tools", "")

selected_category = st.sidebar.radio("Choose a category:", categories)

# Dictionary with AI assistant links
ai_assistants = {
    "Chatbots": [
        {"name": "ChatGPT", "link": "https://chat.openai.com/"},
        {"name": "Google Bard", "link": "https://bard.google.com/"},
        {"name": "Claude AI", "link": "https://claude.ai/"},
        {"name": "Perplexity AI", "link": "https://www.perplexity.ai/"},
    ],
    "Image Generators": [
        {"name": "DALL·E", "link": "https://openai.com/dall-e"},
        {"name": "Deep Dream Generator", "link": "https://deepdreamgenerator.com/"},
        {"name": "Runway ML", "link": "https://runwayml.com/"},
        {"name": "Stable Diffusion", "link": "https://stablediffusionweb.com/"},
    ],
    "Code Assistants": [
        {"name": "GitHub Copilot", "link": "https://github.com/features/copilot"},
        {"name": "Tabnine", "link": "https://www.tabnine.com/"},
        {"name": "Codeium", "link": "https://codeium.com/"},
    ],
    "Voice AI": [
        {"name": "ElevenLabs", "link": "https://elevenlabs.io/"},
        {"name": "Replica Studios", "link": "https://replicastudios.com/"},
    ],
    "Video AI": [
        {"name": "Synthesia", "link": "https://www.synthesia.io/"},
        {"name": "DeepBrain AI", "link": "https://www.deepbrain.io/"},
    ],
    "Other AI Tools": [
        {"name": "Hugging Face", "link": "https://huggingface.co/"},
        {"name": "Runway AI", "link": "https://runwayml.com/"},
    ],
    "AI Learning Platforms": [
        {"name": "Coursera", "link": "https://www.coursera.org/"},
        {"name": "DeepLearning.AI", "link": "https://www.deeplearning.ai/"},
        {"name": "Google AI", "link": "https://ai.google/"},
        {"name": "IBM AI", "link": "https://www.ibm.com/artificial-intelligence"},
        {"name": "LinkedIn Learning", "link": "https://www.linkedin.com/learning/"},
        {"name": "Udacity", "link": "https://www.udacity.com/"},
    ],
}

# Display AI assistants based on category or search query
st.write(f"### 🎨 {selected_category}")

filtered_tools = []
if search_query:
    for cat, tools in ai_assistants.items():
        for tool in tools:
            if search_query.lower() in tool["name"].lower():
                filtered_tools.append(tool)
else:
    filtered_tools = ai_assistants[selected_category]

# Show filtered results
if filtered_tools:
    for tool in filtered_tools:
        st.markdown(f'<a class="hover-link" href="{tool["link"]}" target="_blank" title="Click to visit {tool["name"]}">✅ <b>{tool["name"]}</b></a>', unsafe_allow_html=True)
else:
    st.markdown("❌ No AI tool found matching your search.")

# Random AI Fact Section with Auto-Update
def get_random_fact():
    facts = [
        "AI can now generate art, music, and even poetry!",
        "GPT-4 can process both text and images in its input!",
        "AI chatbots are being used for mental health support.",
        "Voice AI can now mimic human emotions with advanced deep learning techniques.",
    ]
    return random.choice(facts)

placeholder = st.sidebar.empty()

while True:
    placeholder.markdown(f"💡 **Did You Know?** {get_random_fact()}")
    time.sleep(10)

# Footer
st.markdown("---")
st.markdown("🎭 Made with ❤️ using [Streamlit](https://streamlit.io/)")
