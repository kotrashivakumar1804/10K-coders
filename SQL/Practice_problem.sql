use 10000coders;

create table players(Player_id int,Player_name varchar(50),Team varchar(50),Role varchar(50),Matchs int,
Runs int,Wickets int,Stick_rate int,age int);

DESC players;

ALTER table players add column debut_year year;

ALTER table players add column Country_rank int;

ALTER table players modify Runs Bigint;

ALTER table players Rename column player_name to player_names;

ALTER table players drop Country_rank;

ALTER table players MODIFY Stick_rate float ;

INSERT INTO players values(101,'Virat kohli','India','Batsman',274,12657,7,87.9,35,2008),
(102,'Rohith sharma','India','Batsman',275,10112,8,87.6,36,2007),
(103,'joe root','England','Batsman',158,6543,5,81.4,39,2012),
(104,'Babar hazam','Pakistan','Batsman',117,5729,1,80.6,30,2015),
(105,'Ben stockes','England','All rounder',108,8543,3,85.4,32,2011),
(106,'kane williamson','NEW zealand','Batsman',121,6811,5,81.7,34,2010);

SELECT * from players;

UPDATE players set Stick_rate=91.9 where Player_id=101; 
set sql_safe_updates =0;

UPDATE players set Runs=Runs+200 where Player_id=102; 

Update players set Matchs=Matchs+1;

DELETE from players where age > 37;

UPDATE players set Team='INDIA' where Team='India';

-- DQL
SELECT * from players;
select Player_names,Team,Runs from players;
select distinct Team from players;
select distinct Role from players;

SELECT player_names,Runs from players where Runs > 10000;
SELECT player_names,age from players where age between 25 and 35;
Select * from players where Team='INDIA';
Select * from players where NOT Team='INDIA';
select player_names,Runs,Wickets from players where Runs > 5000 AND Wickets > 6;
select player_names,Role,Wickets from players where Role='Bowlers' and Wickets > 5;


select * from players order by Runs DESC;
select * from players order by Stick_rate  DESC;
select * from players order by Runs DESC limit 4;
select * from players where Team='INDIA' order by Wickets DESC;
select * from players where Matchs > 200;


select sum(Runs) as Total_runs from players;
select avg(Stick_rate) as Average_Stick_rate from players;
select * from players order by Runs DESC limit 1;
select * from players order by Stick_rate ASC limit 1;
select count(*) from players;


select Team,sum(Runs) as Total_runs from players group by Team;
select Team,AVG(Stick_rate) as AVG_Stick_rate from players group by Team;
select Role,count(*) from players group by Role;
select Team,sum(Wickets) from players group by Team;


select Team,sum(Runs) as Total_runs from players where Runs > 10000 group by Team ;
select Role,count(*) from players group by Role having count(*) > 2;
select Team,AVG(Stick_rate) as Avg_Stick_rate from players group by Team having AVG(Stick_rate) > 130;