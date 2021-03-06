from math import *

def tree(label, branches=[]):
    """Construct a tree with the given label value and a list of branches."""
    for branch in branches:
        assert is_tree(branch), 'branches must be trees'
    return [label] + list(branches)


def label(tree):
    """Return the label value of a tree."""
    return tree[0]


def branches(tree):
    """Return the list of branches of the given tree."""
    return tree[1:]


def is_tree(tree):
    """Returns True if the given tree is a tree, and False otherwise."""
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True


def is_leaf(tree):
    """Returns True if the given tree's list of branches is empty, and False
    otherwise.
    """
    return not branches(tree)


def print_tree(t, indent=0):
    """Print a representation of this tree in which each node is
    indented by two spaces times its depth from the root.

    >>> print_tree(tree(1))
    1
    >>> print_tree(tree(1, [tree(2)]))
    1
      2
    >>> numbers = tree(1, [tree(2), tree(3, [tree(4), tree(5)]), tree(6, [tree(7)])])
    >>> print_tree(numbers)
    1
      2
      3
        4
        5
      6
        7
    """
    print('  ' * indent + str(label(t)))
    for b in branches(t):
        print_tree(b, indent + 1)


def copy_tree(t):
    """Returns a copy of t. Only for testing purposes.

    >>> t = tree(5)
    >>> copy = copy_tree(t)
    >>> t = tree(6)
    >>> print_tree(copy)
    5
    """
    return tree(label(t), [copy_tree(b) for b in branches(t)])


#############
# Questions #
#############

def replace_leaf(t, old, new):
    """Returns a new tree where every leaf value equal to old has
    been replaced with new.

    >>> yggdrasil = tree('odin',
    ...                  [tree('balder',
    ...                        [tree('thor'),
    ...                         tree('loki')]),
    ...                   tree('frigg',
    ...                        [tree('thor')]),
    ...                   tree('thor',
    ...                        [tree('sif'),
    ...                         tree('thor')]),
    ...                   tree('thor')])
    >>> laerad = copy_tree(yggdrasil) # copy yggdrasil for testing purposes
    >>> print_tree(replace_leaf(yggdrasil, 'thor', 'freya'))
    odin
      balder
        freya
        loki
      frigg
        freya
      thor
        sif
        freya
      freya
    >>> laerad == yggdrasil # Make sure original tree is unmodified
    True
    """
    temp = t[:]
    if label(temp) == old and is_leaf(temp) == 1:
        temp[0] = new
    return tree(label(temp), [replace_leaf(branch, old, new) for branch in branches(temp) if is_tree(branch)])


def print_move(origin, destination):
    """Print instructions to move a disk."""
    print("Move the top disk from rod", origin, "to rod", destination)


def move_stack(n, start, end):
    """Print the moves required to move n disks on the start pole to the end
    pole without violating the rules of Towers of Hanoi.

    n -- number of disks
    start -- a pole position, either 1, 2, or 3
    end -- a pole position, either 1, 2, or 3

    There are exactly three poles, and start and end must be different. Assume
    that the start pole has at least n disks of increasing size, and the end
    pole is either empty or has a top disk larger than the top n start disks.

    >>> move_stack(1, 1, 3)
    Move the top disk from rod 1 to rod 3
    >>> move_stack(2, 1, 3)
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 3
    >>> move_stack(3, 1, 3)
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 3 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 1
    Move the top disk from rod 2 to rod 3
    Move the top disk from rod 1 to rod 3
    """
    assert 1 <= start <= 3 and 1 <= end <= 3 and start != end, "Bad start/end"
    rest = 6-start-end
    if n == 1:
        print_move(start, end)
    else:
        move_stack(n-1, start, rest)
        move_stack(1, start, end)
        move_stack(n-1, rest, end)

###########
# Mobiles #
###########


def mobile(left, right):
    """Construct a mobile from a left side and a right side."""
    return tree('mobile', [left, right])


def is_mobile(m):
    return is_tree(m) and label(m) == 'mobile'


def sides(m):
    """Select the sides of a mobile."""
    assert is_mobile(m), "must call sides on a mobile"
    return branches(m)


def is_side(m):
    return not is_mobile(m) and not is_weight(m) and type(label(m)) == int


def side(length, mobile_or_weight):
    """Construct a side: a length of rod with a mobile or weight at the end."""
    return tree(length, [mobile_or_weight])


def length(s):
    """Select the length of a side."""
    assert is_side(s), "must call length on a side"
    return label(s)


def end(s):
    """Select the mobile or weight hanging at the end of a side."""
    assert is_side(s), "must call end on a side"
    return branches(s)[0]


def weight(size):
    """Construct a weight of some size."""
    assert size > 0
    return tree(size)


def size(w):
    """Select the size of a weight."""
    assert is_weight(w)
    return label(w)


def is_weight(w):
    """Whether w is a weight, not a mobile."""
    return not is_mobile(w) and not branches(w)


def examples():
    t = mobile(side(1, weight(2)),
               side(2, weight(1)))
    u = mobile(side(5, weight(1)),
               side(1, mobile(side(2, weight(3)),
                              side(3, weight(2)))))
    v = mobile(side(4, t), side(2, u))
    return t, u, v


def total_weight(m):
    """Return the total weight of m, a weight or mobile.

    >>> t, u, v = examples()
    >>> total_weight(t)
    3
    >>> total_weight(u)
    6
    >>> total_weight(v)
    9
    """
    if is_weight(m):
        return size(m)
    else:
        assert is_mobile(m), "must get total weight of a mobile or a weight"
        return sum([total_weight(end(s)) for s in sides(m)])


def balanced(m):
    """Return whether m is balanced.

    >>> t, u, v = examples()
    >>> balanced(t)
    True
    >>> balanced(v)
    True
    >>> w = mobile(side(3, t), side(2, u))
    >>> balanced(w)
    False
    >>> balanced(mobile(side(1, v), side(1, w)))
    False
    >>> balanced(mobile(side(1, w), side(1, v)))
    False
    """
    def side_balanced():
        if is_mobile(end(sides(m)[0])) and is_mobile(end(sides(m)[1])):
            return balanced(end(sides(m)[0])) and balanced(end(sides(m)[1]))
        elif is_mobile(end(sides(m)[0])):
            return balanced(end(sides(m)[0]))
        elif is_mobile(end(sides(m)[1])):
            return balanced(end(sides(m)[1]))
        else:
            return False

    left_torque, right_torque = [total_weight(end(x)) * length(x) for x in sides(m)]
    if is_weight(end(sides(m)[0])) and is_weight(end(sides(m)[1])) or side_balanced():
        return left_torque == right_torque
    else:
        return False


#######
# OOP #
#######

class Account:
    """An account has a balance and a holder.

    >>> a = Account('John')
    >>> a.deposit(10)
    10
    >>> a.balance
    10
    >>> a.interest
    0.02

    >>> a.time_to_retire(10.25) # 10 -> 10.2 -> 10.404
    2
    >>> a.balance               # balance should not change
    10
    >>> a.time_to_retire(11)    # 10 -> 10.2 -> ... -> 11.040808032
    5
    >>> a.time_to_retire(100)
    117
    """

    interest = 0.02  # A class attribute

    def __init__(self, account_holder):
        self.holder = account_holder
        self.balance = 0

    def deposit(self, amount):
        """Add amount to balance."""
        self.balance = self.balance + amount
        return self.balance

    def withdraw(self, amount):
        """Subtract amount from balance if funds are available."""
        if amount > self.balance:
            return 'Insufficient funds'
        self.balance = self.balance - amount
        return self.balance

    def time_to_retire(self, amount):
        """Return the number of years until balance would grow to amount."""
        assert self.balance > 0 and amount > 0 and self.interest > 0
        return ceil(log(amount/self.balance, 1+self.interest))


class FreeChecking(Account):
    """A bank account that charges for withdrawals, but the first two are free!

    >>> ch = FreeChecking('Jack')
    >>> ch.balance = 20
    >>> ch.withdraw(100)  # First one's free
    'Insufficient funds'
    >>> ch.withdraw(3)    # And the second
    17
    >>> ch.balance
    17
    >>> ch.withdraw(3)    # Ok, two free withdrawals is enough
    13
    >>> ch.withdraw(3)
    9
    >>> ch2 = FreeChecking('John')
    >>> ch2.balance = 10
    >>> ch2.withdraw(3) # No fee
    7
    >>> ch.withdraw(3)  # ch still charges a fee
    5
    >>> ch.withdraw(5)  # Not enough to cover fee + withdraw
    'Insufficient funds'
    """
    withdraw_fee = 1
    free_withdrawals = 2

    def __init__(self, account_holder):
        self.free_withdrawals = FreeChecking.free_withdrawals

    def withdraw(self, amount):
        if self.free_withdrawals > 0:
            self.free_withdrawals -= 1
            return Account.withdraw(self, amount)
        else:
            return Account.withdraw(self, amount + FreeChecking.withdraw_fee)

############
# Mutation #
############

def make_counter():
    """Return a counter function.

    >>> c = make_counter()
    >>> c('a')
    1
    >>> c('a')
    2
    >>> c('b')
    1
    >>> c('a')
    3
    >>> c2 = make_counter()
    >>> c2('b')
    1
    >>> c2('b')
    2
    >>> c('b') + c2('b')
    5
    """
    counter_list = {}

    def counter(string):
        nonlocal counter_list
        if string in counter_list:
            counter_list[string] += 1
        else:
            counter_list[string] = 1
        return counter_list[string]

    return counter


def make_fib():
    """Returns a function that returns the next Fibonacci number
    every time it is called.

    >>> fib = make_fib()
    >>> fib()
    0
    >>> fib()
    1
    >>> fib()
    1
    >>> fib()
    2
    >>> fib()
    3
    >>> fib2 = make_fib()
    >>> fib() + sum([fib2() for _ in range(5)])
    12
    """
    fib1 = 0
    fib2 = 1
    index = 0
    def fib_next():
        nonlocal index, fib1, fib2
        if index == 0:
            index += 1
            return 0
        elif index == 1:
            index += 1
            return 1
        else:
            fib1, fib2 = fib2, fib1+fib2
            return fib2


    return fib_next


def make_withdraw(balance, password):
    """Return a password-protected withdraw function.

    >>> w = make_withdraw(100, 'hax0r')
    >>> w(25, 'hax0r')
    75
    >>> error = w(90, 'hax0r')
    >>> error
    'Insufficient funds'
    >>> error = w(25, 'hwat')
    >>> error
    'Incorrect password'
    >>> new_bal = w(25, 'hax0r')
    >>> new_bal
    50
    >>> w(75, 'a')
    'Incorrect password'
    >>> w(10, 'hax0r')
    40
    >>> w(20, 'n00b')
    'Incorrect password'
    >>> w(10, 'hax0r')
    "Your account is locked. Attempts: ['hwat', 'a', 'n00b']"
    >>> w(10, 'l33t')
    "Your account is locked. Attempts: ['hwat', 'a', 'n00b']"
    >>> type(w(10, 'l33t')) == str
    True
    """

    def withdraw(amount):
        nonlocal balance
        if amount > balance:
            return 'Insufficient funds'
        balance = balance - amount
        return balance

    wrong_list = []
    lock = False

    def validation(amount, try_password):
        nonlocal password, wrong_list, lock
        if try_password == password and not lock:
            return withdraw(amount)
        elif len(wrong_list) < 3:
            wrong_list.append(try_password)
            if len(wrong_list) == 3:
                lock = True
            return 'Incorrect password'
        else:
            return "Your account is locked. Attempts: "+str(wrong_list)

    return validation

def make_joint(withdraw, old_password, new_password):
    """Return a password-protected withdraw function that has joint access to
    the balance of withdraw.

    >>> w = make_withdraw(100, 'hax0r')
    >>> w(25, 'hax0r')
    75
    >>> make_joint(w, 'my', 'secret')
    'Incorrect password'
    >>> j = make_joint(w, 'hax0r', 'secret')
    >>> w(25, 'secret')
    'Incorrect password'
    >>> j(25, 'secret')
    50
    >>> j(25, 'hax0r')
    25
    >>> j(100, 'secret')
    'Insufficient funds'

    >>> j2 = make_joint(j, 'secret', 'code')
    >>> j2(5, 'code')
    20
    >>> j2(5, 'secret')
    15
    >>> j2(5, 'hax0r')
    10

    >>> j2(25, 'password')
    'Incorrect password'
    >>> j2(5, 'secret')
    "Your account is locked. Attempts: ['my', 'secret', 'password']"
    >>> j(5, 'secret')
    "Your account is locked. Attempts: ['my', 'secret', 'password']"
    >>> w(5, 'hax0r')
    "Your account is locked. Attempts: ['my', 'secret', 'password']"
    >>> make_joint(w, 'hax0r', 'hello')
    "Your account is locked. Attempts: ['my', 'secret', 'password']"
    """
    password_collection = []

    def joint_withdraw(amount, try_password):
        nonlocal password_collection
        if try_password in password_collection:
            return withdraw(amount, old_password)
        else:
            return withdraw(amount, try_password)

    check = withdraw(0, old_password)
    if type(check) == int:
        password_collection.append(old_password)
        password_collection.append(new_password)
    else:
        return check
    return joint_withdraw


###################
# Extra Questions #
###################

def interval(a, b):
    """Construct an interval from a to b."""
    return [a, b]


def lower_bound(x):
    """Return the lower bound of interval x."""
    return min(x)


def upper_bound(x):
    """Return the upper bound of interval x."""
    return max(x)


def str_interval(x):
    """Return a string representation of interval x."""
    return '{0} to {1}'.format(lower_bound(x), upper_bound(x))


def add_interval(x, y):
    """Return an interval that contains the sum of any value in interval x and
    any value in interval y."""
    lower = lower_bound(x) + lower_bound(y)
    upper = upper_bound(x) + upper_bound(y)
    return interval(lower, upper)


def mul_interval(x, y):
    """Return the interval that contains the product of any value in x and any
    value in y."""
    p1 = lower_bound(x) * lower_bound(y)
    p2 = lower_bound(x) * upper_bound(y)
    p3 = upper_bound(x) * lower_bound(y)
    p4 = upper_bound(x) * upper_bound(y)
    return [min(p1, p2, p3, p4), max(p1, p2, p3, p4)]


def sub_interval(x, y):
    """Return the interval that contains the difference between any value in x
    and any value in y."""
    return interval(max(lower_bound(x), lower_bound(x)), min(upper_bound(x), upper_bound(y)))


def div_interval(x, y):
    """Return the interval that contains the quotient of any value in x divided by
    any value in y. Division is implemented as the multiplication of x by the
    reciprocal of y."""
    assert lower_bound(y)*upper_bound(y) > 0, 'y can not be zero'
    reciprocal_y = interval(1/upper_bound(y), 1/lower_bound(y))
    return mul_interval(x, reciprocal_y)


def par1(r1, r2):
    return div_interval(mul_interval(r1, r2), add_interval(r1, r2))


def par2(r1, r2):
    one = interval(1, 1)
    rep_r1 = div_interval(one, r1)
    rep_r2 = div_interval(one, r2)
    return div_interval(one, add_interval(rep_r1, rep_r2))


def check_par():
    """Return two intervals that give different results for parallel resistors.

    >>> r1, r2 = check_par()
    >>> x = par1(r1, r2)
    >>> y = par2(r1, r2)
    >>> lower_bound(x) != lower_bound(y) or upper_bound(x) != upper_bound(y)
    True
    """
    r1 = interval(1/2, 1) # Replace this line!
    r2 = interval(1, 2) # Replace this line!
    return r1, r2


def multiple_references_explanation():
    return """The multiple reference problem..."""


def quadratic(x, a, b, c):
    """Return the interval that is the range of the quadratic defined by
    coefficients a, b, and c, for domain interval x.

    >>> str_interval(quadratic(interval(0, 2), -2, 3, -1))
    '-3 to 0.125'
    >>> str_interval(quadratic(interval(1, 3), 2, -3, 1))
    '0 to 10'
    """
    def ft(t):
        return a*t*t + b*t + c
    critical_point = -b/(2*a)
    if (critical_point-lower_bound(x))*(upper_bound(x)-critical_point) > 0:
        return interval(
            min(ft(critical_point), ft(upper_bound(x)), ft(lower_bound(x))),
            max(ft(critical_point), ft(upper_bound(x)), ft(lower_bound(x))))
    else:
        return interval(min(ft(lower_bound(x)), ft(upper_bound(x))), max(ft(lower_bound(x)), ft(upper_bound(x))))


def polynomial(x, c):
    """Return the interval that is the range of the polynomial defined by
    coefficients c, for domain interval x.

    >>> str_interval(polynomial(interval(0, 2), [-1, 3, -2]))
    '-3.0 to 0.125'
    >>> str_interval(polynomial(interval(1, 3), [1, -3, 2]))
    '0.0 to 10.0'
    >>> str_interval(polynomial(interval(0.5, 2.25), [10, 24, -6, -8, 3]))
    '18.0 to 23.0'
    """

    def add_fn(coeff, k, f):
        return lambda x: coeff * pow(x, k) + f(x)

    def add_dfn(coeff, k, df):
        return lambda x: k * coeff * pow(x, k - 1) + df(x)

    def add_ddfn(coeff, k, ddf):
        return lambda x: k * (k - 1) * coeff * pow(x, k - 2) + ddf(x)

    # Define the polynomial and its first and second derivatives.
    f = lambda x: 0
    df = lambda x: 0
    ddf = lambda x: 0
    for k, coeff in enumerate(c):
        # Actually it's a recursive call. It's a little bit different cause it's from bottom to top
        # as this statement processes, f updates ( and a new lambda func is defined every time this statement executed)
        f = add_fn(coeff, k, f)
        if k > 0:
            df = add_dfn(coeff, k, df)
        if k > 1:
            ddf = add_ddfn(coeff, k, ddf)

    # Find as many extreme points as we can using Newton's method
    lower, upper = lower_bound(x), upper_bound(x)
    num_steps = 20
    step = (upper - lower) / num_steps
    starts = [lower + k * step for k in range(num_steps)]
    extremums = [find_zero(df, ddf, n) for n in starts]

    # Filter for the interval x and return
    ns = [n for n in extremums if n > lower and n < upper] + [lower, upper]
    values = [f(n) for n in ns]
    return interval(min(values), max(values))


# Newton's method from lecture

def improve(update, close, guess=1, max_updates=100):
    """Iteratively improve guess with update until close(guess) is true or
    max_updates have been applied."""
    k = 0
    while not close(guess) and k < max_updates:
        guess = update(guess)
        k = k + 1
    return guess


def approx_eq(x, y, tolerance=1e-15):
    return abs(x - y) < tolerance


def find_zero(f, df, guess=1):
    """Return a zero of the function f with derivative df."""

    def near_zero(x):
        return approx_eq(f(x), 0)

    return improve(newton_update(f, df), near_zero, guess)


def newton_update(f, df):
    """Return an update function for f with derivative df,
    using Newton's method."""

    def update(x):
        return x - f(x) / df(x)

    return update

