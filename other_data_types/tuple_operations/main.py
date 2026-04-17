# Initial items on shelf #1 (provided as a tuple)
shelf1 = ("celery", "spinach", "cucumbers")

# Items being added to the shelf #1 (provided as a list)
shelf1_update = ["tomatoes", "celery", "cilantro"]

# Task 1: Convert the list of new shelf items to a tuple
shelf1_update_tuple = tuple(shelf1_update)

# Task 2: Concatenate the new tuple with the existing tuple
shelf1_concat = shelf1 + shelf1_update_tuple
celery_count = shelf1_concat.count("celery")
celery_index = shelf1_concat.index("celery")

# Task 3 & 4: Print results
print("Updated Shelf #1:", shelf1_concat)
print("Number of Celery:", shelf1_concat.count("celery"))
print("Celery Index:", shelf1_concat.index("celery"))