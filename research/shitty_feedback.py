# shitty feedback system v1

# stub
# returns tuple of ("metric_name [string]", pct_score)
class shitty_feedback:

    def get_highest_score(self):
        return ("articulation", 82.37)

    #- calc highest score (probably %)
    #    - feedback += 

    def get_lowest_score(self):
        return("movement", 32)

    def feedback(self):
        high = self.get_highest_score()
        low  = self.get_lowest_score ()

        articulation_explanation = "which means you spoke clearly and effectively conveyed your message."

        generic_positive_statement = "You did an excellent job with your {}, {}".format(high[0], articulation_explanation) + " Keep up the good work!\n"

        feedback = generic_positive_statement

        movement_explanation = "Moving around the stage effectively can help the audience to stay engaged and resonate with your message."

        generic_negative_statement = "Your {}".format(low[0]) + " fucking sucked, dude. Get the fuck out of here. {}\n".format(movement_explanation)

        feedback+="\n\n" + generic_negative_statement

        return feedback


my_shitty_feedback = shitty_feedback()
print(my_shitty_feedback.feedback())