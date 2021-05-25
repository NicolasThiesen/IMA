BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "services" (
	"id"	INTEGER NOT NULL,
	"service"	TEXT NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "regions" (
	"id"	INTEGER NOT NULL,
	"name"	TEXT NOT NULL,
	"region"	TEXT NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
INSERT INTO "services" ("id","service") VALUES (1,'Auto Scaling'),
 (2,'EBS'),
 (3,'EC2'),
 (4,'ECS'),
 (5,'ELB'),
 (6,'Elastic Beanstalk'),
 (7,'RDS'),
 (8,'VPN');
INSERT INTO "regions" ("id","name","region") VALUES (1,'US East (N. Virginia)','us-east-1'),
 (2,'US East (Ohio)','us-east-2'),
 (3,'US West (N. California)','us-west-1'),
 (4,'US West (Oregon)','us-west-2'),
 (5,'Africa (Cape Town)','af-south-1'),
 (6,'Asia Pacific (Hong Kong)','ap-east-1'),
 (7,'Asia Pacific (Mumbai)','ap-south-1'),
 (8,'Asia Pacific (Tokyo)','ap-northeast-1'),
 (9,'Asia Pacific (Seoul)','ap-northeast-2'),
 (10,'Asia Pacific (Osaka)','ap-northeast-3'),
 (11,'Asia Pacific (Singapore)','ap-southeast-1'),
 (12,'Asia Pacific (Sydney)','ap-southeast-2'),
 (13,'Canada (Central)','ca-central-1'),
 (14,'China (Beijing)','cn-north-1'),
 (15,'China (Ningxia)','cn-northwest-1'),
 (16,'Europe (Frankfurt)','eu-central-1'),
 (17,'Europe (Ireland)','eu-west-1'),
 (18,'Europe (London)','eu-west-2'),
 (19,'Europe (Paris)','eu-west-3'),
 (20,'Europe (Milan)','eu-south-1'),
 (21,'Europe (Stockholm)','eu-north-1'),
 (22,'Middle East (Bahrain)','me-south-1'),
 (23,'South America (São Paulo)','sa-east-1');
COMMIT;
