import streamlit as st

# Set the page config to widen the app and set a title
st.set_page_config(page_title="Learn Music Easly for Dyslexia", layout="wide")

def main():
    # Inject custom CSS for image brightness, spacing, text color, and header color
    st.markdown("""
        <style>
            img { 
                filter: brightness(50%); /* Image brightness */
                display: block; /* Ensures the image is on its own line */
                margin-bottom: 20px; /* Space below the image */
                width: 200px; /* Set a fixed width for the image */
            }
            h1, h2, h3, h4, h5, h6, div, p, a { /* Targeting all text elements */
                color: #f07807; /* Custom text color */
            }
            .sidebar .sidebar-content {
                padding-top: 0px; /* Reduce padding at the top of the sidebar */
            }
        </style>
    """, unsafe_allow_html=True)

    # Sidebar for navigation or additional information
    with st.sidebar:
        st.image("./themes/logo-modified.png")  # Image in the sidebar
        
        # Adding options/features to the sidebar
        feature_selected = st.selectbox(
            "Choose a feature",
            ["Home", "VISUALIZING MUSIC SHEETS IN COLORY WAY", "SHOW INFORMATION ABOUT MUSIC NOTES", "MUSIC GENERATION", "SHOW MUSIC SHEETS FROM YOUR AUDIO"]  # List your features here
        )

    # Main content area based on the selected feature
    if feature_selected == "Home":
        display_home_page()
    elif feature_selected == "VISUALIZING MUSIC SHEETS IN COLORY WAY":
        display_feature_1()
    elif feature_selected == "SHOW INFORMATION ABOUT MUSIC NOTES":
        display_feature_2()
    elif feature_selected == "MUSIC GENERATION":
        display_feature_3()
    elif feature_selected == "SHOW MUSIC SHEETS FROM YOUR AUDIO":
        display_feature_4()

def display_home_page():
    # Home page content
    st.title("Learn Music Easly for Dyslexia")
    st.subheader("Welcome to Music Learning!🎷🎺🪗")
    st.write("This application is designed to help individuals with dyslexia learn music in a more accessible way.")

def display_feature_1():
    # Feature 1 content
    st.title("VISUALIZING MUSIC SHEETS IN COLORY WAY",)

def display_feature_2():
    # Feature 2 content
    st.title("SHOW INFORMATION ABOUT MUSIC NOTES")

def display_feature_3():
    # Feature 3 content
    st.title("MUSIC GENERATION ")
def display_feature_4():
    # Feature 3 content
    st.title("SHOW MUsic SHEETS FROM YOUR AUDIO ")

if __name__ == "__main__":
    main()
