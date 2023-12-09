class StudentGrader:
    def __init__(self, num_students: int) -> None:
        """
        Model class for the student grader.

        Parameters:
            - num_students (int): The initial number of students.
        """
        self.num_students = num_students
        self.scores = []

    def set_scores(self, scores: list) -> None:
        """
        Set the scores for the students.

        Parameters:
            - scores (list): List of test scores for the students.
        """
        self.scores = scores

    def calculate_grades(self) -> tuple:
        """
        Calculate grades, average score, and best score for the students.

        Returns:
            tuple: A tuple containing grade list, average score, and best score.
        """
        if not self.scores:
            #   Handle the case where there are no scores
            return [], None, None

        best_score = max(self.scores)
        grade_list = []

        for i, score in enumerate(self.scores):
            if score <= 60:
                grade = 'F'
            elif score < 70:
                grade = 'D'
            elif score < 80:
                grade = 'C'
            elif score < 90:
                grade = 'B'
            else:
                grade = 'A'
            grade_list.append(grade)

        average_score = sum(self.scores) / len(self.scores)

        return grade_list, average_score, best_score
