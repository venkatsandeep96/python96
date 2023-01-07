import json
j_data = '{"Name":"Kevin", "Age":23, "Group":"Griffas"}'

# Converting JSON data to Python object


py_obj = json.loads(j_data)


print('Converted jSON to Py Object: ', py_obj)



# Converting Python data to JSON object

j_obj = json.dumps(py_obj)

print('Converted Py obj to JSON obj: ', j_obj)
