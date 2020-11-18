-- TRIP FROM HEATHROW TO EDINBURGH - Price is £150 - Discount is 0.1 - Takes 1 hour
INSERT INTO FlightTrip (Aircraft_id, DepartureTime, ArrivalTime, DepartureAirport, ArrivalAirport, AvailableSeats, TicketPrice, TicketDiscount)
VALUES (1, '2020-12-02 10:30', '2020-12-02 11:30', 'LHR', 'EDI', 400, 150, 0.1)

-- TRIP FROM NEWCASTLE TO HEATHROW
INSERT INTO FlightTrip (Aircraft_id, DepartureTime, ArrivalTime, DepartureAirport, ArrivalAirport, AvailableSeats, TicketPrice, TicketDiscount)
VALUES (2, '2020-12-02 10:30', '2020-12-02 11:30', 'NCL', 'LHR', 400, 100, 0.2)
