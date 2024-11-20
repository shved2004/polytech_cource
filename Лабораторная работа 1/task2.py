# TODO Найдите количество книг, которое можно разместить на дискете

disk_size_mb = 1.44
pages = 100
lines = 50
chars = 25
bytes = 4

disk_size_bytes = disk_size_mb * 1024 * 1024

chars_per_page = lines * chars
total_chars_per_book = pages * chars_per_page
book_size_bytes = total_chars_per_book * bytes

books_on_disk = int(disk_size_bytes // book_size_bytes)

print("Количество книг, помещающихся на дискету:", books_on_disk)
