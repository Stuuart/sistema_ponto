DROP TABLE IF EXISTS Attendance;
DROP TABLE IF EXISTS Schedule;
DROP TABLE IF EXISTS Punching;
DROP TABLE IF EXISTS Employee;

CREATE TABLE Employee (
  CardID INT PRIMARY KEY,
  Name VARCHAR(50)
  -- other attributes as needed
);

CREATE TABLE Punching (
  PunchingID INT PRIMARY KEY,
  CardID INT,
  TimeStamp TIMESTAMP,
  PunchType VARCHAR(10), -- check-in or check-out
  FOREIGN KEY (CardID) REFERENCES Employee(CardID)
);

CREATE TABLE Schedule (
  ScheduleID INT PRIMARY KEY,
  CardID INT,
  StartTime TIME,
  EndTime TIME,
  -- other attributes as needed
  FOREIGN KEY (CardID) REFERENCES Employee(CardID)
);


CREATE TABLE Attendance (
  AttendanceID INT PRIMARY KEY,
  CardID INT,
  Date DATE,
  StartTime TIME,
  EndTime TIME,
  -- other attributes as needed
  FOREIGN KEY (CardID) REFERENCES Employee(CardID),
  PunchingID INT,
  FOREIGN KEY (PunchingID) REFERENCES Punching(PunchingID)
);

