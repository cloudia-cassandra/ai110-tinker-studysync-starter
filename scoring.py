"""
StudySync -- Session Scorer (Ticket 1, Tinker 1B).

TICKET: apply_streak_bonus() works but shouldn't live here -- it belongs in
the shared scoring_helpers module. session_rating() has no test coverage,
and neither function has been checked against bad input.

1. Write a pytest test for session_rating() BEFORE touching anything broken.
2. Move apply_streak_bonus() into scoring_helpers.py and fix the import here.
3. Find 2-3 "breaker" inputs for session_rating() and decide if they need handling.
"""
# apply_streak_bonus now lives in scoring_helpers.py; import it so
# run_demo() and render_session_scorer_tab() below can still call it by name.
from scoring_helpers import apply_streak_bonus


def session_rating(combined_score: int) -> str:
    """Rate a study session from its combined minutes+focus score. Correct and tested."""
    # NOTE: `: int` above is just a type hint -- Python never checks it at
    # runtime. Passing a float like 87.5 works fine because `>=` compares
    # ints and floats normally; nothing here actually requires an int.
    if combined_score >= 90:
        return "Great"
    if combined_score >= 80:
        return "Good"
    if combined_score >= 70:
        return "OK"
    if combined_score >= 60:
        return "Meh"
    return "Skip"


def render_session_scorer_tab():
    import streamlit as st

    st.subheader("Score a Session")
    minutes = st.slider("Minutes studied", 0, 60, 30)
    focus = st.slider("Focus (0-60)", 0, 60, 30)
    streak = st.number_input("Current streak (days)", min_value=0, value=0, step=1)

    combined = minutes + focus
    boosted = apply_streak_bonus(combined, streak)
    rating = session_rating(boosted)
    st.metric("Rating", rating, help=f"Combined {combined} -> boosted {boosted}")


def run_demo():
    sessions = [55, 68, 82, 91, 77]
    streak = 3
    for raw in sessions:
        boosted = apply_streak_bonus(raw, streak)
        rating = session_rating(boosted)
        print(f"Raw: {raw} -> Boosted: {boosted} -> Rating: {rating}")

    # Breaker inputs for session_rating() -- checking what happens with
    # values that shouldn't normally occur but aren't blocked by the code.
    print(session_rating(-10))
    # -> "Skip": falls through every >= check and hits the final return.
    # Negative scores are treated as just "very bad", not as an error.

    print(session_rating(150))
    # -> "Great": matches the first check (>= 90) and returns right away.
    # There's no upper bound, so any score above 90 is "Great" no matter
    # how far above -- 150 and 9000 behave the same.

    print(session_rating(87.5))
    # -> "Good": matches the >= 80 check. The `int` type hint on
    # combined_score is not enforced at runtime, so a float compares
    # fine with `>=` and flows through like any other number.


if __name__ == "__main__":
    run_demo()
