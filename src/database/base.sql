create table Users(
	id integer PRIMARY KEY autoincrement,
    login varchar(16) not null unique,
    password varchar(16) not null,
    power_level integer
);

create table subject(
	id integer PRIMARY KEY autoincrement,
    date varchar(50),
    Start_Time time,
    end_Time time
);

create table Teachers(
	id integer PRIMARY KEY autoincrement,
    FirstName varchar(50),
    email  varchar(50),
    Phone integer,
    LastName varchar,
);

create table Students(
    id     integer PRIMARY KEY autoincrement,
    FirsName varchar(50),
        Gender varchar (50),
        email integer,
        LastName varchar(50)
);

create table Courses(
    id     integer PRIMARY KEY autoincrement,
    CourseName varchar(50),
        Description varchar (50)
);

create table Enrollment(
    id     integer PRIMARY KEY autoincrement,
    StudentID integer,
    CourselID integer,
    Date integer
);

create table Grades(
    id     integer PRIMARY KEY autoincrement,
    EnrollmentID integer,
    Grade varchar (50)
);
