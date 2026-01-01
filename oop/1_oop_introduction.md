## 1 - Object Oriented Programming Introduction

**Object-Oriented Programming (OOP)** is a way of writing code by modeling real-world things as **objects**.  
Each object has two parts:  
- **Data** (what it is) → e.g., IP address, port number  
- **Actions** (what it can do) → e.g., scan, connect, crack

### 🔑 4 Basic Concepts

| Concept      | Meaning                          |
|--------------|----------------------------------|
| **Class**    | A blueprint or template for objects |
| **Object**   | A real instance created from a class |
| **Method**   | A function that belongs to an object |
| **Attribute**| A piece of data stored in an object |

### 💡 Example: Simple Security Tool

```
# A class: blueprint for a port scanner
class PortScanner:
    def __init__(self, target):
        self.target = target  # attribute

    def scan(self):  # method
        print(f"Scanning ports on {self.target}...")

# Create an object
my_scanner = PortScanner("192.168.1.1")
my_scanner.scan()  # Output: Scanning ports on 192.168.1.1...
```
### Why OOP in Cybersecurity?
1. Makes tools modular and reusable
2. Easier to read, maintain, and extend
3. Helps model real attacks (like scanners or botnets) naturally


