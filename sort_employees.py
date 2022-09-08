def sort_employees(employees, sort_by):
    sort_indices = ["name", "age", "salary"]
    sort_index = sort_indices.index(sort_by)

    sorted_employees = sorted(employees, key=lambda x: x[sort_index])

    return sorted_employees
