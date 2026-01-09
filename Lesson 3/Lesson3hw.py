# 1
def count_occurrences(lst, x):
    return lst.count(x)

# 2
def sum_elements(lst):
    return sum(lst)

# 3
def max_element(lst):
    return max(lst)

# 4
def min_element(lst):
    return min(lst)

# 5
def check_element(lst, x):
    return x in lst

# 6
def first_element(lst):
    return lst[0] if lst else None

# 7
def last_element(lst):
    return lst[-1] if lst else None

# 8
def first_three(lst):
    return lst[:3]

# 9
def reverse_list(lst):
    return lst[::-1]

# 10
def sort_list(lst):
    return sorted(lst)

# 11
def remove_duplicates(lst):
    return list(set(lst))

# 12
def insert_element(lst, index, x):
    lst.insert(index, x)
    return lst

# 13
def index_of_element(lst, x):
    return lst.index(x) if x in lst else -1

# 14
def is_empty(lst):
    return len(lst) == 0

# 15
def count_even(lst):
    return sum(1 for x in lst if x % 2 == 0)

# 16
def count_odd(lst):
    return sum(1 for x in lst if x % 2 != 0)

# 17
def concatenate_lists(a, b):
    return a + b

# 18
def find_sublist(lst, sub):
    for i in range(len(lst) - len(sub) + 1):
        if lst[i:i+len(sub)] == sub:
            return True
    return False

# 19
def replace_element(lst, old, new):
    if old in lst:
        lst[lst.index(old)] = new
    return lst

# 20
def second_largest(lst):
    unique = sorted(set(lst))
    return unique[-2]

# 21
def second_smallest(lst):
    unique = sorted(set(lst))
    return unique[1]

# 22
def filter_even(lst):
    return [x for x in lst if x % 2 == 0]

# 23
def filter_odd(lst):
    return [x for x in lst if x % 2 != 0]

# 24
def list_length(lst):
    return len(lst)

# 25
def copy_list(lst):
    return lst.copy()

# 26
def middle_element(lst):
    n = len(lst)
    return lst[n//2] if n % 2 else (lst[n//2 - 1], lst[n//2])

# 27
def max_sublist(lst, start, end):
    return max(lst[start:end])

# 28
def min_sublist(lst, start, end):
    return min(lst[start:end])

# 29
def remove_by_index(lst, index):
    if 0 <= index < len(lst):
        lst.pop(index)
    return lst

# 30
def is_sorted(lst):
    return lst == sorted(lst)

# 31
def repeat_elements(lst, n):
    return [x for x in lst for _ in range(n)]

# 32
def merge_and_sort(a, b):
    return sorted(a + b)

# 33
def all_indices(lst, x):
    return [i for i, v in enumerate(lst) if v == x]

# 34
def rotate_right(lst):
    return [lst[-1]] + lst[:-1] if lst else lst

# 35
def range_list(start, end):
    return list(range(start, end + 1))

# 36
def sum_positive(lst):
    return sum(x for x in lst if x > 0)

# 37
def sum_negative(lst):
    return sum(x for x in lst if x < 0)

# 38
def is_palindrome(lst):
    return lst == lst[::-1]

# 39
def nested_list(lst, size):
    return [lst[i:i+size] for i in range(0, len(lst), size)]

# 40
def unique_in_order(lst):
    result = []
    for x in lst:
        if x not in result:
            result.append(x)
    return result


 # Tuple questions

def count_occurrences(t, x): return t.count(x)


def max_element(t): return max(t)


def min_element(t): return min(t)


def check_element(t, x): return x in t


def first_element(t): return t[0] if t else None


def last_element(t): return t[-1] if t else None


def tuple_length(t): return len(t)


def first_three(t): return t[:3]


def concat_tuples(a, b): return a + b


def is_empty(t): return len(t) == 0


def all_indices(t, x):
    return [i for i, v in enumerate(t) if v == x]


def second_largest(t):
    u = sorted(set(t))
    return u[-2]


def second_smallest(t):
    u = sorted(set(t))
    return u[1]


def single_element_tuple(x): return (x,)


def list_to_tuple(lst): return tuple(lst)


def is_sorted(t): return list(t) == sorted(t)


def max_subtuple(t, a, b): return max(t[a:b])


def min_subtuple(t, a, b): return min(t[a:b])


def remove_first(t, x):
    lst = list(t)
    if x in lst: lst.remove(x)
    return tuple(lst)


def nested_tuple(t, size):
    return tuple(tuple(t[i:i + size]) for i in range(0, len(t), size))


def repeat_elements(t, n):
    return tuple(x for x in t for _ in range(n))


def range_tuple(a, b): return tuple(range(a, b + 1))


def reverse_tuple(t): return t[::-1]


def is_palindrome(t): return t == t[::-1]


def unique_tuple(t):
    res = []
    for x in t:
        if x not in res:
            res.append(x)
    return tuple(res)

# Set tasks

def union(a, b): return a | b
def intersection(a, b): return a & b
def difference(a, b): return a - b
def is_subset(a, b): return a.issubset(b)
def check_element(s, x): return x in s
def set_length(s): return len(s)
def list_to_set(lst): return set(lst)
def remove_element(s, x): s.discard(x); return s
def clear_set(s): return set()
def is_empty(s): return len(s) == 0
def symmetric_diff(a, b): return a ^ b
def add_element(s, x): s.add(x); return s
def pop_element(s): return s.pop()
def max_element(s): return max(s)
def min_element(s): return min(s)
def filter_even(s): return {x for x in s if x % 2 == 0}
def filter_odd(s): return {x for x in s if x % 2 != 0}
def range_set(a, b): return set(range(a, b+1))
def merge_lists_to_set(a, b): return set(a + b)
def is_disjoint(a, b): return a.isdisjoint(b)
def remove_duplicates_list(lst): return list(set(lst))
def count_unique(lst): return len(set(lst))

# Dictionary tasks

def get_value(d, k): return d.get(k, None)
def check_key(d, k): return k in d
def count_keys(d): return len(d)
def get_keys(d): return list(d.keys())
def get_values(d): return list(d.values())
def merge_dicts(a, b): return {**a, **b}

def remove_key(d, k):
    d.pop(k, None)
    return d

def clear_dict(): return {}
def is_empty(d): return len(d) == 0
def get_pair(d, k): return (k, d[k]) if k in d else None
def update_value(d, k, v): d[k] = v; return d

def count_value(d, v):
    return list(d.values()).count(v)

def invert_dict(d):
    return {v: k for k, v in d.items()}

def keys_with_value(d, v):
    return [k for k in d if d[k] == v]

def dict_from_lists(keys, values):
    return dict(zip(keys, values))

def has_nested(d):
    return any(isinstance(v, dict) for v in d.values())

def get_nested(d, k1, k2):
    return d[k1][k2]

from collections import defaultdict
def default_dict():
    return defaultdict(int)

def unique_values(d):
    return len(set(d.values()))

def sort_by_key(d):
    return dict(sorted(d.items()))

def sort_by_value(d):
    return dict(sorted(d.items(), key=lambda x: x[1]))

def filter_by_value(d, cond):
    return {k: v for k, v in d.items() if cond(v)}

def common_keys(a, b):
    return set(a.keys()) & set(b.keys())

def dict_from_tuple(t):
    return dict(t)

def first_pair(d):
    return next(iter(d.items()))
