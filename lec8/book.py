import logging

# logger
logger = logging.getLogger('Book')
log_console = logging.StreamHandler()
log_console.setLevel(logging.INFO)
logger.addHandler(log_console)
logger.setLevel(logging.INFO)


class Book:

    def __init__(self, title: str):
        self.title = title
        self.content = {}
        logger.info('Creating an instance of Book class, book\'s title: ' + self.title)

    def add_chapters_title_and_content(self, chapter_title, chapter_content):
        self.content[chapter_title] = chapter_content
        logger.info('Adding chapter\'s title and content to \'%s\'' % self.title)

    def is_palindrome(self, text: str) -> bool:
        if text:
            # remove characters which doesn't matter for palindrome
            raw_text = ''
            for character in text:   # remove non-alpha or non-digits characters, they don't matter for palindrome
                if character.isalnum():
                    raw_text += character
            raw_text = raw_text.lower()   # capital letter doesn't matter for palindrome too

            # check if palindrome
            result = True
            for step in range(len(raw_text)//2):
                result = result and (raw_text[step] == raw_text[-1-step])
                if result is False:  # break loop if false to avoid unnecessary steps
                    break
        else:
            result = False
        return result

    def count_words(self, text: str) -> int:
        if text:
            separator_before = True  # if not set to 'True', first word won't be detected
            counter = 0
            # check all characters in text
            for character in range(len(text)):
                if text[character].isalnum() and separator_before:
                    counter += 1
                    separator_before = False
                elif not text[character].isalnum():     # if separator or punctuation detected
                    separator_before = True
        else:
            counter = 0
        return counter


class DerivedBook(Book):

    def __init__(self, title):
        Book.__init__(self,title)
        self.author = ''
        logger.info('Creating an instance of DerivedBook class, book\'s title: ' + self.title)

    def set_author(self, author: str):
        self.author = author
        logger.info('Adding %s author to \'%s\' book' % (self.author, self.title))


if __name__ == "__main__":
    new_book = DerivedBook('A new book')
    new_book.set_author('Ian Fleming')
    new_book.add_chapters_title_and_content('James Bond', 'Some time ago...')
