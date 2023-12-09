import tkinter as tk
from student_grader_model import StudentGrader


class StudentGraderController:
    def __init__(self, model: "StudentGrader", view) -> None:
        """
        Controller class for the student grader application.

        Parameters:
            - model (StudentGrader): The model representing the student grader.
            - view: The view representing the user interface.
        """
        self.model = model
        self.view = view

    def calculate_grades(self) -> None:
        """
        Calculate grades based on user input and update the view with the results.
        """
        try:
            self.view.display_error("")

            num_students = int(self.view.entry_students.get())
            if num_students <= 0:
                raise ValueError("Number of students must be greater than 0")

            scores_input = self.view.text_scores.get("1.0", tk.END)
            scores = [int(score.strip()) for score in scores_input.split(',') if score.strip()]

            if len(scores) != num_students:
                raise ValueError("Number of test scores entered does not match the number of students")

            self.model.set_scores(scores)
            grade_list, average_score, best_score = self.model.calculate_grades()
            self.view.display_results(grade_list, average_score, best_score)

        except ValueError as e:
            self.view.display_error(str(e))

    def export_data(self) -> None:
        """
        Export calculated data to a text file and display success or error messages.
        """
        try:
            self.view.display_error("")

            num_students = int(self.view.entry_students.get())
            if num_students <= 0:
                raise ValueError("Number of students must be greater than 0")

            scores_input = self.view.text_scores.get("1.0", tk.END)
            scores = [int(score.strip()) for score in scores_input.split(',') if score.strip()]

            if len(scores) != num_students:
                raise ValueError("Number of test scores entered does not match the number of students")

            self.model.set_scores(scores)
            grade_list, average_score, best_score = self.model.calculate_grades()

            with open("student_grades.txt", "w") as file:
                for i, grade in enumerate(grade_list):
                    file.write(f"Student {i + 1} - Grade: {grade}\n")
                file.write("================\n")
                file.write(f"The average score is {average_score:.2f}, with the best score being {best_score}")

            self.view.display_success_message("Data exported to student_grades.txt")

        except ValueError as e:
            self.view.display_error(str(e))
