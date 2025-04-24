import tkinter as tk
from tkinter import messagebox, simpledialog
from cert_generator import generate_certificate
from blockchain_interface import issue_certificate, verify_certificate, revoke_certificate
import datetime

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
                with open(f"certs/{certID}_public_key.pem", "r") as f:
                    pubkey = f.read()
                with open(f"certs/{certID}_signature.sig", "rb") as f:
                    signature = f.read().hex()
                days = simpledialog.askinteger("Input", "Enter validity in days:")
                expiry = int((datetime.datetime.now() + datetime.timedelta(days=days)).timestamp())
                issue_certificate(certID, pubkey, expiry, signature)
                messagebox.showinfo("Success", "Certificate issued on blockchain.")
            except FileNotFoundError:
                messagebox.showerror("Error", "Certificate files not found.")

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
