import os
import random
import time
from datetime import datetime

class GeneradorCombos:
    def __init__(self):
        # Lista ampliada de nombres latinos
        self.nombres_latinos = [
            "Pedro", "Juan", "Carlos", "Luis", "Miguel", "Jose", "Antonio",
            "Francisco", "Manuel", "Javier", "David", "Daniel", "Alejandro",
            "Rafael", "Jorge", "Ricardo", "Fernando", "Roberto", "Andres",
            "Eduardo", "Mario", "Alberto", "Sergio", "Victor", "Rodrigo",
            "Joaquin", "Diego", "Martin", "Gabriel", "Julio", "Leon", "Ulises",
            "Julian", "Raul", "Oscar", "Hector", "Adrian", "Emilio", "Ignacio",
            "Salvador", "Guillermo", "Enrique", "Angel", "Felipe", "Ruben",
            "Esteban", "Tomas", "Agustin", "Alfonso", "Benjamin", "Hugo"
        ]
        
        # Lista de apellidos para combinar
        self.apellidos = [
            "Morales", "Garcia", "Rodriguez", "Martinez", "Hernandez", "Lopez",
            "Gonzalez", "Perez", "Sanchez", "Ramirez", "Torres", "Flores",
            "Rivera", "Gomez", "Diaz", "Reyes", "Cruz", "Ortiz", "Chavez",
            "Ruiz", "Romero", "Alvarez", "Mendoza", "Vasquez", "Castillo",
            "Jimenez", "Moreno", "Ramos", "Silva", "Rojas", "Medina", "Castro"
        ]

    def generar_combo(self):
        """Genera un combo único con diferentes variaciones"""
        # Seleccionar nombre base
        base = random.choice(self.nombres_latinos)
        
        # Aleatoriamente decidir si usar nombre o apellido
        if random.random() < 0.3:  # 30% de probabilidad de usar apellido
            base = random.choice(self.apellidos)
        
        # Aplicar variaciones de mayúsculas/minúsculas
        variacion = random.choice([1, 2, 3])
        if variacion == 1:
            nombre = base.upper()  # Todo mayúsculas
        elif variacion == 2:
            nombre = base.lower()  # Todo minúsculas
        else:
            nombre = base  # Sin cambios (primera mayúscula)
        
        # Agregar números aleatorios (50% de probabilidad)
        if random.random() < 0.5:
            # Generar entre 1 y 5 dígitos
            cantidad_digitos = random.randint(1, 5)
            numeros = ''.join(random.choice('0123456789') for _ in range(cantidad_digitos))
            nombre = f"{nombre}{numeros}"
        
        # Formato final: nombre:nombre
        return f"{nombre}:{nombre}"

    def crear_carpeta_y_guardar(self, cantidad, nombre_carpeta):
        """Crea la carpeta y guarda los combos generados"""
        try:
            # Verificar cantidad válida
            if cantidad < 1 or cantidad > 800000:
                print("❌ Error: Cantidad debe estar entre 1 y 800000")
                return None
            
            # Definir ruta base (SD Card)
            base_path = "/sdcard"
            
            # Crear ruta completa para la carpeta
            carpeta_path = os.path.join(base_path, nombre_carpeta)
            
            # Crear carpeta si no existe
            if not os.path.exists(carpeta_path):
                os.makedirs(carpeta_path)
                print(f"📁 Carpeta creada: {carpeta_path}")
            
            # Crear nombre único para el archivo
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            nombre_archivo = f"combos_latinos_{timestamp}.txt"
            archivo_path = os.path.join(carpeta_path, nombre_archivo)
            
            # Generar y guardar combos
            print(f"⏳ Generando {cantidad:,} combos...")
            inicio = time.time()
            
            with open(archivo_path, 'w', encoding='utf-8') as archivo:
                # Generar en bloques para mejor rendimiento
                for i in range(cantidad):
                    combo = self.generar_combo()
                    archivo.write(f"{combo}\n")
                    
                    # Mostrar progreso cada cierto porcentaje
                    if cantidad > 1000 and (i + 1) % (cantidad // 10) == 0:
                        progreso = ((i + 1) / cantidad) * 100
                        print(f"📊 Progreso: {progreso:.1f}% ({i + 1:,} de {cantidad:,})")
            
            tiempo_total = time.time() - inicio
            
            # Calcular tamaño del archivo
            tamano = os.path.getsize(archivo_path)
            tamano_mb = tamano / (1024 * 1024)
            
            # Información final
            print("\n" + "="*50)
            print("✅ GENERACIÓN COMPLETADA")
            print("="*50)
            print(f"📁 Carpeta: {carpeta_path}")
            print(f"📄 Archivo: {nombre_archivo}")
            print(f"🔢 Combos generados: {cantidad:,}")
            print(f"📏 Tamaño: {tamano_mb:.2f} MB")
            print(f"⏱️  Tiempo: {tiempo_total:.2f} segundos")
            print(f"⚡ Velocidad: {cantidad/tiempo_total:.0f} combos/segundo")
            
            return archivo_path
            
        except PermissionError:
            print("❌ Error: Permiso denegado. Verifica los permisos de QPython")
            return None
        except Exception as e:
            print(f"❌ Error inesperado: {str(e)}")
            return None

def mostrar_ejemplos(generador, cantidad=10):
    """Muestra ejemplos de combos generados"""
    print("\n" + "═"*40)
    print("🎲 EJEMPLOS DE COMBOS GENERADOS")
    print("═"*40)
    for i in range(min(cantidad, 10)):
        print(f"  {i+1:2d}. {generador.generar_combo()}")
    print("═"*40)

def main():
    """Función principal del programa"""
    # Limpiar pantalla
    print("\n" * 3)
    
    # Banner simple y profesional
    print("╔══════════════════════════════════════════╗")
    print("║   GENERADOR DE COMBOS LATINOS - RUAH 🇨🇱  ║")
    print("║         SOLO PARA GUAPOS Y SEXYS         ║")
    print("╚══════════════════════════════════════════╝")
    print("")
    
    # Crear instancia del generador
    generador = GeneradorCombos()
    
    # Mostrar ejemplos
    mostrar_ejemplos(generador)
    
    try:
        # Solicitar cantidad
        while True:
            try:
                entrada = input("\n🔢 ¿Cuántos combos deseas generar? (1-800000): ").strip()
                cantidad = int(entrada)
                if 1 <= cantidad <= 800000:
                    break
                else:
                    print("❌ Por favor, ingresa un número entre 1 y 800000")
            except ValueError:
                print("❌ Entrada inválida. Ingresa un número válido")
        
        # Solicitar nombre de carpeta
        nombre_carpeta = input("\n📁 Nombre de la carpeta (ej: 'MisCombos'): ").strip()
        if not nombre_carpeta:
            nombre_carpeta = "CombosLatinos"
        
        print("\n" + "─"*50)
        print("🚀 INICIANDO GENERACIÓN...")
        print("─"*50)
        
        # Generar combos
        archivo_resultado = generador.crear_carpeta_y_guardar(cantidad, nombre_carpeta)
        
        if archivo_resultado:
            print("\n🎉 ¡Combos generados exitosamente!")
            print(f"📍 Ubicación: /sdcard/{nombre_carpeta}/")
            
            # Preguntar si mostrar más ejemplos
            respuesta = input("\n¿Mostrar más ejemplos? (s/n): ").lower()
            if respuesta == 's':
                mostrar_ejemplos(generador, 15)
            
            print("\n" + "★"*50)
            print("¡Gracias por usar Generador de Combos RUAH 🇨🇱!")
            print("★"*50)
        
    except KeyboardInterrupt:
        print("\n\n⚠️  Operación cancelada por el usuario")
    except Exception as e:
        print(f"\n❌ Error crítico: {str(e)}")

# Punto de entrada del programa
if __name__ == "__main__":
    # Añadir un pequeño delay para asegurar que QPython cargue todo
    try:
        main()
    except Exception as e:
        print(f"Error fatal: {str(e)}")
        input("\nPresiona Enter para salir...")