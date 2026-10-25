"""
Student Grade Processor Module
Contains core calculation functions and input validation.
"""

from typing import List, Dict, Union, Tuple


class InvalidScoreError(Exception):
    """Custom exception raised when a score is outside the valid range (0-100)."""
    pass


def validate_score(score: float) -> float:
    """
    Validates if the provided score is between 0 and 100.
    Raises InvalidScoreError if invalid.
    """
    if score < 0 or score > 100:
        raise InvalidScoreError(f"Invalid score: {score}. Score must be between 0 and 100.")
    return score


def calculate_average(scores: List[float]) -> float:
    """Calculates and returns the average score."""
    if not scores:
        return 0.0
    return sum(scores) / len(scores)


def get_highest_lowest(scores: List[float]) -> Tuple[float, float]:
    """Returns a tuple of (highest_score, lowest_score)."""
    if not scores:
        return 0.0, 0.0
    return max(scores), min(scores)


def determine_pass_fail(score: float, passing_grade: float = 50.0) -> str:
    """Determines whether a student passed or failed based on the passing threshold."""
    return "Pass" if score >= passing_grade else "Fail"


def process_student_records(records: List[Dict[str, Union[str, float]]]) -> Dict[str, Union[float, str, int]]:
    """
    Processes a list of student dictionary records and calculates aggregate metrics.
    Example record: {'name': 'Alice', 'score': 85.0}
    """
    if not records:
        return {}

    scores = [record['score'] for record in records]
    avg_score = calculate_average(scores)
    highest, lowest = get_highest_lowest(scores)
    
    passed_count = sum(1 for s in scores if determine_pass_fail(s) == "Pass")
    failed_count = len(scores) - passed_count

    return {
        "average": round(avg_score, 2),
        "highest": highest,
        "lowest": lowest,
        "total_students": len(records),
        "passed": passed_count,
        "failed": failed_count
    }

