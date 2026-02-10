def test_user_login():
    print("Run!")

class TestUserLogin:
    def test_1(self):
        ...
    def test_2(self):
        ...

def test_assert_positive_case():
    assert (2 + 2) == 4

def test_assert_negative_case():
    assert (2 + 2) == 5, "(2 + 2) is not equal to 5!"

# def test_all_different(l):
#     seen = set()
#     for i in l:
#         if i in seen:
#             return False
#         seen.add(i)
#     return True
# assert test_all_different(1) == True

# lst = [1, 2, 2, 3, 4, 4]
#
# def test_all_different(lst):
#     return len(lst) == len(set(lst))