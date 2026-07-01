# fixing label bug, car label was one but it has to start from zero
import os

label_dirs = [
    r"D:\Dataset\car_parking_dataset\train\labels",
    r"D:\Dataset\car_parking_dataset\test\labels",
]

for label_dir in label_dirs:
    if not os.path.exists(label_dir):
        print(f"folder {label_dir} not found!")
        continue

    for file in os.listdir(label_dir):
        if not file.endswith(".txt"):
            continue

        file_path = os.path.join(label_dir, file)
        with open(file_path, "r") as f:
            lines = f.readlines()

        new_lines = []
        for line in lines:
            parts = line.strip().split()
            if not parts:
                continue
            if parts[0] == "1":
                parts[0] = "0"
            new_lines.append(" ".join(parts))

        with open(file_path, "w") as f:
            f.write("\n".join(new_lines))

print("✅Done!")
