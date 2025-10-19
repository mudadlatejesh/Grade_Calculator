import tkinter as tk
from tkinter import messagebox

# Function to calculate grade
def calculate_grade():
    try:
        # Get marks from input fields
        marks = [float(entry.get()) for entry in entries if entry.get() != ""]
        
        if not marks:
            messagebox.showerror("Error", "Please enter marks for all subjects!")
            return

        total = sum(marks)
        average = total / len(marks)

        # Determine grade
        if average >= 90:
            grade = "A+"
        elif average >= 80:
            grade = "A"
        elif average >= 70:
            grade = "B"
        elif average >= 60:
            grade = "C"
        elif average >= 50:
            grade = "D"
        else:
            grade = "F"

        # Display results
        result_label.config(text=f"Total: {total:.2f}\nAverage: {average:.2f}%\nGrade: {grade}")

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers for marks.")

# Create main window
root = tk.Tk()
root.title("Grade Calculator")
root.geometry("400x400")
root.config(bg="#0f0f0f")  # Dark mode background

# Title Label
title_label = tk.Label(root, text="🎓 Grade Calculator", font=("Helvetica", 18, "bold"), fg="#00FFCC", bg="#0f0f0f")
title_label.pack(pady=15)

# Create entry fields
entries = []
for i in range(5):
    frame = tk.Frame(root, bg="#0f0f0f")
    frame.pack(pady=5)
    tk.Label(frame, text=f"Subject {i+1} Marks:", fg="#FFFFFF", bg="#0f0f0f", font=("Helvetica", 12)).pack(side=tk.LEFT)
    entry = tk.Entry(frame, width=10, font=("Helvetica", 12))
    entry.pack(side=tk.LEFT, padx=10)
    entries.append(entry)

# Calculate Button
calc_button = tk.Button(root, text="Calculate Grade", font=("Helvetica", 12, "bold"),
                        bg="#00FFCC", fg="#000000", command=calculate_grade)
calc_button.pack(pady=20)

# Result Label
result_label = tk.Label(root, text="", font=("Helvetica", 14), fg="#00FFCC", bg="#0f0f0f")
result_label.pack(pady=10)

# Run app
root.mainloop()
