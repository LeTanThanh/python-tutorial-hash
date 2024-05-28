class Person:
  def __init__(self, first_name, last_name, age) -> None:
    self.first_name = first_name
    self.last_name = last_name
    self.age = age

  def __eq__(self, other) -> bool:
    if isinstance(other, Person):
      return self.age == other.age

    return False

  def __hash__(self) -> int:
    return hash(self.age)
