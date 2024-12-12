import tkinter as tk

# Создаем основное окно
window = tk.Tk()
window.title("Clicker")
window.geometry("1300x700")

# Инициализация счетчика и множителя кликов
count = 0
click_multiplier = 1

# Метка для отображения количества кликов
clicks_label = tk.Label(window, text=str(count), font='Arial 50')
clicks_label.pack()

# Загрузка изображения печенья для кнопки
cookie_image = tk.PhotoImage(file="C:/Users/Admin/Downloads/Cookie.png")

# Функция обработки кликов
def on_button_click():
    global count
    count += click_multiplier
    clicks_label.config(text=str(count))

# Функция для улучшения множителя кликов
def on_click_2():
    global count, click_multiplier
    if count >= 100:
        count -= 100
        click_multiplier += 1
        clicks_label.config(text=str(count))
    else:
        print("Недостаточно очков для улучшения!")

# Кнопка для улучшения множителя кликов
upgrade_button = tk.Button(window, text='one click = +1\n   Cost 100', width=20, font='Arial 20', command=on_click_2)
upgrade_button.place(x=50, y=10)

# Кнопка с изображением печенья
cookie_button = tk.Button(window, image=cookie_image, command=on_button_click)
cookie_button.pack(padx=10, pady=10)

# Запуск основного цикла
window.mainloop()
