import boto3

#Crear cliente para conexion a DynamoDB
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
tabla = dynamodb.Table('tabla-johnestiven-restrepo')

##LEER DATOS##

#leer elemento de la tabla
response = tabla.get_item(Key={'id':'1'})

print(response['Item'])

#Leer todos los datos de la tabla
response = tabla.scan()

print(response['Items'])

##INSERTAR UN DATO##

# Especificar la tabla en la que quieres insertar el elemento
table = dynamodb.Table('tabla-johnestiven-restrepo')

# Datos del elemento que quieres insertar
item = {
    'id': '3',
    'Nombre': 'John Estiven',
    'Ciudad': 'Medellin - Antioquia',
    'Descripcion': 'Insert desde Python'
}

# Insertar el elemento en la tabla
table.put_item(Item=item)

print("Registro insertado")

# Especificar la tabla en la que quieres actualizar el elemento
table = dynamodb.Table('tabla-johnestiven-restrepo')

# Clave primaria del elemento que quieres actualizar
key = {
    'id': '2'
}

response = table.get_item(Key=key)
print("Registro antes de actualizar: ", response['Item'])

# Expresión de actualización y valores de los atributos que quieres actualizar
update_expression = 'SET nombre = :nombre'
expression_attribute_values = {
    ':nombre': 'Estiven Marin'
}

# Actualizar el elemento en la tabla
response = table.update_item(
    Key=key,
    UpdateExpression=update_expression,
    ExpressionAttributeValues=expression_attribute_values
)

print("Elemento actualizado exitosamente.")

response = table.get_item(Key={'id':'2'})
print("Registro actualizado: ", response['Item'])


# Crear la tabla
table_name = 'tabla-johnestiven-restrepo2'
try:
    table = dynamodb.create_table(
        TableName=table_name,
        KeySchema=[
            {
                'AttributeName': 'id',
                'KeyType': 'HASH'  # Clave de partición
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'id',
                'AttributeType': 'S'  # Tipo de dato de la clave de partición (S: String, N: Number, B: Binary)
            }
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 5,
            'WriteCapacityUnits': 5
        }
    )
    

    print(f'Tabla {table_name} creada y activa.')

except Exception as e:
    
    print(f'Error creando la tabla: {e}')

#ELIMINAR TABLA

table_name='tabla-johnestiven-restrepo2'
response = dynamodb.delete_table(TableName=table_name)