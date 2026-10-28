import streamlit as st
import pandas as pd
import numpy as np

# Page Configuration
st.set_page_config(
    page_title="Christian Buzarang | Portfolio",
    layout="wide",
)


# Sidebar Navigation
with st.sidebar:
    st.image("static/my_picture.png", width=240)
    st.title("Christian V. Buzarang")
    st.caption("BS Computer Science • CIT-U")
    st.markdown("---")

    st.subheader("Navigation Menu")
    menu = st.radio(
        "Go to",
        [
            "About Me",
            "Autobiography & Milestones",
            "Skills & Analytics",
            "Projects",
            "Contact & Feedback",
        ],
    )

    st.markdown("---")
    st.markdown("**Course:** CS365 Applied AI")
    st.markdown("**Section:** F2")
    st.markdown("**Location:** Cebu, Philippines")

# About Me section
if menu == "About Me":
    st.title("Welcome to My Portfolio")
    st.markdown("### Aspiring Software Engineer & Game Developer")

    col1, col2 = st.columns([2, 1])
    with col1:
        st.write("""
        Hello! I'm **Christian V. Buzarang**, a dedicated Bachelor of Science in Computer Science student at **Cebu Institute of Technology - University (CIT-U)** in Cebu, Philippines. 
        
        My passion lies at the intersection of software development, machine learning applications, and indie game development using Godot Engine. I thrive in terminal-driven Linux environments, favoring clean code architecture, robust backend logic, and interactive user experiences.
        """)

        # Metrics Extra Component
        m1, m2, m3 = st.columns(3)
        m1.metric("Tech Stacks", "5+", "Core Languages")
        m2.metric("Major Projects", "4 Built", "Active Dev")
        m3.metric("Scholarship", "DOST-SEI", "S&T Scholar")

    with col2:
        st.info(
            "💡 **Quick Facts**\n\n- 📍 Based in Lapu-Lapu City, Cebu\n- 🎮 Godot indie game developer\n- 📊 Data analytics & QA focus"
        )

# Autobiography & Milestones Section
elif menu == "Autobiography & Milestones":
    st.title("Autobiography & Journey")

    tab1, tab2, tab3 = st.tabs(
        ["Background", "Education & Philosophy", "Key Milestones"]
    )

    with tab1:
        st.subheader("Roots & Passion")
        st.write("""
        Growing up in Lapu-Lapu City, Cebu, Philippines, technology has always been a medium for creative problem-solving. From early curiosity about how software and games work under the hood to building complex desktop and web applications, my journey in computer science has been driven by a constant desire to build functional, elegant, high-performance systems and fun.
        """)

    with tab2:
        st.subheader("Academic Journey at CIT-U")
        st.write("""
        Pursuing a Bachelor of Science in Computer Science at **Cebu Institute of Technology - University** has sharpened my theoretical foundations and practical engineering skills. From formal language theory and discrete probability to advanced data structures and machine learning models, my academic work directly informs my software projects. 
        
        As a qualified scholar under the **DOST-SEI S&T Undergraduate Scholarship program**, I maintain a rigorous dedication to academic excellence and technical growth.
        """)

    with tab3:
        st.subheader("Milestones & Achievements")
        st.success(
            "🌟 **DOST-SEI S&T Undergraduate Scholar** — Recognized scholar under the national science and technology scholarship program."
        )
        st.success(
            "🚀 **GEAR Program Invitation** — Accepted into the selective GEAR program focusing on artificial intelligence, technical project management, and software development."
        )
        st.success(
            "🏆 **Hackathons & Challenges** — Active participant in regional technical challenges including the NEXT LEVEL Esports Game Dev Challenge (MoyveTeam)."
        )

# Skills & Analytics Section
elif menu == "Skills & Analytics":
    st.title("Technical Proficiency & Analytics")
    st.write(
        "Explore my technical stack breakdown across systems programming, web development, and game engineering."
    )

    # Interactive widgets
    skill_category = st.selectbox(
        "Filter skill proficiency by domain:",
        ["All Domains", "Languages", "Frameworks & Engines"],
    )

    skills_data = {
        "Technology": [
            "Python",
            "C / C++",
            "Java / JavaFX",
            "C# (.NET / Blazor)",
            "PHP & SQL",
            "GDScript (Godot)",
        ],
        "Domain": [
            "Languages",
            "Languages",
            "Frameworks & Engines",
            "Frameworks & Engines",
            "Databases & Web",
            "Frameworks & Engines",
        ],
        "Proficiency (%)": [45, 75, 75, 50, 70, 65],
        "Experience Level": [
            "Beginner",
            "Intermediate",
            "Intermediate",
            "Beginner",
            "Intermediate",
            "Intermediate",
        ],
    }
    df_skills = pd.DataFrame(skills_data)

    if skill_category != "All Domains":
        df_filtered = df_skills[df_skills["Domain"] == skill_category]
    else:
        df_filtered = df_skills

    col_table, col_chart = st.columns([1, 1])

    with col_table:
        st.subheader("Skill Matrix Table")
        st.dataframe(df_filtered, use_container_width=True)

    with col_chart:
        st.subheader("Proficiency Bar Chart")
        st.bar_chart(df_filtered.set_index("Technology")["Proficiency (%)"])

    st.markdown("---")
    st.subheader("Interactive Skill Threshold Analyzer")
    selected_tech = st.select_slider(
        "Select minimum proficiency threshold:", options=[i for i in range(0, 101)]
    )
    matched_tech = df_skills[df_skills["Proficiency (%)"] >= selected_tech][
        "Technology"
    ].tolist()
    st.write(
        f"Technologies with proficiency $\\ge$ {selected_tech}%: **{', '.join(matched_tech) if matched_tech else 'None'}**"
    )

# Projects Section
elif menu == "Projects":
    st.title("Featured Projects")
    st.write(
        "Here are four major projects showcasing my work across desktop apps, enterprise platforms, game development, and web systems."
    )

    tab_p1, tab_p2, tab_p3, tab_p4 = st.tabs(
        ["GymQuest", "Project Ascend", "Se Cognos Chess", "BitFlip Academy"]
    )

    with tab_p1:
        st.subheader("GymQuest")
        st.markdown("**Role:** Lead Developer & Architect")
        st.write("""
        GymQuest is a Java-based desktop program designed to address low member retention and heavy administrative overhead in standard fitness centers. While most systems focus solely on basic record-keeping and labor-intensive workflows, GymQuest bridges the gap between management and motivation.

The system provides a centralized platform for admins, trainers, and members to seamlessly interact. By offering structured session bookings, customizable workout tracking, and an interactive community space, GymQuest transforms standard gym management into a collaborative, highly responsive fitness management experience.
        """)
        st.caption("Tools: Java, JavaFX, FXML, CSS, MySQL")
        st.markdown(
            "[View GymQuest GitHub Repository](https://github.com/ChristianBuzarang/GymQuest)"
        )

    with tab_p2:
        st.subheader("Project Ascend")
        st.markdown("**Role:** Full-Stack & ML Integration Lead")
        st.write("""
        An enterprise resilience and stress inoculation platform that integrates biometric data visualization with machine learning classification pipelines to monitor and assess user stress levels.
        """)
        st.caption("Tools: Python, Scikit-Learn, Pandas, Machine Learning")
        st.markdown(
            "[View Project Ascend GitHub Repository](https://github.com/ChristianBuzarang/Project-Ascenso)"
        )

    with tab_p3:
        st.subheader("Se Cognos Chess")
        st.markdown("**Role:** Project Manager & Game Developer")
        st.write("""
        Se Cognos Chess (Latin for "Know Thyself") is a psychological, cyberpunk strategy game that completely deconstructs the world’s oldest board game. Built from the ground up in Godot 4, it transforms traditional chess into a fast-paced, highly tactical esports and arcade experience.

Developed by MoyveTeam from Cebu Institute of Technology - University for the NEXT LEVEL: ESPORTS GAME DEV CHALLENGE 2026.
        """)
        st.caption("Tools: Godot Engine, GDScript, Blender, Custom Shaders")
        st.markdown(
            "[View Se Cognos Chess GitHub Repository](https://github.com/ChristianBuzarang/Se-Cognos-Chess)"
        )

    with tab_p4:
        st.subheader("BitFlip Academy")
        st.markdown("**Role:** Full-Stack Web Developer")
        st.write("""
        A full-stack web application built using C# .NET Blazor and MySQL, featuring responsive component architecture and secure database connectivity.
        """)
        st.caption("Tools: C#, .NET Blazor, MySQL, Entity Framework")
        st.markdown(
            "[View BitFlip Academy GitHub Repository](https://github.com/ChristianBuzarang/BitFlipAcademy)"
        )

# Contact & Feedback Form Section
elif menu == "Contact & Feedback":
    st.title("Contact & Feedback Form")
    st.write(
        "Have a question, collaboration proposal, or feedback on this app? Drop a message below!"
    )

    with st.form("contact_form"):
        name = st.text_input("Your Name")
        email = st.text_input("Your Email Address")
        topic = st.selectbox(
            "Topic",
            [
                "Collaboration",
                "Job / Internship Opportunity",
                "General Inquiry",
                "App Feedback",
            ],
        )
        message = st.text_area("Your Message")

        checkbox_copy = st.checkbox("Send me a copy of this message")
        submitted = st.form_submit_button("Submit Message")

        if submitted:
            if name and email and message:
                st.success(
                    f"Thank you, {name}! Your message regarding '{topic}' has been successfully submitted. I will get back to you shortly."
                )
                if checkbox_copy:
                    st.info(
                        f"A confirmation copy has been notionally dispatched to {email}."
                    )
            else:
                st.error(
                    "Please fill in all required fields (Name, Email, and Message) before submitting."
                )

# Footer
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: gray;'>Christian V. Buzarang • CSIT 349 Applied AI Portfolio App • Built with Streamlit</div>",
    unsafe_allow_html=True,
)
