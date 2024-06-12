from tkinter import *
import calendar

def display_calendar():
    calendar_window = Tk()
    calendar_window.geometry("1000x1000")
    calendar_window.title("Calendar for the Selected Year")
    calendar_window.config(background = 'lightblue')
    
    selected_year = int(year_entry.get())
    calendar_content = calendar.calendar(selected_year)
    calendar_label = Label(calendar_window, text = calendar_content, font = ("Courier", 20), justify = LEFT)
    calendar_label.grid(row = 5, column = 1)
    calendar_window.mainloop()

if __name__ == '__main__':
    main_window = Tk()
    main_window.geometry("450x500")
    main_window.title("Year Calendar Application")
    main_window.config(background = 'lightblue')
    
    
    title_label = Label(main_window, text = "Year Calendar Application", font = ("Times", 35, "bold",))
    year_label = Label(main_window, text = "Enter Year: ", bg = 'orange', font = ("Times", 25, "bold"))
    year_entry = Entry(main_window, font = ("Times", 20, "bold"))
    show_button = Button(main_window, text = "Display Calendar", command = display_calendar, font = ("Times", 20, "bold"))
    exit_button = Button(main_window, text = "Exit", command = main_window.destroy, font = ("Times", 20, "bold"))
    
    title_label.grid(row = 1, column = 1)
    year_label.grid(row = 2, column = 1)
    year_entry.grid(row = 3, column = 1)
    show_button.grid(row = 4, column = 1)
    exit_button.grid(row = 5, column = 1)
    main_window.mainloop()
    


    
