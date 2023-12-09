import tkinter as tk
from typing import Type


class StudentGraderController:
    pass


class StudentGraderGUI:
    def __init__(self, master: tk.Tk, controller: Type[StudentGraderController]) -> None:
        """
        GUI class for the student grader application.

        Parameters:
            - master (tk.Tk): The root Tkinter window.
            - controller (Type[StudentGraderController]): The controller for the application.
        """
        self.master = master
        self.controller = controller
        self.master.title("Student Grader")

        self.master.geometry("500x350")

        self.master.resizable(False, False)

        self.label_students = tk.Label(self.master, text="Number of students:")
        self.label_students.pack()

        self.entry_students = tk.Entry(self.master)
        self.entry_students.pack()

        self.label_scores = tk.Label(self.master, text="Enter test scores (comma-separated):")
        self.label_scores.pack()

        self.text_scores = tk.Text(self.master, height=5, width=50)
        self.text_scores.pack()

        self.calculate_button = tk.Button(self.master, text="Calculate", command=self.controller.calculate_grades)
        self.calculate_button.pack()

        self.export_button = tk.Button(self.master, text="Export Data", command=self.controller.export_data)
        self.export_button.pack()

        #   Labels to display results
        self.label_best_score = tk.Label(self.master, text="Best Score:")
        self.label_best_score.pack()

        self.label_average_score = tk.Label(self.master, text="Average Score:")
        self.label_average_score.pack()

        #   Label to display error messages
        self.error_label = tk.Label(self.master, text="", fg="red")
        self.error_label.pack()

        #   Label to display export success message
        self.success_label = tk.Label(self.master, text="", fg="green")
        self.success_label.pack()

        #   Add the following lines to update the controller in the view
        self.controller = controller
        self.controller.view = self  # Connect the controller to the view

    def display_results(self, grade_list: list, average_score: float, best_score: int) -> None:
        """
        Display the calculated results.

        Parameters:
            - grade_list (list): List of grades for each student.
            - average_score (float): The average score of all students.
            - best_score (int): The highest score among all students.
        """
        #   Display results
        self.label_best_score.config(text=f"Best Score: {best_score}")
        self.label_average_score.config(text=f"Average Score: {average_score:.2f}")

    def display_error(self, error_message: str) -> None:
        """
        Display error messages.

        Parameters:
            - error_message (str): The error message to display.
        """
        # Display error messages
        self.error_label.config(text=error_message, fg="red")

    def display_success_message(self, success_message: str) -> None:
        """
        Display success messages.

        Parameters:
            - success_message (str): The success message to display.
        """
        #   Display success messages
        self.success_label.config(text=success_message, fg="green")
