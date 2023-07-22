DROP TABLE person;

CREATE TABLE person(
	id INT UNSIGNED NOT NULL AUTO_INCREMENT,
    name VARCHAR(80) NOT NULL,
    age INT UNSIGNED NOT NULL,
    
    CONSTRAINT pk_person_id PRIMARY KEY(id),
    CONSTRAINT chk_age_18 CHECK(age >= 18)
) ENGINE=InnoDB;

DELETE from person where id < 11;

select * from person;

INSERT INTO person (name, age) VALUES ("test", 18);
INSERT INTO person (name, age) VALUES ("test2", 20);
INSERT INTO person (name, age) VALUES ("test3", 19);
INSERT INTO person (name, age) VALUES ("test4", 34);

DESCRIBE person;

CREATE TABLE vehicle(
    type VARCHAR(15) NOT NULL,
    model VARCHAR(40) NOT NULL,
    license_plate CHAR(12) NOT NULL,
    owner_id INT UNSIGNED NOT NULL,
    
    CONSTRAINT pk_vehicle_license_plate PRIMARY KEY(license_plate),
    CONSTRAINT fk_owner_id_to_id FOREIGN KEY(owner_id) REFERENCES person(id)
) ENGINE=InnoDB;
    
describe vehicle;

INSERT INTO vehicle(type, model, license_plate, owner_id) VALUES ("carro", "sla", "12345689012", 11);    

select * from vehicle;
select id, upper(name), age, license_plate, type from person, vehicle where person.id=11;
select * from person, vehicle where id=owner_id;

ALTER TABLE person ADD COLUMN driver_license CHAR(20);
ALTER TABLE person ADD CONSTRAINT u_driver_license UNIQUE(driver_license);
ALTER TABLE person modify name varchar(20);
ALTER TABLE person DROP COLUMN name;