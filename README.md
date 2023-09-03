# War Thunder Analysis
Analysis of War Thunder premium vehicles. Inspired by [this /r/warthunder post](https://www.reddit.com/r/Warthunder/comments/bltmwq/i_counted_how_much_would_every_premium_vehicle/).

Data can be found in [this Google Sheet](https://docs.google.com/spreadsheets/d/1bdOrNknNPzzmNbHoVuX71kgp6ljsx2lDcg_V8GTKbhE/edit?usp=sharing).

## Getting started

Install pyenv and required version from `.python-version`.

Install poetry.

Install dependencies:
```bash
poetry install
```

Make sure to enter virtualenv shell via Poetry before running scripts.
```bash
poetry shell
```

Note: For VSCode compatibility, make sure you are using the python interpretter from the virtualenv that Poetry creates.

## Running Jupyter Notebooks

You will need a way to run the Jupyter Notebooks included in this project (e.g. VSCode w/ Jupyter extension). The `jupyter` python package is included as a Poetry dependency for compatibility.
