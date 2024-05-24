## `in`
- Returns True if the target value is present in a collection of values. Otherwise, it returns False.
- Syntax -> "value in collection"

## `not in`
- Returns True if the target value is not present in a given collection of values. Otherwise, it returns False.
- Syntax -> "value not in collection"

## Note:
- Don’t confuse the in keyword when it works as the membership operator with the in keyword in the for loop syntax. They have entirely different meanings. The in operator checks if a value is in a collection of values, while the in keyword in a for loop indicates the iterable that you want to draw from.

- Example:
`
  def is_member(value, iterable):
        for item in iterable:
             if value is item or value == item:
                return True
        return False
`