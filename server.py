from flask import Flask, render_template, request
import os
import datetime

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATES_DIR = os.path.join(BASE_DIR, "templates")
SCORE_FILE = os.path.join(BASE_DIR, "scoreboard.txt")

app = Flask(__name__, template_folder=TEMPLATES_DIR)


def safe_get(form, key, default=""):
    return (form.get(key) or default).strip()


def append_score_entry(entry_text: str):
    with open(SCORE_FILE, "a", encoding="utf-8") as f:
        f.write(entry_text + "\n\n")


def determine_result(t1_name, t1_runs, t1_wk, t2_name, t2_runs, t2_wk):
    # Determine winner and margin
    try:
        r1 = int(t1_runs)
        r2 = int(t2_runs)
    except ValueError:
        return "Result: Invalid runs"

    if r1 > r2:
        margin = r1 - r2
        # If chasing, margin is runs; if second team all-out earlier, could be wickets but we keep runs margin
        return f"Result: {t1_name} won by {margin} runs"
    elif r2 > r1:
        margin = r2 - r1
        return f"Result: {t2_name} won by {margin} runs"
    else:
        return "Result: Match tied"


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/start", methods=["GET"])
def start():
    return render_template("start.html")


@app.route("/submit", methods=["POST"])
def submit():
    match_title = safe_get(request.form, "match_title")
    team1 = safe_get(request.form, "team1", "Team 1")
    team1_runs = safe_get(request.form, "team1_runs", "0")
    team1_wk = safe_get(request.form, "team1_wk", "")
    team1_overs = safe_get(request.form, "team1_overs", "")

    team2 = safe_get(request.form, "team2", "Team 2")
    team2_runs = safe_get(request.form, "team2_runs", "0")
    team2_wk = safe_get(request.form, "team2_wk", "")
    team2_overs = safe_get(request.form, "team2_overs", "")

    extras = safe_get(request.form, "extras", "")
    top_scorer = safe_get(request.form, "top_scorer", "")
    best_bowler = safe_get(request.form, "best_bowler", "")
    notes = safe_get(request.form, "notes", "")

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    title_line = f"Match: {match_title}" if match_title else f"Match: {team1} vs {team2}"

    # Build entry text
    entry_lines = [
        f"--- Scoreboard saved at {timestamp} ---",
        title_line,
        f"{team1}: {team1_runs} / {team1_wk} ({team1_overs})",
        f"{team2}: {team2_runs} / {team2_wk} ({team2_overs})"
    ]
    if extras:
        entry_lines.append(f"Extras: {extras}")
    if top_scorer:
        entry_lines.append(f"Top Scorer: {top_scorer}")
    if best_bowler:
        entry_lines.append(f"Best Bowler: {best_bowler}")
    if notes:
        entry_lines.append(f"Notes: {notes}")

    # Determine and append result summary
    result_text = determine_result(team1, team1_runs, team1_wk, team2, team2_runs, team2_wk)
    entry_lines.append(result_text)

    entry_text = "\n".join(entry_lines)
    append_score_entry(entry_text)

    saved_msg = f"Saved: {team1} {team1_runs}/{team1_wk} — {team2} {team2_runs}/{team2_wk}  @ {timestamp}"
    return render_template("start.html", saved=saved_msg)


@app.route("/scores", methods=["GET"])
def scores():
    if not os.path.exists(SCORE_FILE):
        content = "(No saved scoreboards yet)"
    else:
        with open(SCORE_FILE, "r", encoding="utf-8") as f:
            content = f.read().strip() or "(No saved scoreboards yet)"
    return render_template("scores.html", content=content)


if __name__ == "_main_":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)