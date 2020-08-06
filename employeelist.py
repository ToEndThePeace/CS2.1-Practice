records = [
    ("Alice", "Engineering"),
    ("Bob", "Sales"),
    ("Dave", "Engineering"),
    ("Erin", "Engineering"),
    ("Grace", "Marketing"),
    ("Carol", "Sales"),
    ("Frank", "Engineering"),
]
# by_dept = {
#     "Sales": ["Bob", "Carol"],
#     "Marketing": ["Grace"],
#     "Engineering": ["Alice", "Dave", "Erin", "Frank"]
# }

by_dept = {}

# build the dict out
for name, dept in records:
    if dept not in by_dept:
        by_dept[dept] = []
    by_dept[dept].append(name)


def emp_by_dept(d):
    # emp = []
    # for name, dept in records:
    #     if dept == d:
    #         emp.append(name)
    # return emp
    return f"{d}: {by_dept[d]}"


def add_employee(name, dept):
    records.append((name, dept))
    if dept not in by_dept:
        by_dept[dept] = []
    by_dept[dept].append(name)


print(emp_by_dept("Marketing"))

add_employee("Hank", "Marketing")

print(emp_by_dept("Marketing"))
