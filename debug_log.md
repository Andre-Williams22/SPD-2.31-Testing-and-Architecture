# Debug Log

**Explain how you used the the techniques covered (Trace Forward, Trace Backward, Divide & Conquer) to uncover the bugs in each exercise. Be specific!**

In your explanations, you may want to answer:

- What is the expected vs. actual output?
- If there is a stack trace, what useful information does it contain?
- Which technique did you use, on which line numbers?
- What assumptions did you have about each line of code, and which ones were proven to be wrong?

_Example: I noticed that the program should show pizza orders once a new order is made, and that it wasn't showing any. So, I used the trace forward technique starting on line 13. I discovered the bug on line 27 was caused by a typo of 'pzza' instead of 'pizza'._

_Then I noticed another bug ..._

## Exercise 1

1. The expected output is that I should be seeing my order stored in the database and a print out telling me that my order was submitted.
2. The stack trace shows that "topping" is an invalid keyword argument for PizzaTopping. 
3. I back traced and found error on line 81, then I found another error doing the same process on line 86. 
4. Then there was no sign of the actual bug so I had to use the trace forward method

### Bug 1: Pizzas aren't being displayed after creation - Trace backward

- `TypeError: 'topping' is an invalid keyword argument for PizzaTopping`

- Change append toppings loop to:
    ``` python
    for topping in toppings_list:
        pizza.toppings.append(PizzaTopping(topping_type=topping))
    ```

- Change request.form.get(NAME) to `order_name` and `pizza_size`
    ```python
        order_name = request.form.get('order_name')
        pizza_size_str = request.form.get('pizza_size')
    ```

- Change `request.form.get('toppings)` to `request.form.getlist('toppings')`
    ```python
        toppings_list = request.form.getlist('toppings')
    ```

- Commit pizza to db in `pizza_order_submit()`:
    ```python
        db.session.add(pizza)
        # Add commit after add
        db.session.commit()
    ```


## Exercise 2

### Bug 1: Missing API key - Trace Backward
### Bug 2: OpenWeather API city query string - Divide and Conquer / Check API docs
        'q': city,
### Bug 3: Incorrect request.args.get(NAME) - Trace Backward
```python
    city = request.args.get('city')
    units = request.args.get('units')
```
### Bug 4: Incorrect JSON key - Trace Backward / Check return JSON data
```python
'temp': result_json['main']['temp'],
```


## Exercise 3

The expected output is for the algorithms to sort the arrays in sequential order; however, the code is breaking and providing an error. The error message has to do with the list index being out of range. I'm going to use the divide and conquer method to identify and fix the bug sense the algorithms are divide and conquer algorithms and there are multiple files I'm working with. I first decided to use back tracking because the stack trace provided a line. I found a typo on line 38. Then I applied divide and conquer for both binary and search after I found the line for the error. Mainly backtracking was the most useful in this case. For binary search the error was on line 53 and was caused by dividing without rounding down so this left a float with decimals. 


### Merge Sort
### Bug 1: `IndexError: list index out of range` - Trace backward
- Change from `i` to `j` -> `right_side[j]`
    ```
    line 37, in merge_sort
        arr[k] = right_side[i]
    ```

### Bug 2: List sorted in descending order - Trace Forward
- Change line 23 `>` to `<` :   
```python
    if left_side[i] < right_side[j]:
```

### Bug 3: `2` appears three times, missing `6` and `7` - Trace Forward
- Increment `k +=1 ` in the `while` `i`/`j` < `len(left_side)`/`len(right_side)` checks
```python
    while i < len(left_side):
        arr[k] = left_side[i]
        i += 1
        k += 1

    while j < len(right_side):
        arr[k] = right_side[j]
        j += 1
        k += 1
```

### Binary Search
### Bug 1: `TypeError: list indices must be integers or slices, not float` - Trace backward
- For line, 51, use floor int division (`//`) for mid  
```python
    mid = (high + low) // 2
```

### Bug 2: Comments/pseudocode is mismatched to code, - Trace Forward
- Rearranged pseudocode to line up with correct code

### Bug 3: Index of 5 is: -1, but should be 4 - Trace Forward / Divide and Conquer
- Change line 49 to include condition when `low == high` so that it can complete and utilize the `else` condition to return `mid`  
```python
    while low <= high:
```
