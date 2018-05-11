import tkinter as tk
root = tk.Tk()
from ConvertXMLToCSV import ConvertXMLToCSV
from GenerateReport import GenerateReport
import subprocess
import os
import time

root.title("Summit Ultra Endurance Coaching")
logo = tk.PhotoImage(file="./images/Logo_Summit_Final_Nobackground_Black.gif")

tk.Label(root, text="Automated Report Generator").pack()
tk.Label(root, image=logo).pack(side="right")

first_name = tk.StringVar()

tk.Label(root, text="First Name").pack()
first_name_entry = tk.Entry(root)
first_name_entry.pack()
tk.Label(root, text="Last Name").pack()
last_name_entry = tk.Entry(root)
last_name_entry.pack()

tk.Label(root, text="Date (yyyy_mm_dd)").pack()
date_entry = tk.Entry(root)
date_entry.pack()

tk.Label(root, text="XML File Name").pack()
xml_file_entry = tk.Entry(root)
xml_file_entry.pack()

tk.Label(root, text="Is this a running file?").pack()
v = tk.IntVar()
yes_button = tk.Radiobutton(root, text="Yes", padx=20, variable=v, value=1)
yes_button.pack(anchor=tk.CENTER)
no_button = tk.Radiobutton(root, text="No", padx=20, variable=v, value=0)
no_button.pack(anchor=tk.CENTER)

def generate_report(event):
    athlete_name = first_name_entry.get() + "_" + last_name_entry.get()

    input_file_name = "./xml/" + xml_file_entry.get()

    is_running_file = True if v.get() else False

    date = date_entry.get()

    output_file_name_base = ("Running_Outline_" if is_running_file else "Biking_Outline_") \
                        + athlete_name \
                        + "_" \
                        + date

    output_file_name = output_file_name_base + ".tex"

    input_csv_file_name = athlete_name + "_" \
                          + ("running_data_" if is_running_file else "biking_data_") \
                          + date \
                          + ".csv"

    ConvertXMLToCSV().XML_to_CSV(input_file_name, input_csv_file_name, is_running_file=is_running_file)

    GenerateReport().generate_report(input_csv_file_name, output_file_name, athlete_name, is_running_file, date)

    subprocess.Popen(["make", ("tex_file=" + output_file_name)], env=os.environ)

    # Let LATEX finish
    time.sleep(5)

    # Clear Widgets
    first_name_entry.delete(0, "end")
    last_name_entry.delete(0, "end")
    date_entry.delete(0, "end")
    xml_file_entry.delete(0, "end")

    # Move the newly generated files to the right folders
    os.rename(output_file_name, ("./tex/" + output_file_name))
    os.rename((output_file_name_base + ".pdf"), ("./reports/" + output_file_name_base + ".pdf"))
    os.rename(input_csv_file_name, ("./csv/" + input_csv_file_name))

    print("Removing Files")
    os.remove(output_file_name_base + ".aux")
    os.remove(output_file_name_base + ".log")
    print("Files Removed")


generate_report_button = tk.Button(root, text='GENERATE REPORT', width=25)
generate_report_button.pack()
generate_report_button.bind("<Button-1>", generate_report)

root.mainloop()