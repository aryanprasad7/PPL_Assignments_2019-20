/* flight database */
/* flight(Source, Airline, Destination, Price(in $), Duration(in minutes) */
flight(london, aircanada, toronto, 500, 360).
flight(toronto, aircanada, madrid, 900, 480).
flight(madrid, aircanada, barcelona, 100, 60).
flight(london, united, toronto, 650, 420).
flight(toronto, united, madrid, 950, 540).
flight(paris, united, toulouse, 900, 480).
flight(toronto, iberia, madrid, 800, 480).
flight(madrid, iberia, malaga, 50, 60).
flight(malaga, iberia, valencia, 80, 120).
flight(madrid, iberia, valencia, 40, 50).
flight(madrid, iberia, barcelona, 120, 65).
flight(barcelona, iberia, valencia, 110, 75).
flight(barcelona, iberia, london, 220, 240).

/* Airport database */
/* airport(Cityname, Airporttax, MinSecDelay) */
airport(london, 75, 80).
airport(toronto, 50, 60).
airport(madrid, 75, 45).
airport(barcelona, 40, 30).
airport(valencia, 40, 20).
airport(malaga, 50, 30).
airport(paris, 50, 60).
airport(toulouse, 40, 30).

/* Flight exists or not */
flight_exists(From, To) :-
	flight(From, Airline, To, Price, Duration);
	flight(To, Airline, From, Price, Duration),
	format('Flight exists from ~w to ~w via the ~w airline ~n', [From, To, Airline]).
	
flight_exist(From, To) :-
	flight(From, Airline, To, Price, Duration);
	flight(To, Airline, From, Price, Duration).
	
/* Can travel from (Cityname) to (Cityname) in two flights or not */
from_to_in2flights(From, To):-
	flight_exist(From, Intermediate),
	flight_exist(Intermediate, To),
	format('Yes!, It is possible to go from ~w to ~w in two flights ~n', [From, To]).
	
/* Is cheap flight available from (Cityname) to (Cityname) 
   Cheap flight => Price < 400$ */
cheap_flight(From, To):-
	flight(From, Airline, To, Price, Duration),
	Price < 400 -> write('There is a cheap flight'); write('There is no cheap flight').
	
/* Is preferred flight available from (Cityname) to (Cityname) 
   Preferred flight is, if Price < 400 or Airline is aircanada */
preferred_flight(From, To):-
	flight(From, Airline, To, Price, Duration),
	Price < 400 -> write('There is a cheap flight from '), write(From), write(' To '), write(To), nl;
	Airline = aircanada -> write('There is a flight from '), write(From), write(' To '), write(To), write(' via the '), write(Airline), write(' airline'), nl; nl,
	write('Your preferred flight is available').

/*
preferred_flight2(From, To):-
	flight(From, Airline, To, Price, Duration),
	Price < 400; Airline = aircanada -> write('Ur preferred flight is available').
*/	

