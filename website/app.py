"""Flask shell for the published F1 Race Intelligence Tableau views."""

from __future__ import annotations

import os
from urllib.parse import urlparse

from flask import Flask, abort, render_template
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__, static_folder="public", static_url_path="")

STORY_POINTS = [
    {"index": 0, "title": "Reliability & Championships", "detail": "Season completion, podiums, constructor progress and headline KPIs."},
    {"index": 1, "title": "Strategy & Talent", "detail": "Circuit footprint, tyre choices, team failures and driver standings."},
    {"index": 2, "title": "Circuit Footprint", "detail": "Compare Grand Prix circuit participation across host countries."},
    {"index": 3, "title": "DNF Failure Patterns", "detail": "Explore recorded failure types across constructor teams."},
    {"index": 4, "title": "Tyre Strategy", "detail": "Inspect recorded compound sequences and strategy patterns."},
    {"index": 5, "title": "Driver Points", "detail": "Compare cumulative driver points in the leaderboard."},
]

VIEWS = {
    "strategy": {
        "title": "Strategy & Talent",
        "eyebrow": "DASHBOARD 01",
        "description": "Circuit footprint, tyre strategy, team DNF patterns and the driver leaderboard.",
        "url": os.environ.get("TABLEAU_STRATEGY_URL", "").strip(),
        "external_url": os.environ.get("TABLEAU_STRATEGY_URL", "").strip(),
    },
    "reliability": {
        "title": "Reliability & Championships",
        "eyebrow": "DASHBOARD 02",
        "description": "Season DNF trend, driver podiums, constructor points and F1 season KPIs.",
        "url": os.environ.get("TABLEAU_RELIABILITY_URL", "").strip(),
        "external_url": os.environ.get("TABLEAU_RELIABILITY_URL", "").strip(),
    },
    "story": {
        "title": "Race Intelligence Story",
        "eyebrow": "SIX STORY POINTS",
        "description": "Move through the strategy, reliability and performance narrative using the point selector.",
        "url": os.environ.get("TABLEAU_STORY_URL", "").strip(),
        "external_url": os.environ.get("TABLEAU_STORY_URL", "").strip(),
    },
}


def is_tableau_public_url(value: str) -> bool:
    """Only allow HTTPS Tableau Public view links in embedded iframes/components."""
    parsed = urlparse(value)
    is_public_host = parsed.hostname == "public.tableau.com"
    is_view_path = parsed.path.startswith("/views/") or parsed.path.startswith("/app/profile/")
    return parsed.scheme == "https" and is_public_host and is_view_path


@app.context_processor
def inject_navigation():
    return {"views": VIEWS}


@app.get("/")
def home():
    return render_template("index.html", active="home", story_points=STORY_POINTS)


@app.get("/dashboard/<view_key>")
def dashboard(view_key: str):
    if view_key not in {"strategy", "reliability"}:
        abort(404)
    view = VIEWS[view_key]
    return render_template(
        "view.html",
        active=view_key,
        view=view,
        view_key=view_key,
        embed_url=view["url"] if is_tableau_public_url(view["url"]) else "",
        story_points=STORY_POINTS,
    )


@app.get("/story")
def story():
    view = VIEWS["story"]
    return render_template(
        "view.html",
        active="story",
        view=view,
        view_key="story",
        embed_url=view["url"] if is_tableau_public_url(view["url"]) else "",
        story_points=STORY_POINTS,
    )


@app.get("/healthz")
def healthz():
    return {"status": "ok"}


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=int(os.environ.get("PORT", "5000")), debug=os.environ.get("FLASK_DEBUG") == "1")

