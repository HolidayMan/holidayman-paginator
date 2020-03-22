from paginator import Paginator

sequence = list(range(30))

paginator = Paginator(sequence, 5)  # sequence to paginate, items on page
print("Amount of pages:", paginator.num_pages)

print()

page = paginator.page(6)

print("Current page:", page)
print("Current page number:", page.number)
print("Current page data:", page.data)

print()

print("Next page:", page.next_page)  # if page is the last, returns None
print("Does current page have next page:", page.has_next())

print()

print("Previous page:", page.previous_page)  # if page is the first, returns None
print("Does current page have previous page:", page.has_previous())

print()

print("Indexes range on page", page.get_range())

print()

print("You can get paginator object from page:", page.paginator)
print(page.paginator.last_page_number)
