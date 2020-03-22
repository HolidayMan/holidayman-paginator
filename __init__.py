from typing import List, Sequence


class Page:
    _previous_page = None
    _next_page = None
    _previous_page_number: int = None
    _next_page_number: int = None
    _data: Sequence = None
    _number: int = None
    _paginator = None
    _start_index: int = None
    _last_index: int = None

    def __init__(self, data: Sequence, number: int, paginator, start_index: int, last_index: int):
        self._data = data
        self._number = number
        self._paginator = paginator
        self._start_index = start_index
        self._last_index = last_index

    def has_next(self) -> bool:
        return bool(self._next_page)

    def has_previous(self) -> bool:
        return bool(self._previous_page)

    def get_range(self) -> range:
        return range(self._start_index, self._last_index + 1)

    @property
    def previous_page(self):
        return self._previous_page

    @property
    def next_page(self):
        return self._next_page

    @property
    def previous_page_number(self):
        return self._previous_page_number

    @property
    def next_page_number(self):
        return self._next_page_number

    @property
    def data(self):
        return self._data

    @property
    def number(self):
        return self._number

    @property
    def paginator(self):
        return self._paginator

    @property
    def data(self):
        return self._data

    @property
    def start_index(self):
        return self._start_index

    @property
    def last_index(self):
        return self._last_index

    @next_page.setter
    def next_page(self, value):
        if self._next_page is None and self._number != self.paginator.last_page_number():
            self._next_page = value
        else:
            raise AttributeError("you can't set next_page attribute")

    @next_page_number.setter
    def next_page_number(self, value):
        if self._next_page_number is None and self._number != self.paginator.last_page_number():
            self._next_page_number = value
        else:
            raise AttributeError("you can't set next_page_numer attribute")

    @previous_page.setter
    def previous_page(self, value):
        if self._previous_page is None and self._number != 1:
            self._previous_page = value
        else:
            raise AttributeError("you can't set previous_page attribute")

    @previous_page_number.setter
    def previous_page_number(self, value):
        if self._previous_page_number is None and self._number != 1:
            self._previous_page_number = value
        else:
            raise AttributeError("you can't set previous_page_number attribute")

    def __repr__(self):
        return f"<Page %d of %d>" % (self._number, self._paginator.num_pages)

    def __getitem__(self, key):
        if key < -1 or key > len(self._data) - 1:
            raise StopIteration
        return self._data[key]


class Paginator:
    pages: List[Page] = None
    num_pages: int = None
    _last_page_number: int = None

    def __init__(self, sequence: Sequence, step: int):
        self.pages = []
        pages = Paginator.build_pages(sequence, step)

        previous_page: Page = None

        for num, page in enumerate(pages, 1):
            start_index = num * step - step
            last_index = num * step - 1
            new_page = Page(data=page, number=num, paginator=self, start_index=start_index, last_index=last_index)
            self.pages.append(new_page)

            if num == 1:  # if the page is first
                previous_page = new_page
                continue

            previous_page._next_page = new_page
            previous_page._next_page_number = new_page.number
            new_page._previous_page = previous_page
            new_page._previous_page_number = previous_page.number
            previous_page = new_page

        self.num_pages = len(self.pages)
        self._last_page_number = self.pages[-1].number

    @staticmethod
    def build_pages(seq: Sequence, step: int) -> list:
        pages: list = []
        page: list = []

        for index, item in enumerate(seq):
            if len(page) < step:
                page.append(item)
            else:
                pages.append(page)
                page = [item]
        pages.append(page)

        return pages

    def page(self, number) -> Page:
        if number < 1 or number > len(self.pages):
            raise ValueError("invalid page number")
        return self[number - 1]

    @property
    def last_page_number(self):
        return self._last_page_number

    def __getitem__(self, key):
        if key < -1 or key > len(self.pages) - 1:
            raise StopIteration
        return self.pages[key]
