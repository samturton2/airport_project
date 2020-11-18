# Connects to DB and creates all of the tables
import pyodbc

class CreateTables:
    def __init__(self):
        server = "ldaijiw-micro.cdix33vx1qyf.eu-west-2.rds.amazonaws.com"
        database = "test_database"
        username = "ldaijiw"
        password = "DreamJLMSU743"
        self.connection = pyodbc.connect(f"""
                DRIVER=ODBC Driver 17 for SQL Server;
                SERVER={server};
                DATABASE={database};
                UID={username};
                PWD={password}""")
        self.cursor = self.connection.cursor()

        self.cursor.execute("""
            CREATE TABLE [Passengers] (
                [Passenger_id] INT IDENTITY(1,1) NOT NULL,
                [PassportNumber] VARCHAR(9) NOT NULL,
                [FirstName] VARCHAR(32) NOT NULL,
                [LastName] VARCHAR(32) NOT NULL,
                [Gender] VARCHAR(16) NOT NULL,
                [DateOfBirth] DATE NOT NULL,
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
                [Username] VARCHAR(32) NOT NULL,
                [UserPassword] VARCHAR(32) NOT NULL,
                [PassportNumber] VARCHAR(9) NOT NULL,
                [OnLocation] INT NOT NULL,
                PRIMARY KEY ([Staff_id]),
                FOREIGN KEY ([Job_id]) REFERENCES Jobs([Job_id])
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

                        """)
        self.connection.commit()

        self.cursor.execute("""INSERT INTO Airports (Airport_ID, AirportName, AirportCountry, Timezone) VALUES ('LHR', 'London Heathrow', 'UK', 0);""")
        self.connection.commit()

        print(self.cursor.execute("SELECT * FROM Airports").fetchone())

c = CreateTables()
