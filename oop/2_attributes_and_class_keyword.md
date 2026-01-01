## 2 - Attributes and the Class Keyword

In Python, the **`class` keyword** is used to define a new class (a blueprint for objects).  
Every object created from a class can store its own **data**, called **attributes**.

### 🔑 Key Terms

- **Class**: Template for creating objects  
- **Instance**: A real object created from a class  
- **Attribute**: A variable that belongs to an object (stores its data)

### 💡 Example: Simple Recon Tool

```
class ReconTool:
    # Class attribute (shared by all instances)
    tool_type = "Recon"

    def __init__(self, target, timeout=5):
        # Instance attributes (unique per object)
        self.target = target
        self.timeout = timeout
        self.status = "Ready"

# Create two different tools
scanner = ReconTool("192.168.1.10")
cracker = ReconTool("admin:hash.txt", timeout=10)

print(scanner.target)   # Output: 192.168.1.10
print(cracker.timeout)  # Output: 10
print(scanner.tool_type)  # Output: Recon (shared)
```
### Important Notes
1. __init__ is called automatically when an object is created.
2. self refers to the current object – it’s how you access its attributes.
3. Class attributes (like tool_type) are shared by all objects.
4. Instance attributes (like target, timeout) are unique per object

### 🔒 Why This Matters in Cybersecurity?
1. Each tool (scanner, cracker, stealer) can have its own target, timeout, status
2. Shared settings (like tool_type = "Offensive") can be defined once.
3. Keeps code clean, organized, and scalable.

