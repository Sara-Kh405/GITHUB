#برج هانوی

def Hanoy(disks ,start ,end ,help):
    if disks > 0:
        Hanoy(disks - 1, start, help, end)

        print(f'{start} -> {end}')

        Hanoy(disks - 1, help, end, start)


Hanoy(3, 1, 3, 2)

