"""
Main Execution CLI for Student Grade Processor
Imports modular logic from grade_processor module.
"""

from grade_processor import (
    validate_score,
    process_student_records,
    determine_pass_fail,
    InvalidScoreError
)


def main():
    print("=" * 50)
    print("     STUDENT GRADE PROCESSOR SYSTEM")
    print("=" * 50)

    students = []

    while True:
        name = input("\nEnter student name (or type 'done' to finish): ").strip()
        if name.lower() == 'done':
            break
        
        if not name:
            print("Student name cannot be empty. Try again.")
            continue

        while True:
            try:
                raw_score = float(input(f"Enter score for {name} (0 - 100): "))
                score = validate_score(raw_score)
                break
            except ValueError:
                print("Error: Please enter a valid numerical value.")
            except InvalidScoreError as e:
                print(f"Error: {e}")

        status = determine_pass_fail(score)
        students.append({'name': name, 'score': score, 'status': status})
        print(f"Added: {name} | Score: {score} | Status: {status}")

    if not students:
        print("\nNo student records entered. Exiting program.")
        return

    summary = process_student_records(students)

    print("\n" + "=" * 50)
    print("             FINAL GRADE REPORT")
    print("=" * 50)
    print(f"{'Name':<20} | {'Score':<10} | {'Status':<10}")
    print("-" * 50)
    for student in students:
        print(f"{student['name']:<20} | {student['score']:<10.2f} | {student['status']:<10}")

    print("-" * 50)
    print(f"Total Students Processed : {summary['total_students']}")
    print(f"Class Average Score      : {summary['average']}")
    print(f"Highest Score            : {summary['highest']}")
    print(f"Lowest Score             : {summary['lowest']}")
    print(f"Passed Students          : {summary['passed']}")
    print(f"Failed Students          : {summary['failed']}")
    print("=" * 50)


if __name__ == "__main__":
    main()
