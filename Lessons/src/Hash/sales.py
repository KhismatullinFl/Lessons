import sys

def main():
    customers = {}
    lines = sys.stdin
    for line in lines:
        line = line.strip()
        if not line:
            continue
        
        parts = line.split()
        if len(parts) != 3:
            continue  
        
        customer, product, quantity = parts
        quantity = int(quantity)
        
        if customer not in customers:
            customers[customer] = {}
        if product not in customers[customer]:
            customers[customer][product] = 0
        customers[customer][product] += quantity
    
    for customer in sorted(customers.keys()):
        print(f"{customer}:")
        for product in sorted(customers[customer].keys()):
            print(f"{product} {customers[customer][product]}")

if __name__ == '__main__':
    main()
