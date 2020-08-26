CREATE TABLE student (
    student_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(20),
    major VARCHAR(20) DEFAULT 'undecided'
);

DESCRIBE student;

DROP TABLE student;

ALTER TABLE student ADD gpa DECIMAL(3,2);

ALTER TABLE student DROP COLUMN gpa;

SELECT * FROM student;

INSERT INTO student(name, major) VALUES('Jack', 'Biology');
INSERT INTO student(name, major) VALUES('Kate', 'Sociology');
INSERT INTO student(name, major) VALUES('Claire', 'Chemistry');
INSERT INTO student(name, major) VALUES('Jack', 'Biology');
INSERT INTO student(name, major) VALUES('Mike', 'Computer Science');

UPDATE student
SET major = 'Bio'
WHERE major = 'Biology';

UPDATE student
SET major = 'Com Sci'
WHERE student_id = 4;

UPDATE student
SET major = 'Com Sci'
WHERE major = 'Computer Science';

Update student
SET major = 'Biochemistry'
WHERE major = 'Chemisty' OR major = 'Bio';

UPDATE student
SET name = 'Tom', major = 'undecided'
WHERE student_id = 1;

DELETE FROM student
WHERE student_id = 5;

SELECT name, major
FROM student
ORDER BY student_id;

SELECT name, major
FROM student
LIMIT 2;

SELECT *
FROM student
WHERE major = 'Biology';

-- <, >, <=, >=, =, <>, AND, OR  <-operators


SELECT *
FROM student
WHERE name IN ('Jack', 'Claire');