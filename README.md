# Proyecto1
+--------------------+         1        * +-----------------+
|  CajeroAutomatico  |--------------------|     Usuario     |
+--------------------+                    +-----------------+
| - usuarios: dict   |                    | - id: int       |
| - contador_id: int |                    | - nombre: str   |
+--------------------+                    | - pin: int      |
| + nuevoUsuario()   |                    | - saldo: float  |
| + menu()           |                    +-----------------+
| + opciones()       |                    | + retirar()     |
|                    |                    | + depositar()   |
|                    |                    | + consultar()   |
|                    |                    | + cambiarPin()  |
+--------------------+                    +-----------------+
     +------------------+
     |     Usuario      |
     +------------------+
           /   |   \
          /    |    \
         V     V     V
 [Retirar] [Depositar] [Consultar saldo]
      \         |        /
       \        |       /
        V       V      V
          [Cambiar PIN]
                |
                V
          [Crear usuario]
