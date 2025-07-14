import os
os.system("cls")


productos={'8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
 '2175HD': ['lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
 'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
 'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
 'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
 '123FHD': ['lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
 '342FHD': ['lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
 'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050'], }

stock = {'8475HD': [387990,10], '2175HD': [327990,4], 'JjfFHD': [424990,1],
 'fgdxFHD': [664990,21], '123FHD': [290890,32], '342FHD': [444990,7],
 'GF75HD': [749990,2], 'UWU131HD': [349990,1], 'FS1230HD': [249990,0],}

def menu():
    print('''
        *** Menu principal ***
        ----------------------
                  
            1. stock marca
            2. busqueda por precio
            3. actualizar precio
            4. salir
          
          ''')
    
    op=input_num("Ingrese una opción entre 1 y 4: ",1,4)
    return op

    def(stock_marca):
        print("Stock Marca")
        print("--------------\n")

    
    for stock_marca(marca) in productos:
        if stock_marca[""] == productos:
            pass


        def(busqueda_por_precio): 
            print("Buscar por precio")
            print("----------------\n")
            stock = input("Ingrese el precio a buscar:  ")
            for precio in stock:
                if precio[""] == stock:
                    print("Datos encontrados: {marca} - {modelo}")
                    print(f"") 
                    return
                else:
                    ("debe entregar valores enteros!!")

        def(actualizar_precio):
        print("------------------\n")
        modelo = input("Ingrese el modelo: ")
        sw=0 #no existe el modelo
        for i in range(len(stock)):
            if stock[i]["modelo"] == modelo:
                print("el modelo existe, los datos son: ")
                print(f" {stock[i]["modelo"]} {stock[i]["precio"]}")
                sw=1 
                nuevo_precio = input("Ingrese el nuevo precio: ")
                       
                stock[i]["precio"] = nuevo_precio
           
                print("Listo! precio actualizado!")
            if sw==0: 
                print("Error, el modelo no existe!")  

        def(salir):
        print("fin del programa") 

while True:
    cls()
    opcion=menu() 
    cls()
    match opcion:
        case 1: listar()
        case 2: buscar()
        case 3: modificar()
        case 4: break
    os.system("pause")

