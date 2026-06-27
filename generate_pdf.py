import subprocess
import os
import sys

def main():
    html_path = os.path.abspath("cv.html")
    pdf_path = os.path.abspath("CVIQBALCOMPLETE.pdf")

    print("--- ATS PDF GENERATOR ---")
    print(f"Source HTML: {html_path}")
    print(f"Target PDF: {pdf_path}")

    # Standard installation paths for MS Edge on Windows
    edge_paths = [
        r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
        r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
        os.path.expandvars(r"%ProgramFiles%\Microsoft\Edge\Application\msedge.exe"),
        os.path.expandvars(r"%ProgramFiles(x86)%\Microsoft\Edge\Application\msedge.exe")
    ]

    edge_exe = None
    for path in edge_paths:
        if os.path.exists(path):
            edge_exe = path
            break

    if not edge_exe:
        print("ERROR: Microsoft Edge tidak ditemukan di lokasi standar Windows.")
        print("Pastikan Microsoft Edge terinstal di sistem Anda.")
        sys.exit(1)

    print(f"Ditemukan Microsoft Edge di: {edge_exe}")
    print("Mengekspor HTML ke PDF berkualitas tinggi (Text-Enabled)...")

    # Command to run Edge in headless mode and print to PDF natively
    cmd = [
        edge_exe,
        "--headless",
        "--disable-gpu",
        "--no-sandbox",
        f"--print-to-pdf={pdf_path}",
        "--no-pdf-header-footer",  # Hides page title and URL margins
        f"file:///{html_path}"
    ]

    try:
        # Delete existing file to avoid conflicts
        if os.path.exists(pdf_path):
            os.remove(pdf_path)

        subprocess.run(cmd, check=True)

        if os.path.exists(pdf_path) and os.path.getsize(pdf_path) > 0:
            print("\n[SUCCESS] BERHASIL!")
            print(f"Berkas PDF ATS-friendly berhasil dibuat di: {pdf_path}")
            print(f"Ukuran berkas: {os.path.getsize(pdf_path)} bytes")
            print("\nSilakan tes kembali dengan menjalankan: python extract_pdf_v2.py")
        else:
            print("\n[FAILED] GAGAL: Proses selesai tetapi berkas PDF tidak terbentuk.")
    except Exception as e:
        print(f"\n[ERROR] ERROR saat menjalankan ekspor: {e}")

if __name__ == "__main__":
    main()
