----- Instalar python -----

Python 3.12.4
-----                 

----- Descargar/ruta comoda/sencilla -----

conparacion.py
----- 


----- En caso de ser necesario -----

pip install pandas openpyxl xlsxwriter
-----                          

----- Cambiar politica de seguridad -----

Get-ExecutionPolicy
Set-ExecutionPolicy RemoteSigned
-----                               


-----Crea un entorno de prueba -----

python -m venv mi_entorno
-----                    

----- Ejecuta -----
mi_entorno\Scripts\activate 
----

----- Probar que sirva -----
python comparacion.py
-----

----- Instalar el programa -----
pyinstaller --onefile --paths=mi_entorno\Lib\site-packages --noconsole comparacion.py
-----

----- para salir del entorno -----
deactivate
-----
