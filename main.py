from blockchain import Blockchain
from wallet import Wallet

# Tạo Blockchain và các ví điện tử
my_blockchain = Blockchain()
alice_wallet = Wallet("Alice")
bob_wallet = Wallet("Bob")

# Alice gửi tiền cho Bob
transaction1 = alice_wallet.send_money(bob_wallet.public_key, 100)
if transaction1:
    my_blockchain.add_transaction(transaction1)

# Bob gửi tiền lại cho Alice
transaction2 = bob_wallet.send_money(alice_wallet.public_key, 50)
if transaction2:
    my_blockchain.add_transaction(transaction2)

# Đào khối để xác nhận giao dịch
print("\n⛏️ Đang đào khối mới...\n")
my_blockchain.mine_pending_transactions()

# Hiển thị chuỗi khối
print("\n🔗 Blockchain:")
for block in my_blockchain.chain:
    print(f"Block #{block.index}, Hash: {block.hash}, Transactions: {block.transactions}")

# Kiểm tra tính hợp lệ của Blockchain
print("\nBlockchain hợp lệ:", my_blockchain.is_chain_valid())
