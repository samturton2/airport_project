-- What's new?
-- Added Gender to Passengers and Staff
-- Removed some NOT NULL restrictions in the FlightTrip table
        -- We can create flights without requiring an Aircraft_id and availableseats

CREATE DATABASE Airport;
USE Airport;


DROP TABLE FlightStaff;
DROP TABLE TicketDetails;
DROP TABLE FlightTrip;
DROP TABLE Aircraft;
DROP TABLE AircraftStatus;
DROP TABLE AircraftType;
DROP TABLE Airports;
DROP TABLE Staff;
DROP TABLE Jobs;
DROP TABLE Passengers;
DROP TABLE StaffLogins;
DROP TABLE PassengerLogins;


SELECT * FROM FlightStaff;
SELECT * FROM TicketDetails;
SELECT * FROM FlightTrip;
SELECT * FROM Aircraft;
SELECT * FROM AircraftStatus;
SELECT * FROM AircraftType;
SELECT * FROM Airports;
SELECT * FROM Staff;
SELECT * FROM StaffLogins;
SELECT * FROM Jobs;
SELECT * FROM Passengers;
SELECT * FROM PassengerLogins;


CREATE TABLE [Passengers] (
    [Passenger_id] INT IDENTITY(1,1) NOT NULL,
    [PassportNumber] VARCHAR(9) NOT NULL,
    [FirstName] VARCHAR(32) NOT NULL,
    [LastName] VARCHAR(32) NOT NULL,
    [Gender] VARCHAR(16) NOT NULL,
    [DateOfBirth] DATE NOT NULL,
    PRIMARY KEY ([Passenger_id]) 
);

CREATE TABLE [PassengerLogins] (
    [Passenger_id] INT IDENTITY(1,1) NOT NULL,
    PassengerUsername VARCHAR(32),
    PassengerPassword VARCHAR(MAX),
    PRIMARY KEY ([Passenger_id])

);

CREATE TABLE [Jobs] (
    [Job_id] INT IDENTITY(1,1) NOT NULL,
    [Job] VARCHAR(32),
    PRIMARY KEY ([Job_id])
);


CREATE TABLE [Staff] (
    [Staff_id] INT IDENTITY(1,1) NOT NULL,
    [Job_id] INT,
    [FirstName] VARCHAR(32) NOT NULL,
    [LastName] VARCHAR(32) NOT NULL,
    [Gender] VARCHAR(32) NOT NULL,
    [PassportNumber] VARCHAR(9) NOT NULL,
    [OnLocation] INT NOT NULL,
    PRIMARY KEY ([Staff_id]),
    FOREIGN KEY ([Job_id]) REFERENCES Jobs([Job_id])
);

CREATE TABLE [StaffLogins] (
    [Staff_id] INT IDENTITY(1,1) NOT NULL,
    [StaffUsername] VARCHAR(32),
    [StaffPassword] VARCHAR(MAX),
    [StaffLevel] INT,
    PRIMARY KEY ([Staff_id])

);

CREATE TABLE [Airports] (
    [Airport_id] VARCHAR(3) NOT NULL,
    [AirportName] VARCHAR(32) NOT NULL,
    [AirportCountry] VARCHAR(32) NOT NULL,
    [Timezone] INT NOT NULL,
    PRIMARY KEY ([Airport_id])
);


CREATE TABLE [AircraftType] (
    [AircraftType_id] INT IDENTITY(1,1) NOT NULL,
    [Type] VARCHAR(32) NOT NULL,
    [MaxCapacity] INT NOT NULL,
    PRIMARY KEY ([AircraftType_id])
);


CREATE TABLE [AircraftStatus] (
    [AircraftStatus_id] INT IDENTITY(1,1) NOT NULL,
    [Status] VARCHAR(32),
    PRIMARY KEY ([AircraftStatus_id])
);


CREATE TABLE [Aircraft] (
    [Aircraft_id] INT IDENTITY(1,1) NOT NULL,
    [AircraftStatus_id] INT NOT NULL,
    [AircraftType_id] INT NOT NULL,
    PRIMARY KEY ([Aircraft_id]),
    FOREIGN KEY ([AircraftType_id]) REFERENCES AircraftType(AircraftType_id),
    FOREIGN KEY ([AircraftStatus_id]) REFERENCES AircraftStatus(AircraftStatus_id)
);


CREATE TABLE [FlightTrip] (
    [FlightTrip_id] INT IDENTITY(1,1) NOT NULL,
    [Aircraft_id] INT,
    [DepartureTime] DATETIME NOT NULL,
    [ArrivalTime] DATETIME NOT NULL,
    [AvailableSeats] INT,
    [DepartureAirport] VARCHAR(3) NOT NULL,
    [ArrivalAirport] VARCHAR(3) NOT NULL,
    [TicketPrice] DECIMAL(6,2) NOT NULL,
    [TicketDiscount] FLOAT NOT NULL,
    PRIMARY KEY ([FlightTrip_id]),
    FOREIGN KEY ([Aircraft_id]) REFERENCES Aircraft(Aircraft_id),
    FOREIGN KEY ([DepartureAirport]) REFERENCES Airports(Airport_id),
    FOREIGN KEY ([ArrivalAirport]) REFERENCES Airports(Airport_id)
);


CREATE TABLE [TicketDetails] (
    [Ticket_id] INT IDENTITY(3246,1) NOT NULL,
    [Passenger_id] INT NOT NULL,
    [FlightTrip_id] INT NOT NULL,
    [PricePaid] DECIMAL(6,2) NOT NULL,
    PRIMARY KEY ([Ticket_id]),
    FOREIGN KEY ([Passenger_id]) REFERENCES Passengers(Passenger_id),
    FOREIGN KEY ([FlightTrip_id]) REFERENCES FlightTrip(FlightTrip_id)
);


CREATE TABLE [FlightStaff] (
    [FlightTrip_id] INT NOT NULL,
    [Staff_id] INT NOT NULL,
    FOREIGN KEY ([FlightTrip_id]) REFERENCES FlightTrip(FlightTrip_id),
    FOREIGN KEY ([Staff_id]) REFERENCES Staff(Staff_id)
);