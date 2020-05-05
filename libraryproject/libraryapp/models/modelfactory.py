# TODO: DO THIS WHEN YOU HAVE A CLEARER UNDERSTANDING

# import sqlite3

# # Higher order function to create instances of models
# # when performing single table queries
# def model_factory(model_type):
#     def create(cursor, row):

#         # instantiating the model/class that's passed in
#         instance = model_type()

#         # created row objects on each row of SQL data specified by
#         # the model
#         smart_row = sqlite3.Row(cursor, row)

#         for col in smart_row.keys():
#             # passing in a model/class instance & setting its obj 
#             # attributes = to the key/value pairs of data from
#             # the smart_row row factory operation.
#             setattr(instance, col, smart_row[col])
#         return instance