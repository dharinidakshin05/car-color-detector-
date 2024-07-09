import tkinter as tk
class CarClassifier:
    def __init__(self, window):
        self.window = window
        self.window.title("Car Classifier")
        self.color_label = tk.Label(window, text="Car Color:")
        self.color_label.pack()
        self.color_entry = tk.Entry(window)
        self.color_entry.pack()

        self.count_label = tk.Label(window, text="Car Count:")
        self.count_label.pack()
        self.count_entry = tk.Entry(window)
        self.count_entry.pack()
        

        self.gender_label = tk.Label(window, text="gender")
        self.gender_label.pack()
        self.gender_entry = tk.Entry(window)
        self.gender_entry.pack()
        self.button = tk.Button(window, text="Classify", command=self.classify_cars)
        
        self.button.pack()
        self.classification_label = tk.Label(window, text="")
        self.classification_label.pack()

    def classify_cars(self):
        color = self.color_entry.get()
        count = self.count_entry.get()

        if color.lower() == "red":
            color = "blue"  
        elif color.lower() == "blue":
            color = "red"  

        self.classification_label.config(text=f"The car is {color} and there are {count} cars ")

window = tk.Tk()
classifier = CarClassifier(window)
window.mainloop()
#print("Predicted other vehicles:", ["1-2", "3-4"][other_vehicles])
