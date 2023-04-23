from suds import WebFault
from suds.client import Client
import logging
import ssl
import os, sys

ssl._create_default_https_context = ssl._create_unverified_context
logging.basicConfig(level=logging.INFO)
 
#try: http://ias.uci.cu:9763/services/PasarelaWS?wsdl
client = Client('https://autenticacion2.uci.cu/v7/PasarelaAutenticacionWS.wsdl')
continuar = 's'
while True:
	os.system('cls')
	username = str(raw_input('Introduzca un usuario: '))
	result=client.service.ObtenerPersonaDadoUsuario(username)
	print('Expediente:	' + unicode(result.IdExpediente))
	print('Nombre:		' + unicode(result.Nombres))
	print('Apellidos:	' + unicode(result.Apellidos))
	print('Credencial:	' + unicode(result.Credencial))
	print('Provincia:	' + unicode(result.Municipio.Provincia.NombreProvincia))
	print('Municipio:	' + unicode(result.Municipio.NombreMunicipio))
	print('Carnet Id:	' + unicode(result.CI))
	print('Categoria:	' + unicode(result.Categoria))
	print('Cargo:		' + unicode(result.Cargo.NombreCargo))
	print('Sexo:		' + unicode(result.Sexo.NombreSexo))
	print('Usuario:	' + unicode(result.Usuario))
	print('Correo:		' + unicode(result.Correo))
	print('Edificio:	' + unicode(result.Residencia.Edificio))
	print('Apartamento:	' + unicode(result.Residencia.Apartamento))
	print('Telefono:	' + unicode(result.Residencia.Telefono))
	print('Area:		' + unicode(result.Area.NombreArea))
	print('UrlFoto:	' + unicode(result.Foto.UrlFoto))

	continuar = unicode(raw_input('Desea continuar s/n: '))
	if continuar != 's':
		break;
os.system('cls')