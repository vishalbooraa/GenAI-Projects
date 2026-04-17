import streamlit as st
from yt_analyzer import build_yt_agent

st.set_page_config(
    page_title="YouTube Video Analyzer",
    layout="centered"
)

st.title("🎥 AI YouTube Video Analyzer")

# Cache agent (so it doesn't reload every time)
@st.cache_resource
def get_agent():
    return build_yt_agent()

agent = get_agent()

# Input
video_url = st.text_input("Enter YouTube Video Link")
button = st.button("Analyze Video")

# Main logic
if video_url and button:
    with st.spinner("Analyzing video... ⏳"):
        try:
            response = agent.run(
                f"""
                Analyze this YouTube video:
                {video_url}

                Provide:
                - 📌 Summary
                - 🎯 Key Points
                - 🧠 Main Topic
                - 💡 Important Insights
                """
            )

            st.markdown("## 📊 Analysis Report")

            # Safe response handling
            if hasattr(response, "content"):
                st.markdown(response.content)
            else:
                st.markdown(str(response))

        except Exception as e:
            st.error(f"❌ Error: {e}")

elif button:
    st.warning("⚠️ Please enter a valid YouTube URL")