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