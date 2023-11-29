import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

# Function to update the bar chart
def update_bar_chart():
    data = [int(entry1.get()), int(entry2.get()), int(entry3.get())]
    bars = ('Bar 1', 'Bar 2', 'Bar 3')
    y_pos = range(len(bars))

    # Clear previous plot
    plt.clf()

    bar_color = color_var.get()
    width = float(width_var.get())
    chart_title = title_var.get()

    plt.bar(y_pos, data, align='center', alpha=0.5, color=bar_color, width=width)
    plt.xticks(y_pos, bars)
    plt.ylabel('Values')
    plt.title(chart_title)

    # Draw the updated plot
    bar_chart = FigureCanvasTkAgg(plt.gcf(), root)
    bar_chart.get_tk_widget().grid(row=3, columnspan=4)

# Create the main window
root = tk.Tk()
root.title('Customizable Bar Chart App')

# Entry fields to input data
label1 = tk.Label(root, text='Bar 1:')
label1.grid(row=0, column=0)
entry1 = tk.Entry(root)
entry1.grid(row=0, column=1)

label2 = tk.Label(root, text='Bar 2:')
label2.grid(row=1, column=0)
entry2 = tk.Entry(root)
entry2.grid(row=1, column=1)

label3 = tk.Label(root, text='Bar 3:')
label3.grid(row=0, column=2)
entry3 = tk.Entry(root)
entry3.grid(row=0, column=3)

# Bar color customization
color_label = tk.Label(root, text='Bar Color:')
color_label.grid(row=1, column=2)
color_var = tk.StringVar(root)
color_var.set('blue')  # Default color
color_entry = tk.Entry(root, textvariable=color_var)
color_entry.grid(row=1, column=3)

# Bar width customization
width_label = tk.Label(root, text='Bar Width:')
width_label.grid(row=2, column=0)
width_var = tk.StringVar(root)
width_var.set('0.5')  # Default width
width_entry = tk.Entry(root, textvariable=width_var)
width_entry.grid(row=2, column=1)

# Chart title customization
title_label = tk.Label(root, text='Chart Title:')
title_label.grid(row=2, column=2)
title_var = tk.StringVar(root)
title_entry = tk.Entry(root, textvariable=title_var)
title_entry.grid(row=2, column=3)

# Button to update the chart
update_button = tk.Button(root, text='Update Chart', command=update_bar_chart)
update_button.grid(row=3, column=0, columnspan=2)

# Initialize the bar chart
update_bar_chart()

# Run the main loop
root.mainloop()
