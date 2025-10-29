import requests
import json

# Piston API endpoint
url = "https://emkc.org/api/v2/piston/execute"

# Code to run
code = """\
import numpy as np

# Create a 1D array
arr = np.array([1, 2, 3, 4, 5])
print("Original Array:", arr)

# Perform element-wise operations
print("Array multiplied by 2:", arr * 2)
print("Array squared:", arr ** 2)

# Create a 2D array (matrix)
matrix = np.array([[1, 2, 3], [4, 5, 6]])
print(matrix)

# Compute basic statistics
print("Mean:", np.mean(arr))
print("Standard Deviation:", np.std(arr))
print("Sum of elements:", np.sum(arr))

# Matrix operations
print("Matrix Transpose:", matrix.T)
print("Matrix multiplied by itself (dot product): " , np.dot(matrix, matrix.T))

print("Hello how are you?")
"""

# Prepare payload
payload = {
    "language": "python",
    "version": "3.10.0",
    "files": [
        {
            "name": "main.py",
            "content": code
        }
    ]
}

# Send POST request
response = requests.post(url, json=payload)

# Parse and print result
if response.status_code == 200:
    data = response.json()
    print("Output:\n", data["run"]["output"])
else:
    print("Error:", response.status_code, response.text)
