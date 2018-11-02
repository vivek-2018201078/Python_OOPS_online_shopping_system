import pickle

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
    #history = []

    def __init__(self, customer_id, name, phone, email):
        Cart.__init__(self)
        self.email = email
        self.phone = phone
        self.name = name
        self.customer_id = customer_id
        self.history = []

    def viewProducts(self):
        print("---------------------------------------------------------")
        print("id   name    price   quantity    group   subgroup")
        product_list = open("products.pickle", "rb")
        products = pickle.load(product_list)
        product_list.close()
        for product in products:
            print(product.product_id, product.name, product.price, product.count, product.group, product.subgroup)
        print("---------------------------------------------------------")

    def addToCard(self, products, customers, product_index, quantity_to_buy):
        self.product_ids.append(products[product_index].product_id)
        self.numberofproducts += 1
        self.product_names.append(products[product_index].name)
        self.prices.append(products[product_index].price)
        self.quantities.append(quantity_to_buy)
        self.total = str(int(self.total) + int(products[product_index].price) * int(quantity_to_buy))
        products[product_index].count = str(int(products[product_index].count) - int(quantity_to_buy))
        customer_list = open("customers.pickle", "wb")
        product_list = open("products.pickle", "wb")
        pickle.dump(customers, customer_list)
        pickle.dump(products, product_list)
        customer_list.close()
        product_list.close()
        print("added to cart successfully")

    def deleteFromCart(self, products, customers, dummy_admin, product_id_to_delete):
        self.numberofproducts -= 1
        product_index_to_change = dummy_admin.existsProduct(product_id_to_delete)
        cart_index_to_delete = self.product_ids.index(product_id_to_delete)
        self.total = str(int(self.total) - int(self.prices[cart_index_to_delete]) * int(
            self.quantities[cart_index_to_delete]))
        del self.product_ids[cart_index_to_delete]
        del self.prices[cart_index_to_delete]
        del self.product_names[cart_index_to_delete]
        products[product_index_to_change].count = str(
            int(products[product_index_to_change].count) + int(self.quantities[cart_index_to_delete]))
        del self.quantities[cart_index_to_delete]
        customer_list = open("customers.pickle", "wb")
        product_list = open("products.pickle", "wb")
        pickle.dump(customers, customer_list)
        pickle.dump(products, product_list)
        customer_list.close()
        product_list.close()
        print("product deleted from cart successfully")

    def viewCart(self):
        print("Total products in cart = ", self.numberofproducts)
        print("---------------------------------------------------------")
        print("id  name     quantity    price")
        for i in range(len(self.product_names)):
            print(self.product_ids[i], self.product_names[i], self.quantities[i], self.prices[i])
        print("---------------------------------------------------------")
        print("Total Amount = ", self.total)

    def buyProducts(self, index):
        self.viewCart()
        customer_list = open("customers.pickle", "rb")
        customers = pickle.load(customer_list)
        customer_list.close()
        confirm = input("Confirm Buy (y/n):")
        if confirm.lower() == "y":

            print("amount of ", self.total, "is paid")
            cart_temp = [self.numberofproducts, self.product_ids, self.product_names, self.prices, self.quantities,
                         self.total]
            customers[index].history.append(cart_temp)
            Cart.__init__(self)
            customer_list = open("customers.pickle", "wb")
            pickle.dump(customers, customer_list)
            customer_list.close()
            print("Transaction done")

            return

        else:
            return

    def viewPurchaseHistory(self, index):
        customer_list = open("customers.pickle", "rb")
        customers = pickle.load(customer_list)
        customer_list.close()
        print("************************Purchase History*******************************")
        for cart in customers[index].history:
            print("------------------------------------------------------------------")
            for i in range(int(cart[0])):
                print(cart[1][i], cart[2][i], cart[3][i], cart[4][i])
            print("Total amount of this purchase:", cart[5])
            print("------------------------------------------------------------------")
        print("************************************************************************")



class Admin():
    passkey = "123"
    def __init__(self, admin_id, name):
        self.name = name
        self.admin_id = admin_id

    def viewProducts(self):
        print("----------------------------------------------------------")
        print("id   name    price   quantity    group   subgroup")
        product_list = open("products.pickle", "rb")
        products = pickle.load(product_list)
        for product in products:
            print(product.product_id, product.name, product.price, product.count, product.group, product.subgroup)
        print("----------------------------------------------------------")
        product_list.close()


    def existsProduct(self, id):
        found = 0
        itr = 0
        product_list = open("products.pickle", "rb")
        products = pickle.load(product_list)
        product_list.close()
        for product in products:
            if str(product.product_id) == str(id):
                found = 1
                break
            itr += 1
        if found:
            return itr
        else:
            return -1


    def addProduct(self, product):
        product_list = open("products.pickle", "rb")
        products = pickle.load(product_list)
        product_list.close()
        products.append(product)
        product_list = open("products.pickle", "wb")
        pickle.dump(products, product_list)
        product_list.close()
        # print("product added successfully")

    def deleteProduct(self, id):
        index = self.existsProduct(id)
        if index == -1:
            print("product not found")
            return
        product_list = open("products.pickle", "rb")
        products = pickle.load(product_list)
        del products[index]
        product_list.close()
        product_list = open("products.pickle", "wb")
        pickle.dump(products, product_list)
        product_list.close()
        print("product deleted successfully")

    def modifyProduct(self, index, product):
        product_list = open("products.pickle", "rb")
        products = pickle.load(product_list)
        products[index] = product
        product_list.close()
        product_list = open("products.pickle", "wb")
        pickle.dump(products, product_list)
        product_list.close()
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
    customer_list = open("customers.pickle", "rb")
    customers = pickle.load(customer_list)
    customer_list.close()
    for customer in customers:
        if str(customer.customer_id) == str(id):
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

            customer_list = open("customers.pickle", "rb")
            continue

        if choice == "2":
            user_detail = input("Provide name phone_number emailid:")
            item = user_detail.split()
            if len(item) != 3:
                print("provide correct details")
                continue
            customer_list = open("customers.pickle", "rb")
            customers = pickle.load(customer_list)
            customer_list.close()
            customers.append(Customer(customer_itr, item[0], item[1], item[2]))
            customer_list = open("customers.pickle", "wb")
            customer_itr += 1
            pickle.dump(customers, customer_list)
            customer_list.close()

            print("Registered Successfully with customer_id = ", customer_itr - 1, "...login with user id ")
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
    customer_list = open("customers.pickle", "rb")
    customers = pickle.load(customer_list)
    print("Welcome", customers[index].name)
    print("1. View Products")
    print("2. Add to cart")
    print("3. Delete from cart")
    print("4. View Cart")
    print("5. Buy Products")
    print("6. View Purchase History")
    print("7. change user type")

    customer_list = open("customers.pickle", "rb")
    customers = pickle.load(customer_list)
    customer_list.close()
    customer = customers[index]
    dummy_admin = Admin(1, "Vivek")

    product_list = open("products.pickle", "rb")
    products = pickle.load(product_list)
    product_list.close()
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

            customer.addToCard(products, customers, product_index, quantity_to_buy)
            continue

        if choice == "3":
            product_id_to_delete = input("Enter product id to delete:")
            if not product_id_to_delete in customer.product_ids:
                print("product with given id doesnt exist in cart")
                continue

            customer.deleteFromCart(products, customers, dummy_admin, product_id_to_delete)
            continue

        if choice == "4":
            customer.viewCart()
            continue

        if choice == "5":
            customer.buyProducts(index)
            continue

        if choice == "6":
            customer.viewPurchaseHistory(index)
            continue

        if choice == "7":
            print("switching user...")
            print("logging out....")
            return

        else:
            print("wrong choice...type again")
            continue


def main():
    global product_itr
    global customer_itr


    product_list = open("products.pickle", "rb")
    customer_list = open("customers.pickle", "rb")
    customers = pickle.load(customer_list)
    products = pickle.load(product_list)


    max_product_id = 0
    for product in products:
        if int(product.product_id) > max_product_id:
            max_product_id = int(product.product_id)

    product_itr = max_product_id + 1
    customer_itr = len(customers) + 1
    product_list.close()
    customer_list.close()
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
        if user_type.lower() == "exit":
            exit()
        else:
            print("wrong choice...type again")
            continue

if __name__ == '__main__':
    main()