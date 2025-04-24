import tkinter as tk
from tkinter import messagebox, simpledialog, filedialog
from cert_generator import generate_certificate
from blockchain_interface import issue_certificate, verify_certificate, revoke_certificate
import datetime
import zipfile
import os

class PKIGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Blockchain PKI System")

        self.label = tk.Label(root, text="=== Blockchain PKI System ===", font=("Helvetica", 16))
        self.label.pack(pady=10)

        tk.Button(root, text="Generate Certificate", command=self.generate_certificate).pack(pady=5)
        tk.Button(root, text="Issue Certificate", command=self.issue_certificate).pack(pady=5)
        tk.Button(root, text="Verify Certificate", command=self.verify_certificate).pack(pady=5)
        tk.Button(root, text="Revoke Certificate", command=self.revoke_certificate).pack(pady=5)
        tk.Button(root, text="Exit", command=root.quit).pack(pady=5)

    def generate_certificate(self):
        name = simpledialog.askstring("Input", "Enter name:")
        if name:
            pub_path, sig_path, message = generate_certificate(name)
            messagebox.showinfo("Certificate Generated", f"Public key: {pub_path}\nSignature: {sig_path}")

    def issue_certificate(self):
        certID = simpledialog.askstring("Input", "Enter certificate ID:")
        if certID:
            try:
                pub_key_path = f"certs/{certID}_public_key.pem"
                sig_path = f"certs/{certID}_signature.sig"

                with open(pub_key_path, "r") as f:
                    pubkey = f.read()
                with open(sig_path, "rb") as f:
                    signature = f.read().hex()
                days = simpledialog.askinteger("Input", "Enter validity in days:")
                expiry = int((datetime.datetime.now() + datetime.timedelta(days=days)).timestamp())

                issue_certificate(certID, pubkey, expiry, signature)
                messagebox.showinfo("Success", "Certificate issued on blockchain.")

                # Prompt user to download certificate files
                self.download_certificate(certID, pub_key_path, sig_path)

            except FileNotFoundError:
                messagebox.showerror("Error", "Certificate files not found.")

    def download_certificate(self, certID, pub_key_path, sig_path):
        save_path = filedialog.asksaveasfilename(
            title="Save Certificate As...",
            defaultextension=".zip",
            filetypes=[("Zip files", "*.zip")],
            initialfile=f"{certID}_certificate.zip"
        )
        if save_path:
            with open(pub_key_path, "r") as f:
                pubkey = f.read()
            with open(sig_path, "rb") as f:
                signature = f.read().hex()

            issue_time = int(datetime.datetime.now().timestamp())
            expiry_time = int((datetime.datetime.now() + datetime.timedelta(days=365)).timestamp())  # placeholder
            cert_content = (
                 f"Certificate ID: {certID}\n"
                 f"Issue Date: {datetime.datetime.fromtimestamp(issue_time)}\n"
                 f"Expiry Date: {datetime.datetime.fromtimestamp(expiry_time)}\n"
                 f"Public Key:\n{pubkey}\n"
                 f"Signature:\n{signature}\n"
            )

            cert_filename = f"certs/{certID}.cert"
            with open(cert_filename, "w") as f:
                 f.write(cert_content)

             # Add all files to zip
            with zipfile.ZipFile(save_path, 'w') as zipf:
                zipf.write(pub_key_path, os.path.basename(pub_key_path))
                zipf.write(sig_path, os.path.basename(sig_path))
                zipf.write(cert_filename, os.path.basename(cert_filename))

            messagebox.showinfo("Download Complete", f"Certificate saved to:\n{save_path}")

            # Optionally delete temp .cert file
            os.remove(cert_filename)

    def verify_certificate(self):
        certID = simpledialog.askstring("Input", "Enter certificate ID:")
        if certID:
            try:
                pubkey, valid, issueDate, expiry, signature = verify_certificate(certID)
                msg = (
                    f"Public Key: {pubkey}\n"
                    f"Valid: {valid}\n"
                    f"Issue Date: {datetime.datetime.fromtimestamp(issueDate)}\n"
                    f"Expiry Date: {datetime.datetime.fromtimestamp(expiry)}\n"
                    f"Signature: {signature}"
                )
                messagebox.showinfo("Certificate Info", msg)
            except Exception as e:
                messagebox.showerror("Error", f"Verification failed: {e}")

    def revoke_certificate(self):
        certID = simpledialog.askstring("Input", "Enter certificate ID:")
        if certID:
            try:
                revoke_certificate(certID)
                messagebox.showinfo("Success", "Certificate revoked.")
            except Exception as e:
                messagebox.showerror("Error", f"Revocation failed: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = PKIGUI(root)
    root.mainloop()
