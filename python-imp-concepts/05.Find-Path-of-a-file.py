from pathlib import Path

myfile = 'rajaprasad'
file_path = str(Path(f'{myfile}.pem').resolve())
print(file_path)
