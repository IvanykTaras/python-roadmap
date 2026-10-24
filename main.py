from dataclasses import dataclass

@dataclass
class Address:
    street: str
    city: str
    state: str
    zip: str

@dataclass
class User:
    name: str
    age: int
    address: Address

# Tworzenie obiektu
obj = User(
    name="John Doe",
    age=30,
    address=Address(
        street="123 Main St",
        city="Anytown",
        state="CA",
        zip="12345"
    )
)

print(obj.address.city)