import csv
from faker import Faker

def main():
    fake = Faker("ru_RU")
    out_path = "/users.csv"

    with open(out_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        for _ in range(600):
            writer.writerow([fake.first_name(), fake.last_name()])

    print("users.csv сгенерирован (600 строк)")

if __name__ == "__main__":
    main()
