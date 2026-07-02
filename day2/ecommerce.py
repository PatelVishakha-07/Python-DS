""" The E-Commerce Price Filter (First occurrence 2 target)

You're on Flipkart. You filter products: "Show me laptops priced 50,000 or above." Products are sorted by price. Flipkart must find the first product ≥ 50,000- classic binary search variant called lower bound. """

price = [10000, 25000, 35000, 40000, 40000, 45000, 48000, 50000, 50000, 500000, 52000, 60000]
start = 0
end = len(price)-1

tar = int(input("enter price: "))
f=0

while start <= end:
    mid = start + (end-start)//2

    if price[mid] == tar:
        print(price,"found at ",mid,"position")
        f=1
        break
    
    elif price[mid] > tar:
        end = mid-1
    else:
        start = mid+1

if f==0:
    print("Not found")