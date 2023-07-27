create table if not exists "clients" (
	"id" serial primary key,
	"name" varchar(40) not null,
	"surname" varchar(40) not null,
	"email" varchar(80) not null
);	

create table if not exists "phone" (
	"id" integer not null references "clients" ("id"),
	"phone_number" integer not null,
	constraint pk primary key ("id", "phone_number")
);
