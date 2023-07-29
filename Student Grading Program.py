def calculate_grade(marks):
    if marks >= 90:
        return "A+"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 50:
        return "D"
    else:
        return "Fail"

def get_valid_marks():
    while True:
        try:
            marks = int(input("Enter the marks obtained by the student: "))
            if marks < 0 or marks > 100:
                print("Invalid marks. Marks should be between 0 and 100.")
            else:
                return marks
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def main():
    while True:
        print("\n--- Student Grading Program ---")
        marks = get_valid_marks()
        grade = calculate_grade(marks)
        print(f"Grade: {grade}")

        repeat = input("Do you want to calculate the grade for another student? (yes/no): ").lower()
        if repeat != "yes":
            print("Exiting the program.")
            break

if __name__ == "__main__":
    main()
