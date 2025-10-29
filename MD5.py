import hashlib

# Function to generate MD5 hash for a given text
def generate_md5(text):
    return hashlib.md5(text.encode()).hexdigest()

# Step 1: Sender creates a message and its signature
message = input("Enter the original message: ")
sender_signature = generate_md5(message)
print("Generated MD5 Signature (Sender):", sender_signature)

# Step 2: Receiver enters received message and signature for verification
received_message = input("\nEnter the received message: ")
received_signature = input("Enter the received MD5 signature: ")

# Step 3: Receiver generates hash of received message
receiver_hash = generate_md5(received_message)

# Step 4: Compare both signatures
print("\nVerifying authenticity...")
if receiver_hash == received_signature:
    print("✅ Signature Verified: The message is authentic.")
else:
    print("❌ Signature Mismatch: The message has been tampered with.")
