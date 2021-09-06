import datetime
import json

with open("record.json", 'r+') as read_it:
    data = json.load(read_it)

purchase = []
items_purchase = []


def show():

    global item_choice, choice, present
    u_name = input('Enter Your Name :')
    u_no = input('Enter Your Number :')
    print(f"Welcome {u_name} what do you want to purchase")
    while 1:
        count = 1
        for i in data:
            print(f'\t{count}. {i}')
            count = count + 1
        category = input('Choose From These Categories:\n')
        if category != '':
            while 1:
                cart = []
                count1 = 0
                index = 0
                for i in data[category]:
                    print(f'\t{count1 + 1}. ', i['name'])
                    count1 += 1
                item = input(f'Which {category} You Want To Purchase:\n')
                if item != '':
                    amount = int(input(f'How Many {item} {category} you  want:\n'))
                    present = 0
                    price = 0

                    for i in data[category]:
                        if i['name'] == item:
                            index=index+1
                            present = i['available']
                            price = i['price']
                    if int(amount) <= int(present):
                        print(f'{item} {category} added\n')
                        cart.append(category)
                        cart.append(item)
                        cart.append(amount)
                        cart.append(price)
                        purchase.append(cart)

                        data[category][index]['available'] =str(int(present) - int(amount))
                        json.dumps(data)
                    else:
                        choice = input(f"Only {present} peice of {item} is present do you want to purchase it yes/no\n")
                        if choice == 'yes':
                            print(f'{item} {category} added\n')
                            cart.append(category)
                            cart.append(item)
                            cart.append(present)
                            cart.append(price)
                            purchase.append(cart)
                            data[category][index]['available'] = 0
                            json.dumps(data)

                    choice = input(f"You Want Any Thing Else From '{category}' yes/no\n")
                    if choice == 'yes':
                        continue
                    else:
                        break
        else:
            print(f'No {category} found ')

        choice = input(f"You Want Any Thing Else yes/no\n")
        if choice == 'yes':
            continue
        else:
            break
    if purchase:
        listi = []

        for i in purchase:
            dicti = {}
            category = i[0]
            name = i[1]
            quantity = i[2]
            price = i[3]
            dicti['name'] = u_name
            dicti['transaction_date_time'] = str(datetime.datetime.now())
            dicti['category'] = category
            dicti['item_name'] = name
            dicti['quantity'] = quantity
            dicti['price per piece'] = price
            with open("order.json", 'r+') as json_file:
                file_data = json.load(json_file)
                file_data['purchased'].append(dicti)
                json_file.seek(0)
                json.dump(file_data, json_file)

        count2 = 0
        sum = 0
        print('*' * 20)
        print("\t\tBill\n")
        print(f'Buyers Name : {u_name}')
        print(f'Buyers Mobile Number : {u_no}')
        print('Items:\n')

        for i in purchase:
            category = i[0]
            name = i[1]
            quantity = i[2]
            price = i[3]
            sum = sum + (int(price) * quantity)
            count2 = count2 + 1
            print(f'Category - {category}')
            print(f'name - {name}')
            print(f'Quantity - {quantity}')
            print(f'Price - {price}', end='\n')

        print(f'Total : {sum}')
    else:
        print('******Here You Come At End Of World******')


if __name__ == '__main__':
    show()
