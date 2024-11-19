from fastapi import FastAPI
import csv


app = FastAPI()

dats = "mydats.csv"

@app.get("/datasets")
def main():
    with open(dats, mode="r") as file:
        reader = csv.DictReader(file)

        return [i for i in reader]