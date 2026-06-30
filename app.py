import base64
from pathlib import Path

import streamlit as st

st.set_page_config(
    page_title="OmegA Computer Education",
    page_icon="assets/logo.png",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ----------------------------------------------------------------------------
# Helpers
# ----------------------------------------------------------------------------

@st.cache_data
def get_base64(path: str) -> str:
    return base64.b64encode(Path(path).read_bytes()).decode()


LOGO_B64 = get_base64("assets/logo.png")

# ----------------------------------------------------------------------------
# Data
# ----------------------------------------------------------------------------

COURSES = [
    {
        "code": "AI",
        "title": "Artificial Intelligence",
        "desc": "Learn intelligent systems, natural language processing, computer vision, generative AI, and AI-powered applications.",
        "tags": [],
    },
    {
        "code": "ML",
        "title": "Machine Learning",
        "desc": "Master supervised and unsupervised learning, model building, data preprocessing, and predictive analytics using industry-standard tools.",
        "tags": [],
    },
    {
        "code": "DS",
        "title": "Data Science & Analytics",
        "desc": "Develop expertise in data visualization, statistical analysis, data mining, and business intelligence techniques.",
        "tags": [],
    },
    {
        "code": "FS",
        "title": "Full Stack Web Development",
        "desc": "Build modern, responsive websites and web applications, front to back.",
        "tags": ["HTML5", "CSS3", "JavaScript", "React.js", "Node.js", "Express.js", "MySQL", "MongoDB"],
    },
    {
        "code": "MA",
        "title": "Mobile Application Development",
        "desc": "Create Android and cross-platform mobile applications that ship to real devices.",
        "tags": ["Android Studio", "Java", "Kotlin", "Flutter", "React Native"],
    },
    {
        "code": "UX",
        "title": "UI/UX Design",
        "desc": "Design engaging digital experiences, from first sketch to tested prototype.",
        "tags": ["User Research", "Wireframing", "Prototyping", "Figma", "Adobe XD", "Usability Testing"],
    },
    {
        "code": "ES",
        "title": "Embedded Systems & IoT",
        "desc": "Learn hardware-software integration, microcontrollers, sensors, and real-time applications.",
        "tags": ["Arduino", "ESP32", "Raspberry Pi", "ARM Processors", "Embedded C"],
    },
    {
        "code": "CC",
        "title": "Cloud Computing & DevOps",
        "desc": "Understand modern deployment practices used by real engineering teams.",
        "tags": ["AWS", "Microsoft Azure", "Docker", "Kubernetes", "CI/CD", "Git & GitHub"],
    },
    {
        "code": "CY",
        "title": "Cybersecurity",
        "desc": "Explore ethical hacking, network security, vulnerability assessment, penetration testing, and security best practices.",
        "tags": [],
    },
]

LANGUAGES = [
    "C", "C++", "Java", "Python", "JavaScript", "TypeScript",
    "Kotlin", "SQL", "PHP", "Go", "Rust", "Swift",
]

EMERGING_TECH = [
    "Generative AI", "Prompt Engineering", "Large Language Models (LLMs)",
    "Data Engineering", "Blockchain Technology", "Augmented Reality (AR)",
    "Virtual Reality (VR)", "Robotics", "Internet of Things (IoT)",
    "Quantum Computing Fundamentals", "Edge Computing",
]

WHY_US = [
    ("Industry-Aligned Curriculum", "Built around what hiring teams actually ask for, updated every term."),
    ("Experienced Mentors", "Learn from practitioners who work in the field, not just teach it."),
    ("Hands-on Projects", "Every module ends with something real you build, not just slides."),
    ("Internship Assistance", "We help place you with partner companies for on-the-job experience."),
    ("Career Guidance & Resume Building", "One-on-one sessions to shape your story for recruiters."),
    ("Interview Preparation Sessions", "Mock interviews and technical rounds before the real thing."),
    ("Flexible Learning Modes", "Join us online or offline, on a schedule that fits your life."),
    ("Certification on Completion", "A credential that signals real, verified skill."),
]

# ----------------------------------------------------------------------------
# CSS
# ----------------------------------------------------------------------------

CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;600;700&family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500;600&display=swap');

:root{
  --void:#120821;
  --bg1:#190c2c;
  --bg2:#22103c;
  --card:#251536;
  --card-hover:#2d1a44;
  --border:rgba(255,255,255,.09);
  --c1:#7b2ff7;
  --c2:#b621c4;
  --c3:#e91e8c;
  --cyan:#2be4e0;
  --ink:#f6f3ff;
  --ink-dim:#bcaedb;
  --ink-mute:#8678a8;
}

html, body, [class*="css"]{
  font-family:'Inter', sans-serif;
}

#MainMenu, header[data-testid="stHeader"], footer{visibility:hidden; height:0;}
.block-container{padding:0 !important; max-width:100% !important;}
.stApp{background:var(--void);}

.omega-wrap{ color:var(--ink); }
.omega-wrap *{ box-sizing:border-box; }

a{ text-decoration:none; color:inherit; }

/* ---------- NAV ---------- */
.nav{
  position:sticky; top:0; z-index:50;
  display:flex; align-items:center; justify-content:space-between;
  padding:16px 6vw;
  background:rgba(18,8,33,.78);
  backdrop-filter:blur(14px);
  border-bottom:1px solid var(--border);
}
.nav-brand{ display:flex; align-items:center; gap:12px; }
.nav-brand img{ height:38px; width:38px; border-radius:9px; object-fit:cover; }
.nav-brand .name{ font-family:'Space Grotesk',sans-serif; font-weight:700; font-size:1.12rem; letter-spacing:.2px; }
.nav-brand .sub{ font-size:.66rem; color:var(--ink-mute); letter-spacing:2.5px; text-transform:uppercase; margin-top:1px; }
.nav-links{ display:flex; gap:30px; font-size:.92rem; color:var(--ink-dim); }
.nav-links a:hover{ color:var(--cyan); }
.nav-cta{
  padding:9px 20px; border-radius:30px; font-size:.86rem; font-weight:600;
  background:linear-gradient(120deg,var(--c1),var(--c3));
  color:white; white-space:nowrap;
}
@media(max-width:900px){ .nav-links{display:none;} }

/* ---------- HERO ---------- */
.hero{
  position:relative; overflow:hidden;
  padding:7vw 6vw 6vw 6vw;
  background:
    radial-gradient(60% 55% at 85% 8%, rgba(123,47,247,.45), transparent 60%),
    radial-gradient(55% 50% at 8% 95%, rgba(233,30,140,.32), transparent 60%),
    var(--void);
  display:flex; align-items:center; gap:5vw;
  border-bottom:1px solid var(--border);
}
.hero-grid{
  position:absolute; inset:0; opacity:.35; pointer-events:none;
  background-image:
    linear-gradient(var(--border) 1px, transparent 1px),
    linear-gradient(90deg, var(--border) 1px, transparent 1px);
  background-size:46px 46px;
  mask-image:radial-gradient(60% 60% at 70% 30%, black, transparent);
}
.hero-left{ position:relative; z-index:2; flex:1.1; min-width:300px; }
.eyebrow{
  display:inline-flex; align-items:center; gap:8px;
  font-family:'JetBrains Mono',monospace; font-size:.74rem; letter-spacing:1.5px;
  color:var(--cyan); background:rgba(43,228,224,.08);
  border:1px solid rgba(43,228,224,.25); padding:6px 14px; border-radius:30px;
  margin-bottom:22px;
}
.eyebrow .dot{ width:6px; height:6px; border-radius:50%; background:var(--cyan); box-shadow:0 0 8px var(--cyan); }
.hero h1{
  font-family:'Space Grotesk',sans-serif; font-weight:700;
  font-size:clamp(2.1rem, 4vw, 3.4rem); line-height:1.12; margin:0 0 22px 0;
}
.hero h1 .grad{
  background:linear-gradient(100deg,var(--c1),var(--c3) 60%, var(--cyan));
  -webkit-background-clip:text; background-clip:text; color:transparent;
}
.hero p{ font-size:1.08rem; line-height:1.7; color:var(--ink-dim); max-width:540px; margin-bottom:34px; }
.hero-ctas{ display:flex; gap:16px; flex-wrap:wrap; }
.btn-primary{
  padding:14px 30px; border-radius:10px; font-weight:600; font-size:.95rem;
  background:linear-gradient(120deg,var(--c1),var(--c3));
  color:white; box-shadow:0 14px 30px -10px rgba(233,30,140,.5);
  border:none; cursor:pointer;
}
.btn-ghost{
  padding:14px 30px; border-radius:10px; font-weight:600; font-size:.95rem;
  background:transparent; border:1px solid var(--border); color:var(--ink);
}
.btn-ghost:hover{ border-color:var(--cyan); color:var(--cyan); }

.hero-right{ position:relative; z-index:2; flex:1; min-width:280px; display:flex; justify-content:center; }
.term{
  width:100%; max-width:420px; background:var(--bg2); border:1px solid var(--border);
  border-radius:14px; overflow:hidden; box-shadow:0 30px 60px -20px rgba(0,0,0,.6);
}
.term-bar{ display:flex; gap:7px; padding:12px 14px; background:rgba(255,255,255,.03); border-bottom:1px solid var(--border); }
.term-bar span{ width:10px; height:10px; border-radius:50%; }
.term-bar span:nth-child(1){ background:#ff5f57; }
.term-bar span:nth-child(2){ background:#febc2e; }
.term-bar span:nth-child(3){ background:#28c840; }
.term-body{ padding:20px 22px; font-family:'JetBrains Mono',monospace; font-size:.84rem; line-height:2; color:var(--ink-dim); }
.term-body .p{ color:var(--cyan); }
.term-body .c{ color:#9ae6a3; }
.term-body .ok{ color:var(--ink-mute); }
.cursor{ display:inline-block; width:7px; height:14px; background:var(--cyan); animation:blink 1.1s steps(1) infinite; vertical-align:-2px; }
@keyframes blink{ 50%{ opacity:0; } }

/* ---------- SECTION SHELL ---------- */
.section{ padding:6vw 6vw; }
.section.alt{ background:var(--bg1); border-top:1px solid var(--border); border-bottom:1px solid var(--border); }
.sec-head{ max-width:680px; margin-bottom:48px; }
.sec-tag{ font-family:'JetBrains Mono',monospace; font-size:.74rem; letter-spacing:2px; color:var(--cyan); text-transform:uppercase; margin-bottom:12px; display:block; }
.sec-head h2{ font-family:'Space Grotesk',sans-serif; font-size:clamp(1.6rem,2.6vw,2.3rem); font-weight:700; margin:0 0 12px 0; }
.sec-head p{ color:var(--ink-dim); font-size:1.02rem; line-height:1.65; }

/* ---------- COURSE CARDS ---------- */
.course-grid{ display:grid; grid-template-columns:repeat(auto-fit,minmax(290px,1fr)); gap:22px; }
.course-card{
  background:var(--card); border:1px solid var(--border); border-radius:16px;
  padding:26px 24px; transition:transform .18s ease, border-color .18s ease, background .18s ease;
}
.course-card:hover{ transform:translateY(-4px); border-color:rgba(123,47,247,.55); background:var(--card-hover); }
.code-badge{
  width:50px; height:50px; border-radius:12px; display:flex; align-items:center; justify-content:center;
  font-family:'JetBrains Mono',monospace; font-weight:600; font-size:.92rem; color:white; margin-bottom:18px;
  background:linear-gradient(135deg,var(--c1),var(--c3));
}
.course-card h3{ font-family:'Space Grotesk',sans-serif; font-size:1.12rem; margin:0 0 10px 0; font-weight:700;}
.course-card p{ color:var(--ink-dim); font-size:.92rem; line-height:1.6; margin-bottom:14px; }
.pill-row{ display:flex; flex-wrap:wrap; gap:7px; }
.pill{
  font-family:'JetBrains Mono',monospace; font-size:.7rem; padding:4px 10px; border-radius:6px;
  background:rgba(43,228,224,.08); color:var(--cyan); border:1px solid rgba(43,228,224,.2);
}

/* ---------- TERMINAL LANGUAGE BLOCK ---------- */
.lang-term{
  background:var(--bg2); border:1px solid var(--border); border-radius:16px; overflow:hidden;
  box-shadow:0 30px 60px -28px rgba(0,0,0,.65);
}
.lang-term .term-bar span{ }
.lang-term .term-title{ font-family:'JetBrains Mono',monospace; font-size:.78rem; color:var(--ink-mute); margin-left:6px; }
.lang-body{ padding:30px 30px 34px 30px; }
.lang-grid{ display:grid; grid-template-columns:repeat(auto-fill,minmax(150px,1fr)); gap:14px; }
.lang-chip{
  font-family:'JetBrains Mono',monospace; font-size:.86rem; color:var(--ink);
  background:rgba(255,255,255,.03); border:1px solid var(--border); border-radius:8px;
  padding:12px 14px; display:flex; align-items:center; gap:10px;
}
.lang-chip::before{ content:'</>'; color:var(--cyan); font-size:.72rem; }

/* ---------- EMERGING TECH ---------- */
.emerge-grid{ display:grid; grid-template-columns:repeat(auto-fit,minmax(230px,1fr)); gap:16px; }
.emerge-card{
  border:1px solid var(--border); border-radius:14px; padding:20px 20px;
  background:linear-gradient(160deg, rgba(43,228,224,.05), rgba(123,47,247,.05));
  position:relative;
}
.emerge-card .num{ font-family:'JetBrains Mono',monospace; font-size:.72rem; color:var(--cyan); display:block; margin-bottom:10px; }
.emerge-card .label{ font-weight:600; font-size:.98rem; }

/* ---------- WHY US ---------- */
.why-grid{ display:grid; grid-template-columns:repeat(auto-fit,minmax(300px,1fr)); gap:20px; }
.why-card{ display:flex; gap:16px; padding:6px 0; }
.check{
  flex:none; width:34px; height:34px; border-radius:50%;
  background:rgba(43,228,224,.1); border:1px solid rgba(43,228,224,.35);
  display:flex; align-items:center; justify-content:center; color:var(--cyan); font-weight:700;
}
.why-card h4{ margin:0 0 4px 0; font-size:1rem; font-weight:700; font-family:'Space Grotesk',sans-serif; }
.why-card p{ margin:0; color:var(--ink-dim); font-size:.9rem; line-height:1.55; }

/* ---------- CTA BANNER ---------- */
.cta-banner{
  margin:6vw; border-radius:22px; padding:5vw 5vw;
  background:linear-gradient(120deg, rgba(123,47,247,.9), rgba(233,30,140,.85));
  position:relative; overflow:hidden; text-align:center;
}
.cta-banner h2{ font-family:'Space Grotesk',sans-serif; font-size:clamp(1.6rem,3vw,2.4rem); margin:0 0 14px 0; font-weight:700;}
.cta-banner p{ max-width:560px; margin:0 auto 28px auto; color:rgba(255,255,255,.9); font-size:1.02rem; line-height:1.65;}
.cta-banner .btn-primary{ background:white; color:#3b0a63; box-shadow:0 14px 30px -10px rgba(0,0,0,.35); }

/* ---------- FOOTER ---------- */
.foot{ padding:40px 6vw 30px 6vw; border-top:1px solid var(--border); display:flex; flex-wrap:wrap; gap:20px; align-items:center; justify-content:space-between; }
.foot-brand{ display:flex; align-items:center; gap:10px; color:var(--ink-mute); font-size:.85rem; }
.foot-brand img{ height:26px; width:26px; border-radius:6px; }
.foot small{ color:var(--ink-mute); font-size:.8rem; }

/* ---------- CONTACT (streamlit native) ---------- */
.contact-head{ padding:6vw 6vw 1vw 6vw; }
div[data-testid="stForm"]{
  background:var(--bg1); border:1px solid var(--border); border-radius:18px;
  padding:34px; max-width:640px; margin:0 6vw 5vw 6vw;
}
div[data-testid="stForm"] label p{ color:var(--ink-dim) !important; font-size:.86rem !important; }
.stTextInput input, .stTextArea textarea, .stSelectbox div[data-baseweb="select"] > div{
  background:var(--bg2) !important; color:var(--ink) !important; border:1px solid var(--border) !important; border-radius:8px !important;
}
.stForm button{
  background:linear-gradient(120deg,var(--c1),var(--c3)) !important; color:white !important; border:none !important;
  border-radius:8px !important; font-weight:600 !important; padding:.55rem 1.6rem !important;
}
</style>
"""

# ----------------------------------------------------------------------------
# Render
# ----------------------------------------------------------------------------

st.markdown(CSS, unsafe_allow_html=True)

course_cards_html = ""
for c in COURSES:
    tags_html = ""
    if c["tags"]:
        chips = "".join(f'<span class="pill">{t}</span>' for t in c["tags"])
        tags_html = f'<div class="pill-row">{chips}</div>'
    course_cards_html += f"""
    <div class="course-card">
      <div class="code-badge">{c['code']}</div>
      <h3>{c['title']}</h3>
      <p>{c['desc']}</p>
      {tags_html}
    </div>
    """

lang_chips_html = "".join(f'<div class="lang-chip">{lang}</div>' for lang in LANGUAGES)

emerge_html = ""
for i, t in enumerate(EMERGING_TECH, start=1):
    emerge_html += f"""
    <div class="emerge-card">
      <span class="num">{i:02d}</span>
      <span class="label">{t}</span>
    </div>
    """

why_html = ""
for title, desc in WHY_US:
    why_html += f"""
    <div class="why-card">
      <div class="check">&#10003;</div>
      <div><h4>{title}</h4><p>{desc}</p></div>
    </div>
    """

page_html = f"""
<div class="omega-wrap">

  <!-- NAV -->
  <div class="nav">
    <div class="nav-brand">
      <img src="data:image/png;base64,{LOGO_B64}" />
      <div>
        <div class="name">OmegA</div>
        <div class="sub">Computer Education</div>
      </div>
    </div>
    <div class="nav-links">
      <a href="#courses">Courses</a>
      <a href="#languages">Languages</a>
      <a href="#emerging">Emerging Tech</a>
      <a href="#why">Why Us</a>
      <a href="#contact">Contact</a>
    </div>
    <a class="nav-cta" href="#contact">Enroll Now</a>
  </div>

  <!-- HERO -->
  <div class="hero">
    <div class="hero-grid"></div>
    <div class="hero-left">
      <div class="eyebrow"><span class="dot"></span> ENROLLMENTS OPEN &middot; ONLINE &amp; OFFLINE</div>
      <h1>Transform Your Career with <span class="grad">Industry-Focused Training</span></h1>
      <p>Join our comprehensive training programs designed for students, graduates, working professionals,
      and tech enthusiasts. Gain practical knowledge, work on real-world projects, and build skills that
      employers value.</p>
      <div class="hero-ctas">
        <a href="#contact"><button class="btn-primary">Start Your Tech Journey &rarr;</button></a>
        <a href="#courses"><button class="btn-ghost">Explore Courses</button></a>
      </div>
    </div>
    <div class="hero-right">
      <div class="term">
        <div class="term-bar"><span></span><span></span><span></span></div>
        <div class="term-body">
          <div><span class="p">&gt;</span> whoami</div>
          <div class="ok">future_engineer</div>
          <div><span class="p">&gt;</span> enroll --course "Full Stack"</div>
          <div class="c">[ok] seat reserved</div>
          <div><span class="p">&gt;</span> build --project "real-world"</div>
          <div class="c">[ok] shipped to production</div>
          <div><span class="p">&gt;</span> career --status<span class="cursor"></span></div>
        </div>
      </div>
    </div>
  </div>

  <!-- COURSES -->
  <div class="section" id="courses">
    <div class="sec-head">
      <span class="sec-tag">// 01 Trending Courses</span>
      <h2>Pick a track, go deep</h2>
      <p>Eight in-demand programs, each built around real tools and real projects &mdash; not just theory.</p>
    </div>
    <div class="course-grid">
      {course_cards_html}
    </div>
  </div>

  <!-- LANGUAGES -->
  <div class="section alt" id="languages">
    <div class="sec-head">
      <span class="sec-tag">// 02 Programming Languages</span>
      <h2>Build a strong coding foundation</h2>
      <p>Industry-relevant languages taught with the syntax, tooling, and habits used on real teams.</p>
    </div>
    <div class="lang-term">
      <div class="term-bar"><span></span><span></span><span></span><span class="term-title">~/omega/languages</span></div>
      <div class="lang-body">
        <div class="lang-grid">
          {lang_chips_html}
        </div>
      </div>
    </div>
  </div>

  <!-- EMERGING TECH -->
  <div class="section" id="emerging">
    <div class="sec-head">
      <span class="sec-tag">// 03 Emerging Technologies</span>
      <h2>Stay ahead of the curve</h2>
      <p>Specialized courses in the technologies shaping what comes next.</p>
    </div>
    <div class="emerge-grid">
      {emerge_html}
    </div>
  </div>

  <!-- WHY US -->
  <div class="section alt" id="why">
    <div class="sec-head">
      <span class="sec-tag">// 04 Why Learn With Us</span>
      <h2>What you actually get</h2>
      <p>Training that's measured by outcomes, not attendance.</p>
    </div>
    <div class="why-grid">
      {why_html}
    </div>
  </div>

  <!-- CTA -->
  <div class="cta-banner">
    <h2>Start Your Tech Journey Today</h2>
    <p>Equip yourself with the skills of tomorrow and become a confident, job-ready professional
    in the ever-evolving world of technology.</p>
    <a href="#contact"><button class="btn-primary">Get Started &rarr;</button></a>
  </div>

  <div class="contact-head">
    <span class="sec-tag">// 05 Get In Touch</span>
    <h2 style="font-family:'Space Grotesk',sans-serif; font-size:1.9rem; font-weight:700; margin:0 0 8px 0;">Reserve your seat</h2>
    <p style="color:var(--ink-dim); max-width:540px;">Tell us which course you're interested in and our team will reach out with batch timings and fees.</p>
  </div>
</div>
"""

st.markdown(page_html, unsafe_allow_html=True)

# ----------------------------------------------------------------------------
# CONTACT FORM (native Streamlit, styled via CSS above)
# ----------------------------------------------------------------------------

with st.form("contact_form", clear_on_submit=True):
    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input("Full name")
    with col2:
        phone = st.text_input("Phone number")
    email = st.text_input("Email address")
    course = st.selectbox("Course of interest", [c["title"] for c in COURSES] + ["Not sure yet"])
    message = st.text_area("Message (optional)", placeholder="Tell us about your background or goals...")
    submitted = st.form_submit_button("Request a Callback")
    if submitted:
        if name and (email or phone):
            st.success(f"Thanks, {name}! Our team will reach out shortly about {course}.")
        else:
            st.error("Please share your name and at least an email or phone number.")

st.markdown(
    f"""
    <div class="omega-wrap">
      <div class="foot">
        <div class="foot-brand">
          <img src="data:image/png;base64,{LOGO_B64}" />
          OmegA Computer Education &mdash; Engineering Tuitions
        </div>
        <small>&copy; 2026 OmegA Computer Education. All rights reserved.</small>
      </div>
    </div>
    """,
    unsafe_allow_html=True,
)
