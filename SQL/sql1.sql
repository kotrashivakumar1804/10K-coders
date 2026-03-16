use 10000coders;

show tables;

create table ecomers(order_id INT,customer_name varchar(50),amount Decimal(8,2),product_name varchar(50));

insert into ecomers values (1,'Ravi',70000,'Laptop'),(2,'shiva',25000,'Mobile'),(3,'ram',2500,'smart_watch'),(4,'sunder',35000,'Tablete_mobile'),(5,'suresh',23000,'Televesion'),(6,'shiva',35000,'Televesion'),(7,'ravi',4000,'grander');
insert into ecomers values(8,'ravi',18000,'Aircolour'),(9,'shiva',50000,'AC');

select * from ecomers;

select SUM(amount) as total_revenue from ecomers;

select MIN(amount) as total_Minimum_amount from ecomers;

select MAX(amount) as total_Maximum_amount from ecomers;

select count(product_name) as total_products from ecomers;

select AVG(amount) as average_amount from ecomers;


select * from ecomers limit 5 offset 3;

select * from ecomers order by amount DESC limit 1 offset 1;

select * from ecomers order by amount ASC limit 1 offset 1;

select * from ecomers order by amount ASC limit 2,1;

(select max(amount) as second_high from ecomers where amount < (select max(amount) as first_high from ecomers where amount));

(select MIN(amount) as second_lowest from ecomers where amount > (select MIN(amount) as first_high from ecomers where amount));

(select MIN(amount) as third_lowest from ecomers where amount > (select MIN(amount) as second_high from ecomers where amount > (select MIN(amount) as first_lowest from ecomers )));

SELECT customer_name,sum(amount) from ecomers group by customer_name;


select customer_name,count(product_name) from ecomers group by customer_name;

select product_name,count(product_name) from ecomers group by product_name;

select product_name,count(product_name),sum(amount) from ecomers group by product_name order by count(product_name) DESC limit 1 ;

select product_name,count(product_name) as quentity from ecomers where max(product_name);


use 10000coders;
create table contact(id int,name varchar(50),email varchar(100),ph varchar(50));

insert INTO contact Values(1,'shiva','shivakumar@gmail.com','+91 8309282800'),(1,'ram','shivaram@gmail.com','+91 876542800'),(2,'vamshi','vamshi@gmail.com',' ');

Select * from contact;

set sql_safe_updates =0;
update contact set id=2 where name='ram';
update contact set id=3 where name='vamshi';
update contact set email='Ramvarma@gmail.com' where id =2;
update contact set ph='+91 7654898674' where id =2;
update contact set ph='+91 4537665234' where id =3;

Alter table contact MODIFY column id int unique,MODIFY column name varchar(50) not null,MODIFY column email varchar(100) unique not null,MODIFY column ph varchar(50) unique not null;
Alter table contact MODIFY column name varchar(50) not null;
Alter table contact MODIFY column id int Primary key;

alter table contact add status varchar(50) default 'Inactive';

DESC contact;

insert into contact values(4,'ravi','ravi@gmail.com','+91 6655433442',default);

update contact set status=default  where status=null;

alter table contact add age int not null check(age>18) Default 20;

alter table contact modify column id int unique auto_increment;

insert into contact values(id,'vanu','vanu@gmail.com','+91 6656783442',Default,23);

---create table product_inventory


