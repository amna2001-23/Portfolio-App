import streamlit as st
from streamlit.components.v1 import html
from PIL import Image

# Define CSS styles for 3D animations and effects
def css_styles():
    st.markdown("""
    <style>
    /* General body styles */
    body {
        font-family: Arial, sans-serif;
        background-color: #f4f4f4;
    }

    /* Animated 3D header styles with color cycle */
    .animated-header {
        font-size: 2.5em;
        font-weight: bold;
        text-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        transform: perspective(1000px) rotateX(0deg) rotateY(0deg);
        animation: bounce 2s infinite, rotate 10s linear infinite, colorchange 5s infinite;
    }

    @keyframes bounce {
        0%, 100% { transform: translateY(0); }
        50% { transform: translateY(-10px); }
    }

    @keyframes rotate {
        0% { transform: perspective(1000px) rotateY(0deg); }
        100% { transform: perspective(1000px) rotateY(360deg); }
    }

    @keyframes colorchange {
        0% { color: red; }
        25% { color: yellow; }
        50% { color: blue; }
        75% { color: green; }
        100% { color: red; }
    }

    /* Animated content styles */
    .animated-content {
        font-size: 1.2em;
        color: #333;
        text-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
        animation: slide 2s ease-in-out;
    }

    @keyframes slide {
        0% { transform: translateX(-100%); opacity: 0; }
        50% { opacity: 0.5; }
        100% { transform: translateX(0); opacity: 1; }
    }

    /* Animated sidebar styles */
    .sidebar {
        background-color: #333;
        color: #fff;
        padding: 10px;
        border-radius: 5px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.3);
    }

    /* 3D effects for elements */
    .card {
        border: 1px solid #ddd;
        border-radius: 10px;
        background-color: #fff;
        box-shadow: 0 10px 20px rgba(0, 0, 0, 0.2);
        padding: 15px;
        transform: perspective(1000px) rotateX(0deg) rotateY(0deg);
        transition: transform 0.3s;
    }
    .card:hover {
        transform: perspective(1000px) rotateX(10deg) rotateY(10deg);
    }
                 /* Keyframes for slide-in animation */
        @keyframes slideIn {
            from {
                opacity: 0;
                transform: translateX(-100%);
            }
            to {
                opacity: 1;
                transform: translateX(0);
            }
        }

        /* Style for social media icons */
        .social-icon {
            display: inline-block;
            margin-right: 15px;
            text-align: center;
        }
    </style>
    """, unsafe_allow_html=True)

# Define functions for each page
def about_page():
    css_styles()
    st.markdown('<h1 class="animated-header">About Me</h1>', unsafe_allow_html=True)
    st.markdown('<div class="animated-content">I\'m a seasoned AI & Full-Stack Developer specializing in creating innovative solutions that harness the power of artificial intelligence and data analysis. With expertise in AI, machine learning, data analysis, and full-stack development, I offer custom solutions tailored to your needs. Whether you need predictive modeling, data visualization, or interactive Streamlit applications, I\'m here to help you turn your data into actionable insights. Let\'s discuss your project and create solutions that drive your business forward.</div>', unsafe_allow_html=True)

    st.markdown('<div class="animated-content">My job is to build your website so that it is functional and user-friendly but at the same time attractive. Moreover, I add a personal touch to your product and make sure that it is eye-catching and easy to use. My aim is to bring across your message and identity in the most creative way. I have created web designs for many renowned brands.</div>', unsafe_allow_html=True)

    st.markdown('<h2 class="animated-header">What I\'m Doing</h2>', unsafe_allow_html=True)
    st.markdown('<div class="animated-content"><strong>Web Design</strong> - The most modern and high-quality design made at a professional level.</div>', unsafe_allow_html=True)
    st.markdown('<div class="animated-content"><strong>Web Development</strong> - High-quality development of sites at the professional level.</div>', unsafe_allow_html=True)
    st.markdown('<div class="animated-content"><strong>Artificial Intelligence</strong> - Professional development of Artificial Intelligence solutions, including machine learning models and natural language processing.</div>', unsafe_allow_html=True)
    st.markdown('<div class="animated-content"><strong>Data Analytics</strong> - High-quality data analysis services, including statistical analysis, data visualization, and predictive modeling, transforming raw data into actionable insights.</div>', unsafe_allow_html=True)
    st.markdown("""
    <style>
    .testimonials-container {
        display: flex;
        overflow-x: auto;
        scroll-snap-type: x mandatory;
        padding: 10px;
        border: 1px solid #ddd;
        border-radius: 5px;
        background: #f4f4f4;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    }
    .testimonial {
        flex: 0 0 auto;
        width: 300px;
        margin-right: 15px;
        padding: 10px;
        border: 1px solid #ddd;
        border-radius: 5px;
        background: #fff;
        scroll-snap-align: start;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    }
    .testimonial h4 {
        margin: 0;
        font-size: 16px;
        font-weight: bold;
        color: #333;
    }
    .testimonial p {
        margin: 5px 0 0;
        font-size: 14px;
        color: #555;
    }
    </style>
    <div class="testimonials-container">
        <div class="testimonial">
            <h4>Daniel Lewis</h4>
            <p>As a web developer, Amna was instrumental in redesigning our online presence. Her expertise in artificial intelligence and WordPress development ensured a seamless user experience.</p>
        </div>
        <div class="testimonial">
            <h4>Jessica Miller</h4>
            <p>Amna's lead generation strategies were pivotal for our growth. Her deep understanding of AI-powered analytics transformed our marketing efforts.</p>
        </div>
        <div class="testimonial">
            <h4>Emily Evans</h4>
            <p>Amna's expertise in WordPress development elevated our online presence. Her AI-driven solutions personalized user interactions, enhancing engagement significantly.</p>
        </div>
        <div class="testimonial">
            <h4>Henry William</h4>
            <p>Amna's WordPress solutions streamlined our operations. Her insights into AI for business optimization were invaluable.</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
def resume_page():
    css_styles()
    st.markdown('<h1 class="animated-header">Resume</h1>', unsafe_allow_html=True)

    st.markdown('<h2 class="animated-header">Education</h2>', unsafe_allow_html=True)
    st.markdown('<div class="animated-content"><strong>Khawaja Fareed College RYK</strong> (2021 - 2023) - BS Computer Science from Govt. Khawaja Fareed Graduate College Rahim Yar Khan</div>', unsafe_allow_html=True)
    st.markdown('<div class="animated-content"><strong>Govt. Women College, Rahim Yar Khan</strong> (2019 - 2021) - ADP from Government Women College Rahim Yar Khan</div>', unsafe_allow_html=True)
    st.markdown('<div class="animated-content"><strong>Govt. Women College, Rahim Yar Khan</strong> (2017 - 2019) - ICS from Government Women College Rahim Yar Khan</div>', unsafe_allow_html=True)

    st.markdown('<h2 class="animated-header">Experience</h2>', unsafe_allow_html=True)
    st.markdown('<div class="animated-content"><strong>Web Development</strong> (2022 - Present) - Offering professional web development services including front-end and back-end development, e-commerce solutions, and custom web applications.</div>', unsafe_allow_html=True)
    st.markdown('<div class="animated-content"><strong>Artificial Intelligence</strong> (2023 - Present) - Specializing in developing advanced AI solutions including machine learning model development, natural language processing, computer vision, and predictive analytics.</div>', unsafe_allow_html=True)
    st.markdown('<div class="animated-content"><strong>Data Analysis</strong> (2024 - Present) - Providing data analysis services including statistical analysis, data visualization, and predictive modeling.</div>', unsafe_allow_html=True)

    st.markdown('<h2 class="animated-header">Skills</h2>', unsafe_allow_html=True)
    st.markdown('<div class="animated-content">- <strong>Web Development</strong>: 90%</div>', unsafe_allow_html=True)
    st.markdown('<div class="animated-content">- <strong>Artificial Intelligence</strong>: 75%</div>', unsafe_allow_html=True)
    st.markdown('<div class="animated-content">- <strong>Data Analysis</strong>: 80%</div>', unsafe_allow_html=True)
    st.markdown('<div class="animated-content">- <strong>WordPress</strong>: 70%</div>', unsafe_allow_html=True)
    st.markdown('<div class="animated-content">- <strong>Lead Generation</strong>: 70%</div>', unsafe_allow_html=True)
    st.markdown('<div class="animated-content">- <strong>Streamlit Developer</strong>: 90%</div>', unsafe_allow_html=True)

def portfolio_page():
    css_styles()
    st.markdown('<h1 class="animated-header">Portfolio</h1>', unsafe_allow_html=True)

    st.markdown('<h2 class="animated-header">Filter by Category</h2>', unsafe_allow_html=True)
    categories = ["All", "Web Development", "Artificial Intelligence", "Lead Generation"]
    selected_category = st.selectbox("Select Category", categories)

    projects = {
        "Web Development": [
            {"title": "E-commerce", "img": "assets/images/p10.png", "category": "Web Development"},
            {"title": "E-commerce", "img": "assets/images/p11.png", "category": "Web Development"},
            {"title": "Web Design", "img": "assets/images/p12.png", "category": "Web Design"},
            {"title": "Hotel Management", "img": "assets/images/p8.png", "category": "Applications"}
        ],
        "Artificial Intelligence": [
            {"title": "Breast Tumor", "img": "assets/images/p1.png", "category": "Artificial Intelligence"},
            {"title": "Data Science App", "img": "assets/images/p2.png", "category": "Artificial Intelligence"},
            {"title": "Chatbot", "img": "assets/images/p5.png", "category": "Artificial Intelligence"},
            {"title": "Converter", "img": "assets/images/p6.png", "category": "Artificial Intelligence"}
        ]
    }

    for category, items in projects.items():
        if selected_category == "All" or selected_category == category:
            for item in items:
                st.image(item["img"], caption=item["title"], use_column_width=True)
                st.write(f"Category: {item['category']}")
                st.write("---")

def contact_page():
    css_styles()

    # Display banner image at the top
    banner_image = Image.open('b2.jpg')
    st.image(banner_image, use_column_width=True)

    # Header with animation
    st.markdown('<h1 class="animated-header">Contact</h1>', unsafe_allow_html=True)

    # Social media icons and links
    st.markdown("""
        <div class="social-icon">
            <a href="https://wa.me/923328360126">
                <img src="https://img.icons8.com/color/48/000000/whatsapp.png" alt="WhatsApp">
            </a>
        </div>
        <div class="social-icon">
            <a href="https://www.facebook.com/profile.php?id=61561065857337">
                <img src="https://img.icons8.com/color/48/000000/facebook.png" alt="Facebook">
            </a>
        </div>
        <div class="social-icon">
            <a href="https://www.instagram.com/amna232372?r=nametag">
                <img src="https://img.icons8.com/color/48/000000/instagram-new.png" alt="Instagram">
            </a>
        </div>
        <div class="social-icon">
            <a href="https://www.tiktok.com/@amna.developer?_t=8oI3tFOaUqt&_r=1">
                <img src="https://img.icons8.com/color/48/000000/tiktok.png" alt="TikTok">
            </a>
        </div>
        <div class="social-icon">
            <a href="https://www.linkedin.com/in/amna-akram-81aa632a6/">
                <img src="https://img.icons8.com/color/48/000000/linkedin.png" alt="LinkedIn">
            </a>
        </div>
        <div class="social-icon">
            <a href="https://github.com/amna2001-23">
                <img src="https://img.icons8.com/ios-glyphs/48/000000/github.png" alt="GitHub">
            </a>
        </div>
    """, unsafe_allow_html=True)



# Define a dictionary of pages
pages = {
    "About": about_page,
    "Resume": resume_page,
    "Portfolio": portfolio_page,
    "Contact": contact_page,
}

# Sidebar navigation
st.sidebar.markdown('<div class="sidebar">', unsafe_allow_html=True)
selected_page = st.sidebar.selectbox("Navigation", pages.keys(), format_func=lambda x: x.capitalize())
pages[selected_page]()
st.sidebar.markdown('</div>', unsafe_allow_html=True)
