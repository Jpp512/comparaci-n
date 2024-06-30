----- instalar python -----
Python 3.12.4
-----                 -----

----- En caso de ser necesario -----
pip install pandas openpyxl xlsxwriter
-----                          -----

----- descargar conparacion.py -----
----- ruta comoda y sencilla -----

Crea un entorno de prueba: python -m venv mi_entorno
mi_entorno\Scripts\activate
pip install pandas openpyxl xlsxwriter (opcional sino funciona)
python comparacion.py

------- De ser necesario -------
Set-ExecutionPolicy RemoteSigned
-------                  -------

pyinstaller --onefile --paths=mi_entorno\Lib\site-packages --noconsole comparacion.py

----- para salir del entorno -----
deactivate
-----                        -----
