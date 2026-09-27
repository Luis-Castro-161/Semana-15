# Creación diccionario
agenda = {}
def agregar_contacto(nombre, telefono):
    """Agrega un nuevo contacto a la agenda o actualiza uno existente. """
    agenda[nombre] = telefono
    print (f"contacto agregado: {nombre} -> {telefono}")

def mostrar_contactos ():
    """Muestra todos los contactos alamacenados en agenda."""
    print("\n---Lista de contactos---")
    if not agenda:
        print("La agenda esta vacia.")
    else:
        for nombre, telefono in agenda. items():
            print (f"{nombre}:{telefono}")

def buscar_contacto(nombre):
    """Buscar contacto por su nombre y muestra su numero."""
    if nombre in agenda:
        print (f"{nombre} tiene el numero: {agenda[nombre]}")
    else:
        print(f"No se encontro ningun contacto llamado ' {nombre}'.")

def eliminar_contacto(nombre):
    """Eliminar contacto nombre si existe."""
    if nombre in agenda:
        del agenda[nombre]
        print(f"Contacto '{nombre}' eliminado correctamente.")
    else:
        print(f"Nose puede eliminar: '{nombre}' no existe en la agenda.")


if __name__ == "__main__":

        agregar_contacto("Ana", "0923487562")
        agregar_contacto("Luis", "0968726495")
        agregar_contacto("Carlos", "0902487633")
        mostrar_contactos()
        buscar_contacto("Ana")
        eliminar_contacto("Carlos")
        mostrar_contactos()

    
