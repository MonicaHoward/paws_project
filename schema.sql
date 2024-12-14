CREATE DATABASE paws_rescue_db;

USE paws_rescue_db;

CREATE TABLE pets (
	id INT AUTO_INCREMENT PRIMARY KEY,
    petName VARCHAR(255) NOT NULL,
    petAge INT NOT NULL,
    petBreed VARCHAR(255) NOT NULL,
    petImage VARCHAR(500)
);

INSERT INTO pets (petName, petAge, petBreed, petImage)
VALUES 
	("Jack", 17, "Beagle Mix", null),
    ("Spike", 2, "Golden Retriever", "https://images.pexels.com/photos/3397939/pexels-photo-3397939.jpeg"),
    ("Lucky", 5, "Husky", "https://images.pexels.com/photos/3640877/pexels-photo-3640877.jpeg")
    