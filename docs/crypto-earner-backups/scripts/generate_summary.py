import os

def summarize_directory(path, output_file):
    """
    Recorre la carpeta especificada y genera un resumen detallado.
    """
    try:
        summary = []
        summary.append(f"Resumen de la carpeta: {path}\n{'=' * 50}\n")

        for root, dirs, files in os.walk(path):
            depth = root.replace(path, "").count(os.sep)
            indent = "  " * depth
            summary.append(f"{indent}📁 {os.path.basename(root)}/\n")

            sub_indent = "  " * (depth + 1)
            for file in files:
                file_path = os.path.join(root, file)
                file_size = os.path.getsize(file_path) / 1024  # Tamaño en KB
                summary.append(f"{sub_indent}📄 {file} - {file_size:.2f} KB\n")

        # Escribir el resumen en un archivo
        with open(output_file, "w") as f:
            f.writelines(summary)

        print(f"Resumen generado exitosamente en: {output_file}")
    except Exception as e:
        print(f"Error al generar el resumen: {e}")

if __name__ == "__main__":
    directory_path = "/home/jeengrasi/crypto-earner"
    output_summary = "/home/jeengrasi/crypto-earner/data/summary.txt"
    summarize_directory(directory_path, output_summary)
