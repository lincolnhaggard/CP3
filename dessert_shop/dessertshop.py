from receipt import make_receipt
from desserts import (Candy,Cookie,IceCream,Sundae,Order)
def main():
    ordor=Order()
    ordor.add(Candy("Candy Corn", 1.5, .25))
    ordor.add(Candy("Gummy Bears", .25, .35))
    ordor.add(Cookie("Chocolate Chip", 6, 3.99))
    ordor.add(IceCream("Pistachio", 2, .79))
    ordor.add(Sundae("Vanilla", 3, .69, "Hot Fudge", 1.29))
    ordor.add(Cookie("Oatmeal Raisin", 2, 3.45))

    for item in ordor.ordor:
        print(item)
    print("Total number of items in ordor:",len(ordor))
    data=[]
    total_tax=0
    subtotal=0
    for item in ordor.ordor:
        data.append([item.name,item.calculate_cost(),item.calculate_tax()])
        total_tax+=item.calculate_tax()
        subtotal+=item.calculate_cost()
    data.append(["--------------------------------------------------------",None,None])
    data.append(["Order Subtotals",subtotal,total_tax])
    data.append(["Order Total",None,subtotal+total_tax])
    data.append(["Total items in the order",None,str(len(ordor))])
    make_receipt(data,"dessert_shop/receipt.pdf")
main()