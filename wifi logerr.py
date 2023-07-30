import subprocess
import tkinter as tk

def show_passwords():
    try:
        data = subprocess.check_output("netsh wlan show profiles").decode('cp866').split('\n')
        profiles = [i.split(":")[1][1:-1] for i in data if "Все профили пользователей" in i] 
        pass_wifi = '' 
        for i in profiles:
            results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('cp866').split('\n')
            for j in results:
                if "Содержимое ключа" in j:
                    pass_wifi += f"{i} -- {j.split(':')[1][1:-1]}\n"

        password_text.delete(1.0, tk.END)
        password_text.insert(tk.END, pass_wifi)
    except Exception as ex:
        password_text.delete(1.0, tk.END)
        password_text.insert(tk.END, f"Ошибка: {ex}")

def add_network():
    subprocess.call('start ms-settings:network-wifi')
    print("тЫ ЧЕ")

root = tk.Tk()
root.title('Просмотр паролей Wi-Fi')

password_label = tk.Label(root, text='Пароли Wi-Fi:')
password_label.grid(row=0, column=0, sticky='w', padx=10, pady=10)

password_text = tk.Text(root, width=50, height=10)
password_text.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

show_button = tk.Button(root, text='Показать пароли', command=show_passwords)
show_button.grid(row=2, column=0, padx=10, pady=10)

add_button = tk.Button(root, text='Добавить сеть', command=add_network)
add_button.grid(row=2, column=1, padx=10, pady=10)

exit_button = tk.Button(root, text='Выход', command=root.quit)
exit_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()
