# SQL DB Creation
The SQL DB and Tables for the Airport were created
based on the ERD diagram as discussed in group meeting.

- First, the database was created for the group:
```sql
CREATE DATABASE Group_3_AirportDatabase
USE Group_3_AirportDatabase
```

- Then each table was created based on the ERD diagram:
```sql
CREATE TABLE [Passengers] (
    [Passenger_id] INT IDENTITY(1,1) NOT NULL,
    [PassportNumber] VARCHAR(9) NOT NULL,
    [FirstName] VARCHAR(32) NOT NULL,
    [LastName] VARCHAR(32) NOT NULL,
    [DateOfBirth] DATE NOT NULL,
    PRIMARY KEY ([Passenger_id]) 
);

CREATE TABLE [Staff] (
    [Staff_id] INT IDENTITY(1,1) NOT NULL,
    [Username] VARCHAR(16) NOT NULL,
    [FirstName] VARCHAR(32) NOT NULL,
    [LastName] VARCHAR(40) NOT NULL,
    [UserPassword] VARCHAR(32) NOT NULL,
    [PassportNumber] VARCHAR(9) NOT NULL,
    [OnLocation] INT NOT NULL,
    PRIMARY KEY ([Staff_id])
);

CREATE TABLE [Airports] (
    [Airport_id] VARCHAR(3) NOT NULL,
    [AirportName] VARCHAR(32) NOT NULL,
    [AirportCity] VARCHAR(32) NOT NULL,
    [AirportCountry] VARCHAR(32) NOT NULL,
    [Timezone] INT NOT NULL,
    PRIMARY KEY ([Airport_id])
);

CREATE TABLE [AircraftType] (
    [AircraftType_id] INT IDENTITY(1,1) NOT NULL,
    [Model] VARCHAR(10) NOT NULL,
    [MaxCapacity] INT NOT NULL,
    PRIMARY KEY ([AircraftType_id])
);

CREATE TABLE [Aircraft] (
    [Aircraft_id] INT IDENTITY(1,1) NOT NULL,
    [AircraftType_id] INT NOT NULL,
    [OnFlight] INT NOT NULL,
    [AssignedToFlight] INT NOT NULL,
    [OnLocation] INT NOT NULL,
    PRIMARY KEY ([Aircraft_id]),
    FOREIGN KEY ([AircraftType_id]) REFERENCES AircraftType(AircraftType_id),
);

CREATE TABLE [FlightTrip] (
    [FlightTrip_id] INT IDENTITY(1,1) NOT NULL,
    [Aircraft_id] INT NOT NULL,
    [DepartureTime] DATETIME NOT NULL,
    [ArrivalTime] DATETIME NOT NULL,
    [AvailableSeats] INT NOT NULL,
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
```
- The following code deletes all of the tables in case
there is an error as well as displaying the contents of 
the table
```sql
DROP TABLE FlightStaff
DROP TABLE TicketDetails
DROP TABLE FlightTrip
DROP TABLE Aircraft
DROP TABLE AircraftType
DROP TABLE Airports
DROP TABLE Staff
DROP TABLE Passengers

SELECT * FROM Passengers
SELECT * FROM TicketDetails
SELECT * FROM FlightTrip
SELECT * FROM FlightStaff
SELECT * FROM Staff
SELECT * FROM Aircraft
SELECT * FROM AircraftType
SELECT * FROM Airports
```
