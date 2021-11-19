import mysql.connector

db = mysql.connector.connect(
    host="localhost"
    user="telegram"
    password="password")

cursor = db.cursor()

# init
cursor.execute("CREATE DATABASE Speiseplan")
cursor.execute("CREATE TABLE Speiseplan(Standort VARCHAR(127), Datum DATE, Gericht VARCHAR(255))")
cursor.execute("CREATE TABLE Gericht(ID ID, Datum DATE, Kategorie, Name, Zutaten, Preis, Zusatzstoffe, Allergene")
cursor.execute("CREATE TABLE Kategorie(ID ID, Name VARCHAR(127), Label VARCHAR(127))")
cursor.execute("CRATE TABLE Zusatzstoffe(ID ID, Name VARCHAR(127)")
cursor.execute("CRATE TABLE Allergene(ID ID, Name VARCHAR(127)")
cursor.execute("CRATE TABLE Zusatzstoffe(ID ID, Name VARCHAR(127)")

