def doc():
    list = []
    list.append(dict(item="cook", qty=50, date="1/2/2015"))
    list.append(dict(item="milk", qty=100, date="2/5/2014"))
    list.append(dict(item="milk", qty=100, date="2/5/2014"))
    list.append(dict(item="milk", qty=100, date="2/5/2014"))
    list.append(dict(item="milk", qty=100, date="2/5/2014"))
    list.append(dict(item="milk", qty=100, date="2/5/2014"))

    total = 0
    for data in list:
        total += data['qty']
    print "Total:" + str(total)

if __name__ == "__main__":
    doc()
