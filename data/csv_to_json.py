import csv
import json


def conver_file(csv_file, json_file, model):
    """
    Функция преобразования csv-файла и конвертации в json
    """
    result = []
    with open(csv_file, encoding="utf-8") as file:
        for line in csv.DictReader(file):
            del line["id"]
            if "price" in line:
                line["price"] = int(line["price"])

            if "is_published" in line:
                if "is_published" == "TRUE":
                    line["is_published"] = True
                else:
                    line["is_published"] = False
            result.append({"model": model, "fields": line})

    with open(json_file, "w", encoding="utf-8")as f:
        f.write(json.dumps(result, ensure_ascii=False))


conver_file("categories.csv", "categories.json", "ads.category")
conver_file("ads.csv", "ads.json", "ads.ad")
