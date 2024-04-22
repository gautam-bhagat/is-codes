import random

def generate_prime():
    primes = [i for i in range(100, 1000) if all(i % j != 0 for j in range(2, i))]
    return random.choice(primes)

def generate_primitive_root(prime):
    primitive_roots = []
    for i in range(2, prime):
        if pow(i, prime - 1, prime) == 1:
            primitive_roots.append(i)
    return random.choice(primitive_roots)

def generate_private_key(prime):
    return random.randint(2, prime - 2)

def generate_public_key(private_key, prime, primitive_root):
    return pow(primitive_root, private_key, prime)

def generate_shared_secret(private_key, public_key, prime):
    return pow(public_key, private_key, prime)

# Generate prime number
prime = generate_prime()

# Generate primitive root modulo prime
primitive_root = generate_primitive_root(prime)

# Alice's side
alice_private_key = generate_private_key(prime)
alice_public_key = generate_public_key(alice_private_key, prime, primitive_root)

# Bob's side
bob_private_key = generate_private_key(prime)
bob_public_key = generate_public_key(bob_private_key, prime, primitive_root)

# Shared secret computation
alice_shared_secret = generate_shared_secret(alice_private_key, bob_public_key, prime)
bob_shared_secret = generate_shared_secret(bob_private_key, alice_public_key, prime)

# Check if both sides computed the same shared secret
print("Shared secret (Alice's side):", alice_shared_secret)
print("Shared secret (Bob's side):", bob_shared_secret)
