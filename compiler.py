# Module Imports
import subprocess   # Module to run external processes (In this case, pyinstaller)
import tkinter      # GUI toolkit used in this program
from tkinter import filedialog, messagebox

class PyToExeConverter(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.title("Python to EXE Converter") # Setting the title of the application window

        #Variable Declaration
        self.file_path = ""                             # Variable to store the path of the .py file
        self.compile_to_one_file = tkinter.BooleanVar() # Boolean variable for the "Compile to One File" option
        self.compile_to_one_file.set(False)             # Default variable value: False
        self.no_console = tkinter.BooleanVar()          # Boolean variable for the "No Console" option
        self.no_console.set(False)                      # Default variable value: False

        self.create_widgets() # Calls the GUI creation method

    def create_widgets(self):
        tkinter.Label(self, text="Select Python File:").pack()  # Label prompting users to select python file
        self.file_entry = tkinter.Entry(self, width=50)         # Widget displaying selected file path
        self.file_entry.pack(padx=5, pady=5)                    # Padding around the widget

        tkinter.Button(self, text="Browse", command=self.browse_file).pack(pady=5) #Button to select file directory

        # Checkboxes for selecting conversion settings
        tkinter.Checkbutton(self, text="Compile to One File", variable=self.compile_to_one_file).pack(pady=5)
        tkinter.Checkbutton(self, text="No Console", variable=self.no_console).pack(pady=5)

        tkinter.Button(self, text="Convert to EXE", command=self.convert_to_exe).pack(pady=5) # Button to start executable conversion process

    def browse_file(self):
        self.file_path = filedialog.askopenfilename(filetypes=[("Python files", "*.py")]) # Open file explorer for selecting Python file & store it's path
        # Displays the file path within the UI
        self.file_entry.delete(0, tkinter.END)
        self.file_entry.insert(0, self.file_path)

    def convert_to_exe(self):
        if not self.file_path: # Checks if no file selected prior to conversion
            messagebox.showerror("Error", "Please select a Python file.")
            return

        # Construct command arguments for PyInstaller based on inputs
        command_args = ["pyinstaller"]
        if self.compile_to_one_file.get():
            command_args.append("--onefile")
        if self.no_console.get():
            command_args.append("--noconsole")
        command_args.append(self.file_path)

        # Run PyInstaller with all the preferences
        subprocess.run(command_args)

        messagebox.showinfo("Success", "Conversion to EXE completed.") # Display messagebox indicating a successful conversion

# Starting the program
if __name__ == "__main__":
    app = PyToExeConverter()
    app.mainloop()