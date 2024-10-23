# TODO Найдите количество книг, которое можно разместить на дискете

disk = 1.44
pages = 100
rows = 50
symbols = 25
size = 4

disk_in_byte = 1.44 * 1024 * 1024
row_size = symbols*size
page_size = row_size*rows
book_size = page_size*pages

count = disk_in_byte // book_size

print("Количество книг, помещающихся на дискету:", int(count))
