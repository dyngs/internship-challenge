import data
from random import randint
from task_02 import task2

def main():
    # generate random amounts and prices for each product in the list
    for diction in data.products:
        amount_dict = diction["amount"]
        amount_generated = randint(amount_dict["min"], amount_dict["max"])
        price_dict = diction["price"]
        price_generated = randint(price_dict["min"], price_dict["max"])

        diction["amount"] = amount_generated #update each dict in the list
        diction["price"] = price_generated


   # create classes and append them to data.obj_list
    for diction in data.products:
        MyProduct = data.Product(diction["name"], diction["amount"], diction["price"])
        data.obj_list.append(MyProduct)


    summary = []
    for my_product in data.obj_list:
        prod_summary = {my_product.get_name() : my_product.calculate_total_value()}
        summary.append(prod_summary)

    results_01 = open("results_01.txt", "w")
    results_01.writelines(str(summary))
    results_01.write(",\n")
    results_01.writelines(str(data.products))
    results_01.write(",\n")
    results_01.writelines(str(data.obj_list))

    input_value = -1
    min = randint(0,150)
    max = -1
    while (max < min):
        max = randint(75, 200)

    task2(input_value, min, max)


if __name__ == '__main__':
    main()