"""
Tinker 1B, Part 1: write an assert-based pytest test for session_rating()
BEFORE you touch anything else. One test is started for you -- add at least
one more.
"""

from scoring import session_rating
from scoring_helpers import apply_streak_bonus


def test_session_rating_boundary_90_is_great():
    assert session_rating(90) == "Great"


# TODO: add at least one more test, e.g. a boundary case for "Skip" (a score
# of 59) or the exact boundary for "Good" (a score of 80).
def test_session_rating_boundary_59_is_skipped():
    assert session_rating(59) == "Skip"

def test_session_rating_boundary_80_is_good():
    assert session_rating(80) == "Good"


def test_session_rating_boundary_70_is_ok():
    assert session_rating(70) == "OK"


def test_session_rating_boundary_60_is_meh():
    assert session_rating(60) == "Meh"


def test_session_rating_one_below_90_is_good():
    assert session_rating(89) == "Good"


def test_session_rating_one_below_80_is_ok():
    assert session_rating(79) == "OK"


def test_session_rating_one_below_70_is_meh():
    assert session_rating(69) == "Meh"


def test_session_rating_mid_bucket_values():
    assert session_rating(95) == "Great"
    assert session_rating(85) == "Good"
    assert session_rating(75) == "OK"
    assert session_rating(65) == "Meh"
    assert session_rating(10) == "Skip"


def test_session_rating_negative_score_is_skip():
    assert session_rating(-10) == "Skip"


def test_session_rating_over_100_is_great():
    assert session_rating(150) == "Great"


def test_apply_streak_bonus_adds_two_points_per_day():
    assert apply_streak_bonus(50, 3) == 56


def test_apply_streak_bonus_with_zero_streak_is_unchanged():
    assert apply_streak_bonus(70, 0) == 70


def test_apply_streak_bonus_caps_at_100():
    assert apply_streak_bonus(95, 5) == 100


def test_apply_streak_bonus_exactly_hits_100_uncapped():
    assert apply_streak_bonus(98, 1) == 100


def test_apply_streak_bonus_one_point_over_cap():
    assert apply_streak_bonus(99, 1) == 100