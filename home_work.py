import matplotlib.pyplot as plt

# Формируем список из файла
def read_sales_data(file_path):
    with open(file_path, "r", encoding='utf-8') as file:
        file = file.read()
        sales_data = []
        for x in range(len(file.split("\n"))):
            sales_data.append(file.split("\n").pop(x).split(","))
    return sales_data

# Формируем словарь продаж в разрезе продуктов
def total_sales_per_product(sales_data):
    product_dict = {}
    for x in range(len(sales_data)):
        if sales_data[x][0] in product_dict.keys():
            product_dict[f"{sales_data[x][0]}"] += int(sales_data[x][1]) * int(sales_data[x][2])
        else:
            product_dict[f"{sales_data[x][0]}"] = int(sales_data[x][1]) * int(sales_data[x][2])
    return product_dict

# Формируем словарь продаж в разрезе дат
def sales_over_time(sales_data):
    date_dict = {}
    for x in range(len(sales_data)):
        if sales_data[x][0] in date_dict.keys():
            date_dict[f"{sales_data[x][3]}"] += int(sales_data[x][1]) * int(sales_data[x][2])
        else:
            date_dict[f"{sales_data[x][3]}"] = int(sales_data[x][1]) * int(sales_data[x][2])
    return date_dict

# Запуск программы
def start():
    file_path = "C:\\Users\\new\\PycharmProjects\\pythonProject\\venv\\home_work.txt" #Путь к файлу
    sales_data = read_sales_data(file_path)
    sales_product = total_sales_per_product(sales_data)
    sales_date = sales_over_time(sales_data)
    print(f"Принес наибольшую выручку: {sorted(sales_product.items(), key = lambda item: item[1], reverse=True)[0][0]}") # Продукт с макс. выручкой
    print(f"Наибольшая сумма продаж была: {sorted(sales_date.items(), key=lambda item: item[1], reverse=True)[0][0]}") # Дата макс. выручки
    plt.plot(sales_product.keys(), sales_product.values())  # Добавление значений на график
    plt.legend(['Продажи']) # Создание легенды на графике
    plt.show() # Отображение графика на экране
    plt.plot(sales_date.keys(), sales_date.values())  # Добавление значений на график
    plt.legend(['Продажи'])  # Создание легенды на графике
    plt.show()  # Отображение графика на экране

start()

