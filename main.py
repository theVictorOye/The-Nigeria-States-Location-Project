import turtle
import pandas
import  time

screen = turtle.Screen()
screen.tracer(0)
screen.setup(width= 730, height= 580)
screen.title("Enter a Nigerian State Below to see its location")
background = "nigeria_states_map.gif"
screen.addshape(background)
turtle.shape(background)

all_entered_states = []
all_text_position = []
abuja_xcor = -90
abuja_ycor = -2
text_font = ("Courier", 10, "normal")

states_data = pandas.read_csv("ng_states.csv")
states_df = pandas.DataFrame(states_data)
states_list = states_df.ng_state.tolist()

while len(all_entered_states) < len(states_list):

    screen.update()
    time.sleep(0.01)

    fct_abuja =turtle.Turtle()
    fct_abuja.hideturtle()
    fct_abuja.penup()
    fct_abuja.goto(abuja_xcor, abuja_ycor)
    fct_abuja.write("Abuja", font= text_font)
    fct_abuja.goto(abuja_xcor, abuja_ycor - 8)
    fct_abuja.dot()

    user_input = screen.textinput(title=f"{len(all_entered_states)}/36 states", prompt="Enter a State").title()
    if user_input == "Exit":
        break

    if user_input in states_list:
        if user_input not in all_entered_states:
            all_entered_states.append(user_input)

        text = turtle.Turtle()
        text.penup()
        text.hideturtle()
        frame_count = states_df[states_df.ng_state == user_input]
        x_cor = int(frame_count.X_cor.item())
        y_cor = int(frame_count.Y_cor.item())

        if (x_cor, y_cor) not in all_text_position:
            all_text_position.append((x_cor, y_cor))
            text.goto(x_cor, y_cor)
            text.write(user_input, font=text_font)
            text.goto(x_cor, y_cor - 10)
            text.dot()
            print(user_input)

screen.exitonclick()