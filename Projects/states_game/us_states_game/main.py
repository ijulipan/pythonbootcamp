import turtle
import pandas

data = pandas.read_csv(r"Projects\states_game\us_states_game\50_states.csv")
data_state = data["state"].to_list()

screen = turtle.Screen()
screen.title("U.S States Game")
image = r"Projects\states_game\us_states_game\blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


correct_guess = []


while len(correct_guess) < 50:
    answer_state = screen.textinput(title=f"{len(correct_guess)}/50 States Correct", prompt="What's another state's name?").title()

# Exit command to exit the while loop and creates a missing states csv file
    if answer_state == "Exit":
        missing_states = []
        missing_states = [state for state in data_state if state not in correct_guess]
        # for state in data_state:
        #     if state not in correct_guess:
        #         missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv(r"Projects\states_game\us_states_game\states_to_learn.csv")
        break

#Check guess is among 50 states
    if answer_state in data_state:
        correct_guess.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(answer_state)
