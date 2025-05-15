create table if not exists users(
	id int auto_increment primary key,
	username varchar(50) not null unique,
	pass varchar(10) not null,
	created_at timestamp default current_timestamp()
	
);

insert into users (username, pass) values('user1','password1');
insert into users (username, pass) values('user2','password2');
insert into users (username, pass) values('user3','password3');

select * from users
