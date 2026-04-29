import streamlit as st
import base64
from pathlib import Path

st.set_page_config(page_title="Senior Omsorg", layout="wide", initial_sidebar_state="collapsed")


def get_img_base64(path):
    return base64.b64encode(Path(path).read_bytes()).decode()


_hero_img = get_img_base64(Path(__file__).parent.parent / "assets" / "hender.webp")

# ── Session state ────────────────────────────────────────────
if "page" not in st.session_state:
    st.session_state.page = "tjenester"
if "selected_service" not in st.session_state:
    st.session_state.selected_service = None
if "faq_open" not in st.session_state:
    st.session_state.faq_open = 0
if "form_when" not in st.session_state:
    st.session_state.form_when = "snarlig"
if "submitted" not in st.session_state:
    st.session_state.submitted = False


def goto(page, service=None):
    st.session_state.page = page
    if service is not None:
        st.session_state.selected_service = service
    st.session_state.submitted = False
    st.rerun()


# ── Data ─────────────────────────────────────────────────────
SERVICES = [
    {
        "id": "besoksvenn",
        "name": "Besøksvenn",
        "badge": "Sosial omsorg",
        "short": "Et menneske å dele dagen med.",
        "description": (
            "Vi tilbyr rask og pålitelig besøksvenntjeneste som gir sosial stimulering "
            "og avlastning for pårørende. Aktivitetene tilpasses den enkeltes ønsker "
            "og gjennomføres hjemme, på omsorgsbolig eller sykehjem. En besøksvenn gir "
            "trygghet, glede og meningsfull samvær i hverdagen."
        ),
        "points": ["Tur i nærområdet", "Høytlesning og samtaler", "Kaffe, spill og musikk", "Avlastning for pårørende"],
        "from": "Fra 590 kr / time",
    },
    {
        "id": "handling",
        "name": "Handling",
        "badge": "Ærender og innkjøp",
        "short": "Handleposer og ærender, uten stress.",
        "description": (
            "Vi tar hånd om dagligvarehandel og andre ærender for deg – raskt, pålitelig "
            "og tilpasset dine ønsker. Du slipper å stresse med transport eller tunge "
            "bæreposer. Vi handler det du trenger, når du trenger det."
        ),
        "points": ["Dagligvarer levert hjem", "Apotek og post", "Følge til butikk", "Faste ukeleveranser"],
        "from": "Fra 490 kr / oppdrag",
    },
    {
        "id": "hjemme",
        "name": "Rydding og fiksing hjemme",
        "badge": "Praktisk hjelp",
        "short": "Orden og små reparasjoner.",
        "description": (
            "Vi hjelper deg med rydding, lettere rengjøring og småjobber i hjemmet. "
            "Enten det er et rom som trenger orden, en lampe som skal skiftes eller noe "
            "som må fikses – vi stiller opp med praktisk hjelp slik at du kan trives godt hjemme."
        ),
        "points": ["Rydding og lett rengjøring", "Bytte lyspærer og batterier", "Henge opp bilder", "Sortere papirer"],
        "from": "Fra 590 kr / time",
    },
    {
        "id": "reise",
        "name": "Reiseledsager",
        "badge": "Omsorg på reise",
        "short": "Trygg følge til familiens store stunder.",
        "description": (
            "Vi tilbyr omsorgsfull ledsagelse under familieutflukter, helgeturer og "
            "spesielle anledninger. Din pårørende deltar fullt ut i fellesskapet, med "
            "trygg avlastning og verdig selskap hele veien. Vi sikrer at alle kan delta – uansett behov."
        ),
        "points": ["Bryllup og jubileer", "Helgeturer med familien", "Legetimer og behandling", "Lengre reiser"],
        "from": "Etter avtale",
    },
]

TEAM = [
    {
        "initial": "M",
        "name": "Mathias",
        "role": "Grunnlegger & Daglig leder",
        "quote": "Alle fortjener omsorg tilpasset akkurat dem.",
        "bio": (
            "Mathias har alltid hatt et brennende engasjement for mennesker i sårbare "
            "situasjoner. Med bakgrunn fra helsefag og flere år i frivillig omsorgsarbeid, "
            "startet han Senior Omsorg ut fra en enkel overbevisning: alle fortjener "
            "omsorg tilpasset akkurat dem. Han leder teamet med varme, tydelig retning "
            "og et ekte ønske om å gjøre hverdagen bedre for både brukere og pårørende."
        ),
        "tags": ["Helsefag", "10+ år erfaring", "Oslo"],
        "variant": 0,
    },
    {
        "initial": "M",
        "name": "Mikkel",
        "role": "Fagansvarlig & Besøksvenn",
        "quote": "Det lille ekstra gjør den største forskjellen.",
        "bio": (
            "Mikkel er hjørnesteinen i det faglige arbeidet hos Senior Omsorg. Med "
            "utdanning innen sykepleie og en naturlig evne til å skape trygghet, sørger "
            "han for at alle tjenester holder høyeste standard. Han er selv aktiv "
            "besøksvenn og kjenner jobben innenfra – det lille ekstra som gjør en stor "
            "forskjell for den som trenger det mest."
        ),
        "tags": ["Sykepleier", "Fagansvar", "Akershus"],
        "variant": 1,
    },
]

VALUES = [
    {"n": "01", "t": "Gratis samtale", "d": "Uforpliktende, alltid. Vi lytter først."},
    {"n": "02", "t": "Personlig match", "d": "Riktig person for riktig behov."},
    {"n": "03", "t": "Faglig tyngde", "d": "Erfarne folk med helsefaglig bakgrunn."},
    {"n": "04", "t": "Fleksibilitet", "d": "Vi tilpasser oss deg, ikke omvendt."},
]

FAQ_ITEMS = [
    {"q": "Hvor raskt kan dere starte?", "a": "Typisk ventetid er 1–4 uker avhengig av område og tjeneste. I akutte tilfeller prøver vi å stille opp raskere."},
    {"q": "Koster første samtale noe?", "a": "Nei. Alle konsultasjoner er gratis og uforpliktende. Vi bruker den første samtalen til å forstå behovet."},
    {"q": "Hvilke områder dekker dere?", "a": "Vi dekker Oslo og store deler av Akershus. Ta kontakt om du er usikker på ditt område."},
    {"q": "Hvordan matches jeg med en omsorgsperson?", "a": "Vi matcher basert på behov, personlighet og praktiske forhold. Kjemi er viktig – du kan bytte om det ikke stemmer."},
]

TIMING_OPTIONS = [
    {"id": "snarlig", "label": "Så snart som mulig"},
    {"id": "maned", "label": "Denne måneden"},
    {"id": "fremtid", "label": "Planlegger for fremtiden"},
]

# ── Global CSS ───────────────────────────────────────────────
st.markdown(
    f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Barlow:wght@200;300;400;500;600;700&family=Fraunces:ital,opsz,wght@0,9..144,300;0,9..144,400;0,9..144,500;1,9..144,300&display=swap');

    :root {{
        --bg: #E8DBCC;
        --bg-soft: #EFE4D6;
        --paper: #FCFAF6;
        --ink: #2B2724;
        --ink-soft: #524c4c;
        --muted: #8A7F73;
        --rule: #CBBBA8;
        --accent: #C4745A;
        --accent-deep: #8B3A22;
        --warm: #B28559;
        --nav: #2A2623;
    }}

    html, body, [class*="css"] {{
        font-family: 'Barlow', sans-serif;
        color: var(--ink);
    }}
    .stApp {{ background: var(--bg); }}
    .serif {{ font-family: 'Fraunces', serif; }}

    header[data-testid="stHeader"] {{ display: none !important; }}
    #MainMenu, footer {{ visibility: hidden; }}
    .block-container {{
        padding-top: 0 !important;
        padding-left: 0 !important;
        padding-right: 0 !important;
        max-width: 100% !important;
    }}

    /* ── Nav bar ── */
    [data-testid="stHorizontalBlock"]:first-of-type {{
        background: rgba(42,38,35,0.96);
        backdrop-filter: blur(10px);
        border-bottom: 1px solid rgba(255,255,255,0.06);
        padding: 14px 40px !important;
        margin: 0 !important;
        align-items: center;
        min-height: 70px;
        position: sticky;
        top: 0;
        z-index: 50;
    }}
    [data-testid="stHorizontalBlock"]:first-of-type > div {{
        display: flex;
        align-items: center;
        min-height: 42px;
    }}
    .logo-wrap {{
        display: flex;
        align-items: center;
        gap: 12px;
    }}
    .logo-text {{
        font-size: 13px;
        font-weight: 600;
        line-height: 1.15;
        color: var(--accent);
        text-transform: uppercase;
        letter-spacing: 0.22em;
    }}

    [data-testid="stHorizontalBlock"]:first-of-type .stButton > button {{
        background: transparent !important;
        color: rgba(255,255,255,0.55) !important;
        border: none !important;
        border-bottom: 1px solid transparent !important;
        border-radius: 0 !important;
        box-shadow: none !important;
        font-size: 13px !important;
        font-weight: 500 !important;
        letter-spacing: 0.22em !important;
        text-transform: uppercase !important;
        padding: 8px 0 !important;
        height: 42px !important;
        transition: color 0.2s, border-color 0.2s !important;
    }}
    [data-testid="stHorizontalBlock"]:first-of-type .stButton > button:hover {{
        color: #fff !important;
    }}
    [data-testid="stHorizontalBlock"]:first-of-type [data-active="true"] .stButton > button {{
        color: #fff !important;
        border-bottom: 1px solid var(--accent) !important;
    }}
    [data-testid="stHorizontalBlock"]:first-of-type .nav-cta .stButton > button {{
        background: var(--accent) !important;
        color: #fff !important;
        padding: 10px 22px !important;
        font-size: 12px !important;
        letter-spacing: 0.2em !important;
        font-weight: 600 !important;
        border-radius: 2px !important;
    }}
    [data-testid="stHorizontalBlock"]:first-of-type .nav-cta .stButton > button:hover {{
        background: var(--accent-deep) !important;
    }}

    .eyebrow {{
        font-size: 11px;
        letter-spacing: 0.24em;
        text-transform: uppercase;
        font-weight: 500;
        color: var(--accent);
    }}

    /* ── Hero (full-bleed) ── */
    .hero {{
        position: relative;
        width: 100%;
        height: min(84vh, 720px);
        min-height: 560px;
        overflow: hidden;
        background-image:
            linear-gradient(180deg, rgba(25,22,20,0.35) 0%, rgba(25,22,20,0.72) 100%),
            url("data:image/webp;base64,{_hero_img}");
        background-size: cover;
        background-position: center;
    }}
    .hero-inner {{
        position: relative;
        max-width: 1100px;
        margin: 0 auto;
        height: 100%;
        padding: 0 40px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: flex-start;
    }}
    .hero .eyebrow {{ color: rgba(255,255,255,0.85); margin-bottom: 32px; }}
    .hero h1 {{
        font-family: 'Fraunces', serif;
        font-size: clamp(52px, 8vw, 108px);
        font-weight: 300;
        line-height: 0.98;
        letter-spacing: -0.02em;
        margin: 0 0 32px;
        color: #fff;
        max-width: 960px;
    }}
    .hero h1 em {{ font-style: italic; color: var(--accent); font-weight: 300; }}
    .hero p.lead {{
        font-size: 20px;
        line-height: 1.55;
        color: rgba(255,255,255,0.85);
        max-width: 520px;
        margin: 0 0 44px;
        font-weight: 300;
    }}
    .hero-stat {{
        position: absolute;
        right: 40px;
        bottom: 40px;
        background: rgba(252,250,246,0.96);
        padding: 22px 28px;
        max-width: 280px;
        border-left: 3px solid var(--accent);
    }}
    .hero-stat .num {{
        font-family: 'Fraunces', serif;
        font-size: 42px;
        font-weight: 300;
        line-height: 1;
        color: var(--ink);
    }}
    .hero-stat .num small {{ font-size: 20px; }}
    .hero-stat .caption {{ font-size: 13px; color: var(--muted); margin-top: 8px; line-height: 1.5; }}

    .hero-slim {{
        background: var(--bg);
        padding: 120px 40px 60px;
        text-align: center;
        border-bottom: 1px solid var(--rule);
    }}
    .hero-slim .eyebrow {{ display: inline-block; margin-bottom: 24px; }}
    .hero-slim h1 {{
        font-family: 'Fraunces', serif;
        font-size: clamp(42px, 5vw, 68px);
        font-weight: 300;
        margin: 0 0 20px;
        letter-spacing: -0.01em;
        color: var(--ink);
    }}
    .hero-slim h1 em {{ font-style: italic; color: var(--accent); font-weight: 300; }}
    .hero-slim p {{ font-size: 18px; color: var(--ink-soft); max-width: 640px; margin: 0 auto; }}

    .section {{ padding: 120px 40px; }}
    .section-wrap {{ max-width: 1180px; margin: 0 auto; }}

    /* ── Services header ── */
    .svc-head {{
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 80px;
        align-items: end;
        margin-bottom: 56px;
    }}
    .svc-head h2 {{
        font-family: 'Fraunces', serif;
        font-size: clamp(40px, 5vw, 64px);
        font-weight: 300;
        line-height: 1.05;
        margin: 20px 0 0;
        letter-spacing: -0.01em;
        color: var(--ink);
    }}
    .svc-head h2 em {{ font-style: italic; color: var(--accent); font-weight: 300; }}
    .svc-head .intro {{
        font-size: 17px;
        line-height: 1.7;
        color: var(--ink-soft);
        margin: 0;
        max-width: 440px;
    }}
    .svc-head .intro strong {{ color: var(--accent); font-weight: 600; }}

    /* Points list styling (scoped globally, unique class) */
    .svc-points {{
        display: grid;
        grid-template-columns: 1fr 1fr;
        row-gap: 8px;
        column-gap: 20px;
    }}
    .svc-points span {{
        font-size: 12px;
        color: var(--muted);
        letter-spacing: 0.04em;
        display: flex;
        align-items: center;
        gap: 8px;
        line-height: 1.4;
    }}
    .svc-points span::before {{
        content: "";
        width: 4px;
        height: 4px;
        border-radius: 50%;
        background: var(--accent);
        flex-shrink: 0;
    }}

    /* Circular arrow button for services */
    .svc-picker .stButton > button {{
        width: 56px !important;
        height: 56px !important;
        min-width: 56px !important;
        border-radius: 50% !important;
        background: transparent !important;
        color: var(--muted) !important;
        border: 1px solid var(--rule) !important;
        padding: 0 !important;
        font-size: 20px !important;
        line-height: 1 !important;
        font-weight: 400 !important;
        transition: all 0.25s !important;
        letter-spacing: 0 !important;
        text-transform: none !important;
    }}
    .svc-picker .stButton > button:hover {{
        border-color: var(--accent) !important;
        color: var(--accent) !important;
        transform: translateX(4px);
    }}

    /* ── Values strip (dark) ── */
    .values {{ background: var(--nav); color: #fff; padding: 100px 40px; }}
    .values .values-head {{
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 80px;
        align-items: end;
        margin-bottom: 56px;
    }}
    .values .values-head h2 {{
        font-family: 'Fraunces', serif;
        font-size: clamp(36px, 4.5vw, 56px);
        font-weight: 300;
        line-height: 1.08;
        margin: 20px 0 0;
        letter-spacing: -0.01em;
        color: #fff;
    }}
    .values .items {{
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 40px;
    }}
    .values .item {{ border-top: 1px solid rgba(255,255,255,0.18); padding-top: 24px; }}
    .values .item .num {{
        font-family: 'Fraunces', serif;
        font-style: italic;
        color: var(--accent);
        font-size: 22px;
        margin-bottom: 16px;
    }}
    .values .item .t {{
        font-family: 'Fraunces', serif;
        font-size: 26px;
        font-weight: 300;
        line-height: 1.2;
        margin-bottom: 12px;
        color: #fff;
    }}
    .values .item .d {{ font-size: 14.5px; color: rgba(255,255,255,0.65); line-height: 1.6; }}

    /* ── Testimonial ── */
    .testimonial {{
        background: var(--bg-soft);
        padding: 120px 40px;
        text-align: center;
    }}
    .testimonial .inner {{ max-width: 900px; margin: 0 auto; }}
    .testimonial .mark {{
        color: var(--accent);
        font-size: 64px;
        line-height: 1;
        margin-bottom: 28px;
        font-family: 'Fraunces', serif;
    }}
    .testimonial blockquote {{
        font-family: 'Fraunces', serif;
        font-size: clamp(26px, 3vw, 38px);
        font-weight: 300;
        font-style: italic;
        line-height: 1.35;
        margin: 0 0 40px;
        color: var(--ink);
    }}
    .testimonial .attrib {{
        font-size: 13px;
        letter-spacing: 0.22em;
        text-transform: uppercase;
        color: var(--muted);
        font-weight: 600;
    }}

    /* ── FAQ ── */
    .faq h2 {{
        font-family: 'Fraunces', serif;
        font-size: clamp(36px, 4.5vw, 52px);
        font-weight: 300;
        line-height: 1.1;
        text-align: center;
        margin: 20px 0 64px;
        color: var(--ink);
    }}
    .faq .inner {{ max-width: 900px; margin: 0 auto; }}
    .faq .eyebrow {{ text-align: center; display: block; margin-bottom: 20px; }}

    .faq-item {{ border-top: 1px solid var(--rule); }}
    .faq-item.last {{ border-bottom: 1px solid var(--rule); }}

    .faq-picker .stButton > button {{
        width: 36px !important;
        min-width: 36px !important;
        height: 36px !important;
        border-radius: 50% !important;
        background: transparent !important;
        color: var(--muted) !important;
        border: 1px solid var(--rule) !important;
        font-size: 16px !important;
        font-weight: 300 !important;
        padding: 0 !important;
        line-height: 1 !important;
        transition: all 0.3s !important;
        letter-spacing: 0 !important;
        text-transform: none !important;
    }}
    .faq-picker[data-open="true"] .stButton > button {{
        color: var(--accent) !important;
        border-color: var(--accent) !important;
    }}

    /* ── Team page ── */
    .person-card {{ background: var(--paper); }}
    .person-portrait {{
        aspect-ratio: 4 / 5;
        width: 100%;
        overflow: hidden;
        display: block;
    }}
    .person-body {{ padding: 36px 40px 44px; }}
    .person-body h3 {{
        font-family: 'Fraunces', serif;
        font-size: 38px;
        font-weight: 300;
        margin: 0 0 6px;
        color: var(--ink);
    }}
    .person-body .role {{
        font-size: 11px;
        letter-spacing: 0.22em;
        text-transform: uppercase;
        font-weight: 600;
        color: var(--accent);
        margin-bottom: 22px;
    }}
    .person-body blockquote {{
        font-family: 'Fraunces', serif;
        font-size: 22px;
        font-style: italic;
        font-weight: 300;
        line-height: 1.35;
        margin: 0 0 24px;
        padding-left: 18px;
        border-left: 2px solid var(--accent);
        color: var(--ink);
    }}
    .person-body p.bio {{
        color: var(--ink-soft);
        font-size: 15.5px;
        line-height: 1.7;
        margin: 0 0 24px;
    }}
    .person-body .tags {{
        display: flex;
        gap: 10px;
        flex-wrap: wrap;
    }}
    .person-body .tags span {{
        font-size: 11px;
        letter-spacing: 0.1em;
        text-transform: uppercase;
        font-weight: 500;
        color: var(--muted);
        padding: 6px 12px;
        border: 1px solid var(--rule);
    }}
    .team-close {{
        text-align: center;
        margin-top: 100px;
        padding: 60px 40px;
        border-top: 1px solid var(--rule);
    }}
    .team-close .line {{
        font-family: 'Fraunces', serif;
        font-size: clamp(28px, 3.5vw, 44px);
        font-weight: 300;
        font-style: italic;
        color: var(--accent);
        line-height: 1.3;
        max-width: 800px;
        margin: 0 auto;
    }}

    /* ── Contact page ── */
    .contact-left h2 {{
        font-family: 'Fraunces', serif;
        font-size: clamp(40px, 5vw, 60px);
        font-weight: 300;
        line-height: 1.05;
        margin: 0 0 28px;
        letter-spacing: -0.01em;
        color: var(--ink);
    }}
    .contact-left h2 em {{ font-style: italic; color: var(--accent); font-weight: 300; }}
    .contact-left p.lead {{
        font-size: 17px;
        line-height: 1.7;
        color: var(--ink-soft);
        margin: 0 0 40px;
        max-width: 440px;
    }}
    .contact-meta {{
        border-top: 1px solid var(--rule);
        padding-top: 32px;
        display: grid;
        gap: 24px;
    }}
    .contact-meta .lbl {{
        font-size: 10px;
        letter-spacing: 0.24em;
        text-transform: uppercase;
        font-weight: 600;
        color: var(--accent);
        margin-bottom: 8px;
    }}
    .contact-meta .phone {{
        font-family: 'Fraunces', serif;
        font-size: 28px;
        font-weight: 300;
        color: var(--ink);
    }}
    .contact-meta .plain {{ font-size: 17px; color: var(--ink); }}

    .contact-card {{
        background: var(--paper);
        padding: 48px;
        border-top: 3px solid var(--accent);
    }}
    .form-label {{
        display: block;
        font-size: 11px;
        letter-spacing: 0.22em;
        text-transform: uppercase;
        font-weight: 600;
        color: var(--muted);
        margin: 0 0 12px;
    }}
    .form-label .req {{ color: var(--accent); }}

    .contact-card .stTextInput input,
    .contact-card .stTextArea textarea {{
        border: none !important;
        border-bottom: 1px solid var(--rule) !important;
        border-radius: 0 !important;
        background: transparent !important;
        padding: 12px 0 !important;
        font-size: 16px !important;
        font-family: 'Barlow', sans-serif !important;
        color: var(--ink) !important;
        box-shadow: none !important;
    }}
    .contact-card .stTextInput input:focus,
    .contact-card .stTextArea textarea:focus {{
        border-bottom-color: var(--accent) !important;
        box-shadow: none !important;
    }}

    .chip-picker .stButton > button {{
        width: 100% !important;
        padding: 12px 14px !important;
        background: transparent !important;
        border: 1px solid var(--rule) !important;
        color: var(--ink) !important;
        border-radius: 0 !important;
        font-size: 13px !important;
        font-weight: 500 !important;
        letter-spacing: 0 !important;
        text-transform: none !important;
        text-align: left !important;
        transition: all 0.2s !important;
        justify-content: flex-start !important;
    }}
    .chip-picker[data-active="true"] .stButton > button {{
        background: var(--accent) !important;
        border-color: var(--accent) !important;
        color: #fff !important;
    }}
    .chip-picker.chip-dark[data-active="true"] .stButton > button {{
        background: var(--nav) !important;
        border-color: var(--nav) !important;
        color: #fff !important;
    }}
    .chip-picker.chip-small .stButton > button {{
        font-size: 12px !important;
        padding: 10px 12px !important;
        text-align: center !important;
        justify-content: center !important;
        color: var(--ink-soft) !important;
    }}

    .submit-btn .stButton > button {{
        width: 100% !important;
        margin-top: 12px !important;
        background: var(--accent) !important;
        color: #fff !important;
        border: none !important;
        border-radius: 0 !important;
        padding: 18px !important;
        font-size: 12px !important;
        letter-spacing: 0.24em !important;
        text-transform: uppercase !important;
        font-weight: 600 !important;
        transition: background 0.2s !important;
    }}
    .submit-btn .stButton > button:hover {{ background: var(--accent-deep) !important; }}
    .submit-btn .stButton > button:disabled {{ background: var(--rule) !important; cursor: not-allowed !important; }}

    .disclaimer {{
        font-size: 12px;
        color: var(--muted);
        margin-top: 16px;
        text-align: center;
        line-height: 1.6;
    }}

    .success-card {{ text-align: center; padding: 40px 0; }}
    .success-card .check {{
        width: 72px;
        height: 72px;
        border-radius: 50%;
        background: var(--accent);
        display: flex;
        align-items: center;
        justify-content: center;
        margin: 0 auto 32px;
        color: #fff;
        font-size: 32px;
    }}
    .success-card h3 {{
        font-family: 'Fraunces', serif;
        font-size: 32px;
        font-weight: 300;
        margin: 0 0 14px;
        color: var(--ink);
    }}
    .success-card p {{
        font-size: 16px;
        color: var(--ink-soft);
        line-height: 1.7;
        margin: 0 0 32px;
    }}
    .success-card p strong {{ color: var(--accent); }}
    .reset-btn .stButton > button {{
        background: transparent !important;
        border: 1px solid var(--rule) !important;
        color: var(--ink-soft) !important;
        padding: 14px 24px !important;
        font-size: 11px !important;
        letter-spacing: 0.22em !important;
        text-transform: uppercase !important;
        font-weight: 600 !important;
        border-radius: 0 !important;
    }}

    /* ── Footer ── */
    .footer {{
        background: var(--nav);
        color: rgba(255,255,255,0.65);
        padding: 80px 40px 40px;
    }}
    .footer .wrap {{ max-width: 1180px; margin: 0 auto; }}
    .footer .cols {{
        display: grid;
        grid-template-columns: 2fr 1fr 1fr 1fr;
        gap: 60px;
        margin-bottom: 64px;
    }}
    .footer .brand {{
        display: flex;
        align-items: center;
        gap: 12px;
        margin-bottom: 24px;
    }}
    .footer .tagline {{
        font-family: 'Fraunces', serif;
        font-size: 22px;
        font-style: italic;
        font-weight: 300;
        color: rgba(255,255,255,0.85);
        line-height: 1.4;
        margin: 0;
        max-width: 340px;
    }}
    .footer .col-title {{
        font-size: 11px;
        letter-spacing: 0.22em;
        text-transform: uppercase;
        font-weight: 600;
        color: #fff;
        margin-bottom: 20px;
    }}
    .footer ul {{
        list-style: none;
        padding: 0;
        margin: 0;
        display: grid;
        gap: 12px;
    }}
    .footer ul li {{ font-size: 14px; }}
    .footer .bottom {{
        border-top: 1px solid rgba(255,255,255,0.12);
        padding-top: 28px;
        display: flex;
        justify-content: space-between;
        font-size: 12px;
        letter-spacing: 0.08em;
    }}

    @media (max-width: 900px) {{
        .svc-head, .values .values-head {{ grid-template-columns: 1fr !important; gap: 32px !important; }}
        .values .items {{ grid-template-columns: 1fr 1fr !important; }}
        .footer .cols {{ grid-template-columns: 1fr 1fr !important; }}
        .svc-points {{ grid-template-columns: 1fr !important; }}
    }}
    </style>
    """,
    unsafe_allow_html=True,
)


LOGO_SVG = """
<svg width="34" height="31" viewBox="0 0 42 38" fill="none" xmlns="http://www.w3.org/2000/svg">
  <path d="M21 35 C21 35 3 23 3 12 C3 6.48 7.48 2 13 2 C16.5 2 19.6 3.8 21 6.5 C22.4 3.8 25.5 2 29 2 C34.52 2 39 6.48 39 12 C39 23 21 35 21 35 Z"
        stroke="#C4745A" stroke-width="2.5" fill="none" stroke-linejoin="round" stroke-linecap="round"/>
</svg>
"""


def portrait_svg(initial, variant):
    accent = "#C4745A"
    deep = "#8B3A22"
    a, b = (accent, deep) if variant == 0 else (deep, accent)
    return f"""
    <svg viewBox="0 0 400 480" preserveAspectRatio="xMidYMid slice" style="width:100%;height:100%;display:block;">
      <defs>
        <linearGradient id="pg{variant}" x1="0" x2="1" y1="0" y2="1">
          <stop offset="0" stop-color="{a}" />
          <stop offset="1" stop-color="{b}" />
        </linearGradient>
        <radialGradient id="pl{variant}" cx="0.3" cy="0.2" r="0.6">
          <stop offset="0" stop-color="#fff" stop-opacity="0.25" />
          <stop offset="1" stop-color="#fff" stop-opacity="0" />
        </radialGradient>
      </defs>
      <rect width="400" height="480" fill="url(#pg{variant})" />
      <rect width="400" height="480" fill="url(#pl{variant})" />
      <circle cx="200" cy="190" r="70" fill="#fff" opacity="0.12" />
      <path d="M90 480 C 100 380 140 320 200 320 C 260 320 300 380 310 480 Z" fill="#fff" opacity="0.12" />
      <text x="200" y="230" text-anchor="middle" fill="#fff"
            font-family="Fraunces, serif" font-size="140" font-weight="300" opacity="0.95">{initial}</text>
    </svg>
    """


# ── Nav bar ──────────────────────────────────────────────────
page = st.session_state.page
nav_cols = st.columns([4, 1.4, 1.6, 1.2, 2])

with nav_cols[0]:
    st.markdown(
        f'<div class="logo-wrap">{LOGO_SVG}<span class="logo-text">Senior<br>Omsorg</span></div>',
        unsafe_allow_html=True,
    )

with nav_cols[1]:
    st.markdown(f'<div data-active="{"true" if page == "tjenester" else "false"}">', unsafe_allow_html=True)
    if st.button("Tjenester", key="nav_tjenester"):
        goto("tjenester")
    st.markdown("</div>", unsafe_allow_html=True)

with nav_cols[2]:
    st.markdown(f'<div data-active="{"true" if page == "hvem" else "false"}">', unsafe_allow_html=True)
    if st.button("Hvem er vi", key="nav_hvem"):
        goto("hvem")
    st.markdown("</div>", unsafe_allow_html=True)

with nav_cols[3]:
    st.markdown(f'<div data-active="{"true" if page == "kontakt" else "false"}">', unsafe_allow_html=True)
    if st.button("Kontakt", key="nav_kontakt"):
        goto("kontakt")
    st.markdown("</div>", unsafe_allow_html=True)

with nav_cols[4]:
    st.markdown('<div class="nav-cta">', unsafe_allow_html=True)
    if st.button("Få en samtale", key="nav_cta"):
        goto("kontakt")
    st.markdown("</div>", unsafe_allow_html=True)


# ============================================================
# PAGE: TJENESTER
# ============================================================
if page == "tjenester":
    st.markdown(
        """
        <section class="hero">
          <div class="hero-inner">
            <div class="eyebrow">Oslo · Akershus</div>
            <h1>Omsorg som<br><em>ser deg</em>.</h1>
            <p class="lead">Besøksvenn, praktisk hjelp og reiseledsager — tilpasset hver enkelt. Gratis og uforpliktende samtale.</p>
          </div>
          <div class="hero-stat">
            <div class="num">1–4 <small>uker</small></div>
            <div class="caption">Typisk ventetid fra samtale til en omsorgsperson er på plass hos deg.</div>
          </div>
        </section>
        """,
        unsafe_allow_html=True,
    )

    st.markdown('<section class="section"><div class="section-wrap">', unsafe_allow_html=True)
    st.markdown(
        """
        <div class="svc-head">
          <div>
            <span class="eyebrow">Våre tjenester</span>
            <h2>Fire måter vi kan<br>gjøre hverdagen <em>bedre</em>.</h2>
          </div>
          <div>
            <p class="intro">Vi matcher deg med riktig omsorgsperson basert på behov, ønsker og personlighet.
            Alle konsultasjoner er <strong>gratis og uforpliktende</strong>.</p>
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div style="border-top:1px solid var(--rule);"></div>',
        unsafe_allow_html=True,
    )

    for i, s in enumerate(SERVICES):
        points_html = "".join(f"<span>{p}</span>" for p in s["points"])
        row_cols = st.columns([0.85, 3.2, 0.9])
        with row_cols[0]:
            st.markdown(
                f"""
                <div style="padding:36px 8px 0;">
                  <div class="serif" style="font-size:44px;font-weight:300;color:var(--accent);
                                            line-height:1;font-style:italic;opacity:0.75;">
                    0{i + 1}
                  </div>
                  <div style="margin-top:18px;">
                    <span style="font-size:10px;letter-spacing:0.22em;text-transform:uppercase;
                                 font-weight:600;color:var(--accent);display:inline-block;margin-bottom:8px;">
                      {s['badge']}
                    </span>
                    <h3 class="serif" style="font-size:30px;font-weight:300;margin:0 0 6px;
                                             color:var(--ink);line-height:1.1;">{s['name']}</h3>
                    <div style="font-size:14px;color:var(--muted);font-style:italic;">{s['from']}</div>
                  </div>
                </div>
                """,
                unsafe_allow_html=True,
            )
        with row_cols[1]:
            st.markdown(
                f"""
                <div style="padding:36px 0 0;">
                  <p style="margin:0 0 14px;color:var(--ink-soft);font-size:16px;
                            line-height:1.65;max-width:520px;">{s['description']}</p>
                  <div class="svc-points">{points_html}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )
        with row_cols[2]:
            st.markdown('<div class="svc-picker" style="padding:50px 0 0;display:flex;justify-content:flex-end;">', unsafe_allow_html=True)
            if st.button("→", key=f"pick_{s['id']}"):
                goto("kontakt", service=s["id"])
            st.markdown("</div>", unsafe_allow_html=True)
        st.markdown(
            '<div style="border-bottom:1px solid var(--rule);margin-top:36px;"></div>',
            unsafe_allow_html=True,
        )

    st.markdown("</div></section>", unsafe_allow_html=True)

    # Values
    values_html = "".join(
        f'<div class="item"><div class="num">— {v["n"]}</div>'
        f'<div class="t">{v["t"]}</div>'
        f'<div class="d">{v["d"]}</div></div>'
        for v in VALUES
    )
    st.markdown(
        f"""
        <section class="values">
          <div class="section-wrap">
            <div class="values-head">
              <div>
                <span class="eyebrow" style="color:var(--accent);">Slik jobber vi</span>
                <h2>Prinsippene våre er<br>enkle, og de står.</h2>
              </div>
            </div>
            <div class="items">{values_html}</div>
          </div>
        </section>
        """,
        unsafe_allow_html=True,
    )

    # Testimonial
    st.markdown(
        """
        <section class="testimonial">
          <div class="inner">
            <div class="mark">“</div>
            <blockquote>Mamma gleder seg til hver onsdag. Besøksvennen fra Senior Omsorg
            er blitt en del av familien — og vi sover roligere om natten.</blockquote>
            <div class="attrib">Ingrid S. · Pårørende, Bærum</div>
          </div>
        </section>
        """,
        unsafe_allow_html=True,
    )

    # FAQ
    st.markdown(
        """
        <section class="section faq"><div class="inner">
          <span class="eyebrow">Ofte stilte spørsmål</span>
          <h2>Godt å vite.</h2>
        """,
        unsafe_allow_html=True,
    )
    for i, f in enumerate(FAQ_ITEMS):
        is_open = st.session_state.faq_open == i
        last_cls = " last" if i == len(FAQ_ITEMS) - 1 else ""
        st.markdown(f'<div class="faq-item{last_cls}">', unsafe_allow_html=True)
        q_cols = st.columns([10, 1])
        with q_cols[0]:
            st.markdown(
                f'<div style="padding:26px 0;"><div class="serif" '
                f'style="font-size:22px;font-weight:400;color:var(--ink);">{f["q"]}</div></div>',
                unsafe_allow_html=True,
            )
        with q_cols[1]:
            st.markdown(
                f'<div class="faq-picker" data-open="{"true" if is_open else "false"}" '
                f'style="padding:26px 0 0;display:flex;justify-content:flex-end;">',
                unsafe_allow_html=True,
            )
            if st.button("−" if is_open else "+", key=f"faq_{i}"):
                st.session_state.faq_open = -1 if is_open else i
                st.rerun()
            st.markdown("</div>", unsafe_allow_html=True)
        if is_open:
            st.markdown(
                f'<div style="padding:0 0 26px;max-width:720px;'
                f'font-size:16px;line-height:1.7;color:var(--ink-soft);">{f["a"]}</div>',
                unsafe_allow_html=True,
            )
        st.markdown("</div>", unsafe_allow_html=True)
    st.markdown("</div></section>", unsafe_allow_html=True)

# ============================================================
# PAGE: HVEM ER VI
# ============================================================
elif page == "hvem":
    st.markdown(
        """
        <div class="hero-slim">
          <span class="eyebrow">Hvem er vi</span>
          <h1>Omsorg er en jobb<br><em>vi er glad i</em>.</h1>
          <p>Vi jobber fra hjertet. For oss handler omsorg om ekte menneskelig kontakt — å se den enkelte, lytte, og gjøre en reell forskjell i hverdagen.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <section class="section" style="padding-bottom:0;">
          <div class="section-wrap">
            <span class="eyebrow">Hvorfor vi startet Senior Omsorg</span>
            <div style="max-width:820px;margin-top:28px;">
              <p style="font-size:17px;line-height:1.75;color:var(--ink-soft);margin:0 0 22px;">
                Mathias Kielland og Mikkel Næs er utdannet innenfor markedsføring og økonomi og har bakgrunn fra bank/IT,
                men vår viktigste erfaring startet allerede i studietiden på et lokalt eldresenter hvor vi jobbet.
                Der ble frøet sådd for det som i dag er Senior Omsorg.
              </p>
              <p style="font-size:17px;line-height:1.75;color:var(--ink-soft);margin:0 0 22px;">
                Etter flere år i DNB og Forte Digital valgte vi å omsette vårt personlige engasjement til handling.
                Vi ser på eldreomsorg som et viktig samfunnsoppdrag, og har dedikert tiden vår til å lære bransjen fra innsiden,
                senest gjennom arbeid i Senior Support og på bo og behandlingssenter.
                Vår visjon er enkel: Å bruke vår kompetanse og vårt engasjement til å hjelpe eldre med å mestre hverdagen,
                samtidig som vi skaper øyeblikk som gir ekte glede og mening.
              </p>
              <p style="font-size:17px;line-height:1.75;color:var(--ink-soft);margin:0 0 22px;">
                Vårt fokus er å finne gode løsninger for den enkelte senior, gjerne i samarbeid med pårørende.
                Det kan være et stort ansvar å være pårørende og det er ofte behov for avlastning.
              </p>
              <p style="font-size:17px;line-height:1.75;color:var(--ink-soft);margin:0 0 8px;">
                Vi hører gjerne fra deg om du er senior, eller pårørende til en senior.
              </p>
              <p style="font-family:'Fraunces',serif;font-size:22px;font-weight:300;font-style:italic;color:var(--accent);margin:24px 0 0;">
                Sammen kan vi skape en mer verdig og meningsfull hverdag.
              </p>
            </div>
          </div>
        </section>
        """,
        unsafe_allow_html=True,
    )

    st.markdown('<section class="section"><div class="section-wrap">', unsafe_allow_html=True)
    cols = st.columns(2, gap="large")
    for col, person in zip(cols, TEAM):
        tags_html = "".join(f"<span>{t}</span>" for t in person["tags"])
        with col:
            st.markdown(
                f"""
                <article class="person-card">
                  <div class="person-portrait">{portrait_svg(person["initial"], person["variant"])}</div>
                  <div class="person-body">
                    <h3>{person['name']}</h3>
                    <div class="role">{person['role']}</div>
                    <blockquote>"{person['quote']}"</blockquote>
                    <p class="bio">{person['bio']}</p>
                    <div class="tags">{tags_html}</div>
                  </div>
                </article>
                """,
                unsafe_allow_html=True,
            )

    st.markdown(
        """
        <div class="team-close">
          <div class="line">Vi jobber fra hjertet — mennesker trenger mennesker.</div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.markdown("</div></section>", unsafe_allow_html=True)

# ============================================================
# PAGE: KONTAKT
# ============================================================
elif page == "kontakt":
    st.markdown(
        """
        <div class="hero-slim">
          <span class="eyebrow">Ta kontakt</span>
          <h1>La oss snakke<br>om <em>deres</em> behov.</h1>
          <p>Alle samtaler er gratis og uforpliktende. Vi ringer deg tilbake innen 24 timer på hverdager.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown('<section class="section"><div class="section-wrap">', unsafe_allow_html=True)

    left, right = st.columns([1, 1.1], gap="large")

    with left:
        st.markdown(
            """
            <div class="contact-left">
              <div class="contact-meta">
                <div>
                  <div class="lbl">Telefon</div>
                  <div class="phone">22 00 00 00</div>
                </div>
                <div>
                  <div class="lbl">E-post</div>
                  <div class="plain">hei@seniorosmorg.no</div>
                </div>
                <div>
                  <div class="lbl">Område</div>
                  <div class="plain">Oslo og Akershus</div>
                </div>
              </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with right:
        st.markdown('<div class="contact-card">', unsafe_allow_html=True)

        if st.session_state.submitted:
            name = st.session_state.get("name_input", "")
            phone = st.session_state.get("phone_input", "")
            svc = next((s for s in SERVICES if s["id"] == st.session_state.selected_service), None)
            svc_name = svc["name"] if svc else "tjenesten"
            st.markdown(
                f"""
                <div class="success-card">
                  <div class="check">✓</div>
                  <h3>Takk, {name or 'du'}!</h3>
                  <p>Vi tar kontakt på <strong>{phone or 'telefonen din'}</strong> innen kort tid for
                  en gratis samtale om <strong>{svc_name}</strong>.</p>
                </div>
                """,
                unsafe_allow_html=True,
            )
            st.markdown('<div class="reset-btn" style="display:flex;justify-content:center;">', unsafe_allow_html=True)
            if st.button("Send ny henvendelse", key="reset_form"):
                st.session_state.submitted = False
                st.session_state.selected_service = None
                for k in ("name_input", "phone_input", "email_input", "message_input"):
                    if k in st.session_state:
                        del st.session_state[k]
                st.rerun()
            st.markdown("</div>", unsafe_allow_html=True)
        else:
            st.markdown(
                '<div style="margin-bottom:28px;"><label class="form-label">Hvilken tjeneste?</label>',
                unsafe_allow_html=True,
            )
            pick_cols = st.columns(2)
            for idx, s in enumerate(SERVICES):
                with pick_cols[idx % 2]:
                    active = st.session_state.selected_service == s["id"]
                    st.markdown(
                        f'<div class="chip-picker" data-active="{"true" if active else "false"}">',
                        unsafe_allow_html=True,
                    )
                    if st.button(s["name"], key=f"pick_svc_{s['id']}"):
                        st.session_state.selected_service = s["id"]
                        st.rerun()
                    st.markdown("</div>", unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)

            st.markdown('<label class="form-label">Navn <span class="req">*</span></label>', unsafe_allow_html=True)
            name = st.text_input("Navn", key="name_input", placeholder="Ditt fulle navn", label_visibility="collapsed")

            st.markdown('<label class="form-label">Telefon <span class="req">*</span></label>', unsafe_allow_html=True)
            phone = st.text_input("Telefon", key="phone_input", placeholder="+47 000 00 000", label_visibility="collapsed")

            st.markdown('<label class="form-label">E-post</label>', unsafe_allow_html=True)
            st.text_input("E-post", key="email_input", placeholder="valgfritt", label_visibility="collapsed")

            st.markdown(
                '<div style="margin:20px 0;"><label class="form-label">Når trenger dere hjelp?</label>',
                unsafe_allow_html=True,
            )
            t_cols = st.columns(3)
            for idx, opt in enumerate(TIMING_OPTIONS):
                with t_cols[idx]:
                    active = st.session_state.form_when == opt["id"]
                    st.markdown(
                        f'<div class="chip-picker chip-small chip-dark" data-active="{"true" if active else "false"}">',
                        unsafe_allow_html=True,
                    )
                    if st.button(opt["label"], key=f"when_{opt['id']}"):
                        st.session_state.form_when = opt["id"]
                        st.rerun()
                    st.markdown("</div>", unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)

            st.markdown('<label class="form-label">Beskriv behovet kort</label>', unsafe_allow_html=True)
            st.text_area(
                "Melding", key="message_input",
                placeholder="Hvem gjelder det? Noen spesielle ønsker?",
                label_visibility="collapsed", height=90,
            )

            valid = bool(name and phone)
            st.markdown('<div class="submit-btn">', unsafe_allow_html=True)
            if st.button("Send henvendelse →", key="submit", disabled=not valid):
                st.session_state.submitted = True
                st.rerun()
            st.markdown("</div>", unsafe_allow_html=True)
            st.markdown(
                '<div class="disclaimer">Ved å sende godtar du at vi tar kontakt. Gratis og uforpliktende.</div>',
                unsafe_allow_html=True,
            )

        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("</section>", unsafe_allow_html=True)


# ── Footer ───────────────────────────────────────────────────
tjenester_items = "".join(f"<li>{s['name']}</li>" for s in SERVICES)
st.markdown(
    f"""
    <footer class="footer">
      <div class="wrap">
        <div class="cols">
          <div>
            <div class="brand">
              {LOGO_SVG}
              <span class="logo-text">Senior<br>Omsorg</span>
            </div>
            <p class="tagline">Trygghet og glede i hverdagen, tilpasset hver enkelt.</p>
          </div>
          <div>
            <div class="col-title">Tjenester</div>
            <ul>{tjenester_items}</ul>
          </div>
          <div>
            <div class="col-title">Selskap</div>
            <ul><li>Hvem er vi</li><li>Karriere</li><li>Kontakt</li><li>Personvern</li></ul>
          </div>
          <div>
            <div class="col-title">Kontakt</div>
            <ul><li>22 00 00 00</li><li>hei@seniorosmorg.no</li><li>Oslo · Akershus</li></ul>
          </div>
        </div>
        <div class="bottom">
          <div>© 2026 Senior Omsorg</div>
          <div>Gratis og uforpliktende samtale</div>
        </div>
      </div>
    </footer>
    """,
    unsafe_allow_html=True,
)
