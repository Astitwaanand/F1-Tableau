# F1 Race Intelligence

A Formula 1 analytics project combining an interactive Tableau Public workbook with a Flask website that embeds two dashboards and a six-point Tableau story.

## Repository layout

- `workbook/F1_Race_Intelligence.twbx` — packaged Tableau workbook with its embedded extracts.
- `data/` — five source CSV datasets used for race, lap, qualifying, circuit, and championship analyses.
- `website/` — Flask application and templates/static assets for the Tableau Public embeds.
- `documentation/` — reserved for the project report and supporting documentation.

## Tableau Public views

- [Race Intelligence Story](https://public.tableau.com/app/profile/astitwa.anand/viz/F1_Race_IntelligenceStory/Story1)
- [Reliability & Championships Dashboard](https://public.tableau.com/app/profile/astitwa.anand/viz/F1_Race_IntelligenceDashBoard1/ReliabilityChampionships)
- [Strategy & Talent Dashboard](https://public.tableau.com/app/profile/astitwa.anand/viz/F1_Race_IntelligenceDashBoard2/StrategyTalent)

## Run the website locally

Requirements: Python 3.10 or newer.

```powershell
cd website
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
Copy-Item .env.example .env
python app.py
```

Open `http://127.0.0.1:5000`. Set the following Tableau Public view URLs in `website/.env` (the file is ignored by Git):

- `TABLEAU_STORY_URL`
- `TABLEAU_RELIABILITY_URL`
- `TABLEAU_STRATEGY_URL`

## Deploy with Vercel

Import this GitHub repository into Vercel and set the project **Root Directory** to `website`. Add the three environment variables above in Vercel Project Settings, then deploy. The Flask entry point and Python requirements are in `website/`.

## Analysis scope

The report explores driver performance, constructors' championship trajectories, tyre compound strategy, circuit and host-country participation, podium outcomes, and driver reliability / DNF patterns. Intended audiences include team strategists, race engineers, motorsport journalists, FIA analysts, and F1 fans.
