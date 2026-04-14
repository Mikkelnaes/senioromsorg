import streamlit as st

st.set_page_config(page_title="SENIOR OMSORG", layout="wide")

if "page" not in st.session_state:
    st.session_state.page = "tjenester"
page = st.session_state.page

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Barlow:wght@300;400;500;600&display=swap');

    html, body, [class*="css"] {
        font-family: 'Barlow', sans-serif;
        color: #524c4c;
        background-color: #DFD0C1;
    }

    .stApp {
        background-color: #DFD0C1;
    }

.block-container {
        padding-top: 0 !important;
    }

    /* ── Top nav bar (Streamlit columns) ── */
    [data-testid="stHorizontalBlock"]:first-of-type {
        background-color: #333333;
        padding: 0 2rem !important;
        margin-top: 0;
        align-items: center;
        min-height: 64px;
    }
    [data-testid="stHorizontalBlock"]:first-of-type > div {
        display: flex;
        align-items: center;
        min-height: 64px;
    }
    .logo-wrap {
        display: flex;
        align-items: center;
        gap: 0.7rem;
    }
    .logo-text {
        font-size: 1.1rem;
        font-weight: 700;
        line-height: 1.15;
        color: #C4745A;
        text-transform: uppercase;
        letter-spacing: 0.06em;
    }
    /* Nav buttons inside the bar */
    [data-testid="stHorizontalBlock"]:first-of-type .stButton > button {
        background: transparent !important;
        color: #C7B6A5 !important;
        border: none !important;
        box-shadow: none !important;
        font-size: 0.88rem !important;
        font-weight: 500 !important;
        letter-spacing: 0.1em !important;
        text-transform: uppercase !important;
        padding: 0 !important;
        width: 100% !important;
        height: 64px !important;
        border-radius: 0 !important;
        transition: color 0.2s !important;
    }
    [data-testid="stHorizontalBlock"]:first-of-type .stButton > button:hover {
        color: #fff !important;
        background: transparent !important;
    }

    /* ── Hero ── */
    .hero {
        background-color: #524c4c;
        color: #fff;
        padding: 7rem 2rem 5rem;
        text-align: center;
        width: 100%;
        margin-bottom: 2.5rem;
        margin-top: 2rem;
    }
    .hero h1 {
        font-size: 2.8rem;
        font-weight: 300;
        letter-spacing: 0.12em;
        color: #fff;
        margin-bottom: 0.6rem;
    }
    .hero p {
        font-size: 1.1rem;
        color: #C7B6A5;
        font-weight: 400;
        max-width: 620px;
        margin: 0 auto;
    }

    /* ── Headings ── */
    h2 {
        color: #b28559;
        font-weight: 300;
        font-size: 1.8rem;
        letter-spacing: 0.05em;
        border-bottom: 1px solid #C7B6A5;
        padding-bottom: 0.5rem;
        margin-bottom: 1.5rem;
    }
    h3, h4 { color: #c9a37b; font-weight: 500; }

    /* ── Service card ── */
    .service-card {
        background: #FCFCFC;
        padding: 1.8rem;
        margin: 1rem 0;
        border-radius: 6px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.08);
    }
    .service-card h4 {
        font-size: 1.2rem;
        color: #b28559;
        margin-top: 0;
        margin-bottom: 0.4rem;
    }
    .service-card .badge {
        display: inline-block;
        background: #e2d0bf;
        color: #524c4c;
        font-size: 0.78rem;
        padding: 0.2rem 0.7rem;
        border-radius: 20px;
        margin-bottom: 0.8rem;
        font-weight: 500;
        letter-spacing: 0.05em;
    }
    .service-card p {
        color: #524c4c;
        font-size: 0.97rem;
        text-align: justify;
        margin: 0;
        line-height: 1.7;
    }

    /* ── Person card ── */
    .person-card {
        background: #FCFCFC;
        border-radius: 8px;
        box-shadow: 0 2px 10px rgba(0,0,0,0.09);
        overflow: hidden;
        text-align: center;
    }
    .person-card .person-photo-placeholder {
        width: 100%;
        height: 280px;
        background: linear-gradient(135deg, #C4745A 0%, #8B3A22 100%);
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 5rem;
        color: #fff;
        font-weight: 300;
        letter-spacing: 0.05em;
    }
    .person-card .person-info { padding: 1.5rem 1.8rem 2rem; }
    .person-card h3 {
        font-size: 1.5rem;
        color: #b28559;
        font-weight: 500;
        margin: 0 0 0.3rem 0;
    }
    .person-card .person-title {
        font-size: 0.85rem;
        text-transform: uppercase;
        letter-spacing: 0.1em;
        color: #C7B6A5;
        margin-bottom: 1rem;
        font-weight: 500;
    }
    .person-card p {
        color: #524c4c;
        font-size: 0.97rem;
        line-height: 1.75;
        text-align: justify;
        margin: 0;
    }

    /* ── Team intro ── */
    .team-intro {
        background: #FCFCFC;
        border-radius: 6px;
        padding: 2rem 2.5rem;
        margin-bottom: 2.5rem;
        text-align: center;
        box-shadow: 0 2px 8px rgba(0,0,0,0.07);
    }
    .team-intro h2 { border: none; margin-bottom: 0.8rem; }
    .team-intro p {
        color: #524c4c;
        font-size: 1.05rem;
        line-height: 1.8;
        max-width: 640px;
        margin: 0 auto;
    }

    /* ── Buttons ── */
    .stButton > button {
        background-color: #333333 !important;
        color: #fff !important;
        border: none !important;
        border-radius: 4px !important;
        padding: 0.5rem 1.5rem !important;
        font-family: 'Barlow', sans-serif !important;
        font-weight: 500 !important;
        letter-spacing: 0.08em !important;
        text-transform: uppercase !important;
        transition: background 0.25s !important;
    }
    .stButton > button:hover { background-color: #51565c !important; }

    /* ── Input fields ── */
    .stTextInput input, .stTextArea textarea {
        border: 1px solid #C7B6A5 !important;
        border-radius: 4px !important;
        background: #FCFCFC !important;
        font-family: 'Barlow', sans-serif !important;
    }

    /* ── Booking box ── */
    .booking-box {
        background: #FCFCFC;
        border-left: 4px solid #b28559;
        padding: 1.5rem 2rem;
        border-radius: 4px;
        margin-top: 1rem;
        line-height: 1.8;
    }

    /* ── Info box ── */
    .info-box {
        background: #FCFCFC;
        border-radius: 6px;
        padding: 1.5rem 2rem;
        margin-bottom: 1.5rem;
        font-size: 0.97rem;
        line-height: 1.7;
        color: #524c4c;
    }
    .info-box strong { color: #b28559; }

    /* ── Footer ── */
    .footer {
        background-color: #e2d0bf;
        text-align: center;
        padding: 2rem;
        margin-top: 3rem;
        font-size: 0.85rem;
        color: #524c4c;
        border-top: 1px solid #C7B6A5;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ── Top navigation bar ───────────────────────────────────────
st.markdown("<br><br>", unsafe_allow_html=True)
c_logo, c_space, c_t, c_h = st.columns([3, 3, 1.5, 1.5])

with c_logo:
    st.markdown(
        """
        <div class="logo-wrap">
            <svg width="42" height="38" viewBox="0 0 42 38" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M21 35 C21 35 3 23 3 12 C3 6.48 7.48 2 13 2 C16.5 2 19.6 3.8 21 6.5 C22.4 3.8 25.5 2 29 2 C34.52 2 39 6.48 39 12 C39 23 21 35 21 35 Z"
                      stroke="#C4745A" stroke-width="2.5" fill="none" stroke-linejoin="round" stroke-linecap="round"/>
            </svg>
            <span class="logo-text">Senior<br>omsorg</span>
        </div>
        """,
        unsafe_allow_html=True,
    )

with c_t:
    if st.button("Våre tjenester", key="nav_tjenester"):
        st.session_state.page = "tjenester"
        if "selected_service" in st.session_state:
            del st.session_state.selected_service
        st.rerun()

with c_h:
    if st.button("Hvem er vi", key="nav_hvem"):
        st.session_state.page = "hvem"
        st.rerun()

# ── Hero ─────────────────────────────────────────────────────
if page == "tjenester":
    st.markdown(
        """
        <div class="hero">
            <h1>SENIOR OMSORG</h1>
            <p>Besøksvenn, sykepleietjenester og døgnomsorg – trygghet og glede i hverdagen</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
else:
    st.markdown(
        """
        <div class="hero">
            <h1>Hvem er vi</h1>
            <p>Vi jobber fra hjertet – mennesker trenger mennesker</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

# ============================================================
# PAGE: TJENESTER
# ============================================================
if page == "tjenester":
    services = [
        {
            "name": "Besøksvenn",
            "badge": "Sosial omsorg",
            "description": (
                "Vi tilbyr rask og pålitelig besøksvenntjeneste som gir sosial stimulering og avlastning for pårørende. "
                "Aktivitetene tilpasses den enkeltes ønsker og gjennomføres hjemme, på omsorgsbolig eller sykehjem. "
                "En besøksvenn gir trygghet, glede og meningsfull samvær i hverdagen."
            ),
        },
        {
            "name": "Handling",
            "badge": "Ærender og innkjøp",
            "description": (
                "Vi tar hånd om dagligvarehandel og andre ærender for deg – raskt, pålitelig og tilpasset dine ønsker. "
                "Du slipper å stresse med transport eller tunge bæreposer. "
                "Vi handler det du trenger, når du trenger det."
            ),
        },
        {
            "name": "Rydding eller fiksing hjemme hos deg",
            "badge": "Praktisk hjelp",
            "description": (
                "Vi hjelper deg med rydding, lettere rengjøring og småjobber i hjemmet. "
                "Enten det er et rom som trenger orden, en lampe som skal skiftes eller noe som må fikses – "
                "vi stiller opp med praktisk hjelp slik at du kan trives godt hjemme."
            ),
        },
        {
            "name": "Reiseledsager",
            "badge": "Omsorg på reise",
            "description": (
                "Vi tilbyr omsorgsfull ledsagelse under familieutflukter, helgeturer og spesielle anledninger. "
                "Din pårørende deltar fullt ut i fellesskapet, med trygg avlastning og verdig selskap hele veien. "
                "Vi sikrer at alle kan delta – uansett behov."
            ),
        },
    ]

    if "selected_service" not in st.session_state:
        st.markdown("## Våre tjenester")
        st.markdown(
            """
            <div class="info-box">
                <strong>Trygghet og glede</strong> – Vi matcher deg med riktig omsorgsperson basert på dine behov,
                ønsker og personlighet. Alle konsultasjoner er gratis og uforpliktende.
                Typisk ventetid er <strong>1–4 uker</strong> avhengig av område og tjenestetype.
            </div>
            """,
            unsafe_allow_html=True,
        )
        for service in services:
            st.markdown(
                f"""
                <div class="service-card">
                    <h4>{service['name']}</h4>
                    <span class="badge">{service['badge']}</span>
                    <p>{service['description']}</p>
                </div>
                """,
                unsafe_allow_html=True,
            )
            if st.button(f"Bestill {service['name']}", key=service["name"]):
                st.session_state.selected_service = service["name"]
                st.rerun()

    if "selected_service" in st.session_state:
        st.markdown("## Ta kontakt")
        st.markdown(
            f"<p>Du har valgt <strong style='color:#b28559'>{st.session_state.selected_service}</strong>. "
            "Fyll inn opplysningene nedenfor, så tar vi kontakt for en gratis samtale.</p>",
            unsafe_allow_html=True,
        )
        name = st.text_input("Navn", key="name_input")
        phone = st.text_input("Telefonnummer", key="phone_input")
        message = st.text_area("Beskriv behovet kort (valgfritt)", key="message_input", height=120)

        if not name or not phone:
            st.warning("Vennligst fyll inn navn og telefonnummer for å sende henvendelsen.")
            st.stop()

        st.markdown(
            f"""
            <div class="booking-box">
                <h4 style="margin-top:0; color:#b28559">Oppsummering</h4>
                <p><strong>Navn:</strong> {name}</p>
                <p><strong>Telefon:</strong> {phone}</p>
                <p><strong>Tjeneste:</strong> {st.session_state.selected_service}</p>
                {"<p><strong>Melding:</strong> " + message + "</p>" if message else ""}
            </div>
            """,
            unsafe_allow_html=True,
        )
        col1, col2 = st.columns([1, 3])
        with col1:
            if st.button("Send henvendelse"):
                st.success(f"Takk, {name}! Vi tar kontakt med deg innen kort tid.")
        with col2:
            if st.button("Velg en annen tjeneste"):
                del st.session_state.selected_service
                st.rerun()

# ============================================================
# PAGE: HVEM ER VI
# ============================================================
elif page == "hvem":
    st.markdown(
        """
        <div class="team-intro">
            <h2>Omsorg er en jobb vi er glad i</h2>
            <p>
                Vi jobber fra hjertet. For oss handler omsorg om ekte menneskelig kontakt –
                å se den enkelte, lytte, og gjøre en reell forskjell i hverdagen.
                Mennesker trenger mennesker, og vi er her for deg og dine.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    col1, col2 = st.columns(2, gap="large")

    with col1:
        st.markdown(
            """
            <div class="person-card">
                <div class="person-photo-placeholder">M</div>
                <div class="person-info">
                    <h3>Mathias</h3>
                    <div class="person-title">Grunnlegger & Daglig leder</div>
                    <p>
                        Mathias har alltid hatt et brennende engasjement for mennesker i sårbare situasjoner.
                        Med bakgrunn fra helsefag og flere år i frivillig omsorgsarbeid, startet han SENIOR OMSORG
                        ut fra en enkel overbevisning: alle fortjener omsorg tilpasset akkurat dem.
                        Han leder teamet med varme, tydelig retning og et ekte ønske om å gjøre hverdagen
                        bedre for både brukere og pårørende.
                    </p>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col2:
        st.markdown(
            """
            <div class="person-card">
                <div class="person-photo-placeholder">M</div>
                <div class="person-info">
                    <h3>Mikkel</h3>
                    <div class="person-title">Fagansvarlig & Besøksvenn</div>
                    <p>
                        Mikkel er hjørnesteinen i det faglige arbeidet hos SENIOR OMSORG. Med utdanning innen
                        sykepleie og en naturlig evne til å skape trygghet, sørger han for at alle tjenester
                        holder høyeste standard. Han er selv aktiv besøksvenn og kjenner jobben innenfra –
                        det lille ekstra som gjør en stor forskjell for den som trenger det mest.
                    </p>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown(
        """
        <div style="text-align:center; margin-top:2.5rem; color:#C4745A; font-size:1.1rem;
                    font-weight:300; letter-spacing:0.05em;">
            Vi jobber fra hjertet &nbsp;·&nbsp; Mennesker trenger mennesker
        </div>
        """,
        unsafe_allow_html=True,
    )

# ── Footer ───────────────────────────────────────────────────
st.markdown(
    """
    <div class="footer">
        © 2026 SENIOR OMSORG &nbsp;|&nbsp; Besøksvenn · Handling · Rydding eller fiksing hjemme hos deg · Reiseledsager<br>
        Oslo og Akershus &nbsp;|&nbsp; Gratis og uforpliktende samtale
    </div>
    """,
    unsafe_allow_html=True,
)
