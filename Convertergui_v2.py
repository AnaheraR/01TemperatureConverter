from tkinter import Tk, Frame, Label, Entry, Button, StringVar


class Stringvar:
    def set(self, param):
        pass


class Converter:

    def __init__(self):

        # Initialise variables (such as the feedback variable)
        self.var_feedback = StringVar()
        self.var_feedback.set("")
        
        self.var_has_error = Stringvar()
        self.var_has_error.set("no")

        # common format for all buttons
        # Arial size 14 bold, with white text
        button_font = ("Arial", "12", "bold")
        button_fg = "#FFFFFF"

        # Set up GUI Frame
        global root
        self.temp_instructions = None
        self.temp_frame = Frame()
        self.temp_frame.grid()

        self.temp_heading = Label(self.temp_frame,
                                  text="Temperature Converter",
                                  font=("Arial", "16", "bold")
                                  )
        self.temp_heading.grid(row=0)

        instructions = "Please enter a temperature below and " \
                       "then press one of the buttons to convert " \
                       "it from centigrade to Fahrenheit."
        self.temp_instructions = Label(self.temp_frame,
                                       text=instructions,
                                       wraplength=250, width=40,
                                       justify="left")
        self.temp_instructions.grid(row=1)

        self.temp_entry = Entry(self.temp_frame,
                                font=("Arial", "14")
                                )
        self.temp_entry.grid(row=2, padx=10, pady=10)

        error = "Please enter a number"
        self.temp_error = Label(self.temp_frame, text="",
                                fg="#9c0000")
        self.temp_error.grid(row=3)

        # Conversion, help and history / export buttons
        self.button_frame = Frame(self.temp_frame)
        self.button_frame.grid(row=4)

        self.to_celsius_button = Button(self.button_frame,
                                        text="To Degrees C",
                                        bg="#990099",
                                        fg=button_fg,
                                        font=button_font, width=12,
                                        command=self.to_celsius)
        self.to_celsius_button.grid(row=0, column=0, padx=5, pady=5)

        self.to_fahrenheit_button = Button(self.button_frame,
                                           text="To Fahrenheit",
                                           bg="#009900",
                                           fg=button_fg,
                                           font=button_font, width=12)
        self.to_fahrenheit_button.grid(row=0, column=1, padx=5, pady=5)

        self.to_help_button = Button(self.button_frame,
                                     text="Help / Info",
                                     bg="#cc6600",
                                     fg=button_fg,
                                     font=button_font, width=12)
        self.to_help_button.grid(row=1, column=0, padx=5, pady=5)

        from tkinter import DISABLED
        self.to_history_button = Button(self.button_frame,
                                        text="History / Export",
                                        bg="#004c99",
                                        fg=button_fg,
                                        font=button_font, width=12,
                                        state=DISABLED)
        self.to_history_button.grid(row=1, column=1, padx=5, pady=5)

    def check_temp(self, min_value):

        has_error = "No"
        error = f"Please enter a number that is more than {min_value}"

        # check that use has entered a valid number...

        response = self.temp_entry.get()

        try:
            response = self.temp_entry.get()
            response = float(response)

            if response < min_value:
                has_error = "Yes"

        except ValueError:
            has_error = "Yes"

        # Sets var_has_error so that entry box and
        # label can be correctly formatted by formatting function
        if has_error == "Yes":
            self.var_has_error.set("Yes")
            self.var_feedback.set(error)
            return "Invalid"

        # If we have no errors...
        else:
            # set to 'no' in case of previous errors
            self.var_has_error.set("no")

            # return number to be
            # converted and enable history button
            self.to_history_button.config(state="normal")
            return response

    # check temperature is more than -459 and convert it
    def to_celsius(self):

        self.check_temp(-459)

    # shows user output

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    Converter()
    root.mainloop()
