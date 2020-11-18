-- This will drop all tables, create them and populate them in one query
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
INSERT INTO Passengers (PassportNumber, FirstName, LastName, Gender, DateOfBirth) VALUES ('481438024', 'Cyrillus', 'Sircomb', 'Male', '7/24/2002');
INSERT INTO Passengers (PassportNumber, FirstName, LastName, Gender, DateOfBirth) VALUES ('950270641', 'Ronni', 'Loren', 'Female', '12/17/1966');
INSERT INTO Passengers (PassportNumber, FirstName, LastName, Gender, DateOfBirth) VALUES ('630727879', 'Sheelagh', 'Yurin', 'Female', '1/14/1977');
INSERT INTO Passengers (PassportNumber, FirstName, LastName, Gender, DateOfBirth) VALUES ('277037086', 'Sonni', 'Hewins', 'Female', '10/22/1988');
INSERT INTO Passengers (PassportNumber, FirstName, LastName, Gender, DateOfBirth) VALUES ('205816031', 'Libbey', 'Bryer', 'Female', '8/31/1996');
INSERT INTO Passengers (PassportNumber, FirstName, LastName, Gender, DateOfBirth) VALUES ('578349876', 'Aggie', 'Trimmill', 'Female', '12/1/2000');
INSERT INTO Passengers (PassportNumber, FirstName, LastName, Gender, DateOfBirth) VALUES ('762872622', 'Gretta', 'Shea', 'Female', '10/22/2012');
INSERT INTO Passengers (PassportNumber, FirstName, LastName, Gender, DateOfBirth) VALUES ('855118996', 'Patrick', 'Heinert', 'Male', '7/20/2018');
INSERT INTO Passengers (PassportNumber, FirstName, LastName, Gender, DateOfBirth) VALUES ('313845943', 'Steve', 'Harken', 'Male', '6/26/1978');
INSERT INTO Passengers (PassportNumber, FirstName, LastName, Gender, DateOfBirth) VALUES ('852811757', 'Anny', 'Cosyns', 'Female', '6/20/1988');
INSERT INTO Passengers (PassportNumber, FirstName, LastName, Gender, DateOfBirth) VALUES ('508192981', 'Spike', 'Conerding', 'Male', '7/24/1954');
INSERT INTO Passengers (PassportNumber, FirstName, LastName, Gender, DateOfBirth) VALUES ('362593999', 'Aeriell', 'Works', 'Female', '8/4/2010');
INSERT INTO Passengers (PassportNumber, FirstName, LastName, Gender, DateOfBirth) VALUES ('508543007', 'Rodolphe', 'Bennie', 'Male', '7/6/1964');
INSERT INTO Passengers (PassportNumber, FirstName, LastName, Gender, DateOfBirth) VALUES ('435147578', 'Chandra', 'Kielty', 'Female', '1/15/1955');
INSERT INTO Passengers (PassportNumber, FirstName, LastName, Gender, DateOfBirth) VALUES ('807218211', 'Cristine', 'Wagge', 'Female', '3/25/1962');
INSERT INTO Passengers (PassportNumber, FirstName, LastName, Gender, DateOfBirth) VALUES ('481629215', 'Francisca', 'Bysouth', 'Female', '12/23/1956');
INSERT INTO Passengers (PassportNumber, FirstName, LastName, Gender, DateOfBirth) VALUES ('080577803', 'Xylia', 'Balmforth', 'Female', '5/13/1969');
INSERT INTO Passengers (PassportNumber, FirstName, LastName, Gender, DateOfBirth) VALUES ('641517933', 'Alec', 'Baccus', 'Male', '9/6/1987');
INSERT INTO Passengers (PassportNumber, FirstName, LastName, Gender, DateOfBirth) VALUES ('302908956', 'Florencia', 'Febre', 'Female', '9/5/1982');
INSERT INTO Passengers (PassportNumber, FirstName, LastName, Gender, DateOfBirth) VALUES ('251187623', 'Pablo', 'Devoy', 'Male', '5/23/1981');
INSERT INTO Passengers (PassportNumber, FirstName, LastName, Gender, DateOfBirth) VALUES ('037024017', 'Karia', 'Richardot', 'Female', '2/21/2018');
INSERT INTO Passengers (PassportNumber, FirstName, LastName, Gender, DateOfBirth) VALUES ('681175658', 'Hyacintha', 'Aimeric', 'Female', '8/15/2000');
INSERT INTO Passengers (PassportNumber, FirstName, LastName, Gender, DateOfBirth) VALUES ('430101607', 'Say', 'Budnk', 'Male', '7/28/2011');
INSERT INTO Passengers (PassportNumber, FirstName, LastName, Gender, DateOfBirth) VALUES ('806791809', 'Nelli', 'Melin', 'Female', '7/17/1957');
INSERT INTO Passengers (PassportNumber, FirstName, LastName, Gender, DateOfBirth) VALUES ('084328372', 'Sigismondo', 'Lissaman', 'Male', '9/19/1978');
INSERT INTO Passengers (PassportNumber, FirstName, LastName, Gender, DateOfBirth) VALUES ('259913632', 'Jozef', 'Battman', 'Male', '5/14/1983');
INSERT INTO Passengers (PassportNumber, FirstName, LastName, Gender, DateOfBirth) VALUES ('076485717', 'Felizio', 'Goldbourn', 'Male', '9/11/1951');
INSERT INTO Passengers (PassportNumber, FirstName, LastName, Gender, DateOfBirth) VALUES ('883804814', 'Moishe', 'Castiglione', 'Male', '10/15/1995');
INSERT INTO Passengers (PassportNumber, FirstName, LastName, Gender, DateOfBirth) VALUES ('171825981', 'Christye', 'Stebbin', 'Female', '9/15/2005');
INSERT INTO Passengers (PassportNumber, FirstName, LastName, Gender, DateOfBirth) VALUES ('679982913', 'Barret', 'Carrivick', 'Male', '12/11/1976');
INSERT INTO Passengers (PassportNumber, FirstName, LastName, Gender, DateOfBirth) VALUES ('492627766', 'Ignazio', 'Clohissy', 'Male', '5/4/2006');
INSERT INTO Passengers (PassportNumber, FirstName, LastName, Gender, DateOfBirth) VALUES ('186287601', 'Annelise', 'Wardingly', 'Female', '1/25/1965');
INSERT INTO Passengers (PassportNumber, FirstName, LastName, Gender, DateOfBirth) VALUES ('813849419', 'Emlen', 'Tinmouth', 'Male', '8/23/1980');
INSERT INTO Passengers (PassportNumber, FirstName, LastName, Gender, DateOfBirth) VALUES ('641431407', 'Ethelind', 'Willets', 'Female', '5/19/2002');
INSERT INTO Passengers (PassportNumber, FirstName, LastName, Gender, DateOfBirth) VALUES ('693617323', 'Ronald', 'Claw', 'Male', '3/28/1985');
INSERT INTO Passengers (PassportNumber, FirstName, LastName, Gender, DateOfBirth) VALUES ('753334261', 'Devon', 'Yielding', 'Female', '10/15/1966');
INSERT INTO Passengers (PassportNumber, FirstName, LastName, Gender, DateOfBirth) VALUES ('532513431', 'Stillman', 'Putley', 'Male', '3/1/1959');
INSERT INTO Passengers (PassportNumber, FirstName, LastName, Gender, DateOfBirth) VALUES ('733529265', 'Massimo', 'Calyton', 'Male', '8/12/1962');
INSERT INTO Passengers (PassportNumber, FirstName, LastName, Gender, DateOfBirth) VALUES ('578639623', 'Rora', 'Stratley', 'Female', '1/26/1987');
INSERT INTO Passengers (PassportNumber, FirstName, LastName, Gender, DateOfBirth) VALUES ('331695842', 'Arvy', 'Murrison', 'Male', '9/25/1960');
INSERT INTO Passengers (PassportNumber, FirstName, LastName, Gender, DateOfBirth) VALUES ('571633762', 'Christen', 'Castaneda', 'Female', '12/25/1984');
INSERT INTO Passengers (PassportNumber, FirstName, LastName, Gender, DateOfBirth) VALUES ('153311066', 'Ellery', 'Christoffels', 'Male', '6/25/2001');
INSERT INTO Passengers (PassportNumber, FirstName, LastName, Gender, DateOfBirth) VALUES ('904969359', 'Konrad', 'Fipp', 'Male', '10/30/1955');
INSERT INTO Passengers (PassportNumber, FirstName, LastName, Gender, DateOfBirth) VALUES ('825080561', 'Galven', 'Hands', 'Male', '11/30/1976');
INSERT INTO Passengers (PassportNumber, FirstName, LastName, Gender, DateOfBirth) VALUES ('404904419', 'Waldo', 'Tribbeck', 'Male', '5/23/1974');
INSERT INTO Passengers (PassportNumber, FirstName, LastName, Gender, DateOfBirth) VALUES ('104481282', 'Klaus', 'Etchell', 'Male', '11/10/2013');
INSERT INTO Passengers (PassportNumber, FirstName, LastName, Gender, DateOfBirth) VALUES ('710202843', 'Hilary', 'Gaber', 'Female', '3/21/1974');
INSERT INTO Passengers (PassportNumber, FirstName, LastName, Gender, DateOfBirth) VALUES ('087826104', 'Halsy', 'Dagworthy', 'Male', '7/8/2001');
INSERT INTO Passengers (PassportNumber, FirstName, LastName, Gender, DateOfBirth) VALUES ('899208255', 'Humphrey', 'Croad', 'Male', '9/7/2008');
INSERT INTO Passengers (PassportNumber, FirstName, LastName, Gender, DateOfBirth) VALUES ('827031806', 'Darnell', 'Dowdney', 'Male', '10/16/1999');
INSERT INTO Passengers (PassportNumber, FirstName, LastName, Gender, DateOfBirth) VALUES ('326246236', 'Winnie', 'Puvia', 'Male', '7/26/2010');
INSERT INTO Passengers (PassportNumber, FirstName, LastName, Gender, DateOfBirth) VALUES ('269019127', 'Ericha', 'Gilhouley', 'Female', '11/16/1957');
INSERT INTO Passengers (PassportNumber, FirstName, LastName, Gender, DateOfBirth) VALUES ('583172921', 'Livvy', 'Youngman', 'Female', '2/15/1982');
INSERT INTO Passengers (PassportNumber, FirstName, LastName, Gender, DateOfBirth) VALUES ('073073202', 'Daffie', 'Fortescue', 'Female', '4/13/1967');
INSERT INTO Passengers (PassportNumber, FirstName, LastName, Gender, DateOfBirth) VALUES ('945008027', 'Feliks', 'Hundley', 'Male', '8/9/1990');
INSERT INTO Passengers (PassportNumber, FirstName, LastName, Gender, DateOfBirth) VALUES ('990346651', 'Benedetto', 'Brannan', 'Male', '6/15/1983');
INSERT INTO Passengers (PassportNumber, FirstName, LastName, Gender, DateOfBirth) VALUES ('262171545', 'Emmy', 'Pellington', 'Male', '7/4/1974');
INSERT INTO Passengers (PassportNumber, FirstName, LastName, Gender, DateOfBirth) VALUES ('001027564', 'Linet', 'Martinek', 'Female', '1/16/1954');
INSERT INTO Passengers (PassportNumber, FirstName, LastName, Gender, DateOfBirth) VALUES ('992556097', 'Linzy', 'Mitchall', 'Female', '10/10/2014');
INSERT INTO Passengers (PassportNumber, FirstName, LastName, Gender, DateOfBirth) VALUES ('872061603', 'My', 'Cicccitti', 'Male', '5/29/1953');
INSERT INTO Passengers (PassportNumber, FirstName, LastName, Gender, DateOfBirth) VALUES ('101249772', 'Finn', 'Porson', 'Male', '9/23/1995');
INSERT INTO Passengers (PassportNumber, FirstName, LastName, Gender, DateOfBirth) VALUES ('648943216', 'Quinton', 'Cockarill', 'Male', '3/25/1955');
INSERT INTO Passengers (PassportNumber, FirstName, LastName, Gender, DateOfBirth) VALUES ('714343898', 'Grantham', 'Munsey', 'Male', '1/15/1953');
INSERT INTO Passengers (PassportNumber, FirstName, LastName, Gender, DateOfBirth) VALUES ('309403533', 'Oralie', 'Divis', 'Female', '6/4/1967');
INSERT INTO Passengers (PassportNumber, FirstName, LastName, Gender, DateOfBirth) VALUES ('201973501', 'Rebeka', 'Adney', 'Female', '5/20/1996');
INSERT INTO Passengers (PassportNumber, FirstName, LastName, Gender, DateOfBirth) VALUES ('753185944', 'Ola', 'Poulston', 'Female', '12/4/1965');
INSERT INTO Passengers (PassportNumber, FirstName, LastName, Gender, DateOfBirth) VALUES ('551170049', 'Susanna', 'Shivell', 'Female', '10/2/1995');
INSERT INTO Passengers (PassportNumber, FirstName, LastName, Gender, DateOfBirth) VALUES ('631796397', 'Marten', 'Gwyllt', 'Male', '12/12/1994');
INSERT INTO Passengers (PassportNumber, FirstName, LastName, Gender, DateOfBirth) VALUES ('987954352', 'Micah', 'Brychan', 'Male', '1/9/1991');
INSERT INTO Passengers (PassportNumber, FirstName, LastName, Gender, DateOfBirth) VALUES ('243933347', 'Billy', 'McGinty', 'Female', '1/24/1956');
INSERT INTO Passengers (PassportNumber, FirstName, LastName, Gender, DateOfBirth) VALUES ('296607404', 'Camel', 'Stoll', 'Female', '1/9/1982');
INSERT INTO Passengers (PassportNumber, FirstName, LastName, Gender, DateOfBirth) VALUES ('595761307', 'Letitia', 'Draycott', 'Female', '6/26/1977');
INSERT INTO Passengers (PassportNumber, FirstName, LastName, Gender, DateOfBirth) VALUES ('918610558', 'Gonzalo', 'Records', 'Male', '1/18/1993');
INSERT INTO Passengers (PassportNumber, FirstName, LastName, Gender, DateOfBirth) VALUES ('886865932', 'Vonny', 'Spencer', 'Female', '10/28/2002');
INSERT INTO Passengers (PassportNumber, FirstName, LastName, Gender, DateOfBirth) VALUES ('509461003', 'Elden', 'Remon', 'Male', '8/28/2016');
INSERT INTO Passengers (PassportNumber, FirstName, LastName, Gender, DateOfBirth) VALUES ('642034944', 'Mollee', 'Weekly', 'Female', '8/26/1996');
INSERT INTO Passengers (PassportNumber, FirstName, LastName, Gender, DateOfBirth) VALUES ('267364861', 'Ritchie', 'McVane', 'Male', '7/23/2003');
INSERT INTO Passengers (PassportNumber, FirstName, LastName, Gender, DateOfBirth) VALUES ('976952746', 'Rudie', 'Egglestone', 'Male', '3/21/1980');
INSERT INTO Passengers (PassportNumber, FirstName, LastName, Gender, DateOfBirth) VALUES ('274968727', 'Forster', 'Jessel', 'Male', '8/29/1975');
INSERT INTO Passengers (PassportNumber, FirstName, LastName, Gender, DateOfBirth) VALUES ('004342781', 'Prue', 'Bryson', 'Female', '5/27/1980');
INSERT INTO Passengers (PassportNumber, FirstName, LastName, Gender, DateOfBirth) VALUES ('869882975', 'Tracy', 'Kwiek', 'Female', '4/6/1996');
INSERT INTO Passengers (PassportNumber, FirstName, LastName, Gender, DateOfBirth) VALUES ('175136361', 'Tonia', 'Pickup', 'Female', '6/20/2000');
INSERT INTO Passengers (PassportNumber, FirstName, LastName, Gender, DateOfBirth) VALUES ('281206553', 'Olivie', 'Scallan', 'Female', '1/27/1977');
INSERT INTO Passengers (PassportNumber, FirstName, LastName, Gender, DateOfBirth) VALUES ('918267798', 'Suzanna', 'Pepperrall', 'Female', '10/15/2012');
INSERT INTO Passengers (PassportNumber, FirstName, LastName, Gender, DateOfBirth) VALUES ('655106701', 'Sherlock', 'McCartan', 'Male', '3/18/1991');
INSERT INTO Passengers (PassportNumber, FirstName, LastName, Gender, DateOfBirth) VALUES ('127789531', 'Gino', 'Nolton', 'Male', '5/13/2000');
INSERT INTO Passengers (PassportNumber, FirstName, LastName, Gender, DateOfBirth) VALUES ('426727934', 'Wendell', 'Bohlens', 'Male', '3/15/1966');
INSERT INTO Passengers (PassportNumber, FirstName, LastName, Gender, DateOfBirth) VALUES ('949648399', 'Kris', 'Done', 'Female', '11/15/1971');
INSERT INTO Passengers (PassportNumber, FirstName, LastName, Gender, DateOfBirth) VALUES ('070415932', 'Kingston', 'Denkel', 'Male', '11/8/1987');
INSERT INTO Passengers (PassportNumber, FirstName, LastName, Gender, DateOfBirth) VALUES ('934898022', 'Damaris', 'Woodroffe', 'Female', '1/23/2008');
INSERT INTO Passengers (PassportNumber, FirstName, LastName, Gender, DateOfBirth) VALUES ('204629607', 'Willy', 'Coomber', 'Female', '10/2/1962');
INSERT INTO Passengers (PassportNumber, FirstName, LastName, Gender, DateOfBirth) VALUES ('429574852', 'Alexandr', 'Dimberline', 'Male', '1/5/2014');
INSERT INTO Passengers (PassportNumber, FirstName, LastName, Gender, DateOfBirth) VALUES ('865119876', 'Gawain', 'Klarzynski', 'Male', '7/24/2001');
INSERT INTO Passengers (PassportNumber, FirstName, LastName, Gender, DateOfBirth) VALUES ('768842279', 'Jethro', 'Blasiak', 'Male', '8/4/2008');
INSERT INTO Passengers (PassportNumber, FirstName, LastName, Gender, DateOfBirth) VALUES ('250357452', 'Bettina', 'Lay', 'Female', '1/28/1976');
INSERT INTO Passengers (PassportNumber, FirstName, LastName, Gender, DateOfBirth) VALUES ('429387159', 'Westbrook', 'Meert', 'Male', '8/24/1998');
INSERT INTO Passengers (PassportNumber, FirstName, LastName, Gender, DateOfBirth) VALUES ('373714212', 'Tyson', 'Cosin', 'Male', '1/23/1959');
INSERT INTO Passengers (PassportNumber, FirstName, LastName, Gender, DateOfBirth) VALUES ('566037899', 'Winthrop', 'Luxmoore', 'Male', '3/6/1988');
INSERT INTO Passengers (PassportNumber, FirstName, LastName, Gender, DateOfBirth) VALUES ('898214291', 'Amandy', 'Hurworth', 'Female', '4/2/2017');
INSERT INTO Passengers (PassportNumber, FirstName, LastName, Gender, DateOfBirth) VALUES ('134051491', 'Stanislas', 'Zanioletti', 'Male', '5/1/2020');

--- A family of four: Two Parents, a 10-year-old and an infant of 5 months
INSERT INTO Passengers (PassportNumber, FirstName, LastName, Gender, DateOfBirth) VALUES ('675045831', 'Eleanor', 'Almeida', 'Female', '12/31/1981');
INSERT INTO Passengers (PassportNumber, FirstName, LastName, Gender, DateOfBirth) VALUES ('960841891', 'Jermaine', 'Almeida', 'Male', '2/11/1982');
INSERT INTO Passengers (PassportNumber, FirstName, LastName, Gender, DateOfBirth) VALUES ('648638683', 'Barnie', 'Almeida', 'Male', '4/10/2010');
INSERT INTO Passengers (PassportNumber, FirstName, LastName, Gender, DateOfBirth) VALUES ('798597089', 'Hope', 'Almeida', 'Female', '12/5/2020');


-- Jobs
INSERT INTO Jobs (Job) VALUES ('Airport Staff')
INSERT INTO Jobs (Job) VALUES ('Flight Crew')

-- Staff
INSERT INTO Staff (PassportNumber, Job_id, FirstName, LastName, Username, UserPassword, Gender, OnLocation) VALUES ('638608473', 2, 'Vilma', 'Feehily', 'vfeehily0', 'AjfGwQW', 'Female', 0);
INSERT INTO Staff (PassportNumber, Job_id, FirstName, LastName, Username, UserPassword, Gender, OnLocation) VALUES ('569112024', 2, 'Stacie', 'Dudny', 'sdudny1', 'bahQ2wiaU31a', 'Female', 0);
INSERT INTO Staff (PassportNumber, Job_id, FirstName, LastName, Username, UserPassword, Gender, OnLocation) VALUES ('010992093', 2, 'Sibbie', 'Lauritzen', 'slauritzen2', 'fJjYEdD', 'Female', 0);
INSERT INTO Staff (PassportNumber, Job_id, FirstName, LastName, Username, UserPassword, Gender, OnLocation) VALUES ('466647063', 2, 'Arnie', 'Idenden', 'aidenden3', 'nyTKb9', 'Male', 0);
INSERT INTO Staff (PassportNumber, Job_id, FirstName, LastName, Username, UserPassword, Gender, OnLocation) VALUES ('509258376', 2, 'Lucina', 'Ainslee', 'lainslee4', 'PgMXq4P1fbI', 'Female', 0);
INSERT INTO Staff (PassportNumber, Job_id, FirstName, LastName, Username, UserPassword, Gender, OnLocation) VALUES ('394889613', 2, 'Neal', 'Mower', 'nmower5', 'hFsVCDIcUpo', 'Male', 0);
INSERT INTO Staff (PassportNumber, Job_id, FirstName, LastName, Username, UserPassword, Gender, OnLocation) VALUES ('181796291', 2, 'Lazaro', 'Teaser', 'lteaser6', '7NKitRk', 'Male', 0);
INSERT INTO Staff (PassportNumber, Job_id, FirstName, LastName, Username, UserPassword, Gender, OnLocation) VALUES ('417510888', 2, 'Grete', 'Dunstone', 'gdunstone7', 'hrrne2vZsu', 'Female', 1);
INSERT INTO Staff (PassportNumber, Job_id, FirstName, LastName, Username, UserPassword, Gender, OnLocation) VALUES ('914337521', 2, 'Erek', 'Darlington', 'edarlington8', 'lB7zlT0UXLD', 'Male', 0);
INSERT INTO Staff (PassportNumber, Job_id, FirstName, LastName, Username, UserPassword, Gender, OnLocation) VALUES ('532063088', 2, 'Selinda', 'Fulep', 'sfulep9', 'NgsBRmBPR', 'Female', 1);
INSERT INTO Staff (PassportNumber, Job_id, FirstName, LastName, Username, UserPassword, Gender, OnLocation) VALUES ('154833766', 2, 'Alvina', 'Pybworth', 'apybwortha', '4fALiTapQL', 'Female', 0);
INSERT INTO Staff (PassportNumber, Job_id, FirstName, LastName, Username, UserPassword, Gender, OnLocation) VALUES ('082206348', 2, 'Rey', 'Haggerston', 'rhaggerstonb', 'nxi1zB8', 'Male', 0);
INSERT INTO Staff (PassportNumber, Job_id, FirstName, LastName, Username, UserPassword, Gender, OnLocation) VALUES ('220255868', 2, 'Margarete', 'Docwra', 'mdocwrac', 'NXjcjS', 'Female', 1);
INSERT INTO Staff (PassportNumber, Job_id, FirstName, LastName, Username, UserPassword, Gender, OnLocation) VALUES ('393426358', 2, 'Nevsa', 'Bahls', 'nbahlsd', 'Ox6F2OD8H', 'Female', 0);
INSERT INTO Staff (PassportNumber, Job_id, FirstName, LastName, Username, UserPassword, Gender, OnLocation) VALUES ('270536407', 2, 'Hilario', 'Pollett', 'hpollette', 'D5kAblkFu', 'Male', 1);
INSERT INTO Staff (PassportNumber, Job_id, FirstName, LastName, Username, UserPassword, Gender, OnLocation) VALUES ('055637518', 2, 'Linn', 'Jinkin', 'ljinkinf', 'JUNE7f', 'Male', 0);
INSERT INTO Staff (PassportNumber, Job_id, FirstName, LastName, Username, UserPassword, Gender, OnLocation) VALUES ('775458001', 2, 'Randolph', 'Ayscough', 'rayscoughg', 'd2sPNi7r', 'Male', 0);
INSERT INTO Staff (PassportNumber, Job_id, FirstName, LastName, Username, UserPassword, Gender, OnLocation) VALUES ('887344562', 2, 'Merlina', 'Gligorijevic', 'mgligorijevich', 'au59B7', 'Female', 0);
INSERT INTO Staff (PassportNumber, Job_id, FirstName, LastName, Username, UserPassword, Gender, OnLocation) VALUES ('784346051', 2, 'Nadia', 'Horrod', 'nhorrodi', 'r3k77bgVnZbN', 'Female', 0);
INSERT INTO Staff (PassportNumber, Job_id, FirstName, LastName, Username, UserPassword, Gender, OnLocation) VALUES ('991593871', 2, 'Jerome', 'Saunper', 'jsaunperj', 'kkigNmKZA56', 'Male', 0);
INSERT INTO Staff (PassportNumber, Job_id, FirstName, LastName, Username, UserPassword, Gender, OnLocation) VALUES ('246794726', 2, 'Jonell', 'McNerlin', 'jmcnerlink', 'C1SvkTppdv1', 'Female', 1);
INSERT INTO Staff (PassportNumber, Job_id, FirstName, LastName, Username, UserPassword, Gender, OnLocation) VALUES ('451906321', 2, 'Gregor', 'Osbidston', 'gosbidstonl', 'tMYv5mzG', 'Male', 0);
INSERT INTO Staff (PassportNumber, Job_id, FirstName, LastName, Username, UserPassword, Gender, OnLocation) VALUES ('697946541', 2, 'Gabriel', 'Hryncewicz', 'ghryncewiczm', 'aaejTbRzTc', 'Male', 1);
INSERT INTO Staff (PassportNumber, Job_id, FirstName, LastName, Username, UserPassword, Gender, OnLocation) VALUES ('394032995', 2, 'Allsun', 'MacKibbon', 'amackibbonn', 'hGx0MKpE', 'Female', 0);
INSERT INTO Staff (PassportNumber, Job_id, FirstName, LastName, Username, UserPassword, Gender, OnLocation) VALUES ('725454886', 2, 'Berkeley', 'Tippler', 'btipplero', 'QNF88D91PP', 'Male', 1);
INSERT INTO Staff (PassportNumber, Job_id, FirstName, LastName, Username, UserPassword, Gender, OnLocation) VALUES ('447824586', 2, 'Brigitta', 'Rowaszkiewicz', 'browaszkiewiczp', 'fNt26nrYzCun', 'Female', 0);
INSERT INTO Staff (PassportNumber, Job_id, FirstName, LastName, Username, UserPassword, Gender, OnLocation) VALUES ('432283666', 2, 'Perice', 'Levesque', 'plevesqueq', 'PAAIE13F', 'Male', 0);
INSERT INTO Staff (PassportNumber, Job_id, FirstName, LastName, Username, UserPassword, Gender, OnLocation) VALUES ('457243322', 2, 'Hartwell', 'Duding', 'hdudingr', 'sJRHyV', 'Male', 1);
INSERT INTO Staff (PassportNumber, Job_id, FirstName, LastName, Username, UserPassword, Gender, OnLocation) VALUES ('478769799', 2, 'Glynn', 'Krysiak', 'gkrysiaks', 'gbIMPY5', 'Male', 0);
INSERT INTO Staff (PassportNumber, Job_id, FirstName, LastName, Username, UserPassword, Gender, OnLocation) VALUES ('565189779', 2, 'Waylin', 'Heino', 'wheinot', 'irofnuriHw', 'Male', 1);
INSERT INTO Staff (PassportNumber, Job_id, FirstName, LastName, Username, UserPassword, Gender, OnLocation) VALUES ('041461347', 2, 'Jarrid', 'Coal', 'jcoalu', 'KiMJUtFO', 'Male', 1);
INSERT INTO Staff (PassportNumber, Job_id, FirstName, LastName, Username, UserPassword, Gender, OnLocation) VALUES ('406164032', 2, 'Gerri', 'Raisbeck', 'graisbeckv', 'XAyS3K', 'Male', 1);
INSERT INTO Staff (PassportNumber, Job_id, FirstName, LastName, Username, UserPassword, Gender, OnLocation) VALUES ('402302414', 2, 'Ileane', 'Szachniewicz', 'iszachniewiczw', 'ZZGkvKTvQHI7', 'Female', 1);
INSERT INTO Staff (PassportNumber, Job_id, FirstName, LastName, Username, UserPassword, Gender, OnLocation) VALUES ('663834896', 2, 'Mufinella', 'Rama', 'mramax', 'sltQCcOE', 'Female', 0);
INSERT INTO Staff (PassportNumber, Job_id, FirstName, LastName, Username, UserPassword, Gender, OnLocation) VALUES ('070945301', 2, 'Charmine', 'Antat', 'cantaty', 'zuSriOljI', 'Female', 0);
INSERT INTO Staff (PassportNumber, Job_id, FirstName, LastName, Username, UserPassword, Gender, OnLocation) VALUES ('606873545', 2, 'Cammi', 'Villaret', 'cvillaretz', 'oKDZG0', 'Female', 0);
INSERT INTO Staff (PassportNumber, Job_id, FirstName, LastName, Username, UserPassword, Gender, OnLocation) VALUES ('772375659', 2, 'Juliann', 'Platts', 'jplatts10', 'DfRQAOj', 'Female', 0);
INSERT INTO Staff (PassportNumber, Job_id, FirstName, LastName, Username, UserPassword, Gender, OnLocation) VALUES ('189912975', 2, 'Averyl', 'Dalloway', 'adalloway11', 'DgdCA1VLZ', 'Female', 0);
INSERT INTO Staff (PassportNumber, Job_id, FirstName, LastName, Username, UserPassword, Gender, OnLocation) VALUES ('990672017', 2, 'Gaby', 'Yegorchenkov', 'gyegorchenkov12', 'UZbga6n1XZ4', 'Male', 1);
INSERT INTO Staff (PassportNumber, Job_id, FirstName, LastName, Username, UserPassword, Gender, OnLocation) VALUES ('965550122', 2, 'Louise', 'Warren', 'lwarren13', 'lH8mirNSpK', 'Female', 1);
INSERT INTO Staff (PassportNumber, Job_id, FirstName, LastName, Username, UserPassword, Gender, OnLocation) VALUES ('915065011', 2, 'Lorena', 'Yallop', 'lyallop14', '9GSrP1MmxvK', 'Female', 1);
INSERT INTO Staff (PassportNumber, Job_id, FirstName, LastName, Username, UserPassword, Gender, OnLocation) VALUES ('740367122', 2, 'Gabrila', 'Gelardi', 'ggelardi15', 'SoI25iv', 'Female', 1);
INSERT INTO Staff (PassportNumber, Job_id, FirstName, LastName, Username, UserPassword, Gender, OnLocation) VALUES ('929895018', 2, 'Cale', 'Swyne', 'cswyne16', 'SsWCci9dB', 'Male', 0);
INSERT INTO Staff (PassportNumber, Job_id, FirstName, LastName, Username, UserPassword, Gender, OnLocation) VALUES ('205512341', 2, 'Taite', 'Maryska', 'tmaryska17', 'CqxhOo4vW', 'Male', 0);
INSERT INTO Staff (PassportNumber, Job_id, FirstName, LastName, Username, UserPassword, Gender, OnLocation) VALUES ('763608017', 2, 'Theo', 'Purkis', 'tpurkis18', 'VaTvCyf5', 'Female', 0);
INSERT INTO Staff (PassportNumber, Job_id, FirstName, LastName, Username, UserPassword, Gender, OnLocation) VALUES ('181266406', 2, 'Urbain', 'Scholtz', 'uscholtz19', 'Sdl3nttVA7J', 'Male', 0);
INSERT INTO Staff (PassportNumber, Job_id, FirstName, LastName, Username, UserPassword, Gender, OnLocation) VALUES ('682150166', 2, 'Candie', 'Vonderdell', 'cvonderdell1a', '6CWEOD6rPM', 'Female', 1);
INSERT INTO Staff (PassportNumber, Job_id, FirstName, LastName, Username, UserPassword, Gender, OnLocation) VALUES ('737375773', 2, 'Miltie', 'Fullerton', 'mfullerton1b', 'cBf9qB', 'Male', 1);
INSERT INTO Staff (PassportNumber, Job_id, FirstName, LastName, Username, UserPassword, Gender, OnLocation) VALUES ('258339499', 2, 'Caroljean', 'Leynton', 'cleynton1c', 'ZM41s0UC1', 'Female', 0);
INSERT INTO Staff (PassportNumber, Job_id, FirstName, LastName, Username, UserPassword, Gender, OnLocation) VALUES ('399671542', 2, 'Dollie', 'Petty', 'dpetty1d', 'MvxnB0Ho', 'Female', 0);
INSERT INTO Staff (PassportNumber, Job_id, FirstName, LastName, Username, UserPassword, Gender, OnLocation) VALUES ('364662091', 1, 'Elijah', 'Milne', 'emilne1e', 'Z98jUpt', 'Male', 0);
INSERT INTO Staff (PassportNumber, Job_id, FirstName, LastName, Username, UserPassword, Gender, OnLocation) VALUES ('094258719', 1, 'Alena', 'Maris', 'amaris1f', 'uXJaPEn2V', 'Female', 1);
INSERT INTO Staff (PassportNumber, Job_id, FirstName, LastName, Username, UserPassword, Gender, OnLocation) VALUES ('285889625', 1, 'Meredith', 'Preator', 'mpreator1g', 'nwO7rKmI13w', 'Male', 1);
INSERT INTO Staff (PassportNumber, Job_id, FirstName, LastName, Username, UserPassword, Gender, OnLocation) VALUES ('325136331', 1, 'Dermot', 'Adkins', 'dadkins1h', 'KUMb85P', 'Male', 0);
INSERT INTO Staff (PassportNumber, Job_id, FirstName, LastName, Username, UserPassword, Gender, OnLocation) VALUES ('729740093', 1, 'Russell', 'Guihen', 'rguihen1i', 'NZcssFEz', 'Male', 0);
INSERT INTO Staff (PassportNumber, Job_id, FirstName, LastName, Username, UserPassword, Gender, OnLocation) VALUES ('789924625', 1, 'Craggy', 'Palfrey', 'cpalfrey1j', '06sXlaO6', 'Male', 1);
INSERT INTO Staff (PassportNumber, Job_id, FirstName, LastName, Username, UserPassword, Gender, OnLocation) VALUES ('380827988', 1, 'Darryl', 'McTeer', 'dmcteer1k', 'gKfY2d', 'Male', 0);
INSERT INTO Staff (PassportNumber, Job_id, FirstName, LastName, Username, UserPassword, Gender, OnLocation) VALUES ('530471769', 1, 'Jamesy', 'Wakes', 'jwakes1l', 'KDK0xV4zX', 'Male', 0);
INSERT INTO Staff (PassportNumber, Job_id, FirstName, LastName, Username, UserPassword, Gender, OnLocation) VALUES ('321332615', 1, 'Hilda', 'Sarjeant', 'hsarjeant1m', 'qyt78p', 'Female', 0);
INSERT INTO Staff (PassportNumber, Job_id, FirstName, LastName, Username, UserPassword, Gender, OnLocation) VALUES ('003916065', 1, 'Gareth', 'Sworne', 'gsworne1n', 'tjWTon9zqM', 'Male', 0);
INSERT INTO Staff (PassportNumber, Job_id, FirstName, LastName, Username, UserPassword, Gender, OnLocation) VALUES ('218178222', 1, 'Terrill', 'Gallaway', 'tgallaway1o', '7IdEXkQm0', 'Male', 1);
INSERT INTO Staff (PassportNumber, Job_id, FirstName, LastName, Username, UserPassword, Gender, OnLocation) VALUES ('370666793', 1, 'Mariel', 'Quibell', 'mquibell1p', 'EarqIh', 'Female', 1);
INSERT INTO Staff (PassportNumber, Job_id, FirstName, LastName, Username, UserPassword, Gender, OnLocation) VALUES ('360590108', 1, 'Aigneis', 'Brinklow', 'abrinklow1q', 'UlaPwWp', 'Female', 1);
INSERT INTO Staff (PassportNumber, Job_id, FirstName, LastName, Username, UserPassword, Gender, OnLocation) VALUES ('510969549', 1, 'Stormie', 'Peterken', 'speterken1r', 'H1B9jX', 'Female', 0);
INSERT INTO Staff (PassportNumber, Job_id, FirstName, LastName, Username, UserPassword, Gender, OnLocation) VALUES ('975184177', 1, 'Candy', 'Carlsson', 'ccarlsson1s', 'n3rPqOyoJuP', 'Female', 0);
INSERT INTO Staff (PassportNumber, Job_id, FirstName, LastName, Username, UserPassword, Gender, OnLocation) VALUES ('564035457', 1, 'Leelah', 'Bigg', 'lbigg1t', 'ZuOy7jk7HNa', 'Female', 1);
INSERT INTO Staff (PassportNumber, Job_id, FirstName, LastName, Username, UserPassword, Gender, OnLocation) VALUES ('120623308', 1, 'Doria', 'Minchenton', 'dminchenton1u', 'h8LlHMngW3F', 'Female', 0);
INSERT INTO Staff (PassportNumber, Job_id, FirstName, LastName, Username, UserPassword, Gender, OnLocation) VALUES ('007100475', 1, 'Gary', 'Thaxton', 'gthaxton1v', 'o8fiD6Wwhy', 'Male', 1);
INSERT INTO Staff (PassportNumber, Job_id, FirstName, LastName, Username, UserPassword, Gender, OnLocation) VALUES ('829251041', 1, 'Les', 'Stirling', 'lstirling1w', 'pF6pnjVRHL', 'Male', 1);
INSERT INTO Staff (PassportNumber, Job_id, FirstName, LastName, Username, UserPassword, Gender, OnLocation) VALUES ('625849736', 1, 'Vida', 'Dyson', 'vdyson1x', 'FQTR2wB8SOx', 'Female', 0);
INSERT INTO Staff (PassportNumber, Job_id, FirstName, LastName, Username, UserPassword, Gender, OnLocation) VALUES ('099304802', 1, 'Webb', 'Staining', 'wstaining1y', 'vrGd4Elmv8', 'Male', 0);
INSERT INTO Staff (PassportNumber, Job_id, FirstName, LastName, Username, UserPassword, Gender, OnLocation) VALUES ('584552309', 1, 'Stacee', 'MacGown', 'smacgown1z', 'JCuibHJjkfgI', 'Male', 0);
INSERT INTO Staff (PassportNumber, Job_id, FirstName, LastName, Username, UserPassword, Gender, OnLocation) VALUES ('125951546', 1, 'Florian', 'Stitle', 'fstitle20', 'QqMqWhweQPaJ', 'Male', 1);
INSERT INTO Staff (PassportNumber, Job_id, FirstName, LastName, Username, UserPassword, Gender, OnLocation) VALUES ('497270616', 1, 'Antonietta', 'Benazet', 'abenazet21', 'jQHypQA', 'Female', 0);
INSERT INTO Staff (PassportNumber, Job_id, FirstName, LastName, Username, UserPassword, Gender, OnLocation) VALUES ('165180488', 1, 'Freddi', 'Crawshaw', 'fcrawshaw22', 'VO0Zxtjz', 'Female', 1);
INSERT INTO Staff (PassportNumber, Job_id, FirstName, LastName, Username, UserPassword, Gender, OnLocation) VALUES ('625497227', 1, 'Analiese', 'MacCauley', 'amaccauley23', 'vHlyxT', 'Female', 1);
INSERT INTO Staff (PassportNumber, Job_id, FirstName, LastName, Username, UserPassword, Gender, OnLocation) VALUES ('209025672', 1, 'Lorine', 'Howden', 'lhowden24', 'NlxKgdquGu', 'Female', 1);
INSERT INTO Staff (PassportNumber, Job_id, FirstName, LastName, Username, UserPassword, Gender, OnLocation) VALUES ('746569567', 1, 'Carina', 'Arnaudot', 'carnaudot25', 'II1h6klATC4', 'Female', 1);
INSERT INTO Staff (PassportNumber, Job_id, FirstName, LastName, Username, UserPassword, Gender, OnLocation) VALUES ('616500524', 1, 'Jacqui', 'Epsly', 'jepsly26', 'pjjkqTp', 'Female', 1);
INSERT INTO Staff (PassportNumber, Job_id, FirstName, LastName, Username, UserPassword, Gender, OnLocation) VALUES ('083771732', 1, 'Denise', 'Point', 'dpoint27', 'Q8RaFT', 'Female', 0);
INSERT INTO Staff (PassportNumber, Job_id, FirstName, LastName, Username, UserPassword, Gender, OnLocation) VALUES ('559904572', 1, 'Lannie', 'Magrannell', 'lmagrannell28', 'zun1k6iK', 'Male', 0);
INSERT INTO Staff (PassportNumber, Job_id, FirstName, LastName, Username, UserPassword, Gender, OnLocation) VALUES ('409797189', 1, 'Lelia', 'Schirak', 'lschirak29', 'Phremwe3u', 'Female', 0);
INSERT INTO Staff (PassportNumber, Job_id, FirstName, LastName, Username, UserPassword, Gender, OnLocation) VALUES ('884132233', 1, 'Leda', 'Fenkel', 'lfenkel2a', 't9N5Ht', 'Female', 1);
INSERT INTO Staff (PassportNumber, Job_id, FirstName, LastName, Username, UserPassword, Gender, OnLocation) VALUES ('629805599', 1, 'Miriam', 'McGraffin', 'mmcgraffin2b', 'cRjkBr1bkY', 'Female', 0);
INSERT INTO Staff (PassportNumber, Job_id, FirstName, LastName, Username, UserPassword, Gender, OnLocation) VALUES ('308331996', 1, 'Marna', 'Darter', 'mdarter2c', 'cq10PAI', 'Female', 1);
INSERT INTO Staff (PassportNumber, Job_id, FirstName, LastName, Username, UserPassword, Gender, OnLocation) VALUES ('668024591', 1, 'Cully', 'Cheng', 'ccheng2d', '3sXOwunEA', 'Male', 1);
INSERT INTO Staff (PassportNumber, Job_id, FirstName, LastName, Username, UserPassword, Gender, OnLocation) VALUES ('178172987', 1, 'Delphine', 'Brinkler', 'dbrinkler2e', 'shTIBe1', 'Female', 0);
INSERT INTO Staff (PassportNumber, Job_id, FirstName, LastName, Username, UserPassword, Gender, OnLocation) VALUES ('325995653', 1, 'Renaud', 'Kobieriecki', 'rkobieriecki2f', '90S57vil5emY', 'Male', 0);
INSERT INTO Staff (PassportNumber, Job_id, FirstName, LastName, Username, UserPassword, Gender, OnLocation) VALUES ('802488904', 1, 'Belle', 'Jirek', 'bjirek2g', 'GbKhXknh', 'Female', 0);
INSERT INTO Staff (PassportNumber, Job_id, FirstName, LastName, Username, UserPassword, Gender, OnLocation) VALUES ('341640004', 1, 'Emmalynne', 'Newiss', 'enewiss2h', 'sBsbkDjx8u', 'Female', 0);
INSERT INTO Staff (PassportNumber, Job_id, FirstName, LastName, Username, UserPassword, Gender, OnLocation) VALUES ('891585236', 1, 'Ciel', 'Parkyn', 'cparkyn2i', 'MhPmHHy', 'Non-Binary', 0);
INSERT INTO Staff (PassportNumber, Job_id, FirstName, LastName, Username, UserPassword, Gender, OnLocation) VALUES ('523132818', 1, 'Nolie', 'Jeffs', 'njeffs2j', 'ImcxPNWME7', 'Female', 1);
INSERT INTO Staff (PassportNumber, Job_id, FirstName, LastName, Username, UserPassword, Gender, OnLocation) VALUES ('611889305', 1, 'Ebony', 'Curnok', 'ecurnok2k', 'YN0JUdzo', 'Female', 0);
INSERT INTO Staff (PassportNumber, Job_id, FirstName, LastName, Username, UserPassword, Gender, OnLocation) VALUES ('950529313', 1, 'Katleen', 'Ivatt', 'kivatt2l', 'GO3dGs6q0f', 'Female', 1);
INSERT INTO Staff (PassportNumber, Job_id, FirstName, LastName, Username, UserPassword, Gender, OnLocation) VALUES ('693808037', 1, 'Shelley', 'Pieche', 'spieche2m', 'dV1zOt4u3', 'Male', 1);
INSERT INTO Staff (PassportNumber, Job_id, FirstName, LastName, Username, UserPassword, Gender, OnLocation) VALUES ('069657418', 1, 'Vinny', 'Canter', 'vcanter2n', '0WmrC4Kit7ti', 'Female', 0);
INSERT INTO Staff (PassportNumber, Job_id, FirstName, LastName, Username, UserPassword, Gender, OnLocation) VALUES ('654508793', 1, 'Ashlan', 'Battlestone', 'abattlestone2o', '3nsG33fOX', 'Female', 1);
INSERT INTO Staff (PassportNumber, Job_id, FirstName, LastName, Username, UserPassword, Gender, OnLocation) VALUES ('186629292', 1, 'Eugenie', 'Rown', 'erown2p', 'nvd73LYDsXJ', 'Female', 1);
INSERT INTO Staff (PassportNumber, Job_id, FirstName, LastName, Username, UserPassword, Gender, OnLocation) VALUES ('009137762', 1, 'Clarissa', 'Dillicate', 'cdillicate2q', 'PudRGdf1', 'Female', 1);
INSERT INTO Staff (PassportNumber, Job_id, FirstName, LastName, Username, UserPassword, Gender, OnLocation) VALUES ('613422892', 1, 'Lock', 'Cawse', 'lcawse2r', 'D1JHSVCSXWaJ', 'Male', 0);


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
INSERT INTO Aircraft (AircraftType_id, AircraftStatus_id) VALUES (2, 1)
INSERT INTO Aircraft (AircraftType_id, AircraftStatus_id) VALUES (2, 1)

-- FlightTrip

-- TRIP FROM HEATHROW TO EDINBURGH - Price is £150 - Discount is 0.1 - Takes 1 hour
INSERT INTO FlightTrip (Aircraft_id, DepartureTime, ArrivalTime, DepartureAirport, ArrivalAirport, AvailableSeats, TicketPrice, TicketDiscount)
VALUES (1, '2020-12-02 10:30', '2020-12-02 11:30', 'LHR', 'EDI', 400, 150, 10)

-- TRIP FROM NEWCASTLE TO HEATHROW
INSERT INTO FlightTrip (Aircraft_id, DepartureTime, ArrivalTime, DepartureAirport, ArrivalAirport, AvailableSeats, TicketPrice, TicketDiscount)
VALUES (2, '2020-12-02 10:30', '2020-12-02 11:30', 'NCL', 'LHR', 400, 100, 20)
