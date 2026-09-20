"""The Walyverse profile README, drawn as one card in dark and light.

The figures come from the profile stats workflow, which measures the organisation
hourly and re-runs this script; run it without arguments to keep the current ones.
"""
import argparse
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "assets"
FOOT_TOP = 1936
W, H = 1200, FOOT_TOP + 170
PAD = 80

SEMI = "'Segoe UI Semibold','Segoe UI',Inter,'Helvetica Neue',Helvetica,Arial,sans-serif"
SANS = "'Segoe UI','Helvetica Neue',Helvetica,Arial,sans-serif"

DARK = {
    "bg": ("#0A0512", "#180E2E", "#0B0716", "#090410"),
    "grid": ("#A78BFA", ".045"),
    "glow": ".45", "glow2": ".35",
    "word": ("#F3E8FF", "#C4B5FD", "#818CF8"),
    "rule": ("#A855F7", ".9", "#6366F1"),
    "tagline": "#B9A9E8",
    "wire": ("#A78BFA", ".42"),
    "cube_edge": ("#DDD6FE", ".35"),
    "pill": [(".14", ".35", "#D8C9FF"), (".14", ".35", "#C7CBFF"), (".10", ".28", "#A5E9F5")],
    "pill_stroke": ("#A855F7", "#818CF8", "#22D3EE"),
    "label": "#A491CF",
    "lead": "#D9D0EE",
    "text": "#D9D0EE",
    "body": "#C6B8E4",
    "name": "#E9E1FA",
    "quote": "#C4B5FD",
    "email": "#E9E1FA",
    "fw": ("#F3E8FF", "#A78BFA"),
    "fsub": "#9A85D0",
    "muted": "#6E5D96",
    "border": ("#A78BFA", ".18"),
    "hair": ("#A855F7", ".40"),
    "dots": ["#F0A030", "#4FA3E3", "#6CC24A", "#FFD343", "#F0F0F0",
             "#00A3C4", "#7A9BE8", "#FF6B5E", "#4FA8F5", "#8F88FF"],
    "ftile": ("#6D5DFC", "#9B6BFF"),
    "fword": ("#F5F6F8", "#B49DFF"),
    "fline2": "#B6BBC6",
    "furl": "#8B78FF",
    "soft": ".5",
}

LIGHT = {
    "bg": ("#FFFFFF", "#F5F1FE", "#FCFAFF", "#FFFFFF"),
    "grid": ("#7C3AED", ".055"),
    "glow": ".20", "glow2": ".18",
    "word": ("#4C1D95", "#6D28D9", "#4338CA"),
    "rule": ("#7C3AED", ".85", "#6366F1"),
    "tagline": "#5B4B8A",
    "wire": ("#7C3AED", ".42"),
    "cube_edge": ("#FFFFFF", ".45"),
    "pill": [(".12", ".40", "#5B21B6"), (".12", ".40", "#3730A3"), (".10", ".35", "#155E75")],
    "pill_stroke": ("#A855F7", "#6366F1", "#06B6D4"),
    "label": "#67558F",
    "lead": "#33285A",
    "text": "#33285A",
    "body": "#463A6E",
    "name": "#2A1F45",
    "quote": "#4C1D95",
    "email": "#2A1F45",
    "fw": ("#4C1D95", "#6D28D9"),
    "fsub": "#6D5A9C",
    "muted": "#8A7CB0",
    "border": ("#7C3AED", ".20"),
    "hair": ("#7C3AED", ".35"),
    "dots": ["#E07B00", "#3178C6", "#4CA13A", "#D9A400", "#111827",
             "#00758F", "#4169E1", "#DC382D", "#2496ED", "#635BFF"],
    "ftile": ("#6D5DFC", "#9333EA"),
    "fword": ("#15171F", "#6D5DFC"),
    "fline2": "#4A5160",
    "furl": "#6D5DFC",
    "soft": ".8",
}

def pills(repos, loc):
    return [
        (247, 181, f"{repos} REPOSITORIES", 151),
        (442, 222, f"{loc} LINES OF CODE", 192),
        (678, 222, "7+ YEARS EXPERIENCE", 192),
    ]

LEAD = [
    "We build and operate the worlds people log into, on the platforms where the players already",
    "are: Minecraft today, Hytale and Roblox tomorrow. Identity, state, the transactional core and",
    "the control plane that schedules the fleet are all ours.",
]

GROUPS = [
    ("CONTROL PLANE", "capacity follows demand, not a spreadsheet", [
        ("Orchestrator", "a reconciliation loop over the fleet"),
        ("Forward", "signed commands on every node"),
        ("Web", "multi tenant account portal"),
    ]),
    ("IDENTITY &amp; STATE", "one player record across the fleet", [
        ("Core", "sessions, entitlements, retention"),
        ("Auth", "verified at the edge and the node"),
        ("Sync", "snapshots, restores, fleet index"),
    ]),
    ("TRANSACTIONAL CORE", "a trade commits or it never happened", [
        ("Economy", "balances on an append only journal"),
        ("Market", "shops, auctions, escrow, delivery"),
        ("Items", "per instance identity, dupes visible"),
        ("Checkout", "exactly one delivery per payment"),
    ]),
    ("RUNTIME", "what the player actually touches", [
        ("Menu", "interfaces compiled from config"),
        ("I18n", "locale carried across the fleet"),
        ("Chat", "routing, moderation, alerting"),
        ("Teleport", "cross node transfer with handover"),
    ]),
]

FERRY_LEAD = "Configuration distribution for server fleets."
FERRY = [
    "A watcher picks a change up where it was made and propagates it to every node that should carry it, substituting what differs",
    "per node on the way. Ten thousand lines of Python, now sold to operators whose fleets have nothing to do with our games.",
]

MAXIM = "When correctness and convenience disagree, correctness wins,"
MAXIM2 = "and the contract is written before the code."

PRINCIPLES = [
    ("ONE SOURCE OF TRUTH", "durable state lives in the database"),
    ("IDEMPOTENT BY DEFAULT", "written to survive being replayed"),
    ("AUDITABLE AFTER THE FACT", "journals and reconciliation, by design"),
    ("BOUNDED WORK", "terminates in predictable time"),
]

STACK = ["Java", "TypeScript", "Node.js", "Python", "Next.js",
         "MySQL", "PostgreSQL", "Redis", "Docker", "Stripe"]

# vertical rhythm, in README order: lead, stack, platform, ferry, how we work.
# type is sized so it stays legible once GitHub scales 1200px into its column
LEAD_Y, LEAD_STEP = 366, 38
STACK_Y, ROW1_Y, ROW2_Y = 542, 600, 648
SEC1_Y, GROUP_Y, ITEM_STEP, BLOCK_STEP = 742, 796, 34, 232
FERRY_Y, FERRY_BODY, FERRY_STEP = 1340, 1408, 30
SEC3_Y, MAXIM_Y, PRINC_Y, PRINC_STEP = 1618, 1672, 1766, 72


def txt(x, y, size, fill, body, family=SANS, weight="400", track=None,
        anchor="start", opacity=None, extra=""):
    a = f' letter-spacing="{track}"' if track else ""
    o = f' fill-opacity="{opacity}"' if opacity else ""
    an = f' text-anchor="{anchor}"' if anchor != "start" else ""
    return (f'<text x="{x}" y="{y}" font-family="{family}" font-size="{size}" '
            f'font-weight="{weight}" fill="{fill}"{a}{o}{an}{extra}>{body}</text>')


def section(c, x, y, label, width=None):
    out = [txt(x, y, 13.5, c["label"], label, weight="700", track="4.6")]
    rule_x = x + 26 + len(label.replace("&amp;", "&")) * 11
    out.append(f'<rect x="{rule_x}" y="{y - 5.5}" width="{width or (W - PAD - rule_x)}" '
               f'height="1.5" rx=".75" fill="url(#srule)"/>')
    return out


def build(c, PILLS):
    p = []
    p.append(f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" '
             f'viewBox="0 0 {W} {H}" role="img" aria-label="Walyverse, distributed systems for '
             f'live game worlds. 42 repositories, 360K+ lines of code, 7+ years, 50K+ players. '
             f'Control plane, identity and state, transactional core, runtime. Ferry, '
             f'configuration distribution for server fleets. Built with Java, TypeScript, '
             f'Node.js, Python, Next.js, MySQL, PostgreSQL, Redis, Docker and Stripe. '
             f'Contact contact@walyverse.com">')
    p.append(f'''<defs>
    <linearGradient id="bg" x1="0" y1="0" x2="220" y2="{H}" gradientUnits="userSpaceOnUse">
      <stop offset="0" stop-color="{c['bg'][0]}"/><stop offset=".17" stop-color="{c['bg'][1]}"/>
      <stop offset=".55" stop-color="{c['bg'][2]}"/><stop offset="1" stop-color="{c['bg'][3]}"/>
    </linearGradient>
    <radialGradient id="glow" cx="0" cy="0" r="1" gradientUnits="userSpaceOnUse"
      gradientTransform="translate(1010 40) scale(430)">
      <stop offset="0" stop-color="#A855F7" stop-opacity="{c['glow']}"/>
      <stop offset="1" stop-color="#A855F7" stop-opacity="0"/>
    </radialGradient>
    <radialGradient id="glow2" cx="0" cy="0" r="1" gradientUnits="userSpaceOnUse"
      gradientTransform="translate(120 300) scale(360)">
      <stop offset="0" stop-color="#6366F1" stop-opacity="{c['glow2']}"/>
      <stop offset="1" stop-color="#6366F1" stop-opacity="0"/>
    </radialGradient>
    <linearGradient id="word" x1="240" y1="90" x2="900" y2="190" gradientUnits="userSpaceOnUse">
      <stop offset="0" stop-color="{c['word'][0]}"/><stop offset=".45" stop-color="{c['word'][1]}"/>
      <stop offset="1" stop-color="{c['word'][2]}"/>
    </linearGradient>
    <linearGradient id="rule" x1="240" y1="0" x2="960" y2="0" gradientUnits="userSpaceOnUse">
      <stop offset="0" stop-color="{c['rule'][0]}" stop-opacity="{c['rule'][1]}"/>
      <stop offset="1" stop-color="{c['rule'][2]}" stop-opacity="0"/>
    </linearGradient>
    <linearGradient id="srule" x1="0" y1="0" x2="{W}" y2="0" gradientUnits="userSpaceOnUse">
      <stop offset="0" stop-color="{c['rule'][0]}" stop-opacity=".45"/>
      <stop offset="1" stop-color="{c['rule'][0]}" stop-opacity="0"/>
    </linearGradient>
    <linearGradient id="fline" x1="0" y1="0" x2="{W}" y2="0" gradientUnits="userSpaceOnUse">
      <stop offset="0" stop-color="{c['hair'][0]}" stop-opacity="0"/>
      <stop offset=".5" stop-color="{c['hair'][0]}" stop-opacity="{c['hair'][1]}"/>
      <stop offset="1" stop-color="{c['hair'][0]}" stop-opacity="0"/>
    </linearGradient>
    <linearGradient id="ftile" x1="80" y1="0" x2="124" y2="44" gradientUnits="userSpaceOnUse">
      <stop offset="0" stop-color="{c['ftile'][0]}"/><stop offset="1" stop-color="{c['ftile'][1]}"/>
    </linearGradient>
    <linearGradient id="fword" x1="142" y1="0" x2="262" y2="26" gradientUnits="userSpaceOnUse">
      <stop offset="0" stop-color="{c['fword'][0]}"/><stop offset="1" stop-color="{c['fword'][1]}"/>
    </linearGradient>
    <linearGradient id="fsep" x1="80" y1="0" x2="1120" y2="0" gradientUnits="userSpaceOnUse">
      <stop offset="0" stop-color="{c['furl']}" stop-opacity=".42"/>
      <stop offset="1" stop-color="{c['furl']}" stop-opacity="0"/>
    </linearGradient>
    <linearGradient id="fw" x1="132" y1="46" x2="290" y2="70" gradientUnits="userSpaceOnUse">
      <stop offset="0" stop-color="{c['fw'][0]}"/><stop offset="1" stop-color="{c['fw'][1]}"/>
    </linearGradient>
    <linearGradient id="cubeTop" x1="70" y1="100" x2="190" y2="170" gradientUnits="userSpaceOnUse">
      <stop offset="0" stop-color="#C084FC"/><stop offset="1" stop-color="#7C3AED"/>
    </linearGradient>
    <linearGradient id="cubeL" x1="70" y1="135" x2="130" y2="240" gradientUnits="userSpaceOnUse">
      <stop offset="0" stop-color="#6D28D9"/><stop offset="1" stop-color="#3B0F70"/>
    </linearGradient>
    <linearGradient id="cubeR" x1="190" y1="135" x2="130" y2="240" gradientUnits="userSpaceOnUse">
      <stop offset="0" stop-color="#8B5CF6"/><stop offset="1" stop-color="#4C1D95"/>
    </linearGradient>
    <filter id="soft" x="-30%" y="-30%" width="160%" height="160%">
      <feGaussianBlur stdDeviation="14" result="b"/>
      <feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
    <pattern id="grid" width="40" height="40" patternUnits="userSpaceOnUse">
      <path d="M40 0H0V40" fill="none" stroke="{c['grid'][0]}" stroke-opacity="{c['grid'][1]}" stroke-width="1"/>
    </pattern>
  </defs>''')

    for fill in ("url(#bg)", "url(#grid)", "url(#glow)", "url(#glow2)"):
        p.append(f'<rect width="{W}" height="{H}" rx="16" fill="{fill}"/>')

    p.append("""<style>
    .fl { animation: fl 7s ease-in-out infinite; }
    .f2 { animation-duration: 9s;  animation-delay: -3s; }
    .f3 { animation-duration: 11s; animation-delay: -6s; }
    @keyframes fl {
      0%, 100% { transform: translate(0, 0) }
      50%      { transform: translate(-8px, -20px) }
    }
    .tilt { animation: tilt 13s ease-in-out infinite;
            transform-box: fill-box; transform-origin: 50% 50%; }
    .t2 { animation-duration: 16s; animation-delay: -5s; }
    .t3 { animation-duration: 19s; animation-delay: -9s; }
    @keyframes tilt {
      0%, 100% { transform: rotate(-8deg) }
      50%      { transform: rotate(8deg) }
    }
    .dw { stroke-dasharray: 100; animation: dw 6s ease-in-out infinite; }
    @keyframes dw {
      0%   { stroke-dashoffset: 100 }
      32%  { stroke-dashoffset: 0 }
      68%  { stroke-dashoffset: 0 }
      100% { stroke-dashoffset: -100 }
    }
  </style>""")
    cubes = [
        (["M1040 92 1076 113 1040 134 1004 113Z", "M1004 113v42l36 21v-42",
          "M1076 113v42l-36 21"], "", 0.0),
        (["M1118 186 1142 200 1118 214 1094 200Z", "M1094 200v28l24 14v-28",
          "M1142 200v28l-24 14"], "2", 2.0),
        (["M952 214 976 228 952 242 928 228Z", "M928 228v28l24 14v-28",
          "M976 228v28l-24 14"], "3", 4.0),
    ]
    p.append(f'<g fill="none" stroke="{c["wire"][0]}" stroke-opacity="{c["wire"][1]}" '
             f'stroke-width="1.6" stroke-linejoin="round" opacity="{c["soft"]}">')
    for paths, n, phase in cubes:
        edges = "".join(
            f'<path class="dw" pathLength="100" d="{d}" '
            f'style="animation-delay:{phase + i * 0.22:.2f}s"/>'
            for i, d in enumerate(paths)
        )
        p.append(f'<g class="fl f{n or 1}"><g class="tilt t{n or 1}">{edges}</g></g>')
    p.append('</g>')

    p.append('''<g filter="url(#soft)">
    <path d="M130 100 190 135 130 170 70 135Z" fill="url(#cubeTop)"/>
    <path d="M70 135 130 170v70l-60-35Z" fill="url(#cubeL)"/>
    <path d="M190 135 130 170v70l60-35Z" fill="url(#cubeR)"/>
  </g>''')
    p.append(f'<path d="M130 100 190 135 130 170 70 135Z M70 135 130 170v70l-60-35Z '
             f'M190 135 130 170v70l60-35Z" fill="none" stroke="{c["cube_edge"][0]}" '
             f'stroke-opacity="{c["cube_edge"][1]}" stroke-width="1.5"/>')

    p.append(txt(243, 163, 82, "url(#word)", "WALYVERSE", SEMI, "700", "9",
                 extra=' textLength="632" lengthAdjust="spacingAndGlyphs"'))
    p.append('<rect x="245" y="186" width="700" height="2" rx="1" fill="url(#rule)"/>')
    p.append(txt(247, 222, 16.5, c["tagline"], "DISTRIBUTED SYSTEMS FOR LIVE GAME WORLDS",
                 SANS, "600", "4.6", opacity=".92",
                 extra=' textLength="553" lengthAdjust="spacingAndGlyphs"'))

    p.append(f'<g font-family="{SANS}" font-size="13.5" font-weight="600" letter-spacing="1.6" '
             f'lengthAdjust="spacingAndGlyphs">')
    for (x, w, label, tlen), (fo, so, tf), stroke in zip(PILLS, c["pill"], c["pill_stroke"]):
        p.append(f'<rect x="{x}" y="242" width="{w}" height="30" rx="15" fill="{stroke}" '
                 f'fill-opacity="{fo}" stroke="{stroke}" stroke-opacity="{so}"/>')
        p.append(f'<text x="{x + w / 2}" y="262" text-anchor="middle" textLength="{tlen}" '
                 f'fill="{tf}">{label}</text>')
    p.append('</g>')

    for i, line in enumerate(LEAD):
        p.append(txt(PAD, LEAD_Y + i * LEAD_STEP, 23, c["lead"], line, SANS, "400"))

    p.extend(section(c, PAD, STACK_Y, "BUILT WITH"))
    p.append(f'<g font-family="{SEMI}" font-size="19" font-weight="600" fill="{c["text"]}">')
    for i, (name, dot) in enumerate(zip(STACK, c["dots"])):
        x = PAD + 8 + (i % 5) * 213
        y = ROW1_Y if i < 5 else ROW2_Y
        p.append(f'<circle cx="{x}" cy="{y - 6}" r="6.5" fill="{dot}"/>'
                 f'<text x="{x + 22}" y="{y}">{name}</text>')
    p.append('</g>')

    p.extend(section(c, PAD, SEC1_Y, "THE PLATFORM"))
    col = (W - 2 * PAD) / 2
    for gi, (name, blurb, items) in enumerate(GROUPS):
        x = PAD + (gi % 2) * col
        top = GROUP_Y + (gi // 2) * BLOCK_STEP
        if gi % 2:
            p.append(f'<rect x="{x - 32}" y="{top - 26}" width="1" height="176" '
                     f'fill="{c["rule"][0]}" fill-opacity=".16"/>')
        p.append(txt(x, top, 17, c["name"], name, SEMI, "700", "2"))
        p.append(txt(x, top + 27, 16, c["body"], blurb, SANS))
        for ii, (item, desc) in enumerate(items):
            y = top + 64 + ii * ITEM_STEP
            p.append(f'<circle cx="{x + 4}" cy="{y - 5}" r="4" fill="{c["rule"][0]}" '
                     f'fill-opacity=".8"/>')
            p.append(txt(x + 20, y, 17, c["name"], item, SEMI, "600"))
            p.append(txt(x + 152, y, 16, c["body"], desc, SANS))

    p.append(f'<g transform="translate({PAD},{FERRY_Y - 19}) scale(1.15)">'
             f'<rect width="32" height="32" rx="9" fill="url(#ftile)"/>'
             f'<g fill="#fff">'
             f'<rect x="9" y="9.4" width="14" height="3.4" rx="1.7" opacity=".45"/>'
             f'<rect x="9" y="14.3" width="14" height="3.4" rx="1.7" opacity=".72"/>'
             f'<rect x="9" y="19.2" width="14" height="3.4" rx="1.7"/>'
             f'</g></g>')
    p.append(txt(134, FERRY_Y - 4, 22, "url(#fword)", "FERRY", SEMI, "700", "4.6",
                 extra=' textLength="92" lengthAdjust="spacingAndGlyphs"'))
    p.append(txt(135, FERRY_Y + 19, 14.5, c["fline2"], "Everything that keeps a fleet aligned",
                 SANS, "400", "1.1"))
    p.append(f'<rect x="{PAD}" y="{FERRY_Y + 38}" width="1040" height="1.5" rx=".75" '
             f'fill="url(#fsep)"/>')
    p.append(txt(PAD, FERRY_BODY, 19, c["name"], FERRY_LEAD, SEMI, "600"))
    for i, line in enumerate(FERRY):
        p.append(txt(PAD, FERRY_BODY + 36 + i * FERRY_STEP, 17, c["body"], line, SANS))
    p.append(txt(PAD, FERRY_BODY + 36 + len(FERRY) * FERRY_STEP + 10, 16, c["furl"],
                 "ferry.walyverse.fr", SEMI, "600", ".6"))

    p.extend(section(c, PAD, SEC3_Y, "HOW WE WORK"))
    p.append(f'<rect x="{PAD}" y="{MAXIM_Y - 25}" width="4" height="62" rx="2" '
             f'fill="{c["rule"][0]}" fill-opacity=".55"/>')
    p.append(txt(PAD + 26, MAXIM_Y, 22, c["quote"], MAXIM, SEMI, "600"))
    p.append(txt(PAD + 26, MAXIM_Y + 32, 22, c["quote"], MAXIM2, SEMI, "600"))
    for i, (name, desc) in enumerate(PRINCIPLES):
        x = PAD + (i % 2) * col
        y = PRINC_Y + (i // 2) * PRINC_STEP
        p.append(txt(x, y, 13, c["label"], name, SANS, "700", "2.6"))
        p.append(txt(x, y + 25, 16, c["body"], desc, SANS))

    p.append(f'<g transform="translate(0,{FOOT_TOP})">')
    p.append(f'<rect x="0" y="0" width="{W}" height="1.5" fill="url(#fline)"/>')
    p.append('<g transform="translate(80,47) scale(0.3) translate(-70,-100)">'
             '<path d="M130 100 190 135 130 170 70 135Z" fill="url(#cubeTop)"/>'
             '<path d="M70 135 130 170v70l-60-35Z" fill="url(#cubeL)"/>'
             '<path d="M190 135 130 170v70l60-35Z" fill="url(#cubeR)"/></g>')
    p.append(txt(132, 63, 19, "url(#fw)", "WALYVERSE", SEMI, "700", "4.5",
                 extra=' textLength="153" lengthAdjust="spacingAndGlyphs"'))
    p.append(txt(133, 86, 12.5, c["fsub"], "Distributed systems for live game worlds", SANS,
                 "400", "1.2", extra=' textLength="315" lengthAdjust="spacingAndGlyphs"'))
    p.append(txt(1120, 55, 11, c["label"], "CONTACT", SANS, "700", "4", anchor="end",
                 extra=' textLength="78" lengthAdjust="spacingAndGlyphs"'))
    p.append(txt(1120, 82, 17, c["email"], "contact@walyverse.com", SEMI, "600", anchor="end",
                 extra=' textLength="185" lengthAdjust="spacingAndGlyphs"'))
    p.append(txt(1120, 106, 12.5, c["fsub"], "walyverse.com, coming soon", SANS, "400", ".6",
                 anchor="end", extra=' textLength="172" lengthAdjust="spacingAndGlyphs"'))
    p.append(txt(80, 138, 11.5, c["muted"], "© 2026 Walyverse", SANS, "400", ".8"))
    p.append('</g>')
    p.append(f'<rect x="1" y="1" width="{W - 2}" height="{H - 2}" rx="16" fill="none" '
             f'stroke="{c["border"][0]}" stroke-opacity="{c["border"][1]}"/>')
    p.append('</svg>')
    return "\n".join(p)


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--repos", default="42", help="repository count shown in the first pill")
    ap.add_argument("--loc", default="360K+", help="line count shown in the second pill")
    args = ap.parse_args()

    for name, palette in (("card-dark", DARK), ("card-light", LIGHT)):
        (OUT / f"{name}.svg").write_text(
            build(palette, pills(args.repos, args.loc)), encoding="utf-8")
        print(f"{name}.svg written with {args.repos} repositories and {args.loc} lines")
