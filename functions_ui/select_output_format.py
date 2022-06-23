## Import libraries and functions
import tkinter


### RADIOBUTTONS 
## UI function to get the output file format
def get_output_format_radiobuttons():
    master = tkinter.Tk()
    master.geometry('350x120')
    master.title('Output format')
    master.resizable(False,False)
    out_type = tkinter.StringVar(None)
    out_type.set(None)
    selection_label = tkinter.Label(master)
    selection_label.config(text = 'Select the output file type')
    selection_label.pack()
    csv_radiobutton = tkinter.Radiobutton(master, text='CSV file(s)', variable=out_type, value='csv', command=lambda: get_output_format_from_ui(master, out_type), state='normal')
    csv_radiobutton.pack(anchor=tkinter.W)
    sheet_radiobutton = tkinter.Radiobutton(master, text='Spreadsheet file', variable=out_type, value='sheet', command=lambda: get_output_format_from_ui(master, out_type), state='normal')
    sheet_radiobutton.pack(anchor=tkinter.W)
    text_radiobutton = tkinter.Radiobutton(master, text='Text file', variable=out_type, value='text', command=lambda: get_output_format_from_ui(master, out_type), state='disabled')
    text_radiobutton.pack(anchor=tkinter.W)
    master.mainloop()

def get_output_format_from_ui(ui: tkinter.Tk, out_type: tkinter.StringVar):
    global output_type
    output_type = str(out_type.get())
    ui.destroy()
    print('Using output type: ' + output_type)
    #return(output_type)


### GET OUTPUT FORMAT
# Initialise variables
output_type = 'sheet'

# Get the authentication type selector
get_output_format_radiobuttons()