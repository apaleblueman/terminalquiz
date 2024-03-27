class QuizBrain:

    def __init__(self, qlist):
        self.qn = 0
        self.qlist = qlist
        self.score = 0

    def still_has_questions(self):
        return self.qn < len(self.qlist)

    def next_question(self):
        current_question = self.qlist[self.qn]
        self.qn += 1
        user_answer = input(f"Q:{self.qn}:{current_question.text}(T/F):")
        self.check_ans(user_answer, current_question.answer)

    def check_ans(self, usr_ans, crr_ans):
        if usr_ans.lower() == crr_ans.lower():
            print("You got it right!")
            self.score +=1
        else:
            print("That's wrong")
        print(f"Your current score is {self.score}/{self.qn}")