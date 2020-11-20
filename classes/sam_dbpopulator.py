from database_connector import DBConnector
from cryptic import Cryptic

#THIS WAS KEPT AS A REFERENCE< SHOULD NOT USE

class DBPopulator(DBConnector):
    def __init__(self):
        super().__init__()

    def populate(self):
        crypto = Cryptic()
        # loop through passenger passwords and encrypt them to add to the db
        passenger_passwords = ['Rb1jaXeu4', 'Kz5CS6gBdy', 'UfL7VEll3', 'Vol5C5c4', 'nm7GMMN', 'E5ZKWgugWz', 'yovvJYp9M51R', '9HJYvnaU7z', 'A3wyaHLowUy', 'XzXiMBjH', 'Mqtg874dg', 'PIi4pXKG1', 'FyBYF9PMOBQ', 'IaHrpHM', 'VcXw0j', 'UPpTFq3T', 'Qb9VF2', '9Q5ANpstk', 'UnYIhmHDJm', 'SkcuZpXbGx', '0Fa3bWRjII', 'dWt6KVWqk2Db', 'k86V29A3sQb', '8YDYNz8b', 'Er5FaWRh', 'hI1BK0h', 'tBdBIphb', 'wVQQQBtv86w', 'RDfxssYI', 'N4bJzmY6', 'eIJcW1go8TBY', 'KmJ7z8', 'iMyQpCiiK', 'uYu9wyaZIS', 'sK59i7ePo5Sa', 'PHv2sfTuDzj', 'kKwitjI', 'kt5xSvSwoC3', 'u1VbFx6zSo4', 'NTTm3owqJAwu', 'BFSa2mcV', 'Nd9ObFytbqgo', '9p5kjZJErY', 'MVu2E960v', 'BxFMAfWs3', '12LYI1Io9', 'cDMlSy5', 'FEbGXDOO3D', 'ZoymSzia0e51', 'lATdjQ4', 'IjaS641O', 'XfSkiw', 'xGcRPxaRCl', 'z2vPRNkbe', 'NLhn1NSXEvMG', 's2RGZv', 'brAb956A', 'vCJ5oCoFVi', 'PaD93lN59xb', '4l1n9A', '146ePb', 'kJdN3lVi', '1cwAcR1', 'rq2f4J1Ss7', 'IHKctP8xK', 'WXJ3MZurX', 'uiuslf9z3yR', 'gshWhlqqsnNb', 'AYp9rPjpDv', 'yJI7FbtfW9H', 'BbOCzqmU66', 'WwQMJnH038', 'tAemGLdLOpo4', 'XvolCv', 'RluN3W', 'uCTTpUP', 'hn75EwfU', '8KVzc4jXV', 'JLuDCiplgTQX', 'wbsjqW828du', 'r0tK06o4r', 'jk234A324', '2BgRQJ', 'kyWq7m', 'zs7w2wfw', 'jKuYs4ZrOEj', 'VYC0GKSWbY4', 'V8PCxlfI14Jq', '0J1W6y', 'VIW6Um', 'a01rRAdBgJ', '8KGzR4OnO7v6', 'deGGa8jcANa', 'sd4vwI', 'Or2m6C', 'u24HZT8xbgtp', 'b2zLfrXb', 'ALHvlKwxNPsp', 'zCPuFGkh', '3wYueKDuJ']
        ppas = []
        for password in passenger_passwords:
            ppas.append(crypto.encrypt(password))

        # repeat for staff passwords
        staff_passwords = ['AjfGwQW', 'bahQ2wiaU31a', 'fJjYEdD', 'nyTKb9', 'PgMXq4P1fbI', 'hFsVCDIcUpo', '7NKitRk', 'hrrne2vZsu', 'lB7zlT0UXLD', 'NgsBRmBPR', '4fALiTapQL', 'nxi1zB8', 'NXjcjS', 'Ox6F2OD8H', 'D5kAblkFu', 'JUNE7f', 'd2sPNi7r', 'au59B7', 'r3k77bgVnZbN', 'kkigNmKZA56', 'C1SvkTppdv1', 'tMYv5mzG', 'aaejTbRzTc', 'hGx0MKpE', 'QNF88D91PP', 'fNt26nrYzCun', 'PAAIE13F', 'sJRHyV', 'gbIMPY5', 'irofnuriHw', 'KiMJUtFO', 'XAyS3K', 'ZZGkvKTvQHI7', 'sltQCcOE', 'zuSriOljI', 'oKDZG0', 'DfRQAOj', 'DgdCA1VLZ', 'UZbga6n1XZ4', 'lH8mirNSpK', '9GSrP1MmxvK', 'SoI25iv', 'SsWCci9dB', 'CqxhOo4vW', 'VaTvCyf5', 'Sdl3nttVA7J', '6CWEOD6rPM', 'cBf9qB', 'ZM41s0UC1', 'MvxnB0Ho', 'Z98jUpt', 'uXJaPEn2V', 'nwO7rKmI13w', 'KUMb85P', 'NZcssFEz', '06sXlaO6', 'gKfY2d', 'KDK0xV4zX', 'qyt78p', 'tjWTon9zqM', '7IdEXkQm0', 'EarqIh', 'UlaPwWp', 'H1B9jX', 'n3rPqOyoJuP', 'ZuOy7jk7HNa', 'h8LlHMngW3F', 'o8fiD6Wwhy', 'pF6pnjVRHL', 'FQTR2wB8SOx', 'vrGd4Elmv8', 'JCuibHJjkfgI', 'QqMqWhweQPaJ', 'jQHypQA', 'VO0Zxtjz', 'vHlyxT', 'NlxKgdquGu', 'II1h6klATC4', 'pjjkqTp', 'Q8RaFT', 'zun1k6iK', 'Phremwe3u', 't9N5Ht', 'cRjkBr1bkY', 'cq10PAI', '3sXOwunEA', 'shTIBe1', '90S57vil5emY', 'GbKhXknh', 'sBsbkDjx8u', 'MhPmHHy', 'ImcxPNWME7', 'YN0JUdzo', 'GO3dGs6q0f', 'dV1zOt4u3', '0WmrC4Kit7ti', '3nsG33fOX', 'nvd73LYDsXJ', 'PudRGdf1', 'D1JHSVCSXWaJ']
        spas = []
        for password in staff_passwords:
            spas.append(crypto.encrypt(password))

        self.cursor.execute(f"""
        -- Drops all tables, creates them and insert data into them in one query
-- DROP TABLE FlightStaff;
-- DROP TABLE TicketDetails;
-- DROP TABLE FlightTrip;
-- DROP TABLE Aircraft;
-- DROP TABLE AircraftStatus;
-- DROP TABLE AircraftType;
-- DROP TABLE Airports;
-- DROP TABLE Staff;
-- DROP TABLE Jobs;
-- DROP TABLE Passengers;
-- DROP TABLE StaffLogins;
-- DROP TABLE PassengerLogins;


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
    PassengerPassword VARCHAR(110),
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
    [StaffPassword] VARCHAR(110),
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

-- AIRPORTS
INSERT INTO Airports (Airport_ID, AirportName, AirportCountry, Timezone) VALUES ('LHR', 'London Heathrow', 'UK', 0);
INSERT INTO Airports (Airport_ID, AirportName, AirportCountry, Timezone) VALUES ('LGW', 'London Gatwick',  'UK', 0);
INSERT INTO Airports (Airport_ID, AirportName, AirportCountry, Timezone) VALUES ('MAN', 'Manchester',  'UK', 0);
INSERT INTO Airports (Airport_ID, AirportName, AirportCountry, Timezone) VALUES ('STN', 'London Stansted', 'UK', 0);
INSERT INTO Airports (Airport_ID, AirportName, AirportCountry, Timezone) VALUES ('BHX', 'Birmingham International', 'UK', 0);
INSERT INTO Airports (Airport_ID, AirportName, AirportCountry, Timezone) VALUES ('GLA', 'Glasgow International', 'UK', 0);
INSERT INTO Airports (Airport_ID, AirportName, AirportCountry, Timezone) VALUES ('EDI', 'Edinburgh', 'UK', 0);
INSERT INTO Airports (Airport_ID, AirportName, AirportCountry, Timezone) VALUES ('LTN', 'London Luton', 'UK', 0);
INSERT INTO Airports (Airport_ID, AirportName, AirportCountry, Timezone) VALUES ('BFS', 'Belfast International', 'UK', 0);
INSERT INTO Airports (Airport_ID, AirportName, AirportCountry, Timezone) VALUES ('BRS', 'Bristol', 'UK', 0);
INSERT INTO Airports (Airport_ID, AirportName, AirportCountry, Timezone) VALUES ('NCL', 'Newcastle', 'UK', 0);
INSERT INTO Airports (Airport_ID, AirportName, AirportCountry, Timezone) VALUES ('LCY', 'London City', 'UK', 0);
INSERT INTO Airports (Airport_ID, AirportName, AirportCountry, Timezone) VALUES ('LPL', 'Liverpool John Lennon', 'UK', 0);

-- PASSENGERS
INSERT INTO Passengers (PassportNumber, FirstName, LastName, Gender, DateOfBirth) VALUES ('797323611', 'Stefan', 'Kingswell', 'Male', '11/5/2016');
INSERT INTO Passengers (PassportNumber, FirstName, LastName, Gender, DateOfBirth) VALUES ('099748344', 'Ursala', 'McIan', 'Female', '6/17/1960');
INSERT INTO Passengers (PassportNumber, FirstName, LastName, Gender, DateOfBirth) VALUES ('665668318', 'Warde', 'Pohlke', 'Male', '10/2/1985');
INSERT INTO Passengers (PassportNumber, FirstName, LastName, Gender, DateOfBirth) VALUES ('332698747', 'Randie', 'Bilton', 'Female', '1/20/2000');
INSERT INTO Passengers (PassportNumber, FirstName, LastName, Gender, DateOfBirth) VALUES ('867781431', 'Tony', 'Weald', 'Female', '6/23/1984');
INSERT INTO Passengers (PassportNumber, FirstName, LastName, Gender, DateOfBirth) VALUES ('528954949', 'Lanie', 'Retchless', 'Male', '10/26/1981');
INSERT INTO Passengers (PassportNumber, FirstName, LastName, Gender, DateOfBirth) VALUES ('158615456', 'Trent', 'Laycock', 'Male', '6/13/1983');
INSERT INTO Passengers (PassportNumber, FirstName, LastName, Gender, DateOfBirth) VALUES ('349446365', 'Alexandros', 'Tattoo', 'Male', '10/8/2020');
INSERT INTO Passengers (PassportNumber, FirstName, LastName, Gender, DateOfBirth) VALUES ('792521364', 'Umberto', 'Le Sieur', 'Male', '12/13/2001');
INSERT INTO Passengers (PassportNumber, FirstName, LastName, Gender, DateOfBirth) VALUES ('979570498', 'Brody', 'Seear', 'Male', '11/7/2012');
INSERT INTO Passengers (PassportNumber, FirstName, LastName, Gender, DateOfBirth) VALUES ('194688206', 'Gaile', 'Tankard', 'Male', '5/22/1970');
INSERT INTO Passengers (PassportNumber, FirstName, LastName, Gender, DateOfBirth) VALUES ('128576717', 'Carce', 'Fillingham', 'Male', '10/6/1963');
INSERT INTO Passengers (PassportNumber, FirstName, LastName, Gender, DateOfBirth) VALUES ('838226749', 'Olva', 'Alphege', 'Female', '1/6/1966');
INSERT INTO Passengers (PassportNumber, FirstName, LastName, Gender, DateOfBirth) VALUES ('190322639', 'Rudd', 'Quig', 'Male', '1/31/2003');
INSERT INTO Passengers (PassportNumber, FirstName, LastName, Gender, DateOfBirth) VALUES ('051739379', 'Kipp', 'Lamp', 'Female', '5/9/1981');
INSERT INTO Passengers (PassportNumber, FirstName, LastName, Gender, DateOfBirth) VALUES ('119832514', 'Lotty', 'McCaskill', 'Female', '5/8/2017');
INSERT INTO Passengers (PassportNumber, FirstName, LastName, Gender, DateOfBirth) VALUES ('815985321', 'Kennett', 'Juliano', 'Male', '12/23/1979');
INSERT INTO Passengers (PassportNumber, FirstName, LastName, Gender, DateOfBirth) VALUES ('081583714', 'Iolanthe', 'Grewe', 'Female', '5/11/1970');
INSERT INTO Passengers (PassportNumber, FirstName, LastName, Gender, DateOfBirth) VALUES ('771422839', 'Orrin', 'Toth', 'Male', '4/15/1967');
INSERT INTO Passengers (PassportNumber, FirstName, LastName, Gender, DateOfBirth) VALUES ('648593314', 'Marv', 'Worsell', 'Male', '8/8/1970');
INSERT INTO Passengers (PassportNumber, FirstName, LastName, Gender, DateOfBirth) VALUES ('362372711', 'Chanda', 'Pollard', 'Female', '1/16/1968');
INSERT INTO Passengers (PassportNumber, FirstName, LastName, Gender, DateOfBirth) VALUES ('635532828', 'Cicily', 'Zanini', 'Female', '5/27/1987');
INSERT INTO Passengers (PassportNumber, FirstName, LastName, Gender, DateOfBirth) VALUES ('615250463', 'Kyle', 'Mellenby', 'Male', '1/25/2001');
INSERT INTO Passengers (PassportNumber, FirstName, LastName, Gender, DateOfBirth) VALUES ('670542829', 'Zedekiah', 'Daintier', 'Male', '5/31/1979');
INSERT INTO Passengers (PassportNumber, FirstName, LastName, Gender, DateOfBirth) VALUES ('290064429', 'Clive', 'Bucklee', 'Male', '8/21/1995');
INSERT INTO Passengers (PassportNumber, FirstName, LastName, Gender, DateOfBirth) VALUES ('778983593', 'Mohandis', 'Manclark', 'Male', '3/10/1993');
INSERT INTO Passengers (PassportNumber, FirstName, LastName, Gender, DateOfBirth) VALUES ('935149274', 'Giorgia', 'Bury', 'Female', '3/4/2001');
INSERT INTO Passengers (PassportNumber, FirstName, LastName, Gender, DateOfBirth) VALUES ('949927471', 'Veronique', 'Caven', 'Female', '9/20/1976');
INSERT INTO Passengers (PassportNumber, FirstName, LastName, Gender, DateOfBirth) VALUES ('665451047', 'Nickolaus', 'Sergeant', 'Male', '11/25/1969');
INSERT INTO Passengers (PassportNumber, FirstName, LastName, Gender, DateOfBirth) VALUES ('787415375', 'Tades', 'Cullerne', 'Male', '8/23/2014');
INSERT INTO Passengers (PassportNumber, FirstName, LastName, Gender, DateOfBirth) VALUES ('457182096', 'Finley', 'Burditt', 'Male', '3/23/1991');
INSERT INTO Passengers (PassportNumber, FirstName, LastName, Gender, DateOfBirth) VALUES ('964588464', 'Sosanna', 'Selesnick', 'Female', '7/20/2002');
INSERT INTO Passengers (PassportNumber, FirstName, LastName, Gender, DateOfBirth) VALUES ('099215501', 'Yank', 'Coleman', 'Male', '6/20/1990');
INSERT INTO Passengers (PassportNumber, FirstName, LastName, Gender, DateOfBirth) VALUES ('099668286', 'Normand', 'Boice', 'Male', '11/19/2000');
INSERT INTO Passengers (PassportNumber, FirstName, LastName, Gender, DateOfBirth) VALUES ('653955621', 'Elwira', 'Benez', 'Female', '5/17/1971');
INSERT INTO Passengers (PassportNumber, FirstName, LastName, Gender, DateOfBirth) VALUES ('097427391', 'Lenore', 'McSperron', 'Female', '2/25/1969');
INSERT INTO Passengers (PassportNumber, FirstName, LastName, Gender, DateOfBirth) VALUES ('614592051', 'Iver', 'Yankeev', 'Male', '5/15/1986');
INSERT INTO Passengers (PassportNumber, FirstName, LastName, Gender, DateOfBirth) VALUES ('184369869', 'Claudetta', 'Peplow', 'Female', '9/15/1981');
INSERT INTO Passengers (PassportNumber, FirstName, LastName, Gender, DateOfBirth) VALUES ('287172495', 'Sergei', 'Wisden', 'Male', '3/18/1981');
INSERT INTO Passengers (PassportNumber, FirstName, LastName, Gender, DateOfBirth) VALUES ('357486705', 'Barnaby', 'Dominichelli', 'Male', '4/24/2019');
INSERT INTO Passengers (PassportNumber, FirstName, LastName, Gender, DateOfBirth) VALUES ('752138183', 'Eustacia', 'Yeowell', 'Female', '6/7/1983');
INSERT INTO Passengers (PassportNumber, FirstName, LastName, Gender, DateOfBirth) VALUES ('132878843', 'Kelbee', 'O''Scannill', 'Male', '6/9/2010');
INSERT INTO Passengers (PassportNumber, FirstName, LastName, Gender, DateOfBirth) VALUES ('310332521', 'Ariella', 'Gibbings', 'Female', '7/9/1966');
INSERT INTO Passengers (PassportNumber, FirstName, LastName, Gender, DateOfBirth) VALUES ('849611493', 'Lorena', 'Diggell', 'Female', '12/13/1996');
INSERT INTO Passengers (PassportNumber, FirstName, LastName, Gender, DateOfBirth) VALUES ('679021936', 'Min', 'Holbie', 'Female', '2/4/1961');
INSERT INTO Passengers (PassportNumber, FirstName, LastName, Gender, DateOfBirth) VALUES ('375163111', 'Pavia', 'Branscombe', 'Female', '4/17/2015');
INSERT INTO Passengers (PassportNumber, FirstName, LastName, Gender, DateOfBirth) VALUES ('610480078', 'Caz', 'Connikie', 'Male', '2/27/1976');
INSERT INTO Passengers (PassportNumber, FirstName, LastName, Gender, DateOfBirth) VALUES ('862216959', 'Odelia', 'Antcliffe', 'Female', '12/16/1974');
INSERT INTO Passengers (PassportNumber, FirstName, LastName, Gender, DateOfBirth) VALUES ('914707164', 'Errol', 'Dederick', 'Male', '3/14/1994');
INSERT INTO Passengers (PassportNumber, FirstName, LastName, Gender, DateOfBirth) VALUES ('209060615', 'Alejoa', 'Coneau', 'Male', '3/2/2014');
INSERT INTO Passengers (PassportNumber, FirstName, LastName, Gender, DateOfBirth) VALUES ('432491123', 'Daphene', 'Kennefick', 'Female', '11/29/1985');
INSERT INTO Passengers (PassportNumber, FirstName, LastName, Gender, DateOfBirth) VALUES ('846772661', 'Shina', 'Elstow', 'Female', '3/21/1956');
INSERT INTO Passengers (PassportNumber, FirstName, LastName, Gender, DateOfBirth) VALUES ('270717502', 'Irving', 'Klimecki', 'Male', '3/31/1977');
INSERT INTO Passengers (PassportNumber, FirstName, LastName, Gender, DateOfBirth) VALUES ('430884091', 'Rem', 'Windebank', 'Male', '11/3/2020');
INSERT INTO Passengers (PassportNumber, FirstName, LastName, Gender, DateOfBirth) VALUES ('256545327', 'Barbara-anne', 'Kimbley', 'Female', '10/15/1988');
INSERT INTO Passengers (PassportNumber, FirstName, LastName, Gender, DateOfBirth) VALUES ('940695872', 'Delaney', 'Naper', 'Male', '3/30/2003');
INSERT INTO Passengers (PassportNumber, FirstName, LastName, Gender, DateOfBirth) VALUES ('692467671', 'Stace', 'Polle', 'Female', '6/30/2004');
INSERT INTO Passengers (PassportNumber, FirstName, LastName, Gender, DateOfBirth) VALUES ('411911996', 'Dona', 'Roskelly', 'Female', '8/7/1956');
INSERT INTO Passengers (PassportNumber, FirstName, LastName, Gender, DateOfBirth) VALUES ('275141026', 'Kevan', 'Aspell', 'Male', '5/17/1999');
INSERT INTO Passengers (PassportNumber, FirstName, LastName, Gender, DateOfBirth) VALUES ('008290466', 'Joelynn', 'Newiss', 'Female', '9/18/1957');
INSERT INTO Passengers (PassportNumber, FirstName, LastName, Gender, DateOfBirth) VALUES ('538905481', 'Rod', 'Pharaoh', 'Male', '2/21/1963');
INSERT INTO Passengers (PassportNumber, FirstName, LastName, Gender, DateOfBirth) VALUES ('592582006', 'Caryl', 'Ruddock', 'Male', '8/10/1963');
INSERT INTO Passengers (PassportNumber, FirstName, LastName, Gender, DateOfBirth) VALUES ('738313584', 'Lonny', 'Collen', 'Male', '8/31/1983');
INSERT INTO Passengers (PassportNumber, FirstName, LastName, Gender, DateOfBirth) VALUES ('279229641', 'Rosemary', 'Berthon', 'Female', '11/11/1995');
INSERT INTO Passengers (PassportNumber, FirstName, LastName, Gender, DateOfBirth) VALUES ('380752928', 'Gussie', 'Grindle', 'Female', '7/29/2013');
INSERT INTO Passengers (PassportNumber, FirstName, LastName, Gender, DateOfBirth) VALUES ('934305924', 'Rosita', 'Tournie', 'Female', '8/28/1972');
INSERT INTO Passengers (PassportNumber, FirstName, LastName, Gender, DateOfBirth) VALUES ('810867075', 'Gabrila', 'Clute', 'emale', '1/17/1992');
INSERT INTO Passengers (PassportNumber, FirstName, LastName, Gender, DateOfBirth) VALUES ('210099769', 'Bordie', 'Kirman', 'Male', '1/27/2006');
INSERT INTO Passengers (PassportNumber, FirstName, LastName, Gender, DateOfBirth) VALUES ('506362474', 'Zeb', 'Haysman', 'Male', '5/14/2008');
INSERT INTO Passengers (PassportNumber, FirstName, LastName, Gender, DateOfBirth) VALUES ('595339478', 'Ber', 'Lemme', 'Male', '6/15/1973');
INSERT INTO Passengers (PassportNumber, FirstName, LastName, Gender, DateOfBirth) VALUES ('797527484', 'Anjanette', 'Kielty', 'Female', '10/28/1953');
INSERT INTO Passengers (PassportNumber, FirstName, LastName, Gender, DateOfBirth) VALUES ('911054393', 'Dotty', 'Endrizzi', 'Female', '6/15/1964');
INSERT INTO Passengers (PassportNumber, FirstName, LastName, Gender, DateOfBirth) VALUES ('678004704', 'Franciskus', 'Messitt', 'Male', '9/27/1960');
INSERT INTO Passengers (PassportNumber, FirstName, LastName, Gender, DateOfBirth) VALUES ('726715048', 'Vanya', 'Bielfelt', 'Male', '10/24/2003');
INSERT INTO Passengers (PassportNumber, FirstName, LastName, Gender, DateOfBirth) VALUES ('934136675', 'Zacharia', 'Tucknott', 'Male', '3/5/1968');
INSERT INTO Passengers (PassportNumber, FirstName, LastName, Gender, DateOfBirth) VALUES ('152896669', 'Dunstan', 'Baudi', 'Male', '9/9/1979');
INSERT INTO Passengers (PassportNumber, FirstName, LastName, Gender, DateOfBirth) VALUES ('836197797', 'Staffard', 'Gainsburgh', 'Male', '12/1/1957');
INSERT INTO Passengers (PassportNumber, FirstName, LastName, Gender, DateOfBirth) VALUES ('125713399', 'Rachelle', 'Schops', 'Female', '1/12/1958');
INSERT INTO Passengers (PassportNumber, FirstName, LastName, Gender, DateOfBirth) VALUES ('575191549', 'Phillis', 'McKeveney', 'Female', '4/5/1965');
INSERT INTO Passengers (PassportNumber, FirstName, LastName, Gender, DateOfBirth) VALUES ('100358926', 'Jackie', 'Sumnall', 'Female', '11/30/1965');
INSERT INTO Passengers (PassportNumber, FirstName, LastName, Gender, DateOfBirth) VALUES ('631569948', 'Pierette', 'Skupinski', 'Female', '9/6/1996');
INSERT INTO Passengers (PassportNumber, FirstName, LastName, Gender, DateOfBirth) VALUES ('167272163', 'Val', 'Helix', 'Male', '12/12/1951');
INSERT INTO Passengers (PassportNumber, FirstName, LastName, Gender, DateOfBirth) VALUES ('706967192', 'Stuart', 'Wrack', 'Male', '3/1/1971');
INSERT INTO Passengers (PassportNumber, FirstName, LastName, Gender, DateOfBirth) VALUES ('223050947', 'Mattheus', 'Branche', 'Male', '9/20/1969');
INSERT INTO Passengers (PassportNumber, FirstName, LastName, Gender, DateOfBirth) VALUES ('545684882', 'Janina', 'Wardlaw', 'Female', '2/7/1985');
INSERT INTO Passengers (PassportNumber, FirstName, LastName, Gender, DateOfBirth) VALUES ('543019174', 'Lindsey', 'Pottle', 'Female', '5/17/1965');
INSERT INTO Passengers (PassportNumber, FirstName, LastName, Gender, DateOfBirth) VALUES ('169940048', 'Dunc', 'Eastcourt', 'Male', '7/30/1997');
INSERT INTO Passengers (PassportNumber, FirstName, LastName, Gender, DateOfBirth) VALUES ('205006784', 'Lurette', 'Danjoie', 'Female', '8/23/1977');
INSERT INTO Passengers (PassportNumber, FirstName, LastName, Gender, DateOfBirth) VALUES ('795288731', 'Valerye', 'Riding', 'Female', '10/2/1962');
INSERT INTO Passengers (PassportNumber, FirstName, LastName, Gender, DateOfBirth) VALUES ('969197118', 'Tannie', 'Le Guin', 'Male', '9/24/2006');
INSERT INTO Passengers (PassportNumber, FirstName, LastName, Gender, DateOfBirth) VALUES ('221528072', 'Chelsie', 'Lockey', 'Female', '8/19/1962');
INSERT INTO Passengers (PassportNumber, FirstName, LastName, Gender, DateOfBirth) VALUES ('415849685', 'Curry', 'Standall', 'Male', '6/25/1971');
INSERT INTO Passengers (PassportNumber, FirstName, LastName, Gender, DateOfBirth) VALUES ('671019788', 'Jaquelyn', 'Pardew', 'Female', '7/18/2010');
INSERT INTO Passengers (PassportNumber, FirstName, LastName, Gender, DateOfBirth) VALUES ('525028971', 'Amara', 'Kennler', 'Female', '3/3/1954');
INSERT INTO Passengers (PassportNumber, FirstName, LastName, Gender, DateOfBirth) VALUES ('943745794', 'Roselia', 'Haughton', 'Female', '6/6/1996');
INSERT INTO Passengers (PassportNumber, FirstName, LastName, Gender, DateOfBirth) VALUES ('379095977', 'Arabella', 'Keely', 'Female', '4/15/1981');
INSERT INTO Passengers (PassportNumber, FirstName, LastName, Gender, DateOfBirth) VALUES ('593522296', 'Brodie', 'Jeffcoat', 'Male', '11/13/1981');
INSERT INTO Passengers (PassportNumber, FirstName, LastName, Gender, DateOfBirth) VALUES ('140995129', 'Zondra', 'Barkhouse', 'Female', '7/30/2011');
INSERT INTO Passengers (PassportNumber, FirstName, LastName, Gender, DateOfBirth) VALUES ('191814948', 'Yehudi', 'Collcutt', 'Male', '8/24/2002');
INSERT INTO Passengers (PassportNumber, FirstName, LastName, Gender, DateOfBirth) VALUES ('983465329', 'Teador', 'Roadknight', 'Male', '11/19/2012');

-- PassengerLogins
INSERT INTO PassengerLogins (PassengerUsername, PassengerPassword) VALUES ('skingswell0', '{ppas[0]}');
INSERT INTO PassengerLogins (PassengerUsername, PassengerPassword) VALUES ('umcian1', '{ppas[1]}');
INSERT INTO PassengerLogins (PassengerUsername, PassengerPassword) VALUES ('wpohlke2', '{ppas[2]}');
INSERT INTO PassengerLogins (PassengerUsername, PassengerPassword) VALUES ('rbilton3', '{ppas[3]}');
INSERT INTO PassengerLogins (PassengerUsername, PassengerPassword) VALUES ('tweald4', '{ppas[4]}');
INSERT INTO PassengerLogins (PassengerUsername, PassengerPassword) VALUES ('lretchless5', '{ppas[5]}');
INSERT INTO PassengerLogins (PassengerUsername, PassengerPassword) VALUES ('tlaycock6', '{ppas[6]}');
INSERT INTO PassengerLogins (PassengerUsername, PassengerPassword) VALUES ('atattoo7', '{ppas[7]}');
INSERT INTO PassengerLogins (PassengerUsername, PassengerPassword) VALUES ('ulesieur8', '{ppas[8]}');
INSERT INTO PassengerLogins (PassengerUsername, PassengerPassword) VALUES ('bseear9', '{ppas[9]}');
INSERT INTO PassengerLogins (PassengerUsername, PassengerPassword) VALUES ('gtankarda', '{ppas[10]}');
INSERT INTO PassengerLogins (PassengerUsername, PassengerPassword) VALUES ('cfillinghamb', '{ppas[11]}');
INSERT INTO PassengerLogins (PassengerUsername, PassengerPassword) VALUES ('oalphegec', '{ppas[12]}');
INSERT INTO PassengerLogins (PassengerUsername, PassengerPassword) VALUES ('rquigd', '{ppas[13]}');
INSERT INTO PassengerLogins (PassengerUsername, PassengerPassword) VALUES ('klampe', '{ppas[14]}');
INSERT INTO PassengerLogins (PassengerUsername, PassengerPassword) VALUES ('lmccaskillf', '{ppas[15]}');
INSERT INTO PassengerLogins (PassengerUsername, PassengerPassword) VALUES ('kjulianog', '{ppas[16]}');
INSERT INTO PassengerLogins (PassengerUsername, PassengerPassword) VALUES ('igreweh', '{ppas[17]}');
INSERT INTO PassengerLogins (PassengerUsername, PassengerPassword) VALUES ('otothi', '{ppas[18]}');
INSERT INTO PassengerLogins (PassengerUsername, PassengerPassword) VALUES ('mworsellj', '{ppas[19]}');
INSERT INTO PassengerLogins (PassengerUsername, PassengerPassword) VALUES ('cpollardk', '{ppas[20]}');
INSERT INTO PassengerLogins (PassengerUsername, PassengerPassword) VALUES ('czaninil', '{ppas[21]}');
INSERT INTO PassengerLogins (PassengerUsername, PassengerPassword) VALUES ('kmellenbym', '{ppas[22]}');
INSERT INTO PassengerLogins (PassengerUsername, PassengerPassword) VALUES ('zdaintiern', '{ppas[23]}');
INSERT INTO PassengerLogins (PassengerUsername, PassengerPassword) VALUES ('cbuckleeo', '{ppas[24]}');
INSERT INTO PassengerLogins (PassengerUsername, PassengerPassword) VALUES ('mmanclarkp', '{ppas[25]}');
INSERT INTO PassengerLogins (PassengerUsername, PassengerPassword) VALUES ('gburyq', '{ppas[26]}');
INSERT INTO PassengerLogins (PassengerUsername, PassengerPassword) VALUES ('vcavenr', '{ppas[27]}');
INSERT INTO PassengerLogins (PassengerUsername, PassengerPassword) VALUES ('nsergeants', '{ppas[28]}');
INSERT INTO PassengerLogins (PassengerUsername, PassengerPassword) VALUES ('tcullernet', '{ppas[29]}');
INSERT INTO PassengerLogins (PassengerUsername, PassengerPassword) VALUES ('fburdittu', '{ppas[30]}');
INSERT INTO PassengerLogins (PassengerUsername, PassengerPassword) VALUES ('sselesnickv', '{ppas[31]}');
INSERT INTO PassengerLogins (PassengerUsername, PassengerPassword) VALUES ('ycolemanw', '{ppas[32]}');
INSERT INTO PassengerLogins (PassengerUsername, PassengerPassword) VALUES ('nboicex', '{ppas[33]}');
INSERT INTO PassengerLogins (PassengerUsername, PassengerPassword) VALUES ('ebenezy', '{ppas[34]}');
INSERT INTO PassengerLogins (PassengerUsername, PassengerPassword) VALUES ('lmcsperronz', '{ppas[35]}');
INSERT INTO PassengerLogins (PassengerUsername, PassengerPassword) VALUES ('iyankeev10', '{ppas[36]}');
INSERT INTO PassengerLogins (PassengerUsername, PassengerPassword) VALUES ('cpeplow11', '{ppas[37]}');
INSERT INTO PassengerLogins (PassengerUsername, PassengerPassword) VALUES ('swisden12', '{ppas[38]}');
INSERT INTO PassengerLogins (PassengerUsername, PassengerPassword) VALUES ('bdominichelli13', '{ppas[39]}');
INSERT INTO PassengerLogins (PassengerUsername, PassengerPassword) VALUES ('eyeowell14', '{ppas[40]}');
INSERT INTO PassengerLogins (PassengerUsername, PassengerPassword) VALUES ('koscannill15', '{ppas[41]}');
INSERT INTO PassengerLogins (PassengerUsername, PassengerPassword) VALUES ('agibbings16', '{ppas[42]}');
INSERT INTO PassengerLogins (PassengerUsername, PassengerPassword) VALUES ('ldiggell17', '{ppas[43]}');
INSERT INTO PassengerLogins (PassengerUsername, PassengerPassword) VALUES ('mholbie18', '{ppas[44]}');
INSERT INTO PassengerLogins (PassengerUsername, PassengerPassword) VALUES ('pbranscombe19', '{ppas[45]}');
INSERT INTO PassengerLogins (PassengerUsername, PassengerPassword) VALUES ('cconnikie1a', '{ppas[46]}');
INSERT INTO PassengerLogins (PassengerUsername, PassengerPassword) VALUES ('oantcliffe1b', '{ppas[47]}');
INSERT INTO PassengerLogins (PassengerUsername, PassengerPassword) VALUES ('edederick1c', '{ppas[48]}');
INSERT INTO PassengerLogins (PassengerUsername, PassengerPassword) VALUES ('aconeau1d', '{ppas[49]}');
INSERT INTO PassengerLogins (PassengerUsername, PassengerPassword) VALUES ('dkennefick1e', '{ppas[50]}');
INSERT INTO PassengerLogins (PassengerUsername, PassengerPassword) VALUES ('selstow1f', '{ppas[51]}');
INSERT INTO PassengerLogins (PassengerUsername, PassengerPassword) VALUES ('iklimecki1g', '{ppas[52]}');
INSERT INTO PassengerLogins (PassengerUsername, PassengerPassword) VALUES ('rwindebank1h', '{ppas[53]}');
INSERT INTO PassengerLogins (PassengerUsername, PassengerPassword) VALUES ('bkimbley1i', '{ppas[54]}');
INSERT INTO PassengerLogins (PassengerUsername, PassengerPassword) VALUES ('dnaper1j', '{ppas[55]}');
INSERT INTO PassengerLogins (PassengerUsername, PassengerPassword) VALUES ('spolle1k', '{ppas[56]}');
INSERT INTO PassengerLogins (PassengerUsername, PassengerPassword) VALUES ('droskelly1l', '{ppas[57]}');
INSERT INTO PassengerLogins (PassengerUsername, PassengerPassword) VALUES ('kaspell1m', '{ppas[58]}');
INSERT INTO PassengerLogins (PassengerUsername, PassengerPassword) VALUES ('jnewiss1n', '{ppas[59]}');
INSERT INTO PassengerLogins (PassengerUsername, PassengerPassword) VALUES ('rpharaoh1o', '{ppas[60]}');
INSERT INTO PassengerLogins (PassengerUsername, PassengerPassword) VALUES ('cruddock1p', '{ppas[61]}');
INSERT INTO PassengerLogins (PassengerUsername, PassengerPassword) VALUES ('lcollen1q', '{ppas[62]}');
INSERT INTO PassengerLogins (PassengerUsername, PassengerPassword) VALUES ('rberthon1r', '{ppas[63]}');
INSERT INTO PassengerLogins (PassengerUsername, PassengerPassword) VALUES ('ggrindle1s', '{ppas[64]}');
INSERT INTO PassengerLogins (PassengerUsername, PassengerPassword) VALUES ('rtournie1t', '{ppas[65]}');
INSERT INTO PassengerLogins (PassengerUsername, PassengerPassword) VALUES ('gclute1u', '{ppas[66]}');
INSERT INTO PassengerLogins (PassengerUsername, PassengerPassword) VALUES ('bkirman1v', '{ppas[67]}');
INSERT INTO PassengerLogins (PassengerUsername, PassengerPassword) VALUES ('zhaysman1w', '{ppas[68]}');
INSERT INTO PassengerLogins (PassengerUsername, PassengerPassword) VALUES ('blemme1x', '{ppas[69]}');
INSERT INTO PassengerLogins (PassengerUsername, PassengerPassword) VALUES ('akielty1y', '{ppas[70]}');
INSERT INTO PassengerLogins (PassengerUsername, PassengerPassword) VALUES ('dendrizzi1z', '{ppas[71]}');
INSERT INTO PassengerLogins (PassengerUsername, PassengerPassword) VALUES ('fmessitt20', '{ppas[72]}');
INSERT INTO PassengerLogins (PassengerUsername, PassengerPassword) VALUES ('vbielfelt21', '{ppas[73]}');
INSERT INTO PassengerLogins (PassengerUsername, PassengerPassword) VALUES ('ztucknott22', '{ppas[74]}');
INSERT INTO PassengerLogins (PassengerUsername, PassengerPassword) VALUES ('dbaudi23', '{ppas[75]}');
INSERT INTO PassengerLogins (PassengerUsername, PassengerPassword) VALUES ('sgainsburgh24', '{ppas[76]}');
INSERT INTO PassengerLogins (PassengerUsername, PassengerPassword) VALUES ('rschops25', '{ppas[77]}');
INSERT INTO PassengerLogins (PassengerUsername, PassengerPassword) VALUES ('pmckeveney26', '{ppas[78]}');
INSERT INTO PassengerLogins (PassengerUsername, PassengerPassword) VALUES ('jsumnall27', '{ppas[79]}');
INSERT INTO PassengerLogins (PassengerUsername, PassengerPassword) VALUES ('pskupinski28', '{ppas[80]}');
INSERT INTO PassengerLogins (PassengerUsername, PassengerPassword) VALUES ('SwAP3SyY', '{ppas[81]}');
INSERT INTO PassengerLogins (PassengerUsername, PassengerPassword) VALUES ('swrack2a', '{ppas[82]}');
INSERT INTO PassengerLogins (PassengerUsername, PassengerPassword) VALUES ('mbranche2b', '{ppas[83]}');
INSERT INTO PassengerLogins (PassengerUsername, PassengerPassword) VALUES ('jwardlaw2c', '{ppas[84]}');
INSERT INTO PassengerLogins (PassengerUsername, PassengerPassword) VALUES ('lpottle2d', '{ppas[85]}');
INSERT INTO PassengerLogins (PassengerUsername, PassengerPassword) VALUES ('deastcourt2e', '{ppas[86]}');
INSERT INTO PassengerLogins (PassengerUsername, PassengerPassword) VALUES ('ldanjoie2f', '{ppas[87]}');
INSERT INTO PassengerLogins (PassengerUsername, PassengerPassword) VALUES ('vriding2g', '{ppas[88]}');
INSERT INTO PassengerLogins (PassengerUsername, PassengerPassword) VALUES ('tleguin2h', '{ppas[89]}');
INSERT INTO PassengerLogins (PassengerUsername, PassengerPassword) VALUES ('clockey2i', '{ppas[90]}');
INSERT INTO PassengerLogins (PassengerUsername, PassengerPassword) VALUES ('cstandall2j', '{ppas[91]}');
INSERT INTO PassengerLogins (PassengerUsername, PassengerPassword) VALUES ('jpardew2k', '{ppas[92]}');
INSERT INTO PassengerLogins (PassengerUsername, PassengerPassword) VALUES ('akennler2l', '{ppas[93]}');
INSERT INTO PassengerLogins (PassengerUsername, PassengerPassword) VALUES ('rhaughton2m', '{ppas[94]}');
INSERT INTO PassengerLogins (PassengerUsername, PassengerPassword) VALUES ('akeely2n', '{ppas[95]}');
INSERT INTO PassengerLogins (PassengerUsername, PassengerPassword) VALUES ('bjeffcoat2o', '{ppas[96]}');
INSERT INTO PassengerLogins (PassengerUsername, PassengerPassword) VALUES ('zbarkhouse2p', '{ppas[97]}');
INSERT INTO PassengerLogins (PassengerUsername, PassengerPassword) VALUES ('ycollcutt2q', '{ppas[98]}');
INSERT INTO PassengerLogins (PassengerUsername, PassengerPassword) VALUES ('troadknight2r', '{ppas[99]}');



-- Jobs
INSERT INTO Jobs (Job) VALUES ('Airport Staff')
INSERT INTO Jobs (Job) VALUES ('Flight Crew')

-- Staff
INSERT INTO Staff (PassportNumber, Job_id, FirstName, LastName, Gender, OnLocation) VALUES ('638608473', 2, 'Vilma', 'Feehily', 'Female', 0);
INSERT INTO Staff (PassportNumber, Job_id, FirstName, LastName, Gender, OnLocation) VALUES ('569112024', 2, 'Stacie', 'Dudny', 'Female', 0);
INSERT INTO Staff (PassportNumber, Job_id, FirstName, LastName, Gender, OnLocation) VALUES ('010992093', 2, 'Sibbie', 'Lauritzen', 'Female', 0);
INSERT INTO Staff (PassportNumber, Job_id, FirstName, LastName, Gender, OnLocation) VALUES ('466647063', 2, 'Arnie', 'Idenden', 'Male', 0);
INSERT INTO Staff (PassportNumber, Job_id, FirstName, LastName, Gender, OnLocation) VALUES ('509258376', 2, 'Lucina', 'Ainslee', 'Female', 0);
INSERT INTO Staff (PassportNumber, Job_id, FirstName, LastName, Gender, OnLocation) VALUES ('394889613', 2, 'Neal', 'Mower', 'Male', 0);
INSERT INTO Staff (PassportNumber, Job_id, FirstName, LastName, Gender, OnLocation) VALUES ('181796291', 2, 'Lazaro', 'Teaser', 'Male', 0);
INSERT INTO Staff (PassportNumber, Job_id, FirstName, LastName, Gender, OnLocation) VALUES ('417510888', 2, 'Grete', 'Dunstone', 'Female', 1);
INSERT INTO Staff (PassportNumber, Job_id, FirstName, LastName, Gender, OnLocation) VALUES ('914337521', 2, 'Erek', 'Darlington', 'Male', 0);
INSERT INTO Staff (PassportNumber, Job_id, FirstName, LastName, Gender, OnLocation) VALUES ('532063088', 2, 'Selinda', 'Fulep', 'Female', 1);
INSERT INTO Staff (PassportNumber, Job_id, FirstName, LastName, Gender, OnLocation) VALUES ('154833766', 2, 'Alvina', 'Pybworth', 'Female', 0);
INSERT INTO Staff (PassportNumber, Job_id, FirstName, LastName, Gender, OnLocation) VALUES ('082206348', 2, 'Rey', 'Haggerston', 'Male', 0);
INSERT INTO Staff (PassportNumber, Job_id, FirstName, LastName, Gender, OnLocation) VALUES ('220255868', 2, 'Margarete', 'Docwra', 'Female', 1);
INSERT INTO Staff (PassportNumber, Job_id, FirstName, LastName, Gender, OnLocation) VALUES ('393426358', 2, 'Nevsa', 'Bahls', 'Female', 0);
INSERT INTO Staff (PassportNumber, Job_id, FirstName, LastName, Gender, OnLocation) VALUES ('270536407', 2, 'Hilario', 'Pollett', 'Male', 1);
INSERT INTO Staff (PassportNumber, Job_id, FirstName, LastName, Gender, OnLocation) VALUES ('055637518', 2, 'Linn', 'Jinkin', 'Male', 0);
INSERT INTO Staff (PassportNumber, Job_id, FirstName, LastName, Gender, OnLocation) VALUES ('775458001', 2, 'Randolph', 'Ayscough', 'Male', 0);
INSERT INTO Staff (PassportNumber, Job_id, FirstName, LastName, Gender, OnLocation) VALUES ('887344562', 2, 'Merlina', 'Gligorijevic', 'Female', 0);
INSERT INTO Staff (PassportNumber, Job_id, FirstName, LastName, Gender, OnLocation) VALUES ('784346051', 2, 'Nadia', 'Horrod', 'Female', 0);
INSERT INTO Staff (PassportNumber, Job_id, FirstName, LastName, Gender, OnLocation) VALUES ('991593871', 2, 'Jerome', 'Saunper', 'Male', 0);
INSERT INTO Staff (PassportNumber, Job_id, FirstName, LastName, Gender, OnLocation) VALUES ('246794726', 2, 'Jonell', 'McNerlin', 'Female', 1);
INSERT INTO Staff (PassportNumber, Job_id, FirstName, LastName, Gender, OnLocation) VALUES ('451906321', 2, 'Gregor', 'Osbidston', 'Male', 0);
INSERT INTO Staff (PassportNumber, Job_id, FirstName, LastName, Gender, OnLocation) VALUES ('697946541', 2, 'Gabriel', 'Hryncewicz', 'Male', 1);
INSERT INTO Staff (PassportNumber, Job_id, FirstName, LastName, Gender, OnLocation) VALUES ('394032995', 2, 'Allsun', 'MacKibbon', 'Female', 0);
INSERT INTO Staff (PassportNumber, Job_id, FirstName, LastName, Gender, OnLocation) VALUES ('725454886', 2, 'Berkeley', 'Tippler', 'Male', 1);
INSERT INTO Staff (PassportNumber, Job_id, FirstName, LastName, Gender, OnLocation) VALUES ('447824586', 2, 'Brigitta', 'Rowaszkiewicz', 'Female', 0);
INSERT INTO Staff (PassportNumber, Job_id, FirstName, LastName, Gender, OnLocation) VALUES ('432283666', 2, 'Perice', 'Levesque', 'Male', 0);
INSERT INTO Staff (PassportNumber, Job_id, FirstName, LastName, Gender, OnLocation) VALUES ('457243322', 2, 'Hartwell', 'Duding', 'Male', 1);
INSERT INTO Staff (PassportNumber, Job_id, FirstName, LastName, Gender, OnLocation) VALUES ('478769799', 2, 'Glynn', 'Krysiak', 'Male', 0);
INSERT INTO Staff (PassportNumber, Job_id, FirstName, LastName, Gender, OnLocation) VALUES ('565189779', 2, 'Waylin', 'Heino', 'Male', 1);
INSERT INTO Staff (PassportNumber, Job_id, FirstName, LastName, Gender, OnLocation) VALUES ('041461347', 2, 'Jarrid', 'Coal', 'Male', 1);
INSERT INTO Staff (PassportNumber, Job_id, FirstName, LastName, Gender, OnLocation) VALUES ('406164032', 2, 'Gerri', 'Raisbeck', 'Male', 1);
INSERT INTO Staff (PassportNumber, Job_id, FirstName, LastName, Gender, OnLocation) VALUES ('402302414', 2, 'Ileane', 'Szachniewicz', 'Female', 1);
INSERT INTO Staff (PassportNumber, Job_id, FirstName, LastName, Gender, OnLocation) VALUES ('663834896', 2, 'Mufinella', 'Rama', 'Female', 0);
INSERT INTO Staff (PassportNumber, Job_id, FirstName, LastName, Gender, OnLocation) VALUES ('070945301', 2, 'Charmine', 'Antat', 'Female', 0);
INSERT INTO Staff (PassportNumber, Job_id, FirstName, LastName, Gender, OnLocation) VALUES ('606873545', 2, 'Cammi', 'Villaret', 'Female', 0);
INSERT INTO Staff (PassportNumber, Job_id, FirstName, LastName, Gender, OnLocation) VALUES ('772375659', 2, 'Juliann', 'Platts', 'Female', 0);
INSERT INTO Staff (PassportNumber, Job_id, FirstName, LastName, Gender, OnLocation) VALUES ('189912975', 2, 'Averyl', 'Dalloway', 'Female', 0);
INSERT INTO Staff (PassportNumber, Job_id, FirstName, LastName, Gender, OnLocation) VALUES ('990672017', 2, 'Gaby', 'Yegorchenkov', 'Male', 1);
INSERT INTO Staff (PassportNumber, Job_id, FirstName, LastName, Gender, OnLocation) VALUES ('965550122', 2, 'Louise', 'Warren', 'Female', 1);
INSERT INTO Staff (PassportNumber, Job_id, FirstName, LastName, Gender, OnLocation) VALUES ('915065011', 2, 'Lorena', 'Yallop', 'Female', 1);
INSERT INTO Staff (PassportNumber, Job_id, FirstName, LastName, Gender, OnLocation) VALUES ('740367122', 2, 'Gabrila', 'Gelardi', 'Female', 1);
INSERT INTO Staff (PassportNumber, Job_id, FirstName, LastName, Gender, OnLocation) VALUES ('929895018', 2, 'Cale', 'Swyne', 'Male', 0);
INSERT INTO Staff (PassportNumber, Job_id, FirstName, LastName, Gender, OnLocation) VALUES ('205512341', 2, 'Taite', 'Maryska', 'Male', 0);
INSERT INTO Staff (PassportNumber, Job_id, FirstName, LastName, Gender, OnLocation) VALUES ('763608017', 2, 'Theo', 'Purkis', 'Female', 0);
INSERT INTO Staff (PassportNumber, Job_id, FirstName, LastName, Gender, OnLocation) VALUES ('181266406', 2, 'Urbain', 'Scholtz', 'Male', 0);
INSERT INTO Staff (PassportNumber, Job_id, FirstName, LastName, Gender, OnLocation) VALUES ('682150166', 2, 'Candie', 'Vonderdell', 'Female', 1);
INSERT INTO Staff (PassportNumber, Job_id, FirstName, LastName, Gender, OnLocation) VALUES ('737375773', 2, 'Miltie', 'Fullerton',  'Male', 1);
INSERT INTO Staff (PassportNumber, Job_id, FirstName, LastName, Gender, OnLocation) VALUES ('258339499', 2, 'Caroljean', 'Leynton', 'Female', 0);
INSERT INTO Staff (PassportNumber, Job_id, FirstName, LastName, Gender, OnLocation) VALUES ('399671542', 2, 'Dollie', 'Petty', 'Female', 0);
INSERT INTO Staff (PassportNumber, Job_id, FirstName, LastName, Gender, OnLocation) VALUES ('364662091', 1, 'Elijah', 'Milne', 'Male', 0);
INSERT INTO Staff (PassportNumber, Job_id, FirstName, LastName, Gender, OnLocation) VALUES ('094258719', 1, 'Alena', 'Maris', 'Female', 1);
INSERT INTO Staff (PassportNumber, Job_id, FirstName, LastName, Gender, OnLocation) VALUES ('285889625', 1, 'Meredith', 'Preator', 'Male', 1);
INSERT INTO Staff (PassportNumber, Job_id, FirstName, LastName, Gender, OnLocation) VALUES ('325136331', 1, 'Dermot', 'Adkins', 'Male', 0);
INSERT INTO Staff (PassportNumber, Job_id, FirstName, LastName, Gender, OnLocation) VALUES ('729740093', 1, 'Russell', 'Guihen', 'Male', 0);
INSERT INTO Staff (PassportNumber, Job_id, FirstName, LastName, Gender, OnLocation) VALUES ('789924625', 1, 'Craggy', 'Palfrey', 'Male', 1);
INSERT INTO Staff (PassportNumber, Job_id, FirstName, LastName, Gender, OnLocation) VALUES ('380827988', 1, 'Darryl', 'McTeer', 'Male', 0);
INSERT INTO Staff (PassportNumber, Job_id, FirstName, LastName, Gender, OnLocation) VALUES ('530471769', 1, 'Jamesy', 'Wakes', 'Male', 0);
INSERT INTO Staff (PassportNumber, Job_id, FirstName, LastName, Gender, OnLocation) VALUES ('321332615', 1, 'Hilda', 'Sarjeant', 'Female', 0);
INSERT INTO Staff (PassportNumber, Job_id, FirstName, LastName, Gender, OnLocation) VALUES ('003916065', 1, 'Gareth', 'Sworne', 'Male', 0);
INSERT INTO Staff (PassportNumber, Job_id, FirstName, LastName, Gender, OnLocation) VALUES ('218178222', 1, 'Terrill', 'Gallaway', 'Male', 1);
INSERT INTO Staff (PassportNumber, Job_id, FirstName, LastName, Gender, OnLocation) VALUES ('370666793', 1, 'Mariel', 'Quibell', 'Female', 1);
INSERT INTO Staff (PassportNumber, Job_id, FirstName, LastName, Gender, OnLocation) VALUES ('360590108', 1, 'Aigneis', 'Brinklow', 'Female', 1);
INSERT INTO Staff (PassportNumber, Job_id, FirstName, LastName, Gender, OnLocation) VALUES ('510969549', 1, 'Stormie', 'Peterken',  'Female', 0);
INSERT INTO Staff (PassportNumber, Job_id, FirstName, LastName, Gender, OnLocation) VALUES ('975184177', 1, 'Candy', 'Carlsson', 'Female', 0);
INSERT INTO Staff (PassportNumber, Job_id, FirstName, LastName, Gender, OnLocation) VALUES ('564035457', 1, 'Leelah', 'Bigg', 'Female', 1);
INSERT INTO Staff (PassportNumber, Job_id, FirstName, LastName, Gender, OnLocation) VALUES ('120623308', 1, 'Doria', 'Minchenton', 'Female', 0);
INSERT INTO Staff (PassportNumber, Job_id, FirstName, LastName, Gender, OnLocation) VALUES ('007100475', 1, 'Gary', 'Thaxton', 'Male', 1);
INSERT INTO Staff (PassportNumber, Job_id, FirstName, LastName, Gender, OnLocation) VALUES ('829251041', 1, 'Les', 'Stirling', 'Male', 1);
INSERT INTO Staff (PassportNumber, Job_id, FirstName, LastName, Gender, OnLocation) VALUES ('625849736', 1, 'Vida', 'Dyson', 'Female', 0);
INSERT INTO Staff (PassportNumber, Job_id, FirstName, LastName, Gender, OnLocation) VALUES ('099304802', 1, 'Webb', 'Staining', 'Male', 0);
INSERT INTO Staff (PassportNumber, Job_id, FirstName, LastName, Gender, OnLocation) VALUES ('584552309', 1, 'Stacee', 'MacGown', 'Male', 0);
INSERT INTO Staff (PassportNumber, Job_id, FirstName, LastName, Gender, OnLocation) VALUES ('125951546', 1, 'Florian', 'Stitle', 'Male', 1);
INSERT INTO Staff (PassportNumber, Job_id, FirstName, LastName, Gender, OnLocation) VALUES ('497270616', 1, 'Antonietta', 'Benazet', 'Female', 0);
INSERT INTO Staff (PassportNumber, Job_id, FirstName, LastName, Gender, OnLocation) VALUES ('165180488', 1, 'Freddi', 'Crawshaw', 'Female', 1);
INSERT INTO Staff (PassportNumber, Job_id, FirstName, LastName, Gender, OnLocation) VALUES ('625497227', 1, 'Analiese', 'MacCauley',  'Female', 1);
INSERT INTO Staff (PassportNumber, Job_id, FirstName, LastName, Gender, OnLocation) VALUES ('209025672', 1, 'Lorine', 'Howden', 'Female', 1);
INSERT INTO Staff (PassportNumber, Job_id, FirstName, LastName, Gender, OnLocation) VALUES ('746569567', 1, 'Carina', 'Arnaudot', 'Female', 1);
INSERT INTO Staff (PassportNumber, Job_id, FirstName, LastName, Gender, OnLocation) VALUES ('616500524', 1, 'Jacqui', 'Epsly', 'Female', 1);
INSERT INTO Staff (PassportNumber, Job_id, FirstName, LastName, Gender, OnLocation) VALUES ('083771732', 1, 'Denise', 'Point', 'Female', 0);
INSERT INTO Staff (PassportNumber, Job_id, FirstName, LastName, Gender, OnLocation) VALUES ('559904572', 1, 'Lannie', 'Magrannell', 'Male', 0);
INSERT INTO Staff (PassportNumber, Job_id, FirstName, LastName, Gender, OnLocation) VALUES ('409797189', 1, 'Lelia', 'Schirak', 'Female', 0);
INSERT INTO Staff (PassportNumber, Job_id, FirstName, LastName, Gender, OnLocation) VALUES ('884132233', 1, 'Leda', 'Fenkel', 'Female', 1);
INSERT INTO Staff (PassportNumber, Job_id, FirstName, LastName, Gender, OnLocation) VALUES ('629805599', 1, 'Miriam', 'McGraffin', 'Female', 0);
INSERT INTO Staff (PassportNumber, Job_id, FirstName, LastName, Gender, OnLocation) VALUES ('308331996', 1, 'Marna', 'Darter', 'Female', 1);
INSERT INTO Staff (PassportNumber, Job_id, FirstName, LastName, Gender, OnLocation) VALUES ('668024591', 1, 'Cully', 'Cheng', 'Male', 1);
INSERT INTO Staff (PassportNumber, Job_id, FirstName, LastName, Gender, OnLocation) VALUES ('178172987', 1, 'Delphine', 'Brinkler', 'Female', 0);
INSERT INTO Staff (PassportNumber, Job_id, FirstName, LastName, Gender, OnLocation) VALUES ('325995653', 1, 'Renaud', 'Kobieriecki',  'Male', 0);
INSERT INTO Staff (PassportNumber, Job_id, FirstName, LastName, Gender, OnLocation) VALUES ('802488904', 1, 'Belle', 'Jirek', 'Female', 0);
INSERT INTO Staff (PassportNumber, Job_id, FirstName, LastName, Gender, OnLocation) VALUES ('341640004', 1, 'Emmalynne', 'Newiss', 'Female', 0);
INSERT INTO Staff (PassportNumber, Job_id, FirstName, LastName, Gender, OnLocation) VALUES ('891585236', 1, 'Ciel', 'Parkyn', 'Female', 0);
INSERT INTO Staff (PassportNumber, Job_id, FirstName, LastName, Gender, OnLocation) VALUES ('523132818', 1, 'Nolie', 'Jeffs', 'Female', 1);
INSERT INTO Staff (PassportNumber, Job_id, FirstName, LastName, Gender, OnLocation) VALUES ('611889305', 1, 'Ebony', 'Curnok', 'Female', 0);
INSERT INTO Staff (PassportNumber, Job_id, FirstName, LastName, Gender, OnLocation) VALUES ('950529313', 1, 'Katleen', 'Ivatt', 'Female', 1);
INSERT INTO Staff (PassportNumber, Job_id, FirstName, LastName, Gender, OnLocation) VALUES ('693808037', 1, 'Shelley', 'Pieche', 'Male', 1);
INSERT INTO Staff (PassportNumber, Job_id, FirstName, LastName, Gender, OnLocation) VALUES ('069657418', 1, 'Vinny', 'Canter', 'Female', 0);
INSERT INTO Staff (PassportNumber, Job_id, FirstName, LastName, Gender, OnLocation) VALUES ('654508793', 1, 'Ashlan', 'Battlestone', 'Female', 1);
INSERT INTO Staff (PassportNumber, Job_id, FirstName, LastName, Gender, OnLocation) VALUES ('186629292', 1, 'Eugenie', 'Rown', 'Female', 1);
INSERT INTO Staff (PassportNumber, Job_id, FirstName, LastName, Gender, OnLocation) VALUES ('009137762', 1, 'Clarissa', 'Dillicate', 'Female', 1);
INSERT INTO Staff (PassportNumber, Job_id, FirstName, LastName, Gender, OnLocation) VALUES ('613422892', 1, 'Lock', 'Cawse', 'Male', 0);


INSERT INTO StaffLogins (StaffLevel, StaffUsername, StaffPassword) VALUES (2, 'vfeehily0', '{spas[0]}');
INSERT INTO StaffLogins (StaffLevel, StaffUsername, StaffPassword) VALUES (2, 'sdudny1', '{spas[1]}');
INSERT INTO StaffLogins (StaffLevel, StaffUsername, StaffPassword) VALUES (2, 'slauritzen2', '{spas[2]}');
INSERT INTO StaffLogins (StaffLevel, StaffUsername, StaffPassword) VALUES (2, 'aidenden3', '{spas[3]}');
INSERT INTO StaffLogins (StaffLevel, StaffUsername, StaffPassword) VALUES (2, 'lainslee4', '{spas[4]}');
INSERT INTO StaffLogins (StaffLevel, StaffUsername, StaffPassword) VALUES (2, 'nmower5', '{spas[5]}');
INSERT INTO StaffLogins (StaffLevel, StaffUsername, StaffPassword) VALUES (2, 'lteaser6', '{spas[6]}');
INSERT INTO StaffLogins (StaffLevel, StaffUsername, StaffPassword) VALUES (2, 'gdunstone7', '{spas[7]}');
INSERT INTO StaffLogins (StaffLevel, StaffUsername, StaffPassword) VALUES (2, 'edarlington8', '{spas[8]}');
INSERT INTO StaffLogins (StaffLevel, StaffUsername, StaffPassword) VALUES (2, 'sfulep9', '{spas[9]}');
INSERT INTO StaffLogins (StaffLevel, StaffUsername, StaffPassword) VALUES (2, 'apybwortha', '{spas[10]}');
INSERT INTO StaffLogins (StaffLevel, StaffUsername, StaffPassword) VALUES (2, 'rhaggerstonb', '{spas[11]}');
INSERT INTO StaffLogins (StaffLevel, StaffUsername, StaffPassword) VALUES (2, 'mdocwrac', '{spas[12]}');
INSERT INTO StaffLogins (StaffLevel, StaffUsername, StaffPassword) VALUES (2, 'nbahlsd', '{spas[13]}');
INSERT INTO StaffLogins (StaffLevel, StaffUsername, StaffPassword) VALUES (2, 'hpollette', '{spas[14]}');
INSERT INTO StaffLogins (StaffLevel, StaffUsername, StaffPassword) VALUES (2, 'ljinkinf', '{spas[15]}');
INSERT INTO StaffLogins (StaffLevel, StaffUsername, StaffPassword) VALUES (2, 'rayscoughg', '{spas[16]}');
INSERT INTO StaffLogins (StaffLevel, StaffUsername, StaffPassword) VALUES (2, 'mgligorijevich', '{spas[17]}');
INSERT INTO StaffLogins (StaffLevel, StaffUsername, StaffPassword) VALUES (2, 'nhorrodi', '{spas[18]}');
INSERT INTO StaffLogins (StaffLevel, StaffUsername, StaffPassword) VALUES (2, 'jsaunperj', '{spas[19]}');
INSERT INTO StaffLogins (StaffLevel, StaffUsername, StaffPassword) VALUES (2, 'jmcnerlink', '{spas[20]}');
INSERT INTO StaffLogins (StaffLevel, StaffUsername, StaffPassword) VALUES (2, 'gosbidstonl', '{spas[21]}');
INSERT INTO StaffLogins (StaffLevel, StaffUsername, StaffPassword) VALUES (2, 'ghryncewiczm', '{spas[22]}');
INSERT INTO StaffLogins (StaffLevel, StaffUsername, StaffPassword) VALUES (2, 'amackibbonn', '{spas[23]}');
INSERT INTO StaffLogins (StaffLevel, StaffUsername, StaffPassword) VALUES (2, 'btipplero', '{spas[24]}');
INSERT INTO StaffLogins (StaffLevel, StaffUsername, StaffPassword) VALUES (2, 'browaszkiewiczp', '{spas[25]}');
INSERT INTO StaffLogins (StaffLevel, StaffUsername, StaffPassword) VALUES (2, 'plevesqueq', '{spas[26]}');
INSERT INTO StaffLogins (StaffLevel, StaffUsername, StaffPassword) VALUES (2, 'hdudingr', '{spas[27]}');
INSERT INTO StaffLogins (StaffLevel, StaffUsername, StaffPassword) VALUES (2, 'gkrysiaks', '{spas[28]}');
INSERT INTO StaffLogins (StaffLevel, StaffUsername, StaffPassword) VALUES (2, 'wheinot', '{spas[29]}');
INSERT INTO StaffLogins (StaffLevel, StaffUsername, StaffPassword) VALUES (1, 'jcoalu', '{spas[30]}');
INSERT INTO StaffLogins (StaffLevel, StaffUsername, StaffPassword) VALUES (1, 'graisbeckv', '{spas[31]}');
INSERT INTO StaffLogins (StaffLevel, StaffUsername, StaffPassword) VALUES (1, 'iszachniewiczw', '{spas[32]}');
INSERT INTO StaffLogins (StaffLevel, StaffUsername, StaffPassword) VALUES (1, 'mramax', '{spas[33]}');
INSERT INTO StaffLogins (StaffLevel, StaffUsername, StaffPassword) VALUES (1, 'cantaty', '{spas[34]}');
INSERT INTO StaffLogins (StaffLevel, StaffUsername, StaffPassword) VALUES (1, 'cvillaretz', '{spas[35]}');
INSERT INTO StaffLogins (StaffLevel, StaffUsername, StaffPassword) VALUES (1, 'jplatts10', '{spas[36]}');
INSERT INTO StaffLogins (StaffLevel, StaffUsername, StaffPassword) VALUES (1, 'adalloway11', '{spas[37]}');
INSERT INTO StaffLogins (StaffLevel, StaffUsername, StaffPassword) VALUES (1, 'gyegorchenkov12', '{spas[38]}');
INSERT INTO StaffLogins (StaffLevel, StaffUsername, StaffPassword) VALUES (1, 'lwarren13', '{spas[39]}');
INSERT INTO StaffLogins (StaffLevel, StaffUsername, StaffPassword) VALUES (1, 'lyallop14', '{spas[40]}');
INSERT INTO StaffLogins (StaffLevel, StaffUsername, StaffPassword) VALUES (1, 'ggelardi15', '{spas[41]}');
INSERT INTO StaffLogins (StaffLevel, StaffUsername, StaffPassword) VALUES (1, 'cswyne16', '{spas[42]}');
INSERT INTO StaffLogins (StaffLevel, StaffUsername, StaffPassword) VALUES (1, 'tmaryska17', '{spas[43]}');
INSERT INTO StaffLogins (StaffLevel, StaffUsername, StaffPassword) VALUES (1, 'tpurkis18', '{spas[44]}');
INSERT INTO StaffLogins (StaffLevel, StaffUsername, StaffPassword) VALUES (1, 'uscholtz19', '{spas[45]}');
INSERT INTO StaffLogins (StaffLevel, StaffUsername, StaffPassword) VALUES (1, 'cvonderdell1a', '{spas[46]}');
INSERT INTO StaffLogins (StaffLevel, StaffUsername, StaffPassword) VALUES (1, 'mfullerton1b', '{spas[47]}');
INSERT INTO StaffLogins (StaffLevel, StaffUsername, StaffPassword) VALUES (1, 'cleynton1c', '{spas[48]}');
INSERT INTO StaffLogins (StaffLevel, StaffUsername, StaffPassword) VALUES (1, 'dpetty1d', '{spas[49]}');
INSERT INTO StaffLogins (StaffLevel, StaffUsername, StaffPassword) VALUES (1, 'emilne1e', '{spas[50]}');
INSERT INTO StaffLogins (StaffLevel, StaffUsername, StaffPassword) VALUES (1, 'amaris1f', '{spas[51]}');
INSERT INTO StaffLogins (StaffLevel, StaffUsername, StaffPassword) VALUES (1, 'mpreator1g', '{spas[52]}');
INSERT INTO StaffLogins (StaffLevel, StaffUsername, StaffPassword) VALUES (1, 'dadkins1h', '{spas[53]}');
INSERT INTO StaffLogins (StaffLevel, StaffUsername, StaffPassword) VALUES (1, 'rguihen1i', '{spas[54]}');
INSERT INTO StaffLogins (StaffLevel, StaffUsername, StaffPassword) VALUES (1, 'cpalfrey1j', '{spas[55]}');
INSERT INTO StaffLogins (StaffLevel, StaffUsername, StaffPassword) VALUES (1, 'dmcteer1k', '{spas[56]}');
INSERT INTO StaffLogins (StaffLevel, StaffUsername, StaffPassword) VALUES (1, 'jwakes1l', '{spas[57]}');
INSERT INTO StaffLogins (StaffLevel, StaffUsername, StaffPassword) VALUES (1, 'hsarjeant1m', '{spas[58]}');
INSERT INTO StaffLogins (StaffLevel, StaffUsername, StaffPassword) VALUES (1, 'gsworne1n', '{spas[59]}');
INSERT INTO StaffLogins (StaffLevel, StaffUsername, StaffPassword) VALUES (1, 'tgallaway1o', '{spas[60]}');
INSERT INTO StaffLogins (StaffLevel, StaffUsername, StaffPassword) VALUES (1, 'mquibell1p', '{spas[61]}');
INSERT INTO StaffLogins (StaffLevel, StaffUsername, StaffPassword) VALUES (1, 'abrinklow1q', '{spas[62]}');
INSERT INTO StaffLogins (StaffLevel, StaffUsername, StaffPassword) VALUES (1, 'speterken1r', '{spas[63]}');
INSERT INTO StaffLogins (StaffLevel, StaffUsername, StaffPassword) VALUES (1, 'ccarlsson1s', '{spas[64]}');
INSERT INTO StaffLogins (StaffLevel, StaffUsername, StaffPassword) VALUES (1, 'lbigg1t', '{spas[65]}');
INSERT INTO StaffLogins (StaffLevel, StaffUsername, StaffPassword) VALUES (1, 'dminchenton1u', '{spas[66]}');
INSERT INTO StaffLogins (StaffLevel, StaffUsername, StaffPassword) VALUES (1, 'gthaxton1v', '{spas[67]}');
INSERT INTO StaffLogins (StaffLevel, StaffUsername, StaffPassword) VALUES (1, 'lstirling1w', '{spas[68]}');
INSERT INTO StaffLogins (StaffLevel, StaffUsername, StaffPassword) VALUES (1, 'vdyson1x', '{spas[69]}');
INSERT INTO StaffLogins (StaffLevel, StaffUsername, StaffPassword) VALUES (1, 'wstaining1y', '{spas[70]}');
INSERT INTO StaffLogins (StaffLevel, StaffUsername, StaffPassword) VALUES (1, 'smacgown1z', '{spas[71]}');
INSERT INTO StaffLogins (StaffLevel, StaffUsername, StaffPassword) VALUES (1, 'fstitle20', '{spas[72]}');
INSERT INTO StaffLogins (StaffLevel, StaffUsername, StaffPassword) VALUES (1, 'abenazet21', '{spas[73]}');
INSERT INTO StaffLogins (StaffLevel, StaffUsername, StaffPassword) VALUES (1, 'fcrawshaw22', '{spas[74]}');
INSERT INTO StaffLogins (StaffLevel, StaffUsername, StaffPassword) VALUES (1, 'amaccauley23', '{spas[75]}');
INSERT INTO StaffLogins (StaffLevel, StaffUsername, StaffPassword) VALUES (1, 'lhowden24', '{spas[76]}');
INSERT INTO StaffLogins (StaffLevel, StaffUsername, StaffPassword) VALUES (1, 'carnaudot25', '{spas[77]}');
INSERT INTO StaffLogins (StaffLevel, StaffUsername, StaffPassword) VALUES (1, 'jepsly26', '{spas[78]}');
INSERT INTO StaffLogins (StaffLevel, StaffUsername, StaffPassword) VALUES (1, 'dpoint27', '{spas[79]}');
INSERT INTO StaffLogins (StaffLevel, StaffUsername, StaffPassword) VALUES (1, 'lmagrannell28', '{spas[80]}');
INSERT INTO StaffLogins (StaffLevel, StaffUsername, StaffPassword) VALUES (1, 'lschirak29', '{spas[81]}');
INSERT INTO StaffLogins (StaffLevel, StaffUsername, StaffPassword) VALUES (1, 'lfenkel2a', '{spas[82]}');
INSERT INTO StaffLogins (StaffLevel, StaffUsername, StaffPassword) VALUES (1, 'mmcgraffin2b', '{spas[83]}');
INSERT INTO StaffLogins (StaffLevel, StaffUsername, StaffPassword) VALUES (1, 'mdarter2c', '{spas[84]}');
INSERT INTO StaffLogins (StaffLevel, StaffUsername, StaffPassword) VALUES (1, 'ccheng2d', '{spas[85]}');
INSERT INTO StaffLogins (StaffLevel, StaffUsername, StaffPassword) VALUES (1, 'dbrinkler2e', '{spas[86]}');
INSERT INTO StaffLogins (StaffLevel, StaffUsername, StaffPassword) VALUES (1, 'rkobieriecki2f', '{spas[87]}');
INSERT INTO StaffLogins (StaffLevel, StaffUsername, StaffPassword) VALUES (1, 'bjirek2g', '{spas[88]}');
INSERT INTO StaffLogins (StaffLevel, StaffUsername, StaffPassword) VALUES (1, 'enewiss2h', '{spas[89]}');
INSERT INTO StaffLogins (StaffLevel, StaffUsername, StaffPassword) VALUES (1, 'cparkyn2i', '{spas[90]}');
INSERT INTO StaffLogins (StaffLevel, StaffUsername, StaffPassword) VALUES (1, 'njeffs2j', '{spas[91]}');
INSERT INTO StaffLogins (StaffLevel, StaffUsername, StaffPassword) VALUES (1, 'ecurnok2k', '{spas[92]}');
INSERT INTO StaffLogins (StaffLevel, StaffUsername, StaffPassword) VALUES (1, 'kivatt2l', '{spas[93]}');
INSERT INTO StaffLogins (StaffLevel, StaffUsername, StaffPassword) VALUES (1, 'spieche2m', '{spas[94]}');
INSERT INTO StaffLogins (StaffLevel, StaffUsername, StaffPassword) VALUES (1, 'vcanter2n', '{spas[95]}');
INSERT INTO StaffLogins (StaffLevel, StaffUsername, StaffPassword) VALUES (1, 'abattlestone2o', '{spas[96]}');
INSERT INTO StaffLogins (StaffLevel, StaffUsername, StaffPassword) VALUES (1, 'erown2p', '{spas[97]}');
INSERT INTO StaffLogins (StaffLevel, StaffUsername, StaffPassword) VALUES (1, 'cdillicate2q', '{spas[98]}');
INSERT INTO StaffLogins (StaffLevel, StaffUsername, StaffPassword) VALUES (1, 'lcawse2r', '{spas[99]}');

-- AIRCRAFT TYPES
INSERT INTO AircraftType (Type, MaxCapacity) VALUES ('Plane', 400);
INSERT INTO AircraftType (Type, MaxCapacity) VALUES ('Helicopter', 6);


-- Aircraft Status
INSERT INTO AircraftStatus (Status) VALUES ('Available');
INSERT INTO AircraftStatus (Status) VALUES ('On Flight');
INSERT INTO AircraftStatus (Status) VALUES ('Assigned To Flight');


-- Aircraft -- The first two planes are assigned to flights
INSERT INTO Aircraft (AircraftType_id, AircraftStatus_id) VALUES (1, 3)
INSERT INTO Aircraft (AircraftType_id, AircraftStatus_id) VALUES (1, 3)
INSERT INTO Aircraft (AircraftType_id, AircraftStatus_id) VALUES (1, 1)
INSERT INTO Aircraft (AircraftType_id, AircraftStatus_id) VALUES (1, 1)
INSERT INTO Aircraft (AircraftType_id, AircraftStatus_id) VALUES (1, 1)
INSERT INTO Aircraft (AircraftType_id, AircraftStatus_id) VALUES (1, 1)
INSERT INTO Aircraft (AircraftType_id, AircraftStatus_id) VALUES (1, 1)
INSERT INTO Aircraft (AircraftType_id, AircraftStatus_id) VALUES (1, 1)
INSERT INTO Aircraft (AircraftType_id, AircraftStatus_id) VALUES (1, 1)
INSERT INTO Aircraft (AircraftType_id, AircraftStatus_id) VALUES (1, 1)
INSERT INTO Aircraft (AircraftType_id, AircraftStatus_id) VALUES (1, 1)
INSERT INTO Aircraft (AircraftType_id, AircraftStatus_id) VALUES (1, 1)
INSERT INTO Aircraft (AircraftType_id, AircraftStatus_id) VALUES (1, 1)
INSERT INTO Aircraft (AircraftType_id, AircraftStatus_id) VALUES (1, 1)
INSERT INTO Aircraft (AircraftType_id, AircraftStatus_id) VALUES (1, 1)
INSERT INTO Aircraft (AircraftType_id, AircraftStatus_id) VALUES (1, 1)
INSERT INTO Aircraft (AircraftType_id, AircraftStatus_id) VALUES (1, 1)
INSERT INTO Aircraft (AircraftType_id, AircraftStatus_id) VALUES (1, 1)
INSERT INTO Aircraft (AircraftType_id, AircraftStatus_id) VALUES (1, 1)
INSERT INTO Aircraft (AircraftType_id, AircraftStatus_id) VALUES (1, 1)
INSERT INTO Aircraft (AircraftType_id, AircraftStatus_id) VALUES (1, 1)
INSERT INTO Aircraft (AircraftType_id, AircraftStatus_id) VALUES (1, 1)
INSERT INTO Aircraft (AircraftType_id, AircraftStatus_id) VALUES (1, 1)
INSERT INTO Aircraft (AircraftType_id, AircraftStatus_id) VALUES (1, 1)
INSERT INTO Aircraft (AircraftType_id, AircraftStatus_id) VALUES (1, 1)
INSERT INTO Aircraft (AircraftType_id, AircraftStatus_id) VALUES (1, 1)
INSERT INTO Aircraft (AircraftType_id, AircraftStatus_id) VALUES (1, 1)
INSERT INTO Aircraft (AircraftType_id, AircraftStatus_id) VALUES (1, 1)
INSERT INTO Aircraft (AircraftType_id, AircraftStatus_id) VALUES (1, 1)
INSERT INTO Aircraft (AircraftType_id, AircraftStatus_id) VALUES (1, 1)
INSERT INTO Aircraft (AircraftType_id, AircraftStatus_id) VALUES (1, 1)
INSERT INTO Aircraft (AircraftType_id, AircraftStatus_id) VALUES (1, 1)
INSERT INTO Aircraft (AircraftType_id, AircraftStatus_id) VALUES (1, 1)
INSERT INTO Aircraft (AircraftType_id, AircraftStatus_id) VALUES (1, 1)
INSERT INTO Aircraft (AircraftType_id, AircraftStatus_id) VALUES (1, 1)
INSERT INTO Aircraft (AircraftType_id, AircraftStatus_id) VALUES (1, 1)
INSERT INTO Aircraft (AircraftType_id, AircraftStatus_id) VALUES (1, 1)
INSERT INTO Aircraft (AircraftType_id, AircraftStatus_id) VALUES (1, 1)
INSERT INTO Aircraft (AircraftType_id, AircraftStatus_id) VALUES (1, 1)
INSERT INTO Aircraft (AircraftType_id, AircraftStatus_id) VALUES (1, 1)
INSERT INTO Aircraft (AircraftType_id, AircraftStatus_id) VALUES (1, 1)
INSERT INTO Aircraft (AircraftType_id, AircraftStatus_id) VALUES (1, 1)
INSERT INTO Aircraft (AircraftType_id, AircraftStatus_id) VALUES (1, 1)
INSERT INTO Aircraft (AircraftType_id, AircraftStatus_id) VALUES (1, 1)
INSERT INTO Aircraft (AircraftType_id, AircraftStatus_id) VALUES (1, 1)
INSERT INTO Aircraft (AircraftType_id, AircraftStatus_id) VALUES (1, 1)
INSERT INTO Aircraft (AircraftType_id, AircraftStatus_id) VALUES (1, 1)
INSERT INTO Aircraft (AircraftType_id, AircraftStatus_id) VALUES (1, 1)
INSERT INTO Aircraft (AircraftType_id, AircraftStatus_id) VALUES (2, 1)
INSERT INTO Aircraft (AircraftType_id, AircraftStatus_id) VALUES (2, 1)
-- FlightTrip

-- TRIP FROM HEATHROW TO EDINBURGH - Price is £150 - Discount is 0.1 - Takes 1 hour
INSERT INTO FlightTrip (Aircraft_id, DepartureTime, ArrivalTime, DepartureAirport, ArrivalAirport, AvailableSeats, TicketPrice, TicketDiscount)
VALUES (1, '2020-12-02 10:30', '2020-12-02 11:30', 'LHR', 'EDI', 400, 150, 10)

-- TRIP FROM NEWCASTLE TO HEATHROW
INSERT INTO FlightTrip (Aircraft_id, DepartureTime, ArrivalTime, DepartureAirport, ArrivalAirport, AvailableSeats, TicketPrice, TicketDiscount)
VALUES (2, '2020-12-02 10:30', '2020-12-02 11:30', 'NCL', 'LHR', 400, 100, 20)
      
        """)
        self.db_connection.commit()

if __name__ == "__main__":
    populate = DBPopulator()
    populate.populate()