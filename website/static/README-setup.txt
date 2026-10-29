TABLEAU PUBLIC VIEW SETUP

Copy .env.example to .env, then set the three view URLs:

TABLEAU_STRATEGY_URL=https://public.tableau.com/views/WorkbookName/StrategyView
TABLEAU_RELIABILITY_URL=https://public.tableau.com/views/WorkbookName/ReliabilityView
TABLEAU_STORY_URL=https://public.tableau.com/views/WorkbookName/StoryView

Use Tableau Public's Share > Copy Link for each view. Restart Flask after changing .env.
