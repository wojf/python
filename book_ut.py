import pytest
from Py_training.lec8.book import *


def test_Book_init_setTitle_requiredTitleIsSet_ut():
    new_book = Book('Test1')
    assert new_book.title == 'Test1'


def test_Book_init_passNoTitle_reiseTypeError_ut():
    with pytest.raises(TypeError):
        new_book = Book()


def test_Book_init_setTitle_contentIsEmpty_ut():
    new_book = Book('Test3')
    assert not bool(new_book.content)


def test_Book_addChaptersTitleAndContent_addTitleAndContent_requiredTitleAndContentAreSet_ut():
    new_book = Book('Test4')
    new_book.add_chapters_title_and_content('Title', 'Content')
    assert 'Title' in new_book.content and new_book.content['Title'] == 'Content'


# test - is_palindrome()
def test_Book_isPalindrome_passPalindorme_returnTrue_ut():
    new_book = Book('Test5')
    assert new_book.is_palindrome('abcddcba')


def test_Book_isPalindrome_passNonPlaindrome_returnFalse():
    new_book = Book('Test6')
    assert not new_book.is_palindrome('abcde')


def test_Book_isPalindrome_passPalindromeWithNonAlphaNum_returnTrue_ut():
    new_book = Book('Test7')
    assert new_book.is_palindrome('no "x" in nixon!')


# test - count_words()
def test_Book_countWords_passOneWord_returnInt_ut():
    new_book = Book('Test8')
    assert new_book.count_words('test') == 1


def test_Book_countWords_passTwoWordsStartingEndingWithSpace_returnInt_ut():
    new_book = Book('Test9')
    assert new_book.count_words(' test two ') == 2


def test_Book_countWords_passTextWithNonAlpha_returnInt_ut():
    new_book = Book('Test10')
    assert new_book.count_words('!@#$') == 0


# Class2 - inherited from Book
def test_DerivedBook_setTitle_requiredTitileIsSet_ut():
    book = DerivedBook('New book - Test11')
    assert book.title == 'New book - Test11'


def test_DerivedBook_SetAuthor_requiredAuthorIsSet_ut():
    book = DerivedBook('Book - Test12')
    book.set_author('Ian Fleming')
    assert book.author == 'Ian Fleming'
