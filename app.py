import streamlit as st
import random

# =========================================================
# NEXAGEN
# =========================================================

st.set_page_config(
    page_title="NexaGen",
    page_icon="✦",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================================================
# SESSION STATE
# =========================================================

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "page" not in st.session_state:
    st.session_state.page = "Home"

if "likes" not in st.session_state:
    st.session_state.likes = set()

if "saved" not in st.session_state:
    st.session_state.saved = set()

if "points" not in st.session_state:
    st.session_state.points = 240

# =========================================================
# DESIGN
# =========================================================

st.markdown("""
<style>

@import url(
'https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap'
);

* {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background:
        radial-gradient(
            circle at 10% 0%,
            rgba(121, 67, 255, 0.18),
            transparent 27%
        ),
        radial-gradient(
            circle at 90% 10%,
            rgba(255, 65, 146, 0.12),
            transparent 25%
        ),
        #080912;

    color: white;
}

header {
    background: transparent !important;
}

footer {
    visibility: hidden;
}

#MainMenu {
    visibility: hidden;
}

/* SIDEBAR */

[data-testid="stSidebar"] {
    background: #0b0d18;
    border-right: 1px solid #20243a;
}

[data-testid="stSidebar"] .stButton button {
    text-align: left;
    background: transparent !important;
    border: none !important;
    color: #9da4bb !important;
}

[data-testid="stSidebar"] .stButton button:hover {
    background: #171a2b !important;
    color: white !important;
}

/* HEADINGS */

h1 {
    color: white !important;
    font-size: 38px !important;
    font-weight: 800 !important;
}

h2 {
    color: white !important;
}

h3 {
    color: white !important;
}

p {
    color: #aab1c6;
}

/* BUTTONS */

.stButton button {
    background: #15192a !important;
    color: #e8eaf3 !important;

    border: 1px solid #303651 !important;

    border-radius: 11px !important;

    min-height: 42px;

    font-weight: 600;
}

.stButton button:hover {
    background: #765cff !important;
    color: white !important;

    border-color: #927dff !important;
}

/* INPUT */

input,
textarea {
    background: #111526 !important;
    color: white !important;

    border: 1px solid #2c3450 !important;
}

/* CONTAINERS */

[data-testid="stVerticalBlockBorderWrapper"] {
    background: rgba(17, 20, 36, 0.95);
    border: 1px solid #252a43;
    border-radius: 18px;
}

/* METRICS */

[data-testid="stMetric"] {
    background: #111526;
    border: 1px solid #272d47;
    padding: 18px;
    border-radius: 16px;
}

/* DIVIDER */

hr {
    border-color: #252a42 !important;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# LOGIN PAGE
# =========================================================

if not st.session_state.logged_in:

    st.markdown("<br><br>", unsafe_allow_html=True)

    left, middle, right = st.columns([1, 2, 1])

    with middle:

        st.markdown(
            "<h1 style='text-align:center;'>✦</h1>",
            unsafe_allow_html=True
        )

        st.markdown(
            "<h1 style='text-align:center;'>NexaGen</h1>",
            unsafe_allow_html=True
        )

        st.markdown(
            "<p style='text-align:center;'>"
            "Discover. Play. Read. Create."
            "</p>",
            unsafe_allow_html=True
        )

        with st.container(border=True):

            st.subheader("Welcome back")

            st.write(
                "Sign in to continue your NexaGen journey."
            )

            username = st.text_input(
                "Username",
                placeholder="Enter your username"
            )

            password = st.text_input(
                "Password",
                type="password",
                placeholder="Enter your password"
            )

            if st.button(
                "Continue →",
                use_container_width=True
            ):

                if username.strip() and password.strip():

                    st.session_state.logged_in = True
                    st.session_state.username = username.strip()

                    st.rerun()

                else:

                    st.warning(
                        "Please enter your username and password."
                    )

        st.caption(
            "By continuing, you agree to the NexaGen experience."
        )

    st.stop()


# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    st.markdown(
        "## Nexa<span style='color:#9b6cff;'>Gen</span> ✦",
        unsafe_allow_html=True
    )

    st.caption(
        "YOUR DAILY DIGITAL ESCAPE"
    )

    st.divider()

    navigation = [
        ("⌂", "Home"),
        ("◉", "Explore"),
        ("◌", "Moments"),
        ("▱", "Stories"),
        ("▣", "Books"),
        ("◇", "Games"),
        ("♫", "Vibes"),
        ("☻", "Fun")
    ]

    for icon, name in navigation:

        if st.button(
            icon + "   " + name,
            use_container_width=True,
            key="nav_" + name
        ):

            st.session_state.page = name
            st.rerun()

    st.divider()

    if st.button(
        "♡   Saved",
        use_container_width=True
    ):

        st.session_state.page = "Saved"
        st.rerun()

    if st.button(
        "♙   Profile",
        use_container_width=True
    ):

        st.session_state.page = "Profile"
        st.rerun()

    st.divider()

    st.caption("NexaGen • 2026")


# =========================================================
# HOME
# =========================================================

if st.session_state.page == "Home":

    st.markdown(
        "### GOOD TO SEE YOU"
    )

    st.title(
        "Your world. Your vibe. ✨"
    )

    st.write(
        "Discover stories, books, games, music, "
        "moments and little things that make "
        "your day more interesting."
    )

    st.divider()

    # -----------------------------------------------------
    # MOMENTS
    # -----------------------------------------------------

    st.subheader("Your Moments")

    stories = [
        ("🌙", "Night"),
        ("🎧", "Music"),
        ("🌸", "Dreams"),
        ("🎬", "Movies"),
        ("🍿", "Fun"),
        ("🚀", "Space"),
        ("🎨", "Art")
    ]

    cols = st.columns(7)

    for i, story in enumerate(stories):

        icon = story[0]
        name = story[1]

        with cols[i]:

            st.markdown(
                f"<div style='text-align:center;font-size:32px;'>"
                f"{icon}"
                f"</div>",
                unsafe_allow_html=True
            )

            st.markdown(
                f"<div style='text-align:center;color:#9299b0;'>"
                f"{name}"
                f"</div>",
                unsafe_allow_html=True
            )

            if st.button(
                "Open",
                key="home_story_" + name,
                use_container_width=True
            ):

                st.session_state.page = "Moments"
                st.rerun()

    st.divider()

    # -----------------------------------------------------
    # EXPLORE YOUR MOOD
    # -----------------------------------------------------

    st.subheader("Explore your mood")

    categories = [
        ("📖", "Stories", "Stories"),
        ("📚", "Books", "Books"),
        ("🎮", "Games", "Games"),
        ("🎵", "Music", "Vibes")
    ]

    cols = st.columns(4)

    for i, category in enumerate(categories):

        icon = category[0]
        title = category[1]
        page = category[2]

        with cols[i]:

            with st.container(border=True):

                st.markdown(
                    f"<div style='font-size:32px;'>{icon}</div>",
                    unsafe_allow_html=True
                )

                st.subheader(title)

                st.caption(
                    "Tap to discover something new."
                )

                if st.button(
                    "Explore →",
                    key="category_" + title,
                    use_container_width=True
                ):

                    st.session_state.page = page
                    st.rerun()

    st.divider()

    # -----------------------------------------------------
    # TRENDING
    # -----------------------------------------------------

    st.subheader("🔥 Trending now")

    feed_items = [
        (
            "🌌",
            "Midnight Stories",
            "A mysterious story collection everyone is talking about."
        ),
        (
            "🎮",
            "Quick Games",
            "Five-minute games for when you have nothing to do."
        ),
        (
            "💜",
            "Main Character Energy",
            "A collection of playlists, stories and mood ideas."
        )
    ]

    for icon, title, description in feed_items:

        with st.container(border=True):

            st.markdown(
                f"### {icon} {title}"
            )

            st.write(description)


# =========================================================
# EXPLORE
# =========================================================

elif st.session_state.page == "Explore":

    st.title("Explore")

    search = st.text_input(
        "Search",
        placeholder="Search stories, books, games..."
    )

    st.subheader("Popular categories")

    items = [
        ("📖", "Mystery Stories"),
        ("🧙", "Fantasy Worlds"),
        ("🚀", "Space Adventures"),
        ("💗", "Feel-Good Stories"),
        ("👻", "Spooky Nights"),
        ("😂", "Comedy"),
        ("🎨", "Creative Corner"),
        ("🎮", "Arcade")
    ]

    if search.strip():

        items = [
            item
            for item in items
            if search.lower() in item[1].lower()
        ]

    cols = st.columns(4)

    for i, item in enumerate(items):

        icon = item[0]
        title = item[1]

        with cols[i % 4]:

            with st.container(border=True):

                st.markdown(
                    f"<div style='font-size:32px;'>{icon}</div>",
                    unsafe_allow_html=True
                )

                st.subheader(title)

                if st.button(
                    "Open",
                    key="explore_" + title,
                    use_container_width=True
                ):

                    st.success(
                        "Opening " + title + " ✨"
                    )


# =========================================================
# MOMENTS
# =========================================================

elif st.session_state.page == "Moments":

    st.title("Moments")

    st.write(
        "Small stories. Big moods."
    )

    moments = [
        (
            "🌅",
            "Golden Hour",
            "Sometimes the best part of the day is simply looking at the sky."
        ),
        (
            "🌧️",
            "Rainy Windows",
            "Headphones on. Rain outside. Everything suddenly feels like a movie."
        ),
        (
            "🌃",
            "After Midnight",
            "The city feels different when almost everyone else is asleep."
        ),
        (
            "🌊",
            "Ocean Mood",
            "Some days don't need answers. They just need waves."
        )
    ]

    for icon, title, description in moments:

        with st.container(border=True):

            st.subheader(
                f"{icon} {title}"
            )

            st.write(description)

            col1, col2 = st.columns(2)

            with col1:

                if st.button(
                    "♡ Like",
                    key="like_" + title,
                    use_container_width=True
                ):

                    st.session_state.likes.add(title)

            with col2:

                if st.button(
                    "🔖 Save",
                    key="save_" + title,
                    use_container_width=True
                ):

                    st.session_state.saved.add(title)

                    st.success("Saved!")


# =========================================================
# STORIES
# =========================================================

elif st.session_state.page == "Stories":

    st.title("Story Universe")

    st.write(
        "Choose a story. Enter another world."
    )

    stories = [
        (
            "🌙",
            "The Girl Who Collected Moonlight",
            "Fantasy",
            "Mira discovered that moonlight could be stored in tiny glass bottles."
        ),
        (
            "🔑",
            "The Door at 3:17",
            "Mystery",
            "Every morning at exactly 3:17, a door appeared where no door had existed before."
        ),
        (
            "🚀",
            "Seven Minutes",
            "Adventure",
            "The spacecraft had seven minutes left when the unknown signal appeared."
        ),
        (
            "💌",
            "The Last Letter",
            "Drama",
            "One anonymous letter arrived with a message meant only for her."
        )
    ]

    for icon, title, genre, description in stories:

        with st.container(border=True):

            st.caption(
                genre.upper()
            )

            st.subheader(
                f"{icon} {title}"
            )

            st.write(description)

            if st.button(
                "Read now →",
                key="read_" + title
            ):

                st.markdown(
                    f"### {title}"
                )

                st.write(
                    description +
                    " The story continues from here..."
                )


# =========================================================
# BOOKS
# =========================================================

elif st.session_state.page == "Books":

    st.title("The Book Shelf")

    st.write(
        "Find your next favourite world."
    )

    books = [
        (
            "🧙",
            "Fantasy",
            "Magic, mythical worlds and unforgettable adventures."
        ),
        (
            "🔍",
            "Mystery",
            "Secrets, clues and stories full of twists."
        ),
        (
            "🚀",
            "Science Fiction",
            "Future worlds, space journeys and impossible technology."
        ),
        (
            "💗",
            "Romance",
            "Friendship, emotions and unexpected connections."
        ),
        (
            "👻",
            "Thriller",
            "Suspenseful stories for late-night reading."
        ),
        (
            "🌎",
            "Adventure",
            "Travel, discovery and characters who refuse to stay home."
        )
    ]

    cols = st.columns(3)

    for i, book in enumerate(books):

        icon = book[0]
        title = book[1]
        description = book[2]

        with cols[i % 3]:

            with st.container(border=True):

                st.markdown(
                    f"<div style='font-size:38px;'>{icon}</div>",
                    unsafe_allow_html=True
                )

                st.subheader(title)

                st.caption(description)

                if st.button(
                    "Open collection",
                    key="book_" + title,
                    use_container_width=True
                ):

                    st.success(
                        "Welcome to the "
                        + title
                        + " collection 📚"
                    )


# =========================================================
# GAMES
# =========================================================

elif st.session_state.page == "Games":

    st.title("Game Zone")

    st.write(
        "Quick games. No downloads."
    )

    st.subheader("🎯 Guess the Number")

    if "secret_number" not in st.session_state:

        st.session_state.secret_number = random.randint(
            1,
            10
        )

    guess = st.number_input(
        "Pick a number between 1 and 10",
        min_value=1,
        max_value=10,
        value=5,
        step=1
    )

    if st.button("Check"):

        if guess == st.session_state.secret_number:

            st.success(
                "🎉 You got it!"
            )

            st.session_state.points += 25

            st.session_state.secret_number = random.randint(
                1,
                10
            )

        elif guess < st.session_state.secret_number:

            st.warning(
                "Try higher ↑"
            )

        else:

            st.warning(
                "Try lower ↓"
            )

    st.divider()

    st.subheader("🎲 Would You Rather?")

    question = random.choice([
        "Fly anywhere ✈️ or breathe underwater 🌊?",
        "Unlimited books 📚 or unlimited movies 🎬?",
        "Live in space 🚀 or explore the ocean 🌊?",
        "Never use social media 📱 or never play games 🎮?"
    ])

    with st.container(border=True):

        st.markdown(
            f"### {question}"
        )

    col1, col2 = st.columns(2)

    with col1:

        st.button(
            "Option A",
            key="option_a",
            use_container_width=True
        )

    with col2:

        st.button(
            "Option B",
            key="option_b",
            use_container_width=True
        )


# =========================================================
# VIBES
# =========================================================

elif st.session_state.page == "Vibes":

    st.title("Vibes")

    st.write(
        "Choose the mood you're feeling."
    )

    vibes = [
        (
            "🌙",
            "Late Night",
            "Dreamy • quiet • mysterious"
        ),
        (
            "☀️",
            "Happy Day",
            "Bright • energetic • cheerful"
        ),
        (
            "🌧️",
            "Rainy Mood",
            "Cozy • calm • peaceful"
        ),
        (
            "🔥",
            "Main Character",
            "Bold • confident • unstoppable"
        )
    ]

    cols = st.columns(2)

    for i, vibe in enumerate(vibes):

        icon = vibe[0]
        title = vibe[1]
        description = vibe[2]

        with cols[i % 2]:

            with st.container(border=True):

                st.markdown(
                    f"<div style='font-size:38px;'>{icon}</div>",
                    unsafe_allow_html=True
                )

                st.subheader(title)

                st.caption(description)

                if st.button(
                    "Set my vibe",
                    key="vibe_" + title,
                    use_container_width=True
                ):

                    st.success(
                        "Your vibe: " + title
                    )


# =========================================================
# FUN
# =========================================================

elif st.session_state.page == "Fun":

    st.title("Fun Room")

    st.write(
        "For absolutely no serious reason. 😂"
    )

    if st.button(
        "😂 Make me laugh"
    ):

        joke = random.choice([
            "I told my room I'd clean it tomorrow. My room has heard this before. 😂",
            "My attention span just left the chat. 👋",
            "I opened my phone to check one thing. Two hours later... 😭",
            "Me: I'll sleep early tonight. Also me at 2 AM: one more video."
        ])

        st.success(joke)

    st.divider()

    st.subheader(
        "💭 Random Question"
    )

    question = random.choice([
        "If you could live inside any movie, which one?",
        "What would your useless superpower be?",
        "If your life had a theme song, what would it sound like?",
        "Which fictional character would be your best friend?"
    ])

    st.info(question)


# =========================================================
# SAVED
# =========================================================

elif st.session_state.page == "Saved":

    st.title("♡ Saved")

    if len(st.session_state.saved) == 0:

        st.info(
            "Nothing saved yet. Explore NexaGen "
            "and save things you love."
        )

    else:

        for item in sorted(st.session_state.saved):

            with st.container(border=True):

                st.subheader(
                    "🔖 " + item
                )


# =========================================================
# PROFILE
# =========================================================

elif st.session_state.page == "Profile":

    username = st.session_state.get(
        "username",
        "Explorer"
    )

    st.title("Your Profile")

    with st.container(border=True):

        st.caption(
            "NEXAGEN MEMBER"
        )

        st.header(
            f"Hey, {username}! ✨"
        )

        st.write(
            "Keep exploring. Your next favourite "
            "thing might be one tap away."
        )

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(
            "✨ Points",
            st.session_state.points
        )

    with col2:

        st.metric(
            "❤️ Liked",
            len(st.session_state.likes)
        )

    with col3:

        st.metric(
            "🔖 Saved",
            len(st.session_state.saved)
        )

    st.divider()

    st.subheader(
        "🏆 Your badges"
    )

    st.write(
        "✨ Curious Explorer"
    )

    st.write(
        "📚 Story Lover"
    )

    st.write(
        "🎮 Game Starter"
    )

    st.write(
        "💜 NexaGen Member"
    )


# =========================================================
# FOOTER
# =========================================================

st.divider()

st.caption(
    "✦ NexaGen — Discover something new every day."
)