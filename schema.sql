drop table if exists pieces;
create table pieces (
  id integer primary key autoincrement,
  x_coord integer not null,
  y_coord integer not null,
  z_coord integer not null,
  piece_object blob not null
);
