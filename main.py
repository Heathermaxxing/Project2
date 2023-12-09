import tkinter as tk
from student_grader_model import StudentGrader
from student_grader_view import StudentGraderGUI
from student_grader_controller import StudentGraderController


def main() -> None:
    """
    Main function to initialize the GUI application.
    """
    root = tk.Tk()
    model = StudentGrader(0)
    controller = StudentGraderController(model, None)
    view = StudentGraderGUI(root, controller)
    controller.view = view

    root.mainloop()


if __name__ == "__main__":
    main()
