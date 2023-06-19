drop table blog;
create table if not exists blog
(
id integer
primary key autoincrement,
head text,
story text,
image text,
visible integer
);