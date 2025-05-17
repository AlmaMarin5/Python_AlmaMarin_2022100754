USE jaguarete;
create table if not exists users(
	id int auto_increment primary key,
	username varchar(50) not null unique,
	pass varchar(10) not null,
	created_at timestamp default current_timestamp()
	
);

insert into users (username, pass) values('amarin','unida123');

select * from users;
SELECT username From users WHERE username = 'amarin' AND pass = 'unida123'
