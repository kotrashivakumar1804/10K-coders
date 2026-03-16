use 10000coders;

create table product_inventory(product_id int,product_name varchar(50),category varchar(50),price int,stock int,supplier_email varchar(50));

DESC 10000coders.product_inventory;

ALTER table product_inventory MODIFY column product_id int primary key,modify column product_name varchar(50) not null;

ALTER table product_inventory MODIFY price Decimal(8,2) check(price > 0),modify stock int check(stock >= 0);

ALTER table product_inventory MODIFY category varchar(50) default 'General';

insert into product_inventory values(1,'soaps',default,230,30,'sopesupplier@gmail.com'),(2,'Paste',default,120,50,'pastesupplier@gmail.com'),(3,'Perfume',default,250,23,'perfumesupplier@gmail.com'),(4,'Sunfloweroil',default,270,60,'oilsupplier@gmail.com'),(5,'Rice_bag',default,1000,20,'ricesupplier@gmail.com');
insert into product_inventory values(6,'Britenia',default,-340,3,'briteniasupplier@gmail.com');

Select * from product_inventory;

update product_inventory set stock=stock+10 where product_name='Perfume';

alter table product_inventory drop rating;
Alter table  product_inventory add rating float check(rating Between 1 and 5) default 4;
ALTER table product_inventory MODIFY rating float check(rating > 1 & rating < 5) default 4;

insert into product_inventory values(6,'Wheet',default,40,30,'wheetsupplier@gmail.com',default);


use 10000coders;

create table players(Player_id int,Player_name varchar(50),Team varchar(50),Role varchar(50),Matchs int,Runs int,Wickets int,Stick_rate int,age int);

ALTER table players add column debut_year int;

ALTER table players add column Country_rank int;

ALTER table players modify Runs Bigint;

ALTER table players Rename column player_name to player_names;

ALTER table players drop Country_rank;












