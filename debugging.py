def b_print(symbol, w, h):
    if len(symbol) != 1:
        raise ValueError('MUST be single char')
    if w<=2 or h<=2:
        raise ValueError('W/H should be > 2')
    assert w>2 and h>2, "Logic Error on Dimension"



    print(symbol*w)
    for i in range (h-2):
        print(symbol + (' ' * (w-2)) +symbol)
    print(symbol*w)


print("-")
try:
    b_print('x', 25, 10)
except Exception as ex_err:
    print(ex_err)
except ValueError as ex_err:
    print(ex_err)
except AssertionError as assert_err:
    print(assert_err)
# ex eption must be caught atleast SOMEWHERE
# Assert is best used for assumptions, not user-facing errors.
