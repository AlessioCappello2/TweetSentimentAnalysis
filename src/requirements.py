import subprocess

packages = [
    "twikit==2.1.3",
    "pandas==2.2.3",
    "nltk==3.9.1",
    "transformers==4.46.1",
    "deep-translator==1.11.4"
]

for package in packages:
    subprocess.run(["pip", "install", package], check=True)