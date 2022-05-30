import getting as gt
import setting as st

items = []

def main():
    items.append(gt.getDataBTC())
    items.append(gt.getDataETH())
    items.append(gt.getDataUSDT())
    items.append(gt.getDataUSDC())
    items.append(gt.getDataBNB())

    print(items)

    st.createTable()
    st.insertCoins(items)
    print("Done")

if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		print("\nSaliendo...")
		exit()

