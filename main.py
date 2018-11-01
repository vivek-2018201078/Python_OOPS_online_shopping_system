
products = []
customers = []
product_itr = 0
customer_itr = 0


class Cart():
    def __init__(self):
        self.numberofproducts = 0
        self.product_ids = []
        self.product_names = []
        self.prices = []
        self.quantities = []
        self.total = 0

class Product:
    def __init__(self, product_id,  name, price, count, group, subgroup):
        self.product_id = product_id
        self.subgroup = subgroup
        self.group = group
        self.count = count
        self.price = price
        self.name = name

class Customer(Cart):
    def __init__(self, customer_id, name, phone, email):
        Cart.__init__(self)
        self.email = email
        self.phone = phone
        self.name = name
        self.customer_id = customer_id

    def viewProducts(self):
        print("---------------------------------------------------------")
        print("id   name    price   quantity    group   subgroup")
        for product in products:
            print(product.product_id, product.name, product.price, product.count, product.group, product.subgroup)
        print("---------------------------------------------------------")
    #def addToCard(self):





class Admin():
    passkey = "123"
    def __init__(self, admin_id, name):
        self.name = name
        self.admin_id = admin_id

    def viewProducts(self):
        print("----------------------------------------------------------")
        print("id   name    price   quantity    group   subgroup")
        for product in products:
            print(product.product_id, product.name, product.price, product.count, product.group, product.subgroup)
        print("----------------------------------------------------------")


    def existsProduct(self, id):
        found = 0
        itr = 0
        for product in products:
            if product.product_id == id:
                found = 1
                break
            itr += 1
        if found:
            return itr
        else:
            return -1

    def addProduct(self, product):
        products.append(product)
        print("product added successfully")

    def deleteProduct(self, id):
        index = self.existsProduct(id)
        if index == -1:
            print("product not found")
            return
        del products[index]
        print("product deleted successfully")

    def modifyProduct(self, index, product):
        products[index] = product
        print("Product modified successfully")



def admin_functions():
    global product_itr
    global customer_itr
    store_admin = Admin(1, "Vivek")
    print("1. View Products")
    print("2. Add Product")
    print("3. Delete Products")
    print("4. Modify Products")
    print("5. Change user type")
    while(True):
        chosen = input("choice?:")
        if chosen == "1":
            store_admin.viewProducts()
            continue
        if chosen == "2":
            item = input("Give name price quantity group subgroup:")
            item = item.split()
            if len(item) != 5:
                print("Give proper produt info")
                continue
            store_admin.addProduct(Product(product_itr, item[0], item[1], item[2], item[3], item[4]))
            product_itr += 1
            print("product added successfully")
            continue
        if chosen == "3":
            id_to_del = input("Give product id to delete:")
            store_admin.deleteProduct(id_to_del)
            continue
        if chosen == "4":
            id_to_modify = input("Give product id to modify:")
            index = store_admin.existsProduct(id_to_modify)
            if index == -1:
                print("product with id doesnt exist")
                continue
            to_modify = input("Enter modified tuple (without id):")
            item = to_modify.split()
            if len(item) != 5:
                print("Incorrect data on product")
                continue
            store_admin.modifyProduct(index, Product(id_to_modify, item[0], item[1], item[2], item[3], item[4]))
            continue

        if chosen == "5":
            print("switching user...")
            print("logging out...")
            return

        else:
            print("wrong choice...type again")
            continue

def exitsCustomer(id):
    found = 0
    itr = 0
    for customer in customers:
        if customer.customer_id == id:
            found = 1
            break
        itr += 1
    if found:
        return itr
    else:
        return -1

def guest_functions():

    global customer_itr
    global product_itr

    print("1. View Products")
    print("2. Register")
    print("3. Change user type")

    while True:
        choice = input("choice?:")

        if choice == "1":
            store_admin = Admin(1, "Vivek")
            store_admin.viewProducts()
            continue

        if choice == "2":
            user_detail = input("Provide name phone_number emailid:")
            item = user_detail.split()
            if len(item) != 3:
                print("provide correct details")
                continue
            customers.append(Customer(customer_itr, item[0], item[1], item[2]))
            print("Registered Successfully...login with user id")
            return
        if choice == "3":
            print("switching user...")
            return

        else:
            print("wrong choice...type again")
            continue


def customerfunctions(index):
    global customer_itr
    global product_itr
    print("1. View Products")
    print("2. Add to cart")
    print("3. Delete from cart")
    print("4. View Cart")
    print("5. Buy Products")
    print("6. change user type")

    customer = customers[index]
    dummy_admin = Admin(1, "Vivek")

    while True:
        choice = input("choice?:")
        if choice == "1":
            customer.viewProducts()
            continue

        if choice == "2":
            product_id, quantity_to_buy = input("Enter product_id and its quantity to purchase:").split()
            product_index = dummy_admin.existsProduct(product_id)
            if product_index == -1:
                print("product with given id does not exist")
                continue
            if int(quantity_to_buy) > int(products[product_index].count):
                print("product not available in required quantity")
                continue
            customer.product_ids.append(products[product_index].product_id)
            customer.numberofproducts += 1
            customer.product_names.append(products[product_index].name)
            customer.prices.append(products[product_index].price)
            customer.quantities.append(quantity_to_buy)
            customer.total = str(int(customer.total) +  int(products[product_index].price) * int(quantity_to_buy))
            products[product_index].count = str(int(products[product_index].count) -  int(quantity_to_buy))
            print("added to cart successfully")
            continue

        if choice == "3":
            product_id_to_delete = input("Enter product id:")
            if not product_id_to_delete in customer.product_ids:
                print("product with given id doesnt exist in cart")
                continue
            customer.numberofproducts -= 1
            product_index_to_change = dummy_admin.existsProduct(product_id_to_delete)
            cart_index_to_delete = customer.product_ids.index(product_id_to_delete)
            customer.total = str(int(customer.total) - int(customer.prices[cart_index_to_delete]) * int(customer.quantities[cart_index_to_delete]))
            del customer.product_ids[cart_index_to_delete]
            del customer.prices[cart_index_to_delete]
            del customer.product_names[cart_index_to_delete]
            products[product_index_to_change].count = str(int(products[product_index_to_change].count) + int(customer.quantities[cart_index_to_delete]))
            del customer.quantities[cart_index_to_delete]
            print("product deleted from cart successfully")
            continue

        if choice == "4":
            print("Total products in cart = ", customer.numberofproducts)
            print("---------------------------------------------------------")
            print("id  name     quantity    price")
            for i in range(len(customer.product_names)):
                print(customer.product_ids[i], customer.product_names[i], customer.quantities[i], customer.prices[i])
            print("---------------------------------------------------------")
            print("Total Amount = ", customer.total)
            continue

        if choice == "5":
            print("Total products in cart = ", customer.numberofproducts)
            print("---------------------------------------------------------")
            print("id  name     quantity    price")
            for i in range(len(customer.product_names)):
                print(customer.product_ids[i], customer.product_names[i], customer.quantities[i], customer.prices[i])
            print("---------------------------------------------------------")
            print("Total Amount = ", customer.total)
            confirm = input("Confirm Buy (y/n):")
            if confirm.lower() == "y":
                print("amount of ", customer.total, "is paid")
                print("Transaction done")
                print("logging out.....")
                return
            continue

        if choice == "6":
            print("switching user...")
            print("logging out....")
            return

        else:
            print("wrong choice...type again")
            continue











def main():
    global product_itr
    global customer_itr
    with open("products.txt", 'r') as fp:
        for line in fp:
            item = line.split()
            products.append(Product(item[0], item[1], item[2], item[3], item[4], item[5]))

        product_itr = len(products) + 1



    with open("customers.txt", 'r') as fp:
        for line in fp:
            item = line.split()
            customers.append(Customer(item[0], item[1], item[2], item[3]))
        customer_itr = len(customers) + 1

    while True:
        user_type  = input("guest, customer, admin?:")
        if user_type.lower() == "admin":
            pass_key = input("Admin Passkey:")
            if pass_key == Admin.passkey:
                admin_functions()
            else:
                print("Incorrect passkey")
                continue
            continue
        if user_type.lower() == "guest":
            guest_functions()
            continue
        if user_type.lower() == "customer":
            customer_id = input("Enter Customer Id:")
            index = exitsCustomer(customer_id)
            if index == -1:
                print("customer with id does not exist")
                continue
            customerfunctions(index)
            continue
        else:
            print("wrong choice...type again")
            continue

if __name__ == '__main__':
    main()