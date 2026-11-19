
import streamlit as st
from datetime import datetime

# ==========================================================
# PAGE CONFIG
# ==========================================================

st.set_page_config(
    page_title="ReCircle | Marketplace",
    page_icon="♻️",
    layout="wide"
)

# ==========================================================
# CSS DESIGN
# ==========================================================

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Manrope:wght@600;700;800&display=swap');

.stApp {
    background-color: #F8F6FF;
    color: #302943;
    font-family: 'DM Sans', sans-serif;
}

.block-container {
    max-width: 1250px;
    padding-top: 1.5rem;
    padding-bottom: 3rem;
}

h1, h2, h3 {
    font-family: 'Manrope', sans-serif !important;
    color: #302943 !important;
}

p, label {
    color: #49415E;
}

[data-testid="stWidgetLabel"] p {
    color: #39314F !important;
    font-weight: 600 !important;
}

.stTextInput input,
.stTextArea textarea,
.stNumberInput input {
    background: #FFFFFF !important;
    color: #302943 !important;
    border: 1px solid #DCD4F0 !important;
    border-radius: 12px !important;
}

.stTextInput input::placeholder,
.stTextArea textarea::placeholder {
    color: #89819D !important;
}

.stSelectbox div[data-baseweb="select"] > div {
    background: white !important;
    color: #302943 !important;
    border-radius: 12px !important;
}

.stButton button,
.stFormSubmitButton button {
    border-radius: 12px !important;
    min-height: 43px;
    font-weight: 700 !important;
}

.stButton button[kind="primary"],
.stFormSubmitButton button[kind="primary"] {
    background: #7355DB !important;
    color: white !important;
    border: none !important;
}

.stButton button[kind="primary"]:hover {
    background: #5D41C4 !important;
}

.stButton button[kind="secondary"] {
    background: white !important;
    color: #6249BC !important;
    border: 1px solid #D8CFF2 !important;
}

.stButton button[kind="secondary"]:hover {
    background: #F0EAFF !important;
}

[data-testid="stFileUploader"] {
    background: white;
    border: 1px dashed #B9A9E8;
    border-radius: 15px;
    padding: 10px;
}

[data-testid="stFileUploader"] section {
    background: #F8F5FF !important;
}

[data-testid="stImage"] img {
    border-radius: 14px;
}

div[data-testid="stVerticalBlockBorderWrapper"] {
    background: #FFFFFF;
    border-radius: 18px;
    border-color: #E8E2F4 !important;
}

[data-testid="stMetric"] {
    background: white;
    padding: 15px;
    border: 1px solid #EAE4F5;
    border-radius: 15px;
}

[data-testid="stMetricLabel"] {
    color: #716786 !important;
}

[data-testid="stMetricValue"] {
    color: #7355DB !important;
}

hr {
    border-color: #E7E0F3 !important;
}

footer {
    visibility: hidden;
}

@media (max-width: 768px) {
    .block-container {
        padding-left: 1rem;
        padding-right: 1rem;
    }
}
</style>
""", unsafe_allow_html=True)


# ==========================================================
# CATEGORIES
# ==========================================================

categories = [
    "All Items",
    "Electronics",
    "Furniture",
    "Clothing",
    "Home & Kitchen",
    "Books",
    "Vehicles & Spares",
    "Tools",
    "Agriculture",
    "Medical",
    "Sports",
    "Construction",
    "Other"
]

category_icons = {
    "Electronics": "📱",
    "Furniture": "🪑",
    "Clothing": "👕",
    "Home & Kitchen": "🍳",
    "Books": "📚",
    "Vehicles & Spares": "🚲",
    "Tools": "🔧",
    "Agriculture": "🌱",
    "Medical": "🩺",
    "Sports": "⚽",
    "Construction": "🧱",
    "Other": "📦"
}


# ==========================================================
# DEMO LISTINGS
# ==========================================================

demo_items = [
    {
        "name": "Wooden Study Chair",
        "category": "Furniture",
        "description": "Strong wooden chair. Comfortable for studying and working.",
        "condition": "Good",
        "price": 850,
        "seller": "Rahul",
        "location": "BTM Layout, Bengaluru",
        "contact": "demo@example.com",
        "image": None,
        "demo": True,
        "emoji": "🪑"
    },
    {
        "name": "Wireless Headphones",
        "category": "Electronics",
        "description": "Wireless headphones with good sound quality. Barely used.",
        "condition": "Like New",
        "price": 1200,
        "seller": "Ananya",
        "location": "Jayanagar, Bengaluru",
        "contact": "demo@example.com",
        "image": None,
        "demo": True,
        "emoji": "🎧"
    },
    {
        "name": "Engineering Textbooks",
        "category": "Books",
        "description": "Engineering textbooks. Useful for college students.",
        "condition": "Good",
        "price": 450,
        "seller": "Kiran",
        "location": "Electronic City, Bengaluru",
        "contact": "demo@example.com",
        "image": None,
        "demo": True,
        "emoji": "📚"
    },
    {
        "name": "Study Table",
        "category": "Furniture",
        "description": "Compact wooden study table with spacious surface.",
        "condition": "Good",
        "price": 1500,
        "seller": "Sneha",
        "location": "Koramangala, Bengaluru",
        "contact": "demo@example.com",
        "image": None,
        "demo": True,
        "emoji": "🪵"
    },
    {
        "name": "City Bicycle",
        "category": "Vehicles & Spares",
        "description": "Everyday bicycle. Suitable for short commutes.",
        "condition": "Fair",
        "price": 2800,
        "seller": "Arjun",
        "location": "HSR Layout, Bengaluru",
        "contact": "demo@example.com",
        "image": None,
        "demo": True,
        "emoji": "🚲"
    },
    {
        "name": "Induction Cooktop",
        "category": "Home & Kitchen",
        "description": "Working induction cooktop. Great for hostel or home.",
        "condition": "Like New",
        "price": 900,
        "seller": "Meera",
        "location": "Marathahalli, Bengaluru",
        "contact": "demo@example.com",
        "image": None,
        "demo": True,
        "emoji": "🍳"
    },
    {
        "name": "School Backpack",
        "category": "Clothing",
        "description": "Spacious backpack with multiple compartments.",
        "condition": "Good",
        "price": 350,
        "seller": "Pooja",
        "location": "Banashankari, Bengaluru",
        "contact": "demo@example.com",
        "image": None,
        "demo": True,
        "emoji": "🎒"
    },
    {
        "name": "Table Lamp",
        "category": "Home & Kitchen",
        "description": "LED desk lamp for reading and studying.",
        "condition": "Like New",
        "price": 400,
        "seller": "Vivek",
        "location": "Whitefield, Bengaluru",
        "contact": "demo@example.com",
        "image": None,
        "demo": True,
        "emoji": "💡"
    },
    {
        "name": "Cricket Bat",
        "category": "Sports",
        "description": "Good quality cricket bat for practice and matches.",
        "condition": "Good",
        "price": 700,
        "seller": "Akhil",
        "location": "Rajajinagar, Bengaluru",
        "contact": "demo@example.com",
        "image": None,
        "demo": True,
        "emoji": "🏏"
    },
    {
        "name": "Tool Kit",
        "category": "Tools",
        "description": "Basic home repair toolkit with useful tools.",
        "condition": "Good",
        "price": 600,
        "seller": "Naveen",
        "location": "Yelahanka, Bengaluru",
        "contact": "demo@example.com",
        "image": None,
        "demo": True,
        "emoji": "🧰"
    },
    {
        "name": "Office Monitor",
        "category": "Electronics",
        "description": "Monitor suitable for office work and study setup.",
        "condition": "Fair",
        "price": 3200,
        "seller": "Divya",
        "location": "Indiranagar, Bengaluru",
        "contact": "demo@example.com",
        "image": None,
        "demo": True,
        "emoji": "🖥️"
    },
    {
        "name": "Flower Pots Set",
        "category": "Agriculture",
        "description": "Set of reusable pots for plants and gardening.",
        "condition": "Good",
        "price": 250,
        "seller": "Sanjay",
        "location": "Hebbal, Bengaluru",
        "contact": "demo@example.com",
        "image": None,
        "demo": True,
        "emoji": "🪴"
    }
]


# ==========================================================
# SESSION STATE
# ==========================================================

if "page" not in st.session_state:
    st.session_state["page"] = "home"

if "listings" not in st.session_state:
    st.session_state["listings"] = demo_items.copy()

if "search_query" not in st.session_state:
    st.session_state["search_query"] = ""

if "category_filter" not in st.session_state:
    st.session_state["category_filter"] = "All Items"


# ==========================================================
# NAVIGATION FUNCTIONS
# ==========================================================

def go_to(page):
    st.session_state["page"] = page


def search_item(query):
    st.session_state["search_query"] = query.strip()
    st.session_state["category_filter"] = "All Items"
    st.session_state["page"] = "buy"


# ==========================================================
# PRODUCT CARD
# ==========================================================

def product_card(item):

    with st.container(border=True):

        # Item image / placeholder
        if item.get("image") is not None:
            st.image(item["image"], use_container_width=True)
        else:
            emoji = item.get(
                "emoji",
                category_icons.get(item["category"], "📦")
            )

            st.markdown(
                f"<div style='background:#F0EAFF;height:175px;"
                f"border-radius:13px;display:flex;"
                f"align-items:center;justify-content:center;"
                f"font-size:75px;'>{emoji}</div>",
                unsafe_allow_html=True
            )

        if item.get("demo"):
            st.caption("🟣 DEMO LISTING")

        st.markdown(f"### {item['name']}")

        st.markdown(
            f"<h2 style='color:#7355DB;margin-top:0;'>"
            f"₹{item['price']:,}</h2>",
            unsafe_allow_html=True
        )

        st.caption(
            f"{item['category']} · {item['condition']}"
        )

        st.write(item["description"])

        st.markdown("---")

        st.caption(f"👤 {item['seller']}")

        if item.get("location"):
            st.caption(f"📍 {item['location']}")

        if item.get("contact"):
            st.caption(f"✉️ {item['contact']}")


# ==========================================================
# HEADER
# ==========================================================

left, middle, right = st.columns([2, 3, 2])

with left:
    st.markdown("## ♻️ ReCircle")

with middle:
    st.markdown(
        "<p style='text-align:center;padding-top:12px;"
        "color:#756A90;'>Give things a second life ✨</p>",
        unsafe_allow_html=True
    )

with right:
    nav_buy, nav_sell = st.columns(2)

    with nav_buy:
        if st.button("🛍️ Buy", use_container_width=True):
            st.session_state["search_query"] = ""
            st.session_state["category_filter"] = "All Items"
            go_to("buy")
            st.rerun()

    with nav_sell:
        if st.button("＋ Sell", use_container_width=True):
            go_to("sell")
            st.rerun()

st.divider()


# ==========================================================
# HOME
# ==========================================================

if st.session_state["page"] == "home":

    st.markdown(
        "<h1 style='font-size:44px;text-align:center;'>"
        "Buy what you need. "
        "<span style='color:#7355DB;'>Sell what you don't.</span>"
        "</h1>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<p style='font-size:18px;text-align:center;color:#655A80;'>"
        "Give useful things a second life. Discover affordable items "
        "from people around you.</p>",
        unsafe_allow_html=True
    )

    st.write("")

    # SEARCH
    with st.form("home_search"):

        search_col, search_button = st.columns([5, 1])

        with search_col:
            home_query = st.text_input(
                "Search",
                placeholder="Search chair, phone, books, table...",
                label_visibility="collapsed"
            )

        with search_button:
            submitted = st.form_submit_button(
                "🔍 Search",
                type="primary",
                use_container_width=True
            )

        if submitted:
            if home_query.strip():
                search_item(home_query)
                st.rerun()
            else:
                st.warning("Type an item to search.")

    st.write("")

    # BUY / SELL
    buy_col, sell_col = st.columns(2, gap="large")

    with buy_col:
        with st.container(border=True):
            st.markdown("### 🛍️ Find something you love")
            st.write("Explore pre-loved items at affordable prices.")
            st.markdown(
                "<p style='color:#7355DB;'>"
                "✨ Save money · Discover unique finds</p>",
                unsafe_allow_html=True
            )

            if st.button(
                "Explore items →",
                type="primary",
                key="home_buy",
                use_container_width=True
            ):
                st.session_state["search_query"] = ""
                st.session_state["category_filter"] = "All Items"
                go_to("buy")
                st.rerun()

    with sell_col:
        with st.container(border=True):
            st.markdown("### 💜 Give your items a new home")
            st.write("Sell things you no longer need and earn money.")
            st.markdown(
                "<p style='color:#E36B56;'>"
                "✨ Easy listing · Less waste</p>",
                unsafe_allow_html=True
            )

            if st.button(
                "Sell an item →",
                key="home_sell",
                use_container_width=True
            ):
                go_to("sell")
                st.rerun()

    st.write("")
    st.markdown("---")

    # BENEFITS
    st.markdown("### 🌈 A marketplace for almost everything")

    benefit1, benefit2, benefit3 = st.columns(3)

    with benefit1:
        st.markdown("### 💰")
        st.markdown("**Save money**")
        st.write("Buy useful things without spending too much.")

    with benefit2:
        st.markdown("### ♻️")
        st.markdown("**Reduce waste**")
        st.write("Give items another chance instead of throwing them.")

    with benefit3:
        st.markdown("### 🤝")
        st.markdown("**Reuse & reconnect**")
        st.write("Find items and connect with their owners.")

    st.write("")
    st.markdown("---")

    # DEMO ITEMS
    st.markdown("### ✨ Explore items")
    st.caption("Sample listings to demonstrate how ReCircle works.")

    items = st.session_state["listings"]
    recent = items[:6]

    cols = st.columns(3, gap="medium")

    for col, item in zip(cols, recent):
        with col:
            product_card(item)

    if st.button("View all items →", type="primary"):
        st.session_state["search_query"] = ""
        st.session_state["category_filter"] = "All Items"
        go_to("buy")
        st.rerun()


# ==========================================================
# BUY PAGE
# ==========================================================

elif st.session_state["page"] == "buy":

    st.markdown("# 🛍️ Find your next treasure")
    st.write("Discover affordable pre-loved items and give them a new home.")

    st.write("")

    # SEARCH
    with st.form("buy_search"):

        search_col, search_button = st.columns([5, 1])

        with search_col:
            buy_query = st.text_input(
                "Search items",
                value=st.session_state["search_query"],
                placeholder="Search chair, phone, books...",
                label_visibility="collapsed"
            )

        with search_button:
            buy_submit = st.form_submit_button(
                "Search",
                type="primary",
                use_container_width=True
            )

        if buy_submit:
            st.session_state["search_query"] = buy_query.strip()
            st.session_state["category_filter"] = "All Items"
            st.rerun()

    st.markdown("### Browse categories")

    selected_category = st.selectbox(
        "Category",
        categories,
        index=categories.index(st.session_state["category_filter"])
        if st.session_state["category_filter"] in categories else 0
    )

    st.session_state["category_filter"] = selected_category

    query = st.session_state["search_query"].lower().strip()

    all_items = st.session_state["listings"]

    filtered_items = []

    for item in all_items:

        matches_search = (
            not query
            or query in item["name"].lower()
            or query in item["description"].lower()
            or query in item["category"].lower()
        )

        matches_category = (
            selected_category == "All Items"
            or item["category"] == selected_category
        )

        if matches_search and matches_category:
            filtered_items.append(item)

    st.write("")

    if query:
        st.markdown(f"### Results for **{query}**")
    elif selected_category != "All Items":
        st.markdown(f"### {category_icons.get(selected_category, '📦')} {selected_category}")
    else:
        st.markdown("### All available items")

    st.caption(f"{len(filtered_items)} items found")

    if filtered_items:

        cols_per_row = 3

        for start in range(0, len(filtered_items), cols_per_row):

            row_items = filtered_items[start:start + cols_per_row]

            cols = st.columns(cols_per_row, gap="medium")

            for col, item in zip(cols, row_items):

                with col:
                    product_card(item)

    else:
        st.info("No matching items found. Try another search.")

        if st.button("Show all items"):
            st.session_state["search_query"] = ""
            st.session_state["category_filter"] = "All Items"
            st.rerun()

    st.write("")

    if st.button("← Back to Home"):
        go_to("home")
        st.rerun()


# ==========================================================
# SELL PAGE
# ==========================================================

elif st.session_state["page"] == "sell":

    st.markdown("# 💜 Sell an item")
    st.write("List something you no longer need. Someone else might love it!")

    st.write("")

    with st.container(border=True):

        with st.form("sell_form"):

            st.markdown("### Tell us about your item")

            item_name = st.text_input(
                "Item name *",
                placeholder="Example: Wooden study table"
            )

            item_category = st.selectbox(
                "Category *",
                categories[1:]
            )

            item_description = st.text_area(
                "Description",
                placeholder="Describe your item...",
                height=100
            )

            item_condition = st.selectbox(
                "Condition *",
                ["Like New", "Good", "Fair", "Needs Repair"]
            )

            item_price = st.number_input(
                "Selling price (₹) *",
                min_value=0,
                step=100
            )

            st.markdown("### 📷 Add item photo")

            item_image = st.file_uploader(
                "Upload a photo",
                type=["jpg", "jpeg", "png", "webp"]
            )

            if item_image:
                st.image(item_image, width=300)

            st.markdown("### Seller details")

            seller_name = st.text_input(
                "Your name *",
                placeholder="Enter your name"
            )

            seller_location = st.text_input(
                "Location",
                placeholder="City / Area"
            )

            seller_contact = st.text_input(
                "Contact information",
                placeholder="Phone number or email"
            )

            st.write("")

            publish = st.form_submit_button(
                "✨ Publish my listing",
                type="primary",
                use_container_width=True
            )

            if publish:

                if not item_name.strip():
                    st.error("Please enter an item name.")

                elif item_price <= 0:
                    st.error("Enter a valid selling price.")

                elif not seller_name.strip():
                    st.error("Please enter your name.")

                else:

                    new_item = {
                        "name": item_name.strip(),
                        "category": item_category,
                        "description": item_description.strip(),
                        "condition": item_condition,
                        "price": int(item_price),
                        "seller": seller_name.strip(),
                        "location": seller_location.strip(),
                        "contact": seller_contact.strip(),
                        "image": item_image.getvalue() if item_image else None,
                        "demo": False,
                        "emoji": category_icons.get(item_category, "📦"),
                        "date": datetime.now().strftime("%d-%m-%Y")
                    }

                    st.session_state["listings"].append(new_item)

                    st.success("🎉 Your item has been listed successfully!")
                    st.balloons()

                    st.session_state["search_query"] = ""
                    st.session_state["category_filter"] = "All Items"
                    st.session_state["page"] = "buy"

                    st.rerun()

    st.write("")

    if st.button("← Back to Home"):
        go_to("home")
        st.rerun()


# ==========================================================
# FOOTER
# ==========================================================

st.write("")
st.markdown("---")

footer1, footer2, footer3 = st.columns(3)

with footer1:
    st.markdown("### ♻️ ReCircle")
    st.caption("Give things a second life.")

with footer2:
    st.caption("Buy more consciously. Sell responsibly.")

with footer3:
    st.caption("A community built around reuse.")
