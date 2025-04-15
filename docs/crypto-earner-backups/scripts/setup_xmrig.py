import os
import subprocess

def setup_xmrig():
    """
    Configura XMRig utilizando un enlace funcional desde el sitio oficial.
    """
    try:
        # Directorio de instalación
        miners_dir = "/home/jeengrasi/crypto-earner/miners/"
        xmrig_dir = os.path.join(miners_dir, "xmrig/")
        os.makedirs(xmrig_dir, exist_ok=True)

        # Enlace confirmado desde el sitio oficial de XMRig
        xmrig_url = "https://github.com/xmrig/xmrig/releases/download/v6.22.2/xmrig-6.22.2-linux-static-x64.tar.gz"
        destination = os.path.join(xmrig_dir, "xmrig.tar.gz")

        print("Descargando XMRig desde el sitio oficial...")
        subprocess.run(["wget", "-O", destination, xmrig_url], check=True)

        # Extraer archivo
        print("Extrayendo XMRig...")
        subprocess.run(["tar", "-xvzf", destination, "-C", xmrig_dir], check=True)

        print("XMRig configurado exitosamente en:", xmrig_dir)
    except Exception as e:
        print(f"Error durante la instalación de XMRig: {e}")

if __name__ == "__main__":
    setup_xmrig()
