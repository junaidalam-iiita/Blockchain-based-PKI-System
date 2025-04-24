from cert_generator import generate_certificate
from blockchain_interface import issue_certificate, verify_certificate, revoke_certificate
import datetime

def main():
    while True:
        print("\n=== Blockchain PKI System ===")
        print("1. Generate Certificate")
        print("2. Issue Certificate")
        print("3. Verify Certificate")
        print("4. Revoke Certificate")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter name: ")
            pub_path, sig_path, message = generate_certificate(name)
            print("Certificate generated.")
            print("Public key:", pub_path)
            print("Signature:", sig_path)

        elif choice == "2":
            certID = input("Enter certificate ID: ")
            with open(f"certs/{certID}_public_key.pem", "r") as f:
                pubkey = f.read()
            with open(f"certs/{certID}_signature.sig", "rb") as f:
                signature = f.read().hex()
            days = int(input("Enter validity in days: "))
            expiry = int((datetime.datetime.now() + datetime.timedelta(days=days)).timestamp())
            issue_certificate(certID, pubkey, expiry, signature)
            print("Certificate issued on blockchain.")

        elif choice == "3":
            certID = input("Enter certificate ID: ")
            pubkey, valid, issueDate, expiry, signature = verify_certificate(certID)
            print(f"Public Key: {pubkey}")
            print(f"Valid: {valid}")
            print(f"Issue Date: {datetime.datetime.fromtimestamp(issueDate)}")
            print(f"Expiry Date: {datetime.datetime.fromtimestamp(expiry)}")
            print(f"Signature: {signature}")

        elif choice == "4":
            certID = input("Enter certificate ID: ")
            revoke_certificate(certID)
            print("Certificate revoked.")

        elif choice == "5":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
