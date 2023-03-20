import csv
import json


def convert_file(csv_file, json_file, model):
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
                if line["is_published"] == "TRUE":
                    line["is_published"] = True
                else:
                    line["is_published"] = False

            if "location_id" in line:
                line["location"] = [line["location_id"]]
                del line["location_id"]

            result.append({"model": model, "fields": line})

    with open(json_file, "w", encoding="utf-8")as f:
        f.write(json.dumps(result, ensure_ascii=False))


convert_file("data_lesson_28/category.csv", "data_lesson_28/category.json", "ads.category")
convert_file("data_lesson_28/ad.csv", "data_lesson_28/ad.json", "ads.ad")
convert_file("data_lesson_28/user.csv", "data_lesson_28/user.json", "users.user")
convert_file("data_lesson_28/location.csv", "data_lesson_28/location.json", "users.location")
