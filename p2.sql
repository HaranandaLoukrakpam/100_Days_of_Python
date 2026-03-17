create DATABASE actvity;
create table activity (Acode integer,ActivityName varchar(25),ParticipantNum integer,PrizeMoney integer);
describe actvity;
insert into activity values(1001,'Relay 100x4',16,10000);
insert into activity values(1002,'High Jump',10,12000);
insert into activity values(1003,'Shot put',12,8000);
insert into activity values(1005,'Long Jump',12,9000);
insert into activity values(1008,'Discuss Throw',10,15000);
select * from activity;
 select ActivityName,PrizeMoney from activity;
 select * from activity where ParticipantNum=12;
 select * from activity where PrizeMoney>10000;
 select * from activity where 8000<PrizeMoney<12000;
 select * from activity where PrizeMoney between 8000 and 12000;
 