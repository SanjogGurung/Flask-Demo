print("1. About to import server...")
import server
print("2. Import complete!")

print(f"3. The imported app name is: {server.app.name}")
print(f"4. Inside this context, server.__name__ is: {server.__name__}")

