from tkinter import *
root = Tk()
root.title("تسعيرة الجنيه")
root.geometry("450x350")
price = {"دولار": 0.020, "يورو": 0.018, "ريال": 0.075}
def convert():
    value = entry.get()
    currency = var.get()
    try:
        egp = float(value)
        rate = price[currency]
        result = egp * rate
        result_label.config(text=f"القيمة: {result:.2f} {currency}")
    except:
        result_label.config(text="ادخل رقم صحيح")
Label(root, text=": المبلغ بالجنيه", font=("Arial", 12)).pack(pady=5)
entry = Entry(root, font=("Arial", 12))
entry.pack(pady=5)
Label(root, text=": اختار العملة", font=("Arial", 12)).pack(pady=5)
var = StringVar()
Radiobutton(root, text="دولار", font=("bold",15), variable=var, value="دولار" , bg="black",fg="red").pack()
Radiobutton(root, text="يورو", font=("bold",15), variable=var, value="يورو" ,bg="black", fg="red").pack()
Radiobutton(root, text="ريال", font=("bold",15), variable=var, value="ريال", bg="black", fg="red").pack()
Button(root, text="حول", font=("Arial", 17), width=30,bg="gray", command=convert).pack(pady=30)
result_label = Label(root, text="", font=("Arial", 12))
result_label.pack(pady=10)
root.mainloop()
